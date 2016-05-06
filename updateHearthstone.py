from datetime import datetime
from helper import *

# Import "database" into memory
cardsTXT = open("cards.txt", "r")
for line in cardsTXT:
  list = line.split("~")
  id = list[0]
  info = {"name": list[1], "mana": int(list[2]), "type": list[3], "rarity": list[4], "expansion": list[5], "race": list[6], "class": list[7], "attack": list[8], "health": list[9], "durability": list[10], "howToGet": list[11], "howToGetGold": list[12]}
  cards[id] = info
cardsTXT.close()

decksTXT = open("decks.txt", "r")
for line in decksTXT:
  if line == "\n":
    continue
  list = line.split("~")
  id = list[0]
  info = {"name": list[1], "class": list[2], "format": list[3], "type": list[4], "cost": int(list[5]), "lastUpdated": list[6]}
  decks[id] = info
decksTXT.close()

containTXT = open("contain.txt", "r")
for line in containTXT:
  list = line.split("~")
  id = list[0]
  contain[id] = int(list[1])
containTXT.close()

possessTXT = open("possess.txt", "r")
for line in possessTXT:
  list = line.split("~")
  possess[list[0]] = int(list[1])
possessTXT.close()

  
command = ''

while command != "exit":

  command = raw_input(">>> ")

  # Add a card to the collection
  if command[:8].upper() == "ADDCARD ":

    card = command[8:]

    # Test for validity
    id = ValidCard(card)
    if id == None:
      continue

    # Find how many of that card the user owns and add it if the user doesn't own it
    try:
      number = possess[id]

      if number == 1:
        possess[id] = 2
      elif number == 2:
        print "error: You already have two of that card"
        continue
      else:
        print "Unspecified error"
        continue
        
    except:
      possess[id] = 1

    # Commit
    SavePossess()



  # Delete a card from the collection
  elif command[:11].upper() == "DELETECARD ":

    card = command[11:]

    # Test for validity
    id = ValidCard(card)
    if id == None:
      continue

    # Find how many of that card the user owns
    try:
      number = possess[id]
    except:
      print "error: You do not own that card"
      continue

    # Update database based on amount
    if number == 1:
      possess.pop(id, 0)
    elif number == 2:
      possess[id] = 1
    else:
      print "Unspecified error"
      continue

    # Commit
    SavePossess()
    
  elif command.upper() == "PRINTCARDS":
  
    cardList = []
    namesToID = {}
    for id in possess:
      cardList.append(id)
      cardName = cards[id]["name"]
      namesToID[cardName] = id
      
    sortedCards = SortCards(cardList)
    
    for id in sortedCards:
      cardName = cards[id]["name"]
      print str(possess[namesToID[cardName]]) + "x " + cardName


  # Add a deck to the users collection
  elif command[:8].upper() == "ADDDECK ":

    name = command[8:]
    Class = raw_input("Class: ")
    if Class not in CLASS_LIST:
      print "error: Not a valid class"
      continue
    format = raw_input("Format: ").upper()
    if format not in ["STANDARD", "WILD"]:
      print "error: Not a valid format"
      continue
    type = raw_input("Type: ").upper()

    # Insert new deck information into memory
    deckID = GetNewDeckID()
    info = {
      "name": name,
      "class": Class,
      "format": format,
      "type": type,
      "cost": 0,
      "lastUpdated": datetime.today().strftime("%Y/%m/%d")
    }
    decks[deckID] = info;

    # Ask for cards until the total number of cards is equal to 30
    print "--- >>> <number of cards> <card name>"
    numCards = 0
    while numCards < 30:

      entry = raw_input("--- >>> ")
      number = int(entry[0])
      card = entry[2:]

      # Test for validity
      id = ValidCard(card)
      if id == None:
        print "Verify the card name and that you are only inserting one or two"
        continue

      # Insert cards into contain, but make sure (if they're inserting two) that both entries are valid
      # before inserting them
      if not CanInsertCard(id, deckID):
        continue
      if number == 2:
        if not CanInsertCard(id, deckID):
          continue
        numCards += 1
      numCards += 1

    # Update deck cost and then commit
    UpdateCost(deckID)
    SaveDecks()
    SaveContain()



  # Delete a deck
  elif command[:11].upper() == "DELETEDECK ":

    name = command[11:]

    deleteDeck = GetDeck(name)
    if deleteDeck == None:
      continue

    decks.pop(deleteDeck, None)

    toDelete = []
    for ids in contain:
      id = ids.split(",")[1]
      if id == deleteDeck:
        toDelete.append(ids)
    
    for id in toDelete:
      contain.pop(id, 0)

    # Commit
    SaveDecks()
    SaveContain()

    
  # Find which pack to get
  elif command.upper() == "PACK":

    print ""
    chance = {
      "Common": 0.71,
      "Rare": 0.245,
      "Epic": 0.04,
      "Legendary": 0.005
    }
    enchantVal = CARD_VALUES
    disenchantVal = {
      "Common": 5.0,
      "Rare": 20.0,
      "Epic": 100.0,
      "Legendary": 400.0
    }

    print "Highest number has greatest value"
    print "--------------------------------------"

    all = {}
    miss = {}
    for curExp in PACK_LIST:

      # Get count of all cards
      results = {
        "Common": 0.0,
        "Rare": 0.0,
        "Epic": 0.0,
        "Legendary": 0.0
      }
      amounts = {
        "Common": 0.0,
        "Rare": 0.0,
        "Epic": 0.0,
        "Legendary": 0.0
      }
      for id in cards:
        if cards[id]["expansion"] == curExp and cards[id]["rarity"] != "Basic":
          results[cards[id]["rarity"]] += 2
          try:
            amounts[cards[id]["rarity"]] += possess[id]
          except:
            continue

      all["Common"] = results["Common"]
      all["Rare"] = results["Rare"]
      all["Epic"] = results["Epic"]
      all["Legendary"] = results["Legendary"] / 2
      miss["Common"] = all["Common"] - amounts["Common"]
      miss["Rare"] = all["Rare"] - amounts["Rare"]
      miss["Epic"] = all["Epic"] - amounts["Epic"]
      miss["Legendary"] = all["Legendary"] - amounts["Legendary"]

      total = 0
      for i in RARITY_LIST:
        val = chance[i] * (float((all[i] - miss[i]) / all[i]) * disenchantVal[i] + float(miss[i] / all[i]) * enchantVal[i]) 
        total += val

      print curExp + ": " + str(total * 5)


      
  # Find out decks the user can make
  elif command.upper() == "CANMAKE" or command[:8].upper() == "CANMAKE ":

    deckList = []
    if command.upper() == "CANMAKE":
      for id in decks:
        deckList.append(id)
    else:
      for id in decks:
        if decks[id]["class"] == command[8:].lower().title():
          deckList.append(id)
    
    if not deckList:
      print "error: Not a valid class"
      continue
      
    deckList = SortDecks(deckList)

    print ""
    curType = ""
    for curDeck in deckList:
      completeDeck = True
      for ids in contain:
        id = ids.split(",")
        if curDeck == id[1]:
          try:
            if possess[id[0]] < contain[ids]:
              completeDeck = False
              break
          except:
            completeDeck = False
            break
          
      if completeDeck:
        if decks[curDeck]["type"] != curType:
          print ""
          print decks[curDeck]["type"].lower().title() + " decks"
          print "----------------"
          curType = decks[curDeck]["type"]
        print decks[curDeck]["name"] + ", Class: " + decks[curDeck]["class"] + ", Cost: " + str(decks[curDeck]["cost"])

    print ""


  # Find the best card to craft
  elif command.upper() == "WHATTOCRAFT" or command[:12].upper() == "WHATTOCRAFT ":

    if command[:12].upper() == "WHATTOCRAFT ":
      Class = command[12:].lower().title()
      if Class not in CLASS_LIST:
        print "error: Invalid class"
        continue
      
    cardSet = {}
    for ids in contain:
      id = ids.split(",")[0]
      if decks[ids.split(",")[1]]["type"].upper() == "SOLO":
        continue
      if command[:12].upper() == "WHATTOCRAFT ":
        if command[12:].lower().title() != decks[ids.split(",")[1]]["class"]:
          continue

      amount = contain[ids]
      
      try:
        cardSet[id][str(amount)] += 1
      except:
        cardSet[id] = {
          "1": 0,
          "2": 0
        }
        cardSet[id][str(amount)] += 1
    
    finalVals = {}
    for id in cardSet:
      try:
        amount = possess[id]
        if (amount == 1) and (cards[id]["rarity"] != "Legendary"):
          finalVals[id] = cardSet[id]["2"] * CARD_VALUES[cards[id]["rarity"]]
        else:
          continue
      except:
        finalVals[id] = (cardSet[id]["1"] + cardSet[id]["2"]) * CARD_VALUES[cards[id]["rarity"]]

    print ""
    for i in range(10):
      cost = 0
      saveID = ""
      for id in finalVals:
        if finalVals[id] > cost:
          cost = finalVals[id]
          saveID = id
      try:
        print cards[saveID]["name"] + " will give you " + str(cost) + " value"
        finalVals[saveID] = -1
      except:
        continue

    print ""


  elif command[:10].upper() == "PRINTLIST ":

    name = command[10:]

    deckID = GetDeck(name)
    if deckID == None:
      continue

    cardList = []
    for ids in contain:
      if deckID == ids.split(",")[1]:
        cardList.append(ids.split(",")[0])

    cardList = SortCards(cardList)

    print ""
    for card in cardList:
      print str(contain[card + "," + deckID]) + "x " + cards[card]["name"]
    print ""

  elif command[:11].upper() == "PRINTDECKS ":

    Class = command[11:].lower().title()
    if Class not in CLASS_LIST:
      print "error: Not a valid class"
      continue

    standardDecks = []
    wildDecks = []
    for id in decks:
      if decks[id]["class"] == Class:
        if decks[id]["format"] == "STANDARD":
          standardDecks.append(id)
        elif decks[id]["format"] == "WILD":
          wildDecks.append(id)
        else:
          print "error: Unrecognized format: " + decks[id]["format"]
        
    standardDecks = SortDecks(standardDecks)
    wildDecks = SortDecks(wildDecks)

    print ""
    print "Standard Decks"
    print "-----------------"
    for curDeck in standardDecks:
      print decks[curDeck]["name"] + ", Cost: " + str(decks[curDeck]["cost"])
    print ""
    print "Wild Decks"
    print "-------------"
    for curDeck in wildDecks:
      print decks[curDeck]["name"] + ", Cost: " + str(decks[curDeck]["cost"])
    print ""
    
  elif command[:15].upper() == "PRINTDECKSWITH ":
  
    name = command[15:].lower().title()
    cardID = ValidCard(name)
    if cardID == None:
      continue
      
    deckList = []
    for id in contain:
      ids = id.split(",")
      if ids[0] == cardID:
        deckList.append(ids[1])
        
    deckList = SortDecks(deckList)
    
    print ""
    curType = ""
    for curDeck in deckList:
      if decks[curDeck]["type"] != curType:
        print ""
        print decks[curDeck]["type"].lower().title() + " decks"
        print "----------------"
        curType = decks[curDeck]["type"]
      print decks[curDeck]["name"] + ", Class: " + decks[curDeck]["class"] + ", Cost: " + str(decks[curDeck]["cost"])
        

    print ""


  elif command[:9].upper() == "EDITDECK ":

    name = command[9:]
    deckID = GetDeck(name)
    if deckID == None:
      continue

    print "Use 'done' to stop editing"
    print "--- >>> <card to replace> / <replacement card>"
    cmd = raw_input("--- >>> ")
    while cmd.upper() != "DONE":

      try:
        toReplace = cmd[:cmd.index('/') - 1]
        replacement = cmd[cmd.index('/') + 2:]
      except:
        print "error: Be sure to include '/' between card names"
        cmd = raw_input("--- >>> ")
        continue

      toReplace = ValidCard(toReplace)
      if toReplace == None:
        cmd = raw_input("--- >>> ")
        continue
      replacement = ValidCard(replacement)
      if replacement == None:
        cmd = raw_input("--- >>> ")
        continue

      if (toReplace == replacement):
        print "error: Please enter two different cards"
        cmd = raw_input("--- >>> ")
        continue

      try:
        amount = contain[toReplace + "," + deckID]
        if amount == 1:
          contain.pop(toReplace + "," + deckID, 0)
        elif amount == 2:
          contain[toReplace + "," + deckID] = 1

        if not CanInsertCard(replacement, deckID):
          contain[toReplace + "," + deckID] = amount
          cmd = raw_input("--- >>> ")
          continue

      except:
        print "error: " + cards[toReplace]["name"] + " isn't contained in this deck"
        cmd = raw_input("--- >>> ")
        continue

      cmd = raw_input("--- >>> ")

    # Commit
    decks[deckID]["lastUpdated"] = datetime.today().strftime("%Y/%m/%d")
    UpdateCost(deckID)
    SaveDecks()
    SaveContain()
    print ""        


  # New line
  elif command == "":
    continue


  # Unrecognized command
  else:
    if command != "exit":
      print "Unrecognized command. Available commands are:"
      print "addCard <card name>"
      print "deleteCard <card name>"
      print "printCards"
      print "addDeck <deck name>"
      print "deleteDeck <deck name>"
      print "pack"
      print "canMake [class name]"
      print "whatToCraft [class name]"
      print "printDecks <class name>"
      print "printDecksWith <card name>"
      print "printList <deck name>"
      print "editDeck <deck name>"
      print "Use the command 'exit' to exit the program"