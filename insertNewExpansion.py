import unirest
import sys

def HandleError(message):
  print message
  sys.exit()

set = ""
for idx in range(1, len(sys.argv)):
  set += sys.argv[idx] + " "
set = set[:-1]

if set == "":
  HandleError("Usage: python unirestTest.py <set name>")

# These code snippets use an open-source library. http://unirest.io/python
try:
  response = unirest.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/" + set,
    headers={
      "X-Mashape-Key": "ku3bC1dtGPmshISX2uNE2Ar5C0Nap1mMM14jsn0ZPPvCY3wAGc"
    }
  )
except:
  HandleError("error: Connection timed out. Check your internet connection.")

try:
  if response.body["error"]:
    HandleError("error: Invalid set")
except:
  print "" # do nothing

# Get file
file = open("cards.txt", "a")

for card in response.body:

  try:
    type = card["type"]
  except:
    continue
    
  if type == "Enchantment":
    continue
  
  try:
    collectible = card["collectible"]
  except:
    continue

  try:
    id = card["cardId"]
    name = card["name"]
    cost = str(card["cost"])
    rarity = card["rarity"]
  except:
    continue

  try:
    race = card["race"]
  except:
    race = "NULL"
  try:
    playerClass = card["playerClass"]
  except:
    playerClass = "NULL"
  try:
    attack = card["attack"]
  except:
    attack = "NULL"
  try:
    health = card["health"]
  except:
    health = "NULL"
  try:
    durability = card["durability"]
  except:
    durability = "NULL"
  try:
    howToGet = card["howToGet"]
  except:
    howToGet = "NULL"
  try:
    howToGetGold = card["howToGetGold"]
  except:
    howToGetGold = "NULL"
    
  # Append card to file
  file.write("\n" + id + "~" + name + "~" + str(cost) + "~" + type + "~" + rarity + "~" + set + "~" + race + "~" + playerClass + "~" + str(attack) + "~" + str(health) + "~" + str(durability) + "~" + howToGet + "~" + howToGetGold)
file.close()