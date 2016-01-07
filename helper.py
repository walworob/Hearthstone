RARITY_LIST = ["Common", "Rare", "Epic", "Legendary"]
CLASS_LIST = ["Druid", "Hunter", "Mage", "Paladin", "Priest", "Rogue", "Shaman", "Warlock", "Warrior"]
EXPANSION_LIST = ["Classic", "Goblins vs Gnomes", "The Grand Tournament"]
ADVENTURE_LIST = ["Curse of Naxxramas", "Blackrock Mountain", "League of Explorers"]

cards = {}
decks = {}
contain = {}
possess = {}

def saveCards():
  cardsTXT = open("cards.txt", "w")
  for id in cards:
    cardsTXT.write(id + "\t" + cards[id]["name"] + "\t" + cards[id]["mana"] + "\t" + cards[id]["type"] + "\t" + cards[id]["rarity"] + "\t" + cards[id]["expansion"] + "\t" + cards[id]["race"] + "\t" + cards[id]["class"] + "\t" + cards[id]["attack"] + "\t" + cards[id]["health"] + "\t" + cards[id]["durability"] + "\t" + cards[id]["howToGet"] + "\t" + cards[id]["howToGetGold"] + "\n")
  cardsTXT.close()
  
def saveDecks():
  decksTXT = open("decks.txt", "w")
  for id in decks:
    decksTXT.write(id + "\t" + decks[id]["name"] + "\t" + decks[id]["class"] + "\t" + decks[id]["reachableRanks"] + "\t" + decks[id]["cost"] + "\t" + decks[id]["lastUpdated"] + "\n")
  decksTXT.close()
  
def saveContain():
  containTXT = open("contain.txt", "w")
  for id in contain:
    ids = id.split(",")
    containTXT.write(ids[0] + "\t" + ids[1] + contain[id] + "\n")
  containTXT.close()
  
def savePossess():
  possessTXT = open("possess.txt", "w")
  for id in possess:
    possessTXT.write(id + "\t" + possess[id] + "\n")
  possessTXT.close()

def validCard(name):
  for id in cards:
    if cards[id]["name"] == name:
      return id
      
  print "error: Not a valid card"
  return None

def getAmount(card):
  return card["amount"]
  
def sortDecks(deckList):
  for x in range(0, len(deckList)):
    for y in range(0, len(deckList)):
      if deckList[x]["class"] > deckList[y]["class"]
        

def getNewDeckID():
  highestID = 0
  for id in decks:
    if id > highestID:
      highestID = id
      
  return str(highestID + 1)

def getDeck(deckName):

  # Get decks with that name
  deckList = []
  for id in decks:
    if decks[id]["name"] == deckName:
      deck = []
      deck.append(id)
      deck.append(decks[id]["class"])
      deck.append(decks[id]["cost"])
      deckList.append(deck)
    
  if not deckList:
    print "error: A deck with that name does not exist"
    return None
      
  else:
    deleteDeck = ""
    
    if len(decks) > 1:
      
      print "\nWhich deck is correct?"
      deckCount = 1
        
      for deck in deckList:
        output = str(deckCount) + ") " + name + ", Class: " + str(deck[1]) + ", Cost: " + str(deck[2])
        print output
        deckCount += 1
        
      deckNum = raw_input("\nPlease enter the correct deck number: ")
      while(1):
        
        try:
          deleteDeck = deckList[int(deckNum) - 1]
        except:
          deckNum = raw_input("Please enter a valid number: ")
          continue
        break
      
    # Only one deck
    else:
      deleteDeck = deckList[0]
      
  return deleteDeck[0]
  
def canInsertCard(cardID, deckID):

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
      print "error: Card not in the same class as this deck"
      return False

  # Check if the card is already in the deck
  try:
    amount = contain[cardID + "," + deckID]
    if amount == "2":
      print "error: Already have two of that card in this deck"
      return False
    else:
      rarity = cards[cardID]["rarity"]
      if rarity == "Legendary":
        print "error: Can only have one of a legendary minion in a deck"
        return False
      else:
        contain[cardID + "," + deckID] = "2"
  except:
    contain[cardID + "," + deckID] = "1"
    
  return True
  
def updateCost(id):

  cardSet = []
  for id in contain:
    deckID = id.split(",")[1]
    if deckID == id:
      card = []
      cardID = id.split(",")[0]
      card.append(cardID)
      card.append(cardID]["rarity"])
      card.append(cardID]["expansion"])
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
  
  decks[id]["cost"] = str(cost)