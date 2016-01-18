RARITY_LIST = ["Common", "Rare", "Epic", "Legendary"]
CLASS_LIST = ["Druid", "Hunter", "Mage", "Paladin", "Priest", "Rogue", "Shaman", "Warlock", "Warrior"]
EXPANSION_LIST = ["Classic", "Goblins vs Gnomes", "The Grand Tournament"]
ADVENTURE_LIST = ["Curse of Naxxramas", "Blackrock Mountain", "League of Explorers"]

cards = {}
decks = {}
contain = {}
possess = {}

def saveDecks():
  decksTXT = open("decks.txt", "wb")
  for id in decks:
    decksTXT.write(id + "~" + decks[id]["name"] + "~" + decks[id]["class"] + "~" + decks[id]["type"] + "~" + str(decks[id]["cost"]) + "~" + decks[id]["lastUpdated"] + '\n')
  decksTXT.close()
  
def saveContain():
  containTXT = open("contain.txt", "wb")
  for id in contain:
    ids = id.split(",")
    containTXT.write(ids[0] + "," + ids[1] + "~" + str(contain[id]) + "\n")
  containTXT.close()
  
def savePossess():
  possessTXT = open("possess.txt", "wb")
  for id in possess:
    possessTXT.write(id + "~" + str(possess[id]) + "\n")
  possessTXT.close()

  
  
def validCard(name):
  for id in cards:
    if cards[id]["name"] == name:
      return id
      
  print "error: Not a valid card"
  return None

  
  
def getAmount(card):
  return card["amount"]        

  
  
def getNewDeckID():
  highestID = 0
  for id in decks:
    if int(id) > highestID:
      highestID = int(id)
      
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
    
    if len(deckList) > 1:
      
      print "\nWhich deck is correct?"
      deckCount = 1
        
      for deck in deckList:
        output = str(deckCount) + ") " + deckName + ", Class: " + str(deck[1]) + ", Cost: " + str(deck[2])
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



def updateCost(deckID):

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
def higherType(deckA, deckB):
  a = deckA["type"].upper()
  b = deckB["type"].upper()
  if a != "META":
    if a != "UNIQUE":
      if a != "BUDGET":
        return b == "SOLO"
      else:
        return b == "SOLO" or b == "UNIQUE"
    else:
      return b != "META"
  else:
    return True

def isHigher(deckA, deckB):
  if deckA["class"] == deckB["class"]:
    if deckA["type"] == deckB["type"]:
      if deckA["lastUpdated"] == deckB["lastUpdated"]:
        return True
      else:
        return deckA["lastUpdated"] > deckB["lastUpdated"]
    else:
      return higherType(deckA, deckB)
  else:
    return deckA["class"] < deckB["class"]
    
def sortDecks(deckList):
  
  if len(deckList) == 1:
    return deckList
  
  firstHalf = deckList[:len(deckList)/2]
  secondHalf = deckList[len(deckList)/2:]
  firstHalf = sortDecks(firstHalf)
  secondHalf = sortDecks(secondHalf)
  
  i = 0
  j = 0
  k = 0
  while (i != len(firstHalf) and j != len(secondHalf) ):
    if i != len(firstHalf) and j != len(secondHalf):
      if isHigher(firstHalf[i], secondHalf[j]):
        deckList[k] = dict(firstHalf[i])
        k += 1
        i += 1
      else:
        deckList[k] = dict(secondHalf[j])
        k += 1
        j += 1
    else:
      if i == len(firstHalf):
        deckList[k] = dict(secondHalf[j])
        k += 1
        j += 1
      else:
        deckList[k] = dict(firstHalf[i])
        k += 1
        i += 1
  
  return deckList
  
















