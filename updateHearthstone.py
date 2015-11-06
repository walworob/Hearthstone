import MySQLdb

def validCard(name):
  try:
    cursor.execute("SELECT id FROM Cards WHERE name=%s", [name])
    return cursor.fetchone()[0]
  except:
    print "error: Not a valid card"
    return None
    
def getAmount(card):
  return card["amount"]

def getDeck(deckName):

  # Get decks with that name
  cursor.execute("SELECT class, cost FROM Decks WHERE name=%s", [name])
  decks = cursor.fetchall()
    
  if not decks:
    print "error: A deck with that name does not exist"
    return None
      
  else:
    deleteDeck = ""
    
    if len(decks) > 1:
      
      print "\nWhich deck is correct?"
      deckCount = 1
        
      for curDeck in decks:
        output = str(deckCount) + ") " + name + ", Class: " + str(curDeck[0]) + ", Cost: " + str(curDeck[1])
        print output
        deckCount += 1
        
      deckNum = raw_input("\nPlease enter the correct deck number: ")
      while(1):
        
        try:
          deleteDeck = decks[int(deckNum) - 1]
        except:
          deckNum = raw_input("Please enter a valid number: ")
          continue
        break
      
    # Only one deck
    else:
      deleteDeck = decks[0]
      
  return deleteDeck

db = MySQLdb.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  db = "hearthstone"
)
cursor = db.cursor()

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
    
    # Find how many of that card the user owns
    cursor.execute("SELECT amount FROM Possess WHERE id=%s", [id])
    number = cursor.fetchone()
    
    # Update the database based on amount
    if number == None:
      cursor.execute("INSERT INTO Possess (id, amount) VALUE (%s, %s)", [id, '1'])
    elif number[0] == 1:
      cursor.execute("UPDATE Possess SET amount=2 WHERE id=%s", [id])
    else:
      print "error: You already have two of that card"
      

  # Delete a card from the collection
  elif command[:11].upper() == "DELETECARD ":
  
    card = command[11:]
    
    # Test for validity
    id = validCard(card)
    if id == None:
      print "error: Not a valid card"
      continue
    
    # Find how many of that card the user owns
    cursor.execute("SELECT amount FROM Possess WHERE id=%s", [id])
    number = cursor.fetchone()
    
    # Update database based on amount
    if number == None:
      print "error: You do not own that card"
    elif number[0] == 2:
      cursor.execute("UPDATE Possess SET amount=1 WHERE id=%s", [id])
    else:
      cursor.execute("DELETE FROM Possess WHERE id=%s", [id])
  
  
  # Add a deck to the users collection
  elif command[:8].upper() == "ADDDECK ":
    
    name = command[8:]
    Class = raw_input("Class: ")
    reachable_ranks = raw_input("Reachable ranks: ")
    cost = raw_input("Cost: ")
    last_updated = raw_input("Last updated: ")
    
    cursor.execute("INSERT INTO Decks (name, class, reachable_ranks, cost, last_updated) VALUES (%s, %s, %s, %s, %s)", [name, Class, reachable_ranks, cost, last_updated])
    cursor.execute("SELECT id FROM Decks WHERE name=%s AND class=%s AND reachable_ranks=%s AND cost=%s ORDER BY id DESC", [name, Class, reachable_ranks, cost])
    deckID = cursor.fetchone()[0]
    
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
        
      # Check if the card is already in the deck
      cursor.execute("SELECT amount FROM Contain WHERE card_id=%s AND deck_id=%s", [id, deckID])
      if cursor.fetchone() != None:
        print "error: This card is already in the deck"
        continue
        
      # Check if the card is valid for this class
      cursor.execute("SELECT playerClass FROM Cards WHERE id=%s", [id])
      cardClass = cursor.fetchone()[0]
      if cardClass != None:
        if cardClass != Class:
          print "error: Can't add cards from other classes to this deck"
          continue
          
      # Check and make sure the number of cards is valid
      if number == 2:
     
        # Can only have one legendary in a deck
        cursor.execute("SELECT rarity FROM Cards WHERE id=%s", [id])
        rarity = cursor.fetchone()[0]
        if rarity == "Legendary":
          print "error: Can only have one of that card in a deck"
          continue
        
        # Can't accidentally make a deck with 31 cards
        if numCards == 29:
          print "error: Only one card slot open"
          continue
          
      # Invalid number of cards
      elif number != 1:
        print "error: Can only have one or two cards in a deck"
        continue
        
      # Add the card to the deck
      cursor.execute("INSERT INTO Contain (card_id, deck_id, amount) VALUES (%s, %s, %s)", [id, deckID, str(number)])
      numCards += number
      
      
  # Delete a deck
  elif command[:11].upper() == "DELETEDECK ":
  
    name = command[11:]
    
    deleteDeck = getDeck(name)
    if deleteDeck == None:
      continue
      
    cursor.execute("SELECT id FROM Decks WHERE name=%s AND class=%s AND cost=%s", [name, deleteDeck[0], deleteDeck[1]])
    id = cursor.fetchone()[0]
    cursor.execute("DELETE FROM Decks WHERE id=%s", [id])
        
  
  # Find which pack to get
  elif command.upper() == "PACK":
  
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
    
    print "\nHighest number has greatest value"
    print "--------------------------------------"
    
    expansions = ["Classic", "Goblins vs Gnomes", "The Grand Tournament"]
    all = {}
    miss = {}
    for curExp in expansions:
      cursor.execute("SELECT count(*) FROM Cards WHERE expansion=%s GROUP BY rarity", [curExp])
      results = cursor.fetchall()
      cursor.execute("SELECT SUM(P.amount) AS Amount, C.rarity FROM Possess P, Cards C WHERE P.id=C.id AND C.expansion=%s GROUP BY rarity", [curExp])
      amounts = cursor.fetchall()
      try:
        all["Common"] = 2 * results[1][0]
        all["Rare"] = 2 * results[4][0]
        all["Epic"] = 2 * results[2][0]
        all["Legendary"] = results[3][0]
        miss["Common"] = all["Common"] - amounts[1][0]
        miss["Rare"] = all["Rare"] - amounts[4][0]
        miss["Epic"] = all["Epic"] - amounts[2][0]
        miss["Legendary"] = all["Legendary"] - amounts[3][0]
      except:
        all["Common"] = 2 * results[0][0]
        all["Rare"] = 2 * results[3][0]
        all["Epic"] = 2 * results[1][0]
        all["Legendary"] = results[2][0]
        miss["Common"] = all["Common"] - amounts[0][0]
        miss["Rare"] = all["Rare"] - amounts[3][0]
        miss["Epic"] = all["Epic"] - amounts[1][0]
        miss["Legendary"] = all["Legendary"] - amounts[2][0]
      
      total = 0
      for i in ["Common", "Rare", "Epic", "Legendary"]:
        val = chance[i] * (float((all[i] - miss[i]) / all[i]) * disenchantVal[i] + float(miss[i] / all[i]) * enchantVal[i]) 
        total += val
        
      print curExp + ": " + str(total * 5)

      
  # Find out decks the user can make
  elif command.upper() == "CANMAKE" or command[:8].upper() == "CANMAKE ":
  
    if command.upper() == "CANMAKE":
      cursor.execute("SELECT * FROM Decks ORDER BY class, last_updated DESC")
    else:
      cursor.execute("SELECT * FROM Decks WHERE class=%s ORDER BY last_updated DESC", command[8:])
        
    decks = cursor.fetchall()
    if not decks:
      print "error: Not a valid class"
      continue
    
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
        if numCompleteDecks == 0:
          print "\n"
        print str(numCompleteDecks + 1) + ") " + name + ", Class: " + Class + ", Cost: " + str(cost)
        numCompleteDecks += 1
        
    print "\n"
          
        
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
    for i in range(5):
      print cards[i]["name"] + " will give you " + str(cards[i]["amount"]) + " value"
    
      
  elif command[:10].upper() == "PRINTLIST ":
    
    name = command[10:]
    
    deckInfo = getDeck(name)
    if deckInfo == None:
      continue
    
    cursor.execute("SELECT id FROM Decks WHERE name=%s AND class=%s AND cost=%s", [name, deckInfo[0], deckInfo[1]])
    id = cursor.fetchone()[0]
    
    cursor.execute("SELECT c.name, d.amount FROM Cards c, Contain d WHERE c.id=d.card_id AND d.deck_id=%s ORDER BY c.playerClass DESC, c.cost, c.type DESC, c.name", id)
    deck = cursor.fetchall()
    for card in deck:
      print str(card[1]) + "x " + card[0]
      
  elif command[:11].upper() == "PRINTDECKS ":
  
    Class = command[11:]
    
    cursor.execute("SELECT name, cost FROM Decks WHERE class=%s ORDER BY last_updated DESC", Class)
    decks = cursor.fetchall()
    for curDeck in decks:
      print curDeck[0] + ", Cost: " + str(curDeck[1])
        
      
  
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
      print "Use the command 'exit' to exit the program"
      
  
  
  
  
  db.commit()  