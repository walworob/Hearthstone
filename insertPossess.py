cards = {}

cardsTXT = open("cards.txt", "r")
for line in cardsTXT:
  list = line.split("\t")
  id = list[0]
  info = {"name": list[1], "mana": list[2], "type": list[3], "rarity": list[4], "expansion": list[5], "race": list[6], "class": list[7], "attack": list[8], "health": list[9], "durability": list[10], "howToGet": list[11], "howToGetGold": list[12]}
  cards[id] = info
cardsTXT.close()

dontHave = ["Captain's Parrot", "Darnassus Aspirant", "Mulch", "Grove Tender", "Astral Communion", "Dark Wispers", "Malorne", "Aviana", "Cenarius", "Bestial Wrath", "Call Pet", "Feign Death", "Lock and Load", "Steamwheedle Sniper", "Dreadscale", "Metaltooth Leaper", "Stablemaster", "Gladiator's Longbow", "Acidmaw", "Gahz'rilla", "King Krush", "Arcane Blast", "Ice Block", "Spellbender", "Echo of Medivh", "Wee Spellstopper", "Rhonin", "Competitive Spirit", "Coghammer", "Bolvar Fordragon", "Quartermaster", "Enter the Coliseum", "Eadric the Pure", "Tirion Fordring", "Light of the Naaru", "Confuse", "Convert", "Lightwell", "Shadowform", "Mindgames", "Vol'jin", "Lightbomb", "Confessor Paletress", "Preparation", "Patient Assassin", "Cogmaster's Wrench", "Beneath the Grounds", "Edwin VanCleef", "Master of Disguise", "Ogre Ninja", "Trade Prince Gallywix", "Anub'arak", "Vitality Totem", "Powermace", "Elemental Destruction", "Far Sight", "Healing Wave", "Charged Hammer", "Ancestor's Call", "Dunemaul Shaman", "Siltfin Spiritwalker", "Earth Elemental", "The Mistcaller", "Neptulon", "Al'Akir the Windlord", "Mistress of Pain", "Dreadsteed", "Bane of Doom", "Dark Bargain", "Anima Golem", "Wilfred Fizzlebang", "Twisting Nether", "Lord Jaraxxus", "Mal'Ganis", "Shield Slam", "Commanding Shout", "Bouncing Blade", "Brawl", "Iron Juggernaut", "Sea Reaver", "Gorehowl", "Crush", "Grommash Hellscream", "Varian Wrynn", "Angry Chicken", "Hungry Crab", "Lightwarden", "Argent Watchman", "Bloodmage Thalnos", "Garrison Commander", "Lorewalker Cho", "Mana Addict", "Millhouse Manastorm", "Nat Pagle", "Recombobulator", "Blood Knight", "Eydis Darkbane", "Fjola Lightbane", "Gnomish Experimenter", "Hobgoblin", "King Mukla", "Murloc Warleader", "Tinkmaster Overspark", "Ancient Mage", "Crowd Favorite", "Gormok the Impaler", "Twilight Guardian", "Blingtron 3000", "Old Murk-Eye", "Captain Greenskin", "Elite Tauren Chieftain", "Fel Reaver", "Harrison Jones", "Hemet Nesingwary", "Junkbot", "Leeroy Jenkins", "Nexus-Champion Saraad", "Recruiter", "Cairne Bloodhoof", "Gazlowe", "Gelbin Mekkatorque", "Illidan Stormrage", "Justicar Trueheart", "Mogor the Ogre", "Sideshow Spelleater", "Sylvanas Windrunner", "The Black Knight", "The Skeleton Knight", "Toshley", "Chillmaw", "Skycap'n Kragg", "Troggzor the Earthinator", "Foe Reaper 4000", "Gruul", "Ragnaros the Firelord", "Sneed's Old Shredder", "Alexstrasza", "Icehowl", "Malygos", "Mekgineer Thermaplugg", "Nozdormu", "Onyxia", "Ysera", "Deathwing", "Frost Giant", "Mountain Giant", "Molten Giant"]
haveOne = ["Savage Combatant", "Soot Spewer", "Fencing Coach", "Bite", "Force of Nature", "Mech-Bear-Cat", "Ancient of Lore", "Ancient of War", "Tree of Life", "Misdirection", "Powershot", "Explosive Shot", "Ball of Spiders", "Effigy", "Spellslinger", "Ethereal Arcanist", "Coldarra Drake", "Argent Lance", "Scarlet Purifier", "Holy Wrath", "Flash Heal", "Shadowbomber", "Wyrmrest Agent", "Shadowfiend", "Mass Dispel", "Burgle", "Iron Sensei", "Poisoned Blade", "Sabotage", "Kidnapper", "Lava Burst", "Mana Tide Totem", "Doomhammer", "Thunder Bluff Valiant", "Tiny Knight of Evil", "Felguard", "Void Terror", "Shadowflame", "Fel Cannon", "Demonheart", "Void Crusher", "Fearsome Doomguard", "Alexstrasza's Champion", "Magnataur Alpha", "Screwjank Clunker", "Injured Kvaldir", "Secretkeeper", "Young Dragonhawk", "Master Swordsmith", "Arcane Golem", "Big Game Hunter", "Coldlight Seer", "Emperor Cobra", "Goblin Sapper", "Illuminator", "Light's Champion", "Mind Control Tech", "Lil' Exorcist", "Questing Adventurer", "Saboteur", "Southsea Captain", "Arcane Nullifier X-21", "Evil Heckler", "Enhance-o Mechano", "Mini-Mage", "Violet Teacher", "Faceless Maniupulator", "Madder Bomber", "Mukla's Champion", "Kodorider", "Piloted Sky Golem", "Ravenholdt Assassin", "Sea Giant", "Clockwork Gnome"]

possessTXT = open("possess.txt", "w")
for id in cards:
  if cards[id]["name"] not in dontHave:
    if cards[id]["name"] in haveOne or cards[id]["rarity"] == "Legendary":
      possessTXT.write(id + "\t1\n")
    else:
      possessTXT.write(id + "\t2\n")
possessTXT.close()