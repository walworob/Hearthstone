import MySQLdb

db = MySQLdb.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  db = "hearthstone"
)
cursor = db.cursor()

cursor.execute("SELECT * FROM Possess")
cards = cursor.fetchall()
file = open("myCards.txt", 'w')

for curCard in cards:
  id = curCard[0]
  num = str(curCard[1])
  
  cursor.execute("SELECT name FROM Cards WHERE id=%s", [id])
  name = cursor.fetchone()[0]
  
  line = num + " " + name
  file.write(line + "\n")