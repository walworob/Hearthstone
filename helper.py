RARITY_LIST = ["Common", "Rare", "Epic", "Legendary"]
CLASS_LIST = ["Druid", "Hunter", "Mage", "Paladin", "Priest", "Rogue", "Shaman", "Warlock", "Warrior"]
EXPANSION_LIST = ["Classic", "Goblins vs Gnomes", "The Grand Tournament", "Whispers of the Old Gods"]
PACK_LIST = ["Classic", "The Grand Tournament", "Whispers of the Old Gods"]
ADVENTURE_LIST = ["Curse of Naxxramas", "Blackrock Mountain", "League of Explorers"]
STANDARD_EXPANSIONS = ["Classic", "Blackrock Mountain", "The Grand Tournament", "League of Explorers", "Whispers of the Old Gods"]
CARD_VALUES = {"Common": 40, "Rare": 100, "Epic": 400, "Legendary": 1600}

cards = {}
decks = {}
contain = {}
possess = {}

def SaveDecks():
  decksTXT = open("decks.txt", "wb")
  for id in decks:
    decksTXT.write(id + "~" + decks[id]["name"] + "~" + decks[id]["class"] + "~" + decks[id]["format"] + "~" + decks[id]["type"] + "~" + str(decks[id]["cost"]) + "~" + decks[id]["lastUpdated"] + '\n')
  decksTXT.close()

def SaveContain():
  containTXT = open("contain.txt", "wb")
  for id in contain:
    ids = id.split(",")
    containTXT.write(ids[0] + "," + ids[1] + "~" + str(contain[id]) + "\n")
  containTXT.close()

def SavePossess():
  possessTXT = open("possess.txt", "wb")
  for id in possess:
    possessTXT.write(id + "~" + str(possess[id]) + "\n")
  possessTXT.close()



def ValidCard(name):
  for id in cards:
    if cards[id]["name"] == name:
      return id

  print "error: Not a valid card"
  return None
  

def GetNewDeckID():
  highestID = 0
  for id in decks:
    if int(id) > highestID:
      highestID = int(id)

  return str(highestID + 1)



def GetDeck(deckName):

  # Get decks with that name
  deckList = []
  for id in decks:
    if decks[id]["name"] == deckName:
      deckList.append(id)

  if not deckList:
    print "error: A deck with that name does not exist"
    return None

  else:
    returnDeck = ""

    if len(deckList) > 1:

      print "\nWhich deck is correct?"
      deckCount = 1

      for deck in deckList:
        output = str(deckCount) + ") " + deckName + ", Format: " + decks[deck]["format"].title() + ", Class: " + decks[deck]["class"] + ", Cost: " + str(decks[deck]["cost"])
        print output
        deckCount += 1

      deckNum = raw_input("\nPlease enter the correct deck number: ")
      while(1):

        try:
          returnDeck = deckList[int(deckNum) - 1]
        except:
          deckNum = raw_input("Please enter a valid number: ")
          continue
        break

    # Only one deck
    else:
      returnDeck = deckList[0]

  return returnDeck



def CanInsertCard(cardID, deckID):

  # Check the deck size
  size = 0
  for id in contain:
    deckid = id.split(",")[1]
    if deckid == deckID:
      size += contain[id]
  if size >= 30:
    print "error: Deck already at max size"
    return False

  # Check if the card is valid for this class
  cardClass = cards[cardID]["class"]
  if cardClass != "NULL":
    deckClass = decks[deckID]["class"]
    if cardClass != deckClass:
      print "error: " + cards[cardID]["name"] + " not in the same class as this deck"
      return False
      
  # Check if the card is valid for this format
  deckFormat = decks[deckID]["format"]
  if deckFormat == "STANDARD":
    if cards[cardID]["expansion"] not in STANDARD_EXPANSIONS:
      print "error: Card not valid for this deck format"
      return False

  # Check if the card is already in the deck
  try:
    amount = contain[cardID + "," + deckID]
    if amount == 2:
      print "error: Already have two of that card in this deck"
      return False
    else:
      rarity = cards[cardID]["rarity"]
      if rarity == "Legendary":
        print "error: Can only have one of a legendary minion in a deck"
        return False
      else:
        contain[cardID + "," + deckID] = 2
  except:
    contain[cardID + "," + deckID] = 1

  return True



def UpdateCost(deckID):

  cardSet = []
  for id in contain:
    deckid = id.split(",")[1]
    if deckid == deckID:
      card = []
      cardID = id.split(",")[0]
      card.append(cardID)
      card.append(cards[cardID]["rarity"])
      card.append(cards[cardID]["expansion"])
      card.append(contain[id])
      cardSet.append(card)

  cost = 0
  for card in cardSet:
    cardID = card[0]
    rarity = card[1]
    expansion = card[2]
    amount = card[3]

    if expansion in EXPANSION_LIST:
      if rarity == "Common":
        cost += (40 * amount)
      elif rarity == "Rare":
        cost += (100 * amount)
      elif rarity == "Epic":
        cost += (400 * amount)
      elif rarity == "Legendary":
        cost += (1600 * amount)
      elif rarity != "Basic":
        print "error: " + rarity + " is not a recognized rarity. " + cardID

  decks[deckID]["cost"] = cost



# These functions will measure if deckA is higher than deckB and return true or false
# Ties go to deckA
def HigherType(a, b):
  if a != "META":
    if a != "UNIQUE":
      if a != "BUDGET":
        return b == "SOLO"
      else:
        return b == "SOLO" or b == "BUDGET"
    else:
      return b != "META"
  else:
    return True

def DeckIsHigher(deckA, deckB):
  a = decks[deckA]
  b = decks[deckB]
  if a["type"] == b["type"]:
    if a["class"] == b["class"]:
      if a["lastUpdated"] == b["lastUpdated"]:
        return True
      else:
        return a["lastUpdated"] > b["lastUpdated"]
    else:
      return a["class"] < b["class"]
  else:
    return HigherType(a["type"].upper(), b["type"].upper())

def SortDecks(deckList):

  for x in range(0, len(deckList)):
    curBest = x
    for y in range(x, len(deckList)):
      if DeckIsHigher(deckList[y], deckList[curBest]):
        curBest = y

    temp = deckList[x]
    deckList[x] = deckList[curBest]
    deckList[curBest] = temp

  return deckList



def CardIsHigher(cardA, cardB):
  a = cards[cardA]
  b = cards[cardB]
  if a["class"] == b["class"]:
    if a["mana"] == b["mana"]:
      if a["type"] == b["type"]:
        return a["name"] < b["name"]
      else:
        return a["type"] > b["type"]
    else:
      return int(a["mana"]) < int(b["mana"])
  else:
    return (b["class"] == "NULL") or ( (a["class"] < b["class"]) and (a["class"] != "NULL") )

def SortCards(cardList):

  for x in range(0, len(cardList)):
    curBest = x
    for y in range(x, len(cardList)):
      if CardIsHigher(cardList[y], cardList[curBest]):
        curBest = y

    temp = cardList[x]
    cardList[x] = cardList[curBest]
    cardList[curBest] = temp

  return cardList

def PrintDeck(deck):
  print decks[deck]["name"] + ", Class: " + decks[deck]["class"] + ", Cost: " + str(decks[deck]["cost"])
  return
  
def PrintDecks(deckList):

  standardDecks = []
  wildDecks = []
  for curDeck in deckList:
    if decks[curDeck]["format"] == "STANDARD":
      standardDecks.append(curDeck)
    elif decks[curDeck]["format"] == "WILD":
      wildDecks.append(curDeck)
    else:
      print "error: Unknown format " + decks[curDeck]["format"]
      continue
      
  standardDecks = SortDecks(standardDecks)
  wildDecks = SortDecks(wildDecks)
  curType = ""
  
  print ""
  print "Standard Decks"
  print "-----------------"
  for curDeck in standardDecks:
    if decks[curDeck]["type"] != curType:
      print ""
      print "  " + decks[curDeck]["type"] + " Decks"
      print "  --------------------------"
      curType = decks[curDeck]["type"]
    PrintDeck(curDeck)
  curType = ""
  print ""
  print "Wild Decks"
  print "-------------"
  for curDeck in wildDecks:
    if decks[curDeck]["type"] != curType:
      print ""
      print "  " + decks[curDeck]["type"] + " Decks"
      print "  --------------------------"
      curType = decks[curDeck]["type"]
    PrintDeck(curDeck)
  print ""
  
  return
  