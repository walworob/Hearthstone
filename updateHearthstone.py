from datetime import datetime
from helper import *

cardsTXT = open("cards.txt", "r")
for line in cardsTXT:
  list = line.split("~")
  id = list[0]
  info = {"name": list[1], "mana": list[2], "type": list[3], "rarity": list[4], "expansion": list[5], "race": list[6], "class": list[7], "attack": list[8], "health": list[9], "durability": list[10], "howToGet": list[11], "howToGetGold": list[12]}
  cards[id] = info
cardsTXT.close()

decksTXT = open("decks.txt", "r")
for line in decksTXT:
  list = line.split("~")
  id = list[0]
  info = {"name": list[1], "class": list[2], "type": list[3], "reachableRanks": list[4], "cost": int(list[5]), "lastUpdated": list[6]}
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
    id = validCard(card)
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
      possess[id] = 2

    # Commit
    savePossess()



  # Delete a card from the collection
  elif command[:11].upper() == "DELETECARD ":

    card = command[11:]

    # Test for validity
    id = validCard(card)
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
    savePossess()



  # Add a deck to the users collection
  elif command[:8].upper() == "ADDDECK ":

    name = command[8:]
    Class = raw_input("Class: ")
    if Class not in CLASS_LIST:
	  print "error: Not a valid class"
	  continue
    type = raw_input("Type: ")
    reachableRanks = raw_input("Reachable ranks: ")
    if reachableRanks == "":
	  reachableRanks == "NULL"
    last_Updated = raw_input("Last updated:")

    deckID = getNewDeckID()
    info = {"name": name, "class": Class, "type": type, "reachableRanks": reachableRanks, "cost": 0, "lastUpdated": last_Updated}
    decks[deckID] = info;

    print "--- >>> <number of cards> <card name>"
    numCards = 0
    while numCards < 30:

      entry = raw_input("--- >>> ")
      number = int(entry[0])
      card = entry[2:]

      # Test for validity
      id = validCard(card)
      if id == None:
        print "Verify the card name and that you are only inserting one or two"
        continue

      if not canInsertCard(id, deckID):
        continue
      numCards += 1
      if number == 2:
        if not canInsertCard(id, deckID):
          continue
        numCards += 1

    # Commit
    updateCost(deckID)
    saveDecks()
    saveContain()



  # Delete a deck
  elif command[:11].upper() == "DELETEDECK ":

    print ""
    name = command[11:]

    deleteDeck = getDeck(name)
    if deleteDeck == None:
      continue

    decks.pop(deleteDeck, None)
    print ""

    # Commit
    saveDecks()



  # Find which pack to get
  elif command.upper() == "PACK":

    print ""
    chance = {
      "Common": 0.71,
      "Rare": 0.245,
      "Epic": 0.04,
      "Legendary": 0.005
    }
    enchantVal = {
      "Common": 40.0,
      "Rare": 100.0,
      "Epic": 400.0,
      "Legendary": 1600.0
    }
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
    for curExp in EXPANSION_LIST:

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
        deck = []
        deck.append(id)
        deck.append(decks[id]["class"])
        deck.append(decks[id]["cost"])
        deck.append(decks[id]["lastUpdated"])
        deckList.append(deck)

      sortDecks(deckList)

    else:
      cursor.execute("SELECT * FROM Decks WHERE class=%s ORDER BY last_updated DESC", command[8:])

    decks = cursor.fetchall()
    if not decks:
      print "error: Not a valid class"
      continue

    print ""
    numCompleteDecks = 0
    for curDeck in decks:
      id = curDeck[0]
      name = curDeck[1]
      Class = curDeck[2]
      reachableRanks = curDeck[3]
      cost = curDeck[4]

      cursor.execute("SELECT card_id, amount FROM Contain WHERE deck_id=%s", id)
      cards = cursor.fetchall()

      completeDeck = True
      for curCard in cards:

        cursor.execute("SELECT id, amount FROM Possess WHERE id=%s", curCard[0])
        results = cursor.fetchone()
        try:
          id = results[0]
        except:
          completeDeck = False
          break
        
        amount = results[1]
        if amount < curCard[1]:
          completeDeck = False
          break

      if completeDeck:
        print str(numCompleteDecks + 1) + ") " + name + ", Class: " + Class + ", Cost: " + str(cost)
        numCompleteDecks += 1

    print ""


  # Find the best card to craft
  elif command.upper() == "WHATTOCRAFT":

    cards = []

    cursor.execute("SELECT DISTINCT c.id, c.name, c.rarity FROM Cards c, Contain d WHERE c.id=d.card_id ORDER BY c.playerClass, c.cost, c.type DESC, c.name")
    rawCards = cursor.fetchall()
    for card in rawCards:
      newCard = {}
      newCard["id"] = card[0]
      newCard["name"] = card[1]
      newCard["rarity"] = card[2]
      newCard["amount"] = 0
      cards.append(newCard)

    value = {"Common": 40, "Rare": 100, "Epic": 400, "Legendary": 1600}
    for card in cards:
      cursor.execute("SELECT amount FROM Possess WHERE id=%s", card["id"])
      try:
        num = int(cursor.fetchone()[0])
        if (num == 1) and (card["rarity"] != "Legendary"):
          cursor.execute("SELECT sum(amount) AS Total FROM Contain WHERE card_id=%s AND amount!=1", card["id"])
          card["amount"] = (int(cursor.fetchone()[0]) / 2) * value[card["rarity"]]
        else:
          continue
      except:    
        cursor.execute("SELECT sum(amount) AS Total FROM Contain WHERE card_id=%s", card["id"])
        card["amount"] = int(cursor.fetchone()[0]) * value[card["rarity"]]

    cards.sort(key=getAmount, reverse=True)
    print ""
    for i in range(5):
      print cards[i]["name"] + " will give you " + str(cards[i]["amount"]) + " value"
    print ""


  elif command[:10].upper() == "PRINTLIST ":

    name = command[10:]

    deckInfo = getDeck(name)
    if deckInfo == None:
      continue

    cursor.execute("SELECT id FROM Decks WHERE name=%s AND class=%s AND cost=%s", [name, deckInfo[0], deckInfo[1]])
    id = cursor.fetchone()[0]

    cursor.execute("SELECT c.name, d.amount FROM Cards c, Contain d WHERE c.id=d.card_id AND d.deck_id=%s ORDER BY c.playerClass DESC, c.cost, c.type DESC, c.name", id)
    deck = cursor.fetchall()
    print ""
    for card in deck:
      print str(card[1]) + "x " + card[0]
    print ""

  elif command[:11].upper() == "PRINTDECKS ":

    Class = command[11:]

    cursor.execute("SELECT name, cost FROM Decks WHERE class=%s ORDER BY last_updated DESC", Class)
    decks = cursor.fetchall()
    print ""
    for curDeck in decks:
      print curDeck[0] + ", Cost: " + str(curDeck[1])
    print ""


  elif command[:9].upper() == "EDITDECK ":

    name = command[9:]
    deckInfo = getDeck(name)
    if deckInfo == None:
      continue

    cursor.execute("SELECT id FROM Decks WHERE name=%s AND class=%s AND cost=%s", [name, deckInfo[0], deckInfo[1]])
    id = cursor.fetchone()[0]

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

      toReplace = validCard(toReplace)
      if toReplace == None:
        cmd = raw_input("--- >>> ")
        continue
      replacement = validCard(replacement)
      if replacement == None:
        cmd = raw_input("--- >>> ")
        continue

      cursor.execute("SELECT amount FROM Contain WHERE card_id=%s AND deck_id=%s", [toReplace, id])
      if cursor.rowcount == 0:
        print "error: that card isn't contained in this deck"
        cmd = raw_input("--- >>> ")
        continue

      amount = cursor.fetchone()[0]
      if amount == 1:
        cursor.execute("DELETE FROM Contain WHERE card_id=%s AND deck_id=%s", [toReplace, id])
      else:
        cursor.execute("UPDATE Contain SET amount=1 WHERE card_id=%s AND deck_id=%s", [toReplace, id])


      if not canInsertCard(replacement, id):
        cmd = raw_input("--- >>> ")
        continue

      cmd = raw_input("--- >>> ")

    updateCost(id)
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
      print "addDeck <deck name>"
      print "deleteDeck <deck name>"
      print "pack"
      print "canMake [class name]"
      print "whatToCraft"
      print "printDecks <class name>"
      print "printList <deck name>"
      print "editDeck <deckname>"
      print "Use the command 'exit' to exit the program"
