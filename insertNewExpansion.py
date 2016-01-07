import json

JSON_datalist = r"""
{
  "League of Explorers": [
    {
      "id": "LOEA04_28",
      "name": "A Glowing Pool",
      "type": "Spell",
      "cost": 0,
      "text": "<b>Drink?</b>"
    },
    {
      "id": "LOE_110t",
      "name": "Ancient Curse",
      "type": "Spell",
      "cost": 0,
      "text": "When you draw this, take 7 damage and draw a card.",
      "artist": "Slawomir Maniak",
      "mechanics": [
        "ImmuneToSpellpower"
      ]
    },
    {
      "id": "LOEA13_2",
      "name": "Ancient Power",
      "type": "Hero Power",
      "cost": 0,
      "text": "<b>Hero Power</b>\nGive each player a random card. It costs (0)."
    },
    {
      "id": "LOEA13_2H",
      "name": "Ancient Power",
      "type": "Hero Power",
      "cost": 0,
      "text": "<b>Hero Power</b>\nAdd a random card to your hand. It costs (0)."
    },
    {
      "id": "LOE_110",
      "name": "Ancient Shade",
      "type": "Minion",
      "rarity": "Rare",
      "cost": 4,
      "attack": 7,
      "health": 4,
      "text": "<b>Battlecry:</b> Shuffle an 'Ancient Curse' into your deck that deals 7 damage to you when drawn.",
      "flavor": "Warning: Do not expose to direct sunlight.",
      "artist": "Slawomir Maniak",
      "collectible": "true",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA06_03",
      "name": "Animate Earthen",
      "type": "Spell",
      "cost": 2,
      "text": "Give your minions +1/+1 and <b>Taunt</b>."
    },
    {
      "id": "LOEA06_03h",
      "name": "Animate Earthen",
      "type": "Spell",
      "cost": 2,
      "text": "Give your minions +3/+3 and <b>Taunt</b>."
    },
    {
      "id": "LOEA06_03e",
      "name": "Animated",
      "type": "Enchantment",
      "text": "+1/+1 and <b>Taunt</b>."
    },
    {
      "id": "LOEA06_03eh",
      "name": "Animated",
      "type": "Enchantment",
      "text": "+3/+3 and <b>Taunt</b>."
    },
    {
      "id": "LOE_119",
      "name": "Animated Armor",
      "type": "Minion",
      "rarity": "Rare",
      "cost": 4,
      "attack": 4,
      "health": 4,
      "text": "Your hero can only take 1 damage at a time.",
      "flavor": "Try putting it on.  Wait, let me get my camera.",
      "artist": "Mike Sass",
      "collectible": "true",
      "playerClass": "Mage"
    },
    {
      "id": "LOEA04_27",
      "name": "Animated Statue",
      "type": "Minion",
      "cost": 1,
      "attack": 10,
      "health": 10,
      "text": "You've disturbed the ancient statue..."
    },
    {
      "id": "LOEA16_17",
      "name": "Animated Statue",
      "type": "Minion",
      "cost": 10,
      "attack": 10,
      "health": 10
    },
    {
      "id": "LOE_061",
      "name": "Anubisath Sentinel",
      "type": "Minion",
      "rarity": "Common",
      "cost": 5,
      "attack": 4,
      "health": 4,
      "text": "<b>Deathrattle:</b> Give a random friendly minion +3/+3.",
      "flavor": "He's actually a 1/1 who picked up the hammer from the last guy.",
      "artist": "Paul Mafayon",
      "collectible": "true",
      "mechanics": [
        "Deathrattle"
      ]
    },
    {
      "id": "LOEA04_24h",
      "name": "Anubisath Temple Guard",
      "type": "Minion",
      "cost": 8,
      "attack": 6,
      "health": 15
    },
    {
      "id": "LOEA04_24",
      "name": "Anubisath Temple Guard",
      "type": "Minion",
      "cost": 8,
      "attack": 5,
      "health": 10
    },
    {
      "id": "LOE_026",
      "name": "Anyfin Can Happen",
      "type": "Spell",
      "rarity": "Rare",
      "cost": 10,
      "text": "Summon 7 Murlocs that died this game.",
      "flavor": "Theme song by Ellie Goldfin and Blagghghlrlrl Harris.",
      "artist": "Ryan Metcalf",
      "collectible": "true",
      "playerClass": "Paladin"
    },
    {
      "id": "LOE_092",
      "name": "Arch-Thief Rafaam",
      "type": "Minion",
      "rarity": "Legendary",
      "cost": 9,
      "attack": 7,
      "health": 8,
      "text": "<b>Battlecry: Discover</b> a powerful Artifact.",
      "flavor": "He's very good at retrieving artifacts.  From other people's museums.",
      "artist": "Alex Horley Orlandelli",
      "collectible": "true",
      "elite": true,
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA16_22",
      "name": "Archaedas",
      "type": "Minion",
      "cost": 5,
      "attack": 5,
      "health": 5,
      "text": "At the end of your turn, turn a random enemy minion into a 0/2 Statue.",
      "elite": true
    },
    {
      "id": "LOEA08_01",
      "name": "Archaedas",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA16_22H",
      "name": "Archaedas",
      "type": "Minion",
      "cost": 10,
      "attack": 10,
      "health": 10,
      "text": "At the end of your turn, turn a random enemy minion into a 0/2 Statue.",
      "elite": true
    },
    {
      "id": "LOEA07_21",
      "name": "Barrel Forward",
      "type": "Spell",
      "cost": 1,
      "text": "Get 1 turn closer to the Exit!"
    },
    {
      "id": "LOEA16_7",
      "name": "Benediction Splinter",
      "type": "Spell",
      "cost": 0,
      "text": "Restore #10 Health to ALL characters."
    },
    {
      "id": "LOEA16_20e",
      "name": "Blessed",
      "type": "Enchantment",
      "text": "<b>Immune</b> this turn.",
      "mechanics": [
        "OneTurnEffect"
      ]
    },
    {
      "id": "LOEA16_20H",
      "name": "Blessing of the Sun",
      "type": "Enchantment",
      "text": "<b>Immune</b>."
    },
    {
      "id": "LOEA16_20",
      "name": "Blessing of the Sun",
      "type": "Spell",
      "cost": 1,
      "text": "Give a minion <b>Immune</b> this turn."
    },
    {
      "id": "LOEA01_02h",
      "name": "Blessings of the Sun",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\n Phaerix is <b>Immune</b> while he controls the Rod of the Sun."
    },
    {
      "id": "LOEA01_02",
      "name": "Blessings of the Sun",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\nWhoever controls the Rod of the Sun is <b>Immune.</b>"
    },
    {
      "id": "LOEA15_3",
      "name": "Boneraptor",
      "type": "Minion",
      "cost": 3,
      "attack": 2,
      "health": 2,
      "text": "<b>Battlecry:</b>Take control of your opponent's weapon."
    },
    {
      "id": "LOEA15_3H",
      "name": "Boneraptor",
      "type": "Minion",
      "cost": 3,
      "attack": 2,
      "health": 2,
      "text": "<b>Battlecry:</b>Take control of your opponent's weapon."
    },
    {
      "id": "LOEA07_20",
      "name": "Boom!",
      "type": "Spell",
      "cost": 1,
      "text": "Deal 3 damage to all enemy minions."
    },
    {
      "id": "LOE_077",
      "name": "Brann Bronzebeard",
      "type": "Minion",
      "rarity": "Legendary",
      "cost": 3,
      "attack": 2,
      "health": 4,
      "text": "Your <b>Battlecries</b> trigger twice.",
      "flavor": "Contains 75% more fiber than his brother Magni!",
      "artist": "Sam Nielson",
      "collectible": "true",
      "elite": true,
      "mechanics": [
        "Aura"
      ]
    },
    {
      "id": "LOEA09_7H",
      "name": "Cauldron",
      "type": "Minion",
      "cost": 0,
      "attack": 0,
      "health": 10,
      "text": "<b>Taunt</b>\n<b>Deathrattle:</b> Save Sir Finley!",
      "mechanics": [
        "Deathrattle",
        "Taunt"
      ]
    },
    {
      "id": "LOEA09_7e",
      "name": "Cauldron",
      "type": "Enchantment"
    },
    {
      "id": "LOEA09_7",
      "name": "Cauldron",
      "type": "Minion",
      "cost": 0,
      "attack": 0,
      "health": 5,
      "text": "<b>Taunt</b>\n<b>Deathrattle:</b> Save Sir Finley and stop the Naga onslaught!",
      "mechanics": [
        "Deathrattle",
        "Taunt"
      ]
    },
    {
      "id": "LOEA07_09",
      "name": "Chasing Trogg",
      "type": "Minion",
      "cost": 4,
      "attack": 2,
      "health": 6
    },
    {
      "id": "LOEA05_01",
      "name": "Chieftain Scarvash",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA16_21",
      "name": "Chieftain Scarvash",
      "type": "Minion",
      "cost": 5,
      "attack": 5,
      "health": 5,
      "text": "Enemy cards cost (1) more.",
      "elite": true,
      "mechanics": [
        "Aura"
      ]
    },
    {
      "id": "LOEA16_21H",
      "name": "Chieftain Scarvash",
      "type": "Minion",
      "cost": 10,
      "attack": 10,
      "health": 10,
      "text": "Enemy cards cost (2) more.",
      "elite": true,
      "mechanics": [
        "Aura"
      ]
    },
    {
      "id": "LOEA07_26",
      "name": "Consult Brann",
      "type": "Spell",
      "cost": 1,
      "text": "Draw 3 cards."
    },
    {
      "id": "LOEA16_11",
      "name": "Crown of Kael'thas",
      "type": "Spell",
      "cost": 0,
      "text": "Deal $10 damage randomly split among ALL characters."
    },
    {
      "id": "LOE_007",
      "name": "Curse of Rafaam",
      "type": "Spell",
      "rarity": "Common",
      "cost": 2,
      "text": "Give your opponent a 'Cursed!' card.\nWhile they hold it, they take 2 damage on their turn.",
      "flavor": "This is what happens when Rafaam stubs his toe unexpectedly.",
      "artist": "Alex Horley Orlandelli",
      "collectible": "true",
      "playerClass": "Warlock"
    },
    {
      "id": "LOE_118",
      "name": "Cursed Blade",
      "type": "Weapon",
      "rarity": "Rare",
      "cost": 1,
      "attack": 2,
      "durability": 3,
      "text": "Double all damage dealt to your hero.",
      "flavor": "The Curse is that you have to listen to \"MMMBop\" on repeat.",
      "artist": "Craig Mullins",
      "collectible": "true",
      "playerClass": "Warrior"
    },
    {
      "id": "LOE_118e",
      "name": "Cursed Blade",
      "type": "Enchantment",
      "text": "Double all damage dealt to your hero.",
      "playerClass": "Warrior"
    },
    {
      "id": "LOE_007t",
      "name": "Cursed!",
      "type": "Spell",
      "cost": 2,
      "text": "While this is in your hand, take 2 damage at the start of your turn.",
      "artist": "Jim Nelson",
      "playerClass": "Warlock",
      "mechanics": [
        "ImmuneToSpellpower"
      ]
    },
    {
      "id": "LOE_023",
      "name": "Dark Peddler",
      "type": "Minion",
      "rarity": "Common",
      "cost": 2,
      "attack": 2,
      "health": 2,
      "text": "<b>Battlecry: Discover</b> a\n1-Cost card.",
      "flavor": "I'm offering you a bargain here!  This amazing vacuum cleaner for your soul!",
      "artist": "George Davis",
      "collectible": "true",
      "playerClass": "Warlock",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOE_021",
      "name": "Dart Trap",
      "type": "Spell",
      "rarity": "Common",
      "cost": 2,
      "text": "<b>Secret:</b> When an opposing Hero Power is used, deal 5 damage to a random enemy.",
      "flavor": "Five years of tap-dancing lessons are FINALLY going to pay off!",
      "artist": "Zoltan Boros",
      "collectible": "true",
      "playerClass": "Hunter",
      "mechanics": [
        "Secret"
      ]
    },
    {
      "id": "LOEA07_11",
      "name": "Debris",
      "type": "Minion",
      "cost": 1,
      "attack": 0,
      "health": 3,
      "text": "<b>Taunt.</b>",
      "mechanics": [
        "Taunt"
      ]
    },
    {
      "id": "LOE_020",
      "name": "Desert Camel",
      "type": "Minion",
      "rarity": "Common",
      "cost": 3,
      "attack": 2,
      "health": 4,
      "text": "<b>Battlecry:</b> Put a 1-Cost minion from each deck into the battlefield.",
      "flavor": "Dang.  This card is sweet.  Almost as sweet as Dessert Camel.",
      "artist": "Matt Dixon",
      "collectible": "true",
      "race": "Beast",
      "playerClass": "Hunter",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA02_02",
      "name": "Djinn's Intuition",
      "type": "Hero Power",
      "cost": 0,
      "text": "Draw a card.\nGive your opponent a Wish."
    },
    {
      "id": "LOEA02_02h",
      "name": "Djinn's Intuition",
      "type": "Hero Power",
      "cost": 0,
      "text": "Draw a card. Gain a Mana Crystal. Give your opponent a Wish."
    },
    {
      "id": "LOE_053",
      "name": "Djinni of Zephyrs",
      "type": "Minion",
      "rarity": "Epic",
      "cost": 5,
      "attack": 4,
      "health": 6,
      "text": "Whenever you cast a spell on another friendly minion, cast a copy of it on this one.",
      "flavor": "If you want your wish granted, don't rub him the wrong way.",
      "artist": "Jakub Kasper",
      "collectible": "true"
    },
    {
      "id": "LOEA04_28a",
      "name": "Drink Deeply",
      "type": "Spell",
      "cost": 0,
      "text": "Draw a card."
    },
    {
      "id": "LOEA07_18",
      "name": "Dynamite",
      "type": "Spell",
      "cost": 1,
      "text": "Deal $10 damage."
    },
    {
      "id": "LOEA07_12",
      "name": "Earthen Pursuer",
      "type": "Minion",
      "cost": 5,
      "attack": 4,
      "health": 6
    },
    {
      "id": "LOEA06_02t",
      "name": "Earthen Statue",
      "type": "Minion",
      "cost": 1,
      "attack": 0,
      "health": 2
    },
    {
      "id": "LOEA06_02th",
      "name": "Earthen Statue",
      "type": "Minion",
      "cost": 1,
      "attack": 0,
      "health": 5
    },
    {
      "id": "LOE_107",
      "name": "Eerie Statue",
      "type": "Minion",
      "rarity": "Rare",
      "cost": 4,
      "attack": 7,
      "health": 7,
      "text": "Can't attack unless it's the only minion in the battlefield.",
      "flavor": "Don't blink!  Don't turn your back, don't look away, and DON'T BLINK.",
      "artist": "Jim Nelson",
      "collectible": "true"
    },
    {
      "id": "LOE_079",
      "name": "Elise Starseeker",
      "type": "Minion",
      "rarity": "Legendary",
      "cost": 4,
      "attack": 3,
      "health": 5,
      "text": "<b>Battlecry:</b> Shuffle the 'Map to the Golden Monkey'   into your deck.",
      "flavor": "A large part of her job entails not mixing up the Map to the Golden Monkey with the Map to Monkey Island.",
      "artist": "Luke Mancini",
      "collectible": "true",
      "elite": true,
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA09_3H",
      "name": "Endless Hunger",
      "type": "Hero Power",
      "cost": 0,
      "text": "<b>Hero Power</b>\nSummon a Hungry Naga."
    },
    {
      "id": "LOEA09_2eH",
      "name": "Enraged",
      "type": "Enchantment",
      "text": "+5 Attack",
      "mechanics": [
        "OneTurnEffect"
      ]
    },
    {
      "id": "LOEA09_2e",
      "name": "Enraged",
      "type": "Enchantment",
      "text": "+2 Attack",
      "mechanics": [
        "OneTurnEffect"
      ]
    },
    {
      "id": "LOEA09_2H",
      "name": "Enraged!",
      "type": "Hero Power",
      "cost": 2,
      "text": "Give your hero +5 attack this turn."
    },
    {
      "id": "LOEA09_2",
      "name": "Enraged!",
      "type": "Hero Power",
      "cost": 2,
      "text": "Give your hero +2 attack this turn."
    },
    {
      "id": "LOE_104",
      "name": "Entomb",
      "type": "Spell",
      "rarity": "Common",
      "cost": 6,
      "text": "Choose an enemy minion.\nShuffle it into your deck.",
      "flavor": "It's perfectly safe as long as you remember to put in air holes.",
      "artist": "Alex Konstad",
      "collectible": "true",
      "playerClass": "Priest"
    },
    {
      "id": "LOEA04_02",
      "name": "Escape!",
      "type": "Hero Power",
      "rarity": "Free",
      "cost": 0,
      "text": "Encounter new obstacles!"
    },
    {
      "id": "LOEA04_02h",
      "name": "Escape!",
      "type": "Hero Power",
      "cost": 0,
      "text": "Encounter new obstacles!"
    },
    {
      "id": "LOE_003",
      "name": "Ethereal Conjurer",
      "type": "Minion",
      "rarity": "Common",
      "cost": 5,
      "attack": 6,
      "health": 3,
      "text": "<b>Battlecry: Discover</b> a spell.",
      "flavor": "Despite the name, he's a solid conjurer.",
      "artist": "Ben Zhang",
      "collectible": "true",
      "playerClass": "Mage",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOE_113",
      "name": "Everyfin is Awesome",
      "type": "Spell",
      "rarity": "Rare",
      "cost": 7,
      "text": "Give your minions +2/+2.\nCosts (1) less for each Murloc you control.",
      "flavor": "Everyfin is cool when you're part of a murloc team!",
      "artist": "Andrius Matijoshius",
      "collectible": "true",
      "playerClass": "Shaman"
    },
    {
      "id": "LOE_111",
      "name": "Excavated Evil",
      "type": "Spell",
      "rarity": "Rare",
      "cost": 5,
      "text": "Deal $3 damage to all minions.\nShuffle this card into your opponent's deck.",
      "flavor": "MOM! DAD! DON'T TOUCH IT! IT'S EVIL!!!!!!",
      "artist": "Raymond Swanland",
      "collectible": "true",
      "playerClass": "Priest"
    },
    {
      "id": "LOE_105e",
      "name": "Explorer's Hat",
      "type": "Enchantment",
      "text": "+1/+1. <b>Deathrattle:</b> Add an Explorer's Hat to your hand.",
      "playerClass": "Hunter"
    },
    {
      "id": "LOE_105",
      "name": "Explorer's Hat",
      "type": "Spell",
      "rarity": "Rare",
      "cost": 2,
      "text": "Give a minion +1/+1 and \"<b>Deathrattle:</b> Add an Explorer's Hat to your hand.\"",
      "flavor": "Harrison Jones was disappointed that he didn't get to be part of the League of Explorers, but his hat did.",
      "artist": "Joe Wilson",
      "collectible": "true",
      "playerClass": "Hunter"
    },
    {
      "id": "LOE_008",
      "name": "Eye of Hakkar",
      "type": "Spell",
      "cost": 1,
      "text": "Take a secret from your opponent's deck and put it into the battlefield.",
      "flavor": "-"
    },
    {
      "id": "LOE_008H",
      "name": "Eye of Hakkar",
      "type": "Spell",
      "cost": 1,
      "text": "Take a secret from your opponent's deck and put it into the battlefield."
    },
    {
      "id": "LOEA16_13",
      "name": "Eye of Orsis",
      "type": "Spell",
      "cost": 0,
      "text": "<b>Discover</b> a minion and gain 3 copies of it."
    },
    {
      "id": "LOEA09_3aH",
      "name": "Famished",
      "type": "Enchantment",
      "text": "Quite Hungry."
    },
    {
      "id": "LOEA09_3a",
      "name": "Famished",
      "type": "Enchantment",
      "text": "Quite Hungry."
    },
    {
      "id": "LOE_022",
      "name": "Fierce Monkey",
      "type": "Minion",
      "rarity": "Common",
      "cost": 3,
      "attack": 3,
      "health": 4,
      "text": "<b>Taunt</b>",
      "flavor": "Fierce monkey.  That funky monkey.",
      "artist": "Peter Stapleton",
      "collectible": "true",
      "race": "Beast",
      "playerClass": "Warrior",
      "mechanics": [
        "Taunt"
      ]
    },
    {
      "id": "LOEA07_03h",
      "name": "Flee the Mine!",
      "type": "Hero Power",
      "cost": 0,
      "text": "Escape the Troggs!"
    },
    {
      "id": "LOEA07_03",
      "name": "Flee the Mine!",
      "type": "Hero Power",
      "cost": 0,
      "text": "Escape the Troggs!"
    },
    {
      "id": "LOE_002",
      "name": "Forgotten Torch",
      "type": "Spell",
      "rarity": "Common",
      "cost": 3,
      "text": "Deal $3 damage. Shuffle a 'Roaring Torch' into your deck that deals 6 damage.",
      "flavor": "Why does a forgotten torch turn into a roaring torch with no provocation?  It's one of life's many mysteries.",
      "artist": "Richard Wright",
      "collectible": "true",
      "playerClass": "Mage"
    },
    {
      "id": "LOE_073e",
      "name": "Fossilized",
      "type": "Enchantment",
      "text": "Has <b>Taunt</b>."
    },
    {
      "id": "LOE_073",
      "name": "Fossilized Devilsaur",
      "type": "Minion",
      "rarity": "Common",
      "cost": 8,
      "attack": 8,
      "health": 8,
      "text": "<b>Battlecry:</b> If you control a Beast, gain <b>Taunt</b>.",
      "flavor": "This was the only job he could get after the dinosaur theme park debacle.",
      "artist": "Trent Kaniuga",
      "collectible": "true",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA09_3b",
      "name": "Getting Hungry",
      "type": "Hero Power",
      "cost": 0,
      "text": "<b>Hero Power</b>\nSummon a 1/1 Hungry Naga."
    },
    {
      "id": "LOEA09_3",
      "name": "Getting Hungry",
      "type": "Hero Power",
      "cost": 0,
      "text": "<b>Hero Power</b>\nSummon a Hungry Naga."
    },
    {
      "id": "LOEA09_3c",
      "name": "Getting Hungry",
      "type": "Hero Power",
      "cost": 0,
      "text": "<b>Hero Power</b>\nSummon a 2/1 Hungry Naga."
    },
    {
      "id": "LOEA09_3d",
      "name": "Getting Hungry",
      "type": "Hero Power",
      "cost": 0,
      "text": "<b>Hero Power</b>\nSummon a 5/1 Hungry Naga."
    },
    {
      "id": "LOEA04_23h",
      "name": "Giant Insect",
      "type": "Minion",
      "cost": 7,
      "attack": 10,
      "health": 6
    },
    {
      "id": "LOEA04_23",
      "name": "Giant Insect",
      "type": "Minion",
      "cost": 7,
      "attack": 10,
      "health": 3
    },
    {
      "id": "LOEA10_1",
      "name": "Giantfin",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA16_24H",
      "name": "Giantfin",
      "type": "Minion",
      "cost": 10,
      "attack": 10,
      "health": 10,
      "text": "At the end of your turn, draw 2 cards.",
      "elite": true,
      "race": "Murloc"
    },
    {
      "id": "LOEA16_24",
      "name": "Giantfin",
      "type": "Minion",
      "cost": 5,
      "attack": 5,
      "health": 5,
      "text": "At the end of your turn, draw until you have as many cards as your opponent.",
      "elite": true,
      "race": "Murloc"
    },
    {
      "id": "LOE_019t2",
      "name": "Golden Monkey",
      "type": "Minion",
      "cost": 4,
      "attack": 6,
      "health": 6,
      "text": "<b>Taunt</b>\n<b>Battlecry:</b> Replace your hand and deck with <b>Legendary</b> minions.",
      "artist": "A.J. Nazzaro",
      "mechanics": [
        "Battlecry",
        "Taunt"
      ]
    },
    {
      "id": "LOE_039",
      "name": "Gorillabot A-3",
      "type": "Minion",
      "rarity": "Common",
      "cost": 4,
      "attack": 3,
      "health": 4,
      "text": "<b>Battlecry:</b> If you control another Mech, <b>Discover</b> a Mech.",
      "flavor": "A-1 and A-2 went nuts, when they should have gone bolts.",
      "artist": "Skan Srisuwan",
      "collectible": "true",
      "race": "Mech",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOE_089t3",
      "name": "Grumbly Runt",
      "type": "Minion",
      "cost": 2,
      "attack": 2,
      "health": 2,
      "artist": "Matt Dixon"
    },
    {
      "id": "LOEA16_10",
      "name": "Hakkari Blood Goblet",
      "type": "Spell",
      "cost": 0,
      "text": "Transform a minion into a 2/1 Pit Snake."
    },
    {
      "id": "LOEA08_01h",
      "name": "Heroic Archaedas",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA04_01h",
      "name": "Heroic Escape",
      "type": "Hero",
      "health": 100
    },
    {
      "id": "LOEA10_1H",
      "name": "Heroic Giantfin",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA07_02h",
      "name": "Heroic Mine Shaft",
      "type": "Hero",
      "health": 80
    },
    {
      "id": "LOEA01_11he",
      "name": "Heroic Mode",
      "type": "Enchantment",
      "text": "+3/+3 if Phaerix controls the Rod."
    },
    {
      "id": "LOEA12_1H",
      "name": "Heroic Naz'jar",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA01_01h",
      "name": "Heroic Phaerix",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA15_1H",
      "name": "Heroic Rafaam",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA16_1H",
      "name": "Heroic Rafaam",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA05_01h",
      "name": "Heroic Scarvash",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA14_1H",
      "name": "Heroic Sentinel",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA13_1h",
      "name": "Heroic Skelesaurus",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA09_1H",
      "name": "Heroic Slitherspear",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA02_01h",
      "name": "Heroic Zinaar",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOE_030e",
      "name": "Hollow",
      "type": "Enchantment",
      "text": "Stats copied."
    },
    {
      "id": "LOE_046",
      "name": "Huge Toad",
      "type": "Minion",
      "rarity": "Common",
      "cost": 2,
      "attack": 3,
      "health": 2,
      "text": "<b>Deathrattle:</b> Deal 1 damage to a random enemy.",
      "flavor": "Deals damage when he croaks.",
      "artist": "Matt Dixon",
      "collectible": "true",
      "race": "Beast",
      "mechanics": [
        "Deathrattle"
      ]
    },
    {
      "id": "LOEA09_12",
      "name": "Hungry Naga",
      "type": "Minion",
      "cost": 4,
      "attack": 2,
      "health": 1
    },
    {
      "id": "LOEA09_5",
      "name": "Hungry Naga",
      "type": "Minion",
      "cost": 1,
      "attack": 1,
      "health": 1
    },
    {
      "id": "LOEA09_11",
      "name": "Hungry Naga",
      "type": "Minion",
      "cost": 3,
      "attack": 1,
      "health": 1
    },
    {
      "id": "LOEA09_5H",
      "name": "Hungry Naga",
      "type": "Minion",
      "cost": 3,
      "attack": 3,
      "health": 3
    },
    {
      "id": "LOEA09_13",
      "name": "Hungry Naga",
      "type": "Minion",
      "cost": 5,
      "attack": 5,
      "health": 1
    },
    {
      "id": "LOEA09_10",
      "name": "Hungry Naga",
      "type": "Minion",
      "cost": 2,
      "attack": 2,
      "health": 1
    },
    {
      "id": "LOEA04_29b",
      "name": "Investigate the Runes",
      "type": "Spell",
      "text": "Draw 2 cards."
    },
    {
      "id": "LOE_029",
      "name": "Jeweled Scarab",
      "type": "Minion",
      "rarity": "Common",
      "cost": 2,
      "attack": 1,
      "health": 1,
      "text": "<b>Battlecry: Discover</b> a\n3-Cost card.",
      "flavor": "It's amazing what you can do with super glue!",
      "artist": "Jaemin Kim",
      "collectible": "true",
      "race": "Beast",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOE_051",
      "name": "Jungle Moonkin",
      "type": "Minion",
      "rarity": "Rare",
      "cost": 4,
      "attack": 4,
      "health": 4,
      "text": "Both players have\n<b>Spell Damage +2</b>.",
      "flavor": "The REAL angry chicken!",
      "artist": "Mike Sass",
      "collectible": "true",
      "race": "Beast",
      "playerClass": "Druid"
    },
    {
      "id": "LOE_017",
      "name": "Keeper of Uldaman",
      "type": "Minion",
      "rarity": "Common",
      "cost": 4,
      "attack": 3,
      "health": 4,
      "text": "<b>Battlecry:</b> Set a minion's Attack and Health to 3.",
      "flavor": "U da man!  No, U da man!",
      "artist": "James Ryman",
      "collectible": "true",
      "playerClass": "Paladin",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA16_14",
      "name": "Khadgar's Pipe",
      "type": "Spell",
      "cost": 0,
      "text": "Put a random spell into each player's hand.  Yours costs (0)."
    },
    {
      "id": "LOEA12_1",
      "name": "Lady Naz'jar",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA16_25",
      "name": "Lady Naz'jar",
      "type": "Minion",
      "cost": 5,
      "attack": 5,
      "health": 5,
      "text": "At the end of your turn, replace all other minions with new ones of the same Cost.",
      "elite": true
    },
    {
      "id": "LOEA16_25H",
      "name": "Lady Naz'jar",
      "type": "Minion",
      "cost": 10,
      "attack": 10,
      "health": 10,
      "text": "At the end of your turn, replace all other minions with new ones of the same Cost.",
      "elite": true
    },
    {
      "id": "LOEA16_3e",
      "name": "Lantern of Power",
      "type": "Enchantment",
      "text": "+10/+10."
    },
    {
      "id": "LOEA16_3",
      "name": "Lantern of Power",
      "type": "Spell",
      "cost": 10,
      "text": "Give a minion +10/+10."
    },
    {
      "id": "LOEA02_10a",
      "name": "Leokk",
      "type": "Minion",
      "attack": 2,
      "health": 4,
      "text": "Your minions have +1 Attack.",
      "race": "Beast",
      "playerClass": "Hunter",
      "cost": 0
    },
    {
      "id": "LOEA_01",
      "name": "Looming Presence",
      "type": "Spell",
      "cost": 3,
      "text": "Draw 2 cards. Gain 4 Armor."
    },
    {
      "id": "LOEA_01H",
      "name": "Looming Presence",
      "type": "Spell",
      "cost": 3,
      "text": "Draw 3 cards. Gain 6 Armor."
    },
    {
      "id": "LOEA16_23",
      "name": "Lord Slitherspear",
      "type": "Minion",
      "cost": 5,
      "attack": 5,
      "health": 5,
      "text": "At the end of your turn, summon 1/1 Hungry Naga for each enemy minion.",
      "elite": true
    },
    {
      "id": "LOEA16_23H",
      "name": "Lord Slitherspear",
      "type": "Minion",
      "cost": 10,
      "attack": 10,
      "health": 10,
      "text": "At the end of your turn, summon 1/1 Hungry Naga for each enemy minion.",
      "elite": true
    },
    {
      "id": "LOEA09_1",
      "name": "Lord Slitherspear",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA16_9",
      "name": "Lothar's Left Greave",
      "type": "Spell",
      "cost": 0,
      "text": "Deal 3 damage to all enemies."
    },
    {
      "id": "LOEA07_14",
      "name": "Lumbering Golem",
      "type": "Minion",
      "cost": 6,
      "attack": 6,
      "health": 6
    },
    {
      "id": "LOE_019t",
      "name": "Map to the Golden Monkey",
      "type": "Spell",
      "cost": 2,
      "text": "Shuffle the Golden Monkey into your deck. Draw a card.",
      "artist": "Milivoj Ceran"
    },
    {
      "id": "LOEA07_25",
      "name": "Mechanical Parrot",
      "type": "Minion",
      "cost": 1,
      "attack": 3,
      "health": 6,
      "race": "Mech"
    },
    {
      "id": "LOEA16_12",
      "name": "Medivh's Locket",
      "type": "Spell",
      "cost": 0,
      "text": "Replace your hand with Unstable Portals."
    },
    {
      "id": "LOEA07_01",
      "name": "Mine Cart",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA07_02",
      "name": "Mine Shaft",
      "type": "Hero",
      "health": 80
    },
    {
      "id": "LOEA16_5",
      "name": "Mirror of Doom",
      "type": "Spell",
      "cost": 10,
      "text": "Fill your board with 3/3 Mummy Zombies."
    },
    {
      "id": "LOEA02_10c",
      "name": "Misha",
      "type": "Minion",
      "attack": 4,
      "health": 4,
      "text": "<b>Taunt</b>",
      "race": "Beast",
      "playerClass": "Hunter",
      "cost": 0
    },
    {
      "id": "LOE_050",
      "name": "Mounted Raptor",
      "type": "Minion",
      "rarity": "Common",
      "cost": 3,
      "attack": 3,
      "health": 2,
      "text": "<b>Deathrattle:</b> Summon a random 1-Cost minion.",
      "flavor": "Clever girl!",
      "artist": "Ben Zhang",
      "collectible": "true",
      "race": "Beast",
      "playerClass": "Druid",
      "mechanics": [
        "Deathrattle"
      ]
    },
    {
      "id": "LOEA10_5H",
      "name": "Mrgl Mrgl Nyah Nyah",
      "type": "Spell",
      "rarity": "Common",
      "cost": 3,
      "text": "Summon 5 Murlocs that died this game."
    },
    {
      "id": "LOEA10_5",
      "name": "Mrgl Mrgl Nyah Nyah",
      "type": "Spell",
      "rarity": "Common",
      "cost": 5,
      "text": "Summon 3 Murlocs that died this game."
    },
    {
      "id": "LOE_113e",
      "name": "Mrglllraawrrrglrur!",
      "type": "Enchantment",
      "text": "+2/+2."
    },
    {
      "id": "LOEA10_2H",
      "name": "Mrglmrgl MRGL!",
      "type": "Hero Power",
      "cost": 0,
      "text": "<b>Hero Power</b>\nDraw 2 cards."
    },
    {
      "id": "LOEA10_2",
      "name": "Mrglmrgl MRGL!",
      "type": "Hero Power",
      "cost": 0,
      "text": "<b>Hero Power</b>\nDraw cards until you have as many in hand as your opponent."
    },
    {
      "id": "LOEA16_5t",
      "name": "Mummy Zombie",
      "type": "Minion",
      "cost": 3,
      "attack": 3,
      "health": 3
    },
    {
      "id": "LOEA10_3",
      "name": "Murloc Tinyfin",
      "type": "Minion",
      "rarity": "Common",
      "cost": 0,
      "attack": 1,
      "health": 1,
      "flavor": "High mortality rate, from often being hugged to death.",
      "artist": "Oliver Chipping",
      "collectible": "true",
      "race": "Murloc"
    },
    {
      "id": "LOE_006",
      "name": "Museum Curator",
      "type": "Minion",
      "rarity": "Common",
      "cost": 2,
      "attack": 1,
      "health": 2,
      "text": "<b>Battlecry: Discover</b> a <b>Deathrattle</b> card.",
      "flavor": "He is forever cursing the kids who climb on the rails and the evil archeologists who animate the exhibits.",
      "artist": "Steve Prescott",
      "collectible": "true",
      "playerClass": "Priest",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA09_9H",
      "name": "Naga Repellent",
      "type": "Spell",
      "cost": 1,
      "text": "Change the Attack of all Hungry Naga to 1."
    },
    {
      "id": "LOEA09_9",
      "name": "Naga Repellent",
      "type": "Spell",
      "cost": 1,
      "text": "Destroy all Hungry Naga."
    },
    {
      "id": "LOE_038",
      "name": "Naga Sea Witch",
      "type": "Minion",
      "rarity": "Epic",
      "cost": 5,
      "attack": 5,
      "health": 5,
      "text": "Your cards cost (5).",
      "flavor": "If she had studied harder, she would have been a C+ witch.",
      "artist": "Ben Zhang",
      "collectible": "true",
      "mechanics": [
        "Aura"
      ]
    },
    {
      "id": "LOEA04_31b",
      "name": "No Way!",
      "type": "Spell",
      "text": "Do nothing."
    },
    {
      "id": "LOE_009",
      "name": "Obsidian Destroyer",
      "type": "Minion",
      "rarity": "Common",
      "cost": 7,
      "attack": 7,
      "health": 7,
      "text": "At the end of your turn, summon a 1/1 Scarab with <b>Taunt</b>.",
      "flavor": "No obsidian is safe around the Obsidian Destroyer!",
      "artist": "Anton Zemskov",
      "collectible": "true",
      "playerClass": "Warrior"
    },
    {
      "id": "LOEA04_13bt",
      "name": "Orsis Guard",
      "type": "Minion",
      "cost": 4,
      "attack": 7,
      "health": 5,
      "text": "<b>Divine Shield</b>",
      "mechanics": [
        "Divine Shield"
      ]
    },
    {
      "id": "LOEA04_13bth",
      "name": "Orsis Guard",
      "type": "Minion",
      "cost": 4,
      "attack": 8,
      "health": 8,
      "text": "<b>Divine Shield</b>",
      "mechanics": [
        "Divine Shield"
      ]
    },
    {
      "id": "LOEA12_2",
      "name": "Pearl of the Tides",
      "type": "Hero Power",
      "text": "At the end of your turn, replace all minions with new ones that cost (1) more."
    },
    {
      "id": "LOEA12_2H",
      "name": "Pearl of the Tides",
      "type": "Hero Power",
      "text": "At the end of your turn, replace all minions with new ones. Yours cost (1) more."
    },
    {
      "id": "LOEA04_06",
      "name": "Pit of Spikes",
      "type": "Spell",
      "cost": 0,
      "text": "<b>Choose Your Path!</b>"
    },
    {
      "id": "LOE_010",
      "name": "Pit Snake",
      "type": "Minion",
      "rarity": "Common",
      "cost": 1,
      "attack": 2,
      "health": 1,
      "text": "Destroy any minion damaged by this minion.",
      "flavor": "It could be worse.  It could be a Snake Pit.",
      "artist": "Bernie Kang",
      "collectible": "true",
      "race": "Beast",
      "playerClass": "Rogue",
      "mechanics": [
        "Poisonous"
      ]
    },
    {
      "id": "LOEA14_2H",
      "name": "Platemail Armor",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\nYour Hero and your minions can only take 1 damage at a time."
    },
    {
      "id": "LOEA14_2",
      "name": "Platemail Armor",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\nYour Hero can only take 1 damage at a time."
    },
    {
      "id": "LOE_061e",
      "name": "Power of the Titans",
      "type": "Enchantment",
      "text": "+3/+3."
    },
    {
      "id": "LOEA16_8",
      "name": "Putress' Vial",
      "type": "Spell",
      "cost": 0,
      "text": "Destroy a random enemy minion."
    },
    {
      "id": "LOEA16_8a",
      "name": "Putressed",
      "type": "Enchantment",
      "text": "Attack and Health swapped."
    },
    {
      "id": "LOEA15_1",
      "name": "Rafaam",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA16_1",
      "name": "Rafaam",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA09_4",
      "name": "Rare Spear",
      "type": "Weapon",
      "cost": 1,
      "attack": 1,
      "durability": 2,
      "text": "Whenever your opponent plays a Rare card, gain +1/+1."
    },
    {
      "id": "LOEA09_4H",
      "name": "Rare Spear",
      "type": "Weapon",
      "cost": 1,
      "attack": 1,
      "durability": 2,
      "text": "Whenever your opponent plays a Rare card, gain +1/+1."
    },
    {
      "id": "LOE_089t",
      "name": "Rascally Runt",
      "type": "Minion",
      "cost": 2,
      "attack": 2,
      "health": 2,
      "artist": "Matt Dixon"
    },
    {
      "id": "LOE_115",
      "name": "Raven Idol",
      "type": "Spell",
      "rarity": "Common",
      "cost": 1,
      "text": "<b>Choose One -</b>\n<b>Discover</b> a minion; or <b>Discover</b> a spell.",
      "flavor": "Was petrified when it found out it didn't make the cut for Azerothean Idol.",
      "artist": "A.J. Nazzaro",
      "collectible": "true",
      "playerClass": "Druid"
    },
    {
      "id": "LOE_115b",
      "name": "Raven Idol",
      "type": "Spell",
      "rarity": "Common",
      "text": "<b>Discover</b> a spell.",
      "artist": "A.J. Nazzaro",
      "playerClass": "Druid"
    },
    {
      "id": "LOE_115a",
      "name": "Raven Idol",
      "type": "Spell",
      "rarity": "Common",
      "text": "<b>Discover</b> a minion.",
      "artist": "A.J. Nazzaro",
      "playerClass": "Druid"
    },
    {
      "id": "LOE_116",
      "name": "Reliquary Seeker",
      "type": "Minion",
      "rarity": "Rare",
      "cost": 1,
      "attack": 1,
      "health": 1,
      "text": "<b>Battlecry:</b> If you have 6 other minions, gain +4/+4.",
      "flavor": "The Reliquary considers itself the equal of the League of Explorers.  The League of Explorers doesn't.",
      "artist": "Wayne Reynolds",
      "collectible": "true",
      "playerClass": "Warlock",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOE_011",
      "name": "Reno Jackson",
      "type": "Minion",
      "rarity": "Legendary",
      "cost": 6,
      "attack": 4,
      "health": 6,
      "text": "<b>Battlecry:</b> If your deck contains no more than 1 of any card, fully heal your hero.",
      "flavor": "Reno is a four-time winner of the 'Best Accessorized Explorer' award.",
      "artist": "Tyson Murphy",
      "collectible": "true",
      "elite": true,
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA07_28",
      "name": "Repairs",
      "type": "Spell",
      "cost": 1,
      "text": "Restore 10 Health."
    },
    {
      "id": "LOE_002t",
      "name": "Roaring Torch",
      "type": "Spell",
      "cost": 3,
      "text": "Deal $6 damage.",
      "artist": "Richard Wright",
      "playerClass": "Mage"
    },
    {
      "id": "LOE_016t",
      "name": "Rock",
      "type": "Minion",
      "cost": 1,
      "attack": 0,
      "health": 6,
      "text": "<b>Taunt.</b>",
      "mechanics": [
        "Taunt"
      ]
    },
    {
      "id": "LOEA01_11",
      "name": "Rod of the Sun",
      "type": "Minion",
      "cost": 0,
      "attack": 0,
      "health": 5,
      "text": "<b>Deathrattle:</b> Surrender this to your opponent.",
      "mechanics": [
        "Deathrattle"
      ]
    },
    {
      "id": "LOEA01_11h",
      "name": "Rod of the Sun",
      "type": "Minion",
      "cost": 0,
      "attack": 0,
      "health": 5,
      "text": "<b>Deathrattle:</b> Surrender this to your opponent.",
      "mechanics": [
        "Deathrattle"
      ]
    },
    {
      "id": "LOE_024t",
      "name": "Rolling Boulder",
      "type": "Minion",
      "cost": 4,
      "attack": 0,
      "health": 4,
      "text": "At the end of your turn, destroy the minion to the left.",
      "artist": "Richard Wright"
    },
    {
      "id": "LOE_016",
      "name": "Rumbling Elemental",
      "type": "Minion",
      "rarity": "Common",
      "cost": 4,
      "attack": 2,
      "health": 6,
      "text": "After you play a <b>Battlecry</b> minion, deal 2 damage to a random enemy.",
      "flavor": "He's a very hungry elemental.",
      "artist": "Cole Eastburn",
      "collectible": "true",
      "playerClass": "Shaman"
    },
    {
      "id": "LOEA16_16H",
      "name": "Rummage",
      "type": "Hero Power",
      "cost": 2,
      "text": "Find an artifact."
    },
    {
      "id": "LOEA16_16",
      "name": "Rummage",
      "type": "Hero Power",
      "cost": 0,
      "text": "Find an artifact."
    },
    {
      "id": "LOE_027",
      "name": "Sacred Trial",
      "type": "Spell",
      "rarity": "Common",
      "cost": 1,
      "text": "<b>Secret:</b> When your opponent has at least 3 minions and plays another, destroy it.",
      "flavor": "You have chosen poorly.",
      "artist": "Zoltan Boros",
      "collectible": "true",
      "playerClass": "Paladin",
      "mechanics": [
        "Secret"
      ]
    },
    {
      "id": "LOE_009t",
      "name": "Scarab",
      "type": "Minion",
      "cost": 1,
      "attack": 1,
      "health": 1,
      "text": "<b>Taunt</b>",
      "artist": "Jaemin Kim",
      "playerClass": "Warrior",
      "mechanics": [
        "Taunt"
      ]
    },
    {
      "id": "LOEA04_25",
      "name": "Seething Statue",
      "type": "Minion",
      "cost": 8,
      "attack": 0,
      "health": 9,
      "text": "At the end of your turn, deal 2 damage to all enemies."
    },
    {
      "id": "LOEA04_25h",
      "name": "Seething Statue",
      "type": "Minion",
      "cost": 8,
      "attack": 5,
      "health": 9,
      "text": "At the end of your turn, deal 5 damage to all enemies."
    },
    {
      "id": "LOEA16_6",
      "name": "Shard of Sulfuras",
      "type": "Spell",
      "cost": 0,
      "text": "Deal $5 damage to ALL characters."
    },
    {
      "id": "LOEA06_04",
      "name": "Shattering Spree",
      "type": "Spell",
      "cost": 2,
      "text": "Destroy all Statues. For each destroyed, deal $1 damage."
    },
    {
      "id": "LOEA06_04h",
      "name": "Shattering Spree",
      "type": "Spell",
      "cost": 2,
      "text": "Destroy all Statues. For each destroyed, deal $3 damage."
    },
    {
      "id": "LOE_009e",
      "name": "Sinister Power",
      "type": "Enchantment",
      "text": "+4/+4.",
      "playerClass": "Warlock"
    },
    {
      "id": "LOE_076",
      "name": "Sir Finley Mrrgglton",
      "type": "Minion",
      "rarity": "Legendary",
      "cost": 1,
      "attack": 1,
      "health": 3,
      "text": "<b>Battlecry: Discover</b> a new basic Hero Power.",
      "flavor": "In addition to fluent Common, he also speaks fourteen dialects of 'mrgl'.",
      "artist": "Matt Dixon",
      "collectible": "true",
      "elite": true,
      "race": "Murloc",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA13_1",
      "name": "Skelesaurus Hex",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA16_26",
      "name": "Skelesaurus Hex",
      "type": "Minion",
      "cost": 5,
      "attack": 5,
      "health": 5,
      "text": "At the end of your turn, give each player a random card. It costs (0).",
      "elite": true
    },
    {
      "id": "LOEA16_26H",
      "name": "Skelesaurus Hex",
      "type": "Minion",
      "cost": 10,
      "attack": 10,
      "health": 10,
      "text": "At the end of your turn, put a random card in your hand. It costs (0).",
      "elite": true
    },
    {
      "id": "LOEA09_6H",
      "name": "Slithering Archer",
      "type": "Minion",
      "cost": 2,
      "attack": 2,
      "health": 2,
      "text": "<b>Battlecry:</b> Deal 2 damage to all enemy minions.",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA09_6",
      "name": "Slithering Archer",
      "type": "Minion",
      "cost": 2,
      "attack": 2,
      "health": 2,
      "text": "<b>Battlecry:</b> Deal 1 damage.",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA09_8",
      "name": "Slithering Guard",
      "type": "Minion",
      "cost": 5,
      "attack": 3,
      "health": 6,
      "text": "<b>Taunt</b>",
      "mechanics": [
        "Taunt"
      ]
    },
    {
      "id": "LOEA09_8H",
      "name": "Slithering Guard",
      "type": "Minion",
      "cost": 5,
      "attack": 5,
      "health": 7,
      "text": "<b>Taunt</b>",
      "mechanics": [
        "Taunt"
      ]
    },
    {
      "id": "LOEA07_24",
      "name": "Spiked Decoy",
      "type": "Minion",
      "cost": 1,
      "attack": 3,
      "health": 6,
      "text": "<b>Taunt</b>\nCan't attack.",
      "race": "Mech",
      "mechanics": [
        "Taunt"
      ]
    },
    {
      "id": "LOEA16_2H",
      "name": "Staff of Origination",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\nYour hero is <b>Immune</b>."
    },
    {
      "id": "LOEA16_2",
      "name": "Staff of Origination",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\nYour hero is <b>Immune</b> while the staff charges."
    },
    {
      "id": "LOEA06_02h",
      "name": "Stonesculpting",
      "type": "Hero Power",
      "cost": 1,
      "text": "<b>Hero Power</b>\n Summon a Statue for both players."
    },
    {
      "id": "LOEA06_02",
      "name": "Stonesculpting",
      "type": "Hero Power",
      "cost": 1,
      "text": "<b>Hero Power</b>\n Summon a 0/2 Statue for both players."
    },
    {
      "id": "LOE_086",
      "name": "Summoning Stone",
      "type": "Minion",
      "rarity": "Rare",
      "cost": 5,
      "attack": 0,
      "health": 6,
      "text": "Whenever you cast a spell, summon a random minion of the same Cost.",
      "flavor": "Sometimes it feels like it's always the same slackers that are waiting for a summon.",
      "artist": "Jason Kang",
      "collectible": "true"
    },
    {
      "id": "LOEA01_01",
      "name": "Sun Raider Phaerix",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA16_19",
      "name": "Sun Raider Phaerix",
      "type": "Minion",
      "cost": 5,
      "attack": 5,
      "health": 5,
      "text": "At the end of your turn, add a Blessing of the Sun to your hand.",
      "elite": true
    },
    {
      "id": "LOEA16_19H",
      "name": "Sun Raider Phaerix",
      "type": "Minion",
      "cost": 10,
      "attack": 10,
      "health": 10,
      "text": "Your other minions are <b>Immune</b>.",
      "elite": true
    },
    {
      "id": "LOEA04_06a",
      "name": "Swing Across",
      "type": "Spell",
      "text": "Take 10 damage or no damage, at random.",
      "mechanics": [
        "ImmuneToSpellpower"
      ]
    },
    {
      "id": "LOEA04_30a",
      "name": "Take the Shortcut",
      "type": "Spell",
      "text": "Get 1 turn closer to the Exit! Encounter a 7/7 War Golem."
    },
    {
      "id": "LOEA04_01",
      "name": "Temple Escape",
      "type": "Hero",
      "health": 100
    },
    {
      "id": "LOEA04_01e",
      "name": "Temple Escape Enchant",
      "type": "Enchantment"
    },
    {
      "id": "LOEA04_01eh",
      "name": "Temple Escape Enchant",
      "type": "Enchantment"
    },
    {
      "id": "LOEA04_30",
      "name": "The Darkness",
      "type": "Spell",
      "cost": 0,
      "text": "<b>Take the Shortcut?</b>"
    },
    {
      "id": "LOEA04_29",
      "name": "The Eye",
      "type": "Spell",
      "cost": 0,
      "text": "<b>Choose Your Path!</b>"
    },
    {
      "id": "LOEA16_27",
      "name": "The Steel Sentinel",
      "type": "Minion",
      "cost": 5,
      "attack": 5,
      "health": 5,
      "text": "This minion can only take 1 damage at a time.",
      "elite": true
    },
    {
      "id": "LOEA16_27H",
      "name": "The Steel Sentinel",
      "type": "Minion",
      "cost": 10,
      "attack": 10,
      "health": 10,
      "text": "This minion can only take 1 damage at a time.",
      "elite": true
    },
    {
      "id": "LOEA14_1",
      "name": "The Steel Sentinel",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA07_29",
      "name": "Throw Rocks",
      "type": "Hero Power",
      "cost": 1,
      "text": "<b>Hero Power</b>\n Deal 3 damage to a random enemy minion."
    },
    {
      "id": "LOEA16_4",
      "name": "Timepiece of Horror",
      "type": "Spell",
      "cost": 10,
      "text": "Deal $10 damage randomly split among all enemies.",
      "mechanics": [
        "ImmuneToSpellpower"
      ]
    },
    {
      "id": "LOEA01_12h",
      "name": "Tol'vir Hoplite",
      "type": "Minion",
      "cost": 3,
      "attack": 5,
      "health": 5,
      "text": "<b>Deathrattle:</b> Deal 5 damage to both heroes.",
      "mechanics": [
        "Deathrattle"
      ]
    },
    {
      "id": "LOEA01_12",
      "name": "Tol'vir Hoplite",
      "type": "Minion",
      "cost": 3,
      "attack": 5,
      "health": 2,
      "text": "<b>Deathrattle:</b> Deal 5 damage to both heroes.",
      "mechanics": [
        "Deathrattle"
      ]
    },
    {
      "id": "LOE_012",
      "name": "Tomb Pillager",
      "type": "Minion",
      "rarity": "Common",
      "cost": 4,
      "attack": 5,
      "health": 4,
      "text": "<b>Deathrattle:</b> Add a Coin to your hand.",
      "flavor": "After the guild broke up, he could no longer raid the tombs.",
      "artist": "Dave Allsop",
      "collectible": "true",
      "playerClass": "Rogue",
      "mechanics": [
        "Deathrattle"
      ]
    },
    {
      "id": "LOE_047",
      "name": "Tomb Spider",
      "type": "Minion",
      "rarity": "Common",
      "cost": 4,
      "attack": 3,
      "health": 3,
      "text": "<b>Battlecry: Discover</b> a Beast.",
      "flavor": "Less serious than its cousin, the Grave Spider.",
      "artist": "Turovec Konstantin",
      "collectible": "true",
      "race": "Beast",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOEA04_29a",
      "name": "Touch It",
      "type": "Spell",
      "text": "Restore 10 Health to your hero."
    },
    {
      "id": "LOEA05_02h",
      "name": "Trogg Hate Minions!",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\n Enemy minions cost (11). Swap at the start of your turn."
    },
    {
      "id": "LOEA05_02a",
      "name": "Trogg Hate Minions!",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\n Enemy minions cost (2) more. Swap at the start of your turn."
    },
    {
      "id": "LOEA05_02ha",
      "name": "Trogg Hate Minions!",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\n Enemy minions cost (11). Swap at the start of your turn."
    },
    {
      "id": "LOEA05_02",
      "name": "Trogg Hate Minions!",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\n Enemy minions cost (2) more. Swap at the start of your turn."
    },
    {
      "id": "LOEA05_03h",
      "name": "Trogg Hate Spells!",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\n Enemy spells cost (11). Swap at the start of your turn."
    },
    {
      "id": "LOEA05_03",
      "name": "Trogg Hate Spells!",
      "type": "Hero Power",
      "text": "<b>Passive Hero Power</b>\n Enemy spells cost (2) more. Swap at the start of your turn."
    },
    {
      "id": "LOE_018e",
      "name": "Trogg No Stupid",
      "type": "Enchantment",
      "text": "Increased Attack.",
      "playerClass": "Shaman"
    },
    {
      "id": "LOE_018",
      "name": "Tunnel Trogg",
      "type": "Minion",
      "rarity": "Common",
      "cost": 1,
      "attack": 1,
      "health": 3,
      "text": "Whenever you <b>Overload</b>, gain +1 Attack per locked Mana Crystal.",
      "flavor": "Sure, they're ugly, but they live in tunnels.  You try your beauty routine without natural light.",
      "artist": "Andrew Hou",
      "collectible": "true",
      "playerClass": "Shaman"
    },
    {
      "id": "LOE_019",
      "name": "Unearthed Raptor",
      "type": "Minion",
      "rarity": "Rare",
      "cost": 3,
      "attack": 3,
      "health": 4,
      "text": "<b>Battlecry:</b> Choose a friendly minion. Gain a copy of its <b>Deathrattle</b> effect.",
      "flavor": "Still hunting for the ones who earthed him.",
      "artist": "Trent Kaniuga",
      "collectible": "true",
      "playerClass": "Rogue",
      "mechanics": [
        "Battlecry"
      ]
    },
    {
      "id": "LOE_019e",
      "name": "Unearthed Raptor",
      "type": "Enchantment",
      "text": "Copied <b>Deathrattle</b> from CARD_NAME.",
      "playerClass": "Rogue"
    },
    {
      "id": "LOEA15_2",
      "name": "Unstable Portal",
      "type": "Hero Power",
      "cost": 2,
      "text": "<b>Hero Power</b>\nAdd a random minion to your hand. It costs (3) less."
    },
    {
      "id": "LOEA15_2H",
      "name": "Unstable Portal",
      "type": "Hero Power",
      "cost": 0,
      "text": "<b>Hero Power</b>\nAdd a random minion to your hand. It costs (3) less."
    },
    {
      "id": "LOEA04_28b",
      "name": "Wade Through",
      "type": "Spell",
      "cost": 0,
      "text": "Gain a Mana Crystal"
    },
    {
      "id": "LOEA04_06b",
      "name": "Walk Across Gingerly",
      "type": "Spell",
      "text": "Take 5 damage."
    },
    {
      "id": "LOE_017e",
      "name": "Watched",
      "type": "Enchantment",
      "text": "Stats changed to 3/3.",
      "playerClass": "Paladin"
    },
    {
      "id": "LOE_089t2",
      "name": "Wily Runt",
      "type": "Minion",
      "cost": 2,
      "attack": 2,
      "health": 2,
      "artist": "Matt Dixon"
    },
    {
      "id": "LOEA02_10",
      "name": "Wish for Companionship",
      "type": "Spell",
      "cost": 0,
      "text": "<b>Discover</b> a Companion."
    },
    {
      "id": "LOEA02_05",
      "name": "Wish for Glory",
      "type": "Spell",
      "cost": 0,
      "text": "<b>Discover</b> a minion."
    },
    {
      "id": "LOEA02_06",
      "name": "Wish for More Wishes",
      "type": "Spell",
      "cost": 0,
      "text": "Gain 2 Wishes."
    },
    {
      "id": "LOEA02_03",
      "name": "Wish for Power",
      "type": "Spell",
      "cost": 0,
      "text": "<b>Discover</b> a spell."
    },
    {
      "id": "LOEA02_04",
      "name": "Wish for Valor",
      "type": "Spell",
      "cost": 0,
      "text": "<b>Discover</b> a (4)-Cost card."
    },
    {
      "id": "LOE_089",
      "name": "Wobbling Runts",
      "type": "Minion",
      "rarity": "Rare",
      "cost": 6,
      "attack": 2,
      "health": 6,
      "text": "<b>Deathrattle:</b> Summon three 2/2 Runts.",
      "flavor": "The fourth one fell off in a tragic accident.  They don't talk about it.",
      "artist": "Sam Nielson",
      "collectible": "true",
      "mechanics": [
        "Deathrattle"
      ]
    },
    {
      "id": "LOEA16_15",
      "name": "Ysera's Tear",
      "type": "Spell",
      "cost": 0,
      "text": "Gain 4 Mana Crystals this turn only."
    },
    {
      "id": "LOEA02_01",
      "name": "Zinaar",
      "type": "Hero",
      "health": 30
    },
    {
      "id": "LOEA16_18H",
      "name": "Zinaar",
      "type": "Minion",
      "cost": 10,
      "attack": 10,
      "health": 10,
      "text": "At the end of your turn, gain a wish.",
      "elite": true
    },
    {
      "id": "LOEA16_18",
      "name": "Zinaar",
      "type": "Minion",
      "cost": 5,
      "attack": 5,
      "health": 5,
      "text": "At the end of your turn, gain a wish.",
      "elite": true
    },
    {
      "id": "LOE_012e",
      "name": "zzDELETE Tomb Explorer",
      "type": "Enchantment",
      "text": "Copied Deathrattle from CARD_NAME",
      "playerClass": "Rogue"
    },
    {
      "id": "LOE_030",
      "name": "zzDELETE? Animated Armor",
      "type": "Minion",
      "rarity": "Common",
      "cost": 4,
      "attack": 1,
      "health": 1,
      "text": "<b>Taunt</b>\n<b>Battlecry:</b> Copy a friendly minion's Attack and Health.",
      "collectible": "false",
      "mechanics": [
        "Battlecry",
        "Taunt"
      ]
    }
  ]
}
"""

dict = json.loads(JSON_datalist)

list = dict["League of Explorers"]
file = open("cards.txt", "a")
  
for card in list:

  expansion = "League of Explorers"
  
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
      
  if collectible != "true":
    continue

  try:
    id = card["id"]
    name = card["name"]
    cost = str(card["cost"])
    rarity = card["rarity"]
  except:
    continue

  try:
    race = card["race"]
  except:
    race = None
  try:
    playerClass = card["playerClass"]
  except:
    playerClass = None
  try:
    attack = card["attack"]
  except:
    attack = None
  try:
    health = card["health"]
  except:
    health = None
  try:
    durability = card["durability"]
  except:
    durability = None
  try:
    howToGet = card["howToGet"]
  except:
    howToGet = None
  try:
    howToGetGold = card["howToGetGold"]
  except:
    howToGetGold = None
    
  if rarity == "Free":
    rarity = "Basic"
    
  file.write(str(id) + "\t" + str(name) + "\t" + str(cost) + "\t" + str(type) + "\t" + str(rarity) + "\t" + str(expansion) + "\t" + str(race) + "\t" + str(playerClass) + "\t" + str(attack) + "\t" + str(health) + "\t" + str(durability) + "\t" + str(howToGet) + "\t" + str(howToGetGold) + "\n")

file.close()