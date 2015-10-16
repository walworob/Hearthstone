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
      
  elif command[:8].upper() == "ADDDECK ":
    
    name = command[8:]
    Class = raw_input("Class: ").upper()
    reachable_ranks = raw_input("Reachable ranks: ")
    cost = raw_input("Cost: ")
    
    cursor.execute("INSERT INTO Decks (name, class, reachable_ranks, cost) VALUES (%s, %s, %s, %s)", [name, Class, reachable_ranks, cost])
    cursor.execute("SELECT id FROM Decks WHERE name=%s AND class=%s AND reachable_ranks=%s AND cost=%s", [name, Class, reachable_ranks, cost])
    deckID = cursor.fetchone()[0]
    
    print "--- >>> <number of cards> <card name>"
    numCards = 0
    while numCards < 30:
    
      entry = raw_input("--- >>> ")
      number = entry[0]
      card = entry[2:]
      
      # Test for validity
      id = validCard(card)
      if id == None:
        print "error: Invalid input, please verify the card name and that you are only inserting one or two"
        
      # Verify the user has the card
      cursor.execute("SELECT amount FROM Possess WHERE id=%s", [id])
      if cursor.fetchone() == None:
        print "error: You don't own that card"
        continue
        
      # Check if the card is already in the deck
      cursor.execute("SELECT amount FROM Contain WHERE card_id=%s AND deck_id=%s", [id, deckID])
      if cursor.fetchone() != None:
        print "error: This card is already in the deck"
        
      # Check if the card is valid for this class
      cursor.execute("SELECT playerClass FROM Cards WHERE id=%s", [id])
      cardClass = cursor.fetchone()[0]
      if cardClass != None:
        if cardClass != Class:
          print "error: Can't add cards from other classes to this deck"
      
  
  
  # Unrecognized command
  else:
    if command != "exit":
      print "Unrecognized command. Available commands are:"
      print "addcard <card name>"
      print "deletecard <card name>"
      print "Use the command 'exit' to exit the program"
      
  
  
  
  
  db.commit()  