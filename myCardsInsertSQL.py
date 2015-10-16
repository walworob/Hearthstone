import MySQLdb

db = MySQLdb.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  db = "hearthstone"
)
cursor = db.cursor()

file = open("myCards.txt", 'r')

for line in file:
  number = line[0]
  card = line[2:-1]

  cursor.execute("SELECT id FROM Cards WHERE name=%s", [card])
  id = cursor.fetchone()[0]
  cursor.execute("INSERT INTO Possess (id, amount) VALUES (%s, %s)", [id, number])
  
db.commit()