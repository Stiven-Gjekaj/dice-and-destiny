"""Original NPCs of the sea, the towers, the wild places, and the shadows."""
from monster_engine import M
R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())
S, SC, W, A = "Sailors and Pirates", "Scholars and Mages", "Wilderness Folk", "Assassins and Duelists"
HUM = "Humanoid"

NPCS = [
# ================= SAILORS AND PIRATES =================
(S, M("Boatswain", "M", HUM, "Neutral", 1, "15 12 14 10 12 11", ac=13, skills="Athletics, Intimidation", speed="30 ft., swim 30 ft.", lang="Common",
  traits=[("All Hands", "Allies within 30 feet of the boatswain that can hear it have Advantage on Strength (Athletics) checks.")],
  attacks=[("Rope's End", "m", "1d6", "Bludgeoning"), ("Cutlass", "m", "1d6", "Slashing")], multi=2,
  desc="The loud, scarred officer who makes the crew work. The crew hates them, and would follow them into a storm.")),
(S, M("Wave Singer", "M", HUM, "Neutral", 4, "10 14 14 12 16 16", ac=13, skills="Nature, Performance, Survival", speed="30 ft., swim 40 ft.", lang="Common, Primordial (Aquan)",
  traits=[("Sea Born", "The singer can breathe air and water.")],
  attacks=[("Water Lash", "s:wis", "2d8", "Bludgeoning", "and the target is pushed 10 feet away", "60 ft.")], multi=2,
  actions=[("Spellcasting", "The singer casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). At will: Druidcraft. 1/Day each: Fog Cloud, Gust of Wind, Water Breathing."),
           ("Call the Swell (Recharge 5–6)", "Each creature of the singer's choice in a 30-foot Cone makes a {dc:wis} Strength saving throw. On a failed save, a creature takes {4d8} Bludgeoning damage and has the Prone condition. On a successful save, it takes half as much damage only.")],
  desc="A ship's singer whose songs calm the waves, or raise them against the ship's enemies.")),
(S, M("Privateer Captain", "M", HUM, "Lawful Neutral", 5, "14 16 14 12 12 16", ac=16, saves="Dex, Wis", skills="Athletics, Intimidation, Perception", speed="30 ft., swim 30 ft.", lang="Common, and two other languages",
  traits=[("Letter of Marque", "The captain sails with the permission of a crown. Its crew fights with discipline, and it surrenders when the fight is lost.")],
  attacks=[("Saber", "f", "1d8", "Slashing"), ("Pistol Crossbow", "r", "1d10", "Piercing", "", "60/180 ft.")], multi=3,
  react=[("Parry", "The captain adds 3 to its AC against one melee attack that would hit it. To do so, the captain must see the attacker.")],
  desc="A pirate with papers. It robs only the ships of the enemy crown, and it pays its taxes.")),

# ================= SCHOLARS AND MAGES =================
(SC, M("Clockwork Tinker", "S", HUM, "Chaotic Good", 3, "8 14 12 17 12 10", ac=15, skills="Arcana, Investigation, Sleight of Hand", lang="Common, and two other languages",
  traits=[("Mechanical Friend", "The tinker has a Clockwork Spider that obeys it. When you build an encounter, count the spider as a separate monster.")],
  attacks=[("Spark Gun", "r", "2d6", "Lightning", "", "60/180 ft.")], multi=2,
  actions=[("Smoke Bomb (1/Day)", "Smoke fills a 20-foot-radius Sphere centered on a point within 60 feet. The area is Heavily Obscured for 1 minute.")],
  desc="An inventor with grease on their face and three half-built machines in their pockets. Some of the machines work.")),
(SC, M("Elementalist", "M", HUM, "Neutral", 8, "10 14 14 18 14 12", ac=15, saves="Int, Wis", skills="Arcana*, Nature", lang="Common, Primordial",
  res=R(Resistances="Cold, Fire, Lightning"),
  traits=[("Elemental Bond", "The elementalist can't be harmed by a creature of the Elemental type that it summoned.")],
  attacks=[("Elemental Bolt", "s:int", "4d8", "Fire", "The elementalist can change the damage to Cold or Lightning", "120 ft.")], multi=2,
  actions=[("Spellcasting", "The elementalist casts one of the following spells, using Intelligence as the spellcasting ability ({dc:int}). 1/Day each: Conjure Elemental, Fireball, Ice Storm, Lightning Bolt.")],
  desc="A mage who studies the four elements and argues with them. The elements don't always lose the argument.")),
(SC, M("Chronomancer", "M", HUM, "Lawful Neutral", 13, "10 16 14 22 18 14", ac=17, saves="Dex, Int, Wis", skills="Arcana*, History*, Insight", lang="Common, and five other languages",
  res=R(Resistances="Force, Psychic"),
  traits=[("Out of Step", "The chronomancer has Advantage on Initiative rolls and can't be surprised."),
          ("Magic Resistance", "The chronomancer has Advantage on saving throws against spells and other magical effects.")],
  attacks=[("Time Lance", "s:int", "5d10", "Force", "", "120 ft.")], multi=2,
  actions=[("Spellcasting", "The chronomancer casts one of the following spells, using Intelligence as the spellcasting ability ({dc:int}). 2/Day each: Haste, Slow. 1/Day each: Counterspell, Time Stop.")],
  react=[("Rewind (1/Day)", "When the chronomancer takes damage, it takes no damage instead, and it moves back to the space it was in at the start of its last turn.")],
  desc="A mage who studies time, and remembers things that have not happened yet. It is always one step ahead.")),

# ================= WILDERNESS FOLK =================
(W, M("Shepherd", "M", HUM, "Neutral Good", 0.125, "11 12 12 10 13 10", skills="Animal Handling, Perception", lang="Common",
  traits=[("Sheepdog", "The shepherd has a loyal dog (a Wolf from the SRD) that guards the flock. When you build an encounter, count the dog as a separate monster.")],
  attacks=[("Crook", "m", "1d6", "Bludgeoning"), ("Sling", "r", "1d4", "Bludgeoning", "", "30/120 ft.")],
  desc="The person on the hill with the flock and the long view. They see everything that crosses the valley.")),
(W, M("Falconer", "M", HUM, "Neutral", 0.5, "10 14 12 11 14 11", skills="Animal Handling, Nature, Perception", lang="Common",
  traits=[("Falcon", "The falconer has a trained hawk. The hawk can attack a creature within 60 feet of the falconer as a Bonus Action: {atk:dex} to hit, {1d4+2} Slashing damage.")],
  attacks=[("Shortbow", "r", "1d6", "Piercing")])),
(W, M("Clan Chieftain", "M", HUM, "Chaotic Neutral", 9, "20 14 18 10 14 16", ac=16, saves="Str, Con", skills="Athletics, Intimidation, Survival", lang="Common, and one other language",
  traits=[("Battle Rage", "While the chieftain has half its Hit Points or fewer, it has Resistance to Bludgeoning, Piercing, and Slashing damage, and its weapon attacks deal an extra {1d8} damage."),
          ("Clan Pride", "Allies within 30 feet of the chieftain that can see it can't have the Frightened condition.")],
  attacks=[("Greataxe", "m", "1d12", "Slashing"), ("Throwing Axe", "t", "1d6", "Slashing", "", "20/60 ft.")], multi=3,
  bonus=[("War Cry", "Up to three allies within 30 feet that can hear the chieftain can each use a Reaction to make one weapon attack. (1/Day)")],
  desc="The leader of a hill clan, chosen by the clan in a fight. It will listen to you if you beat it at something.")),

# ================= ASSASSINS AND DUELISTS =================
(A, M("Strangler", "M", HUM, "Neutral Evil", 2, "15 15 12 10 12 8", skills="Athletics, Stealth", lang="Common, Thieves' Cant",
  traits=[("Garrote", "When the strangler hits a creature that didn't see it with its Garrote, the target has the Grappled condition (escape {dc:str}), and it can't breathe or speak while Grappled.")],
  attacks=[("Garrote", "f", "1d6", "Bludgeoning"), ("Knife", "f", "1d4", "Piercing")], multi=2,
  desc="A quiet killer who comes from behind with a wire. The city watch finds them by the shape of the marks.")),
(A, M("Shadow Archer", "M", HUM, "Neutral Evil", 6, "12 20 14 12 16 10", ac=16, skills="Perception, Stealth*", lang="Common, Thieves' Cant",
  traits=[("Sharpshooter", "The archer's ranged attacks ignore Half Cover and Three-Quarters Cover, and long range doesn't impose Disadvantage on its ranged attack rolls.")],
  attacks=[("Longbow", "r", "1d8", "Piercing", "", "150/600 ft.")], multi=3,
  bonus=[("Hide", "The archer takes the Hide action.")],
  desc="The killer on the roof three streets away. The victim never sees the archer, only the arrow.")),
(A, M("Blade Dancer", "M", HUM, "Chaotic Neutral", 10, "12 22 16 12 14 16", ac=19, saves="Dex, Wis", skills="Acrobatics*, Performance, Perception", lang="Common, and one other language",
  traits=[("Dance of Blades", "The dancer doesn't provoke Opportunity Attacks.")],
  attacks=[("Twin Scimitars", "f", "2d6", "Slashing")], multi=4,
  bonus=[("Whirl", "The dancer moves up to half its Speed.")],
  react=[("Riposte", "When a creature misses the dancer with a melee attack, the dancer makes one Twin Scimitars attack against it."),
         ("Parry", "The dancer adds 4 to its AC against one melee attack that would hit it. To do so, the dancer must see the attacker.")],
  desc="A sword dancer of the southern courts whose performance ends with an execution. The audience never sees the blades.")),
]
