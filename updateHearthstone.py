import MySQLdb

def validCard(name):
  try:
    cursor.execute("SELECT id FROM Cards WHERE name=%s", [name])
    return cursor.fetchone()[0]
  except:
    print "error: Not a valid card"
    return None

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
    
    cursor.execute("INSERT INTO Decks (name, class, reachable_ranks, cost) VALUES (%s, %s, %s, %s)", [name, Class, reachable_ranks, cost])
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
    
    # Get decks with that name
    cursor.execute("SELECT class, cost FROM Decks WHERE name=%s", [name])
    decks = cursor.fetchall()
    
    if not decks:
      print "error: A deck with that name does not exist"
      
    else:
      deleteDeck = ""
    
      if len(decks) > 1:
      
        print "\nWhich deck is correct?"
        deckCount = 1
        
        for curDeck in decks:
          output = str(deckCount) + ") " + name + ", Class: " + str(curDeck[0]) + ", Cost: " + str(curDeck[1])
          print output
          deckCount += 1
        
        deckNum = raw_input("\nPlease enter the number of the deck you would like to delete: ")
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
      
      cursor.execute("SELECT id FROM Decks WHERE name=%s AND class=%s AND cost=%s", [name, deleteDeck[0], deleteDeck[1]])
      id = cursor.fetchone()[0]
      cursor.execute("DELETE FROM Decks WHERE id=%s", [id])
        
  
  # Find which pack to get
  elif command[:5].upper() == "PACK":
  
    chance = {
      "Common": 0.71,
      "Rare": 0.245,
      "Epic": 0.04,
      "Legendary": 0.005
    }
    enchantVal = {
      "Common": 40,
      "Rare": 100,
      "Epic": 400,
      "Legendary": 1600
    }
    disenchantVal = {
      "Common": 5,
      "Rare": 20,
      "Epic": 100,
      "Legendary": 400
    }
    
    expansions = ["Classic", "Goblins vs Gnomes", "The Grand Tournament"]
    data = {}
    for curExp in expansions:
      cursor.execute("SELECT count(*) FROM Cards WHERE expansion=%s GROUP BY rarity", [curExp])
      results = cursor.fetchall()
      data[curExp] = {}
      try:
        data[curExp]["Common"] = results[1][0]
        data[curExp]["Rare"] = results[4][0]
        data[curExp]["Epic"] = results[2][0]
        data[curExp]["Legendary"] = results[3][0]
      except:
        data[curExp]["Common"] = results[0][0]
        data[curExp]["Rare"] = results[3][0]
        data[curExp]["Epic"] = results[1][0]
        data[curExp]["Legendary"] = results[2][0]
      
      print data[curExp]
      
    classicAll = [188, 162, 74, 33]
    gvgAll = [78, 74, 52, 20]
    tgtAll = [49, 36, 27, 20]
    classicMiss = [0, 0, 0, 0]
    gvgMiss = [0, 0, 0, 0]
    tgtMiss = [0, 0, 0, 0]
  
  



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
      print "Use the command 'exit' to exit the program"
      
  
  
  
  
  db.commit()  