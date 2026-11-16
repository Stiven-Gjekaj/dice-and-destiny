"""Original NPCs of the sea, the schools, the wild, and the shadows."""
from monster_engine import M
R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())
S, SC, W, A = "Sailors and Pirates", "Scholars and Mages", "Wilderness Folk", "Assassins and Duelists"
HUM = "Humanoid"

NPCS = [
# ================= SAILORS AND PIRATES =================
(S, M("Deckhand", "M", HUM, "Neutral", 0.125, "13 12 12 9 10 9", skills="Athletics", speed="30 ft., swim 30 ft.", lang="Common",
  traits=[("Sea Legs", "The deckhand has Advantage on saving throws against the Prone condition on a ship.")],
  attacks=[("Belaying Pin", "m", "1d4", "Bludgeoning")])),
(S, M("Harpooner", "M", HUM, "Neutral", 2, "16 14 14 10 12 10", ac=13, skills="Athletics, Perception", speed="30 ft., swim 30 ft.", lang="Common",
  attacks=[("Harpoon", "m", "1d10", "Piercing", "and the target has the Grappled condition (escape {dc:str}) if it is Large or smaller. The harpooner can pull the target up to 15 feet toward it", "10 ft."),
           ("Boarding Axe", "m", "1d8", "Slashing")], multi=2,
  desc="A whaler with forearms like rope and the patience to wait for the right throw.")),
(S, M("Corsair Commodore", "M", HUM, "Chaotic Neutral", 9, "16 18 16 14 14 18", ac=17, saves="Dex, Wis, Cha", skills="Acrobatics, Athletics, Intimidation, Perception", speed="30 ft., swim 30 ft.", lang="Common, and the languages of three ports",
  traits=[("Fleet Signal", "The commodore can signal its fleet with flags or lanterns. Its orders reach every ship within 1 mile in 1 minute.")],
  attacks=[("Cutlass", "f", "2d8", "Slashing"), ("Pistol Crossbow", "r", "2d6", "Piercing", "", "60/180 ft.")], multi=3,
  bonus=[("Swing on the Rigging", "The commodore moves up to its Speed without provoking Opportunity Attacks. It can move across open air between two ships in this way.")],
  react=[("Parry", "The commodore adds 3 to its AC against one melee attack that would hit it. To do so, the commodore must see the attacker.")],
  desc="The admiral of the free fleets, whom three crowns call a pirate and a fourth calls an ally.")),

# ================= SCHOLARS AND MAGES =================
(SC, M("Battle Wizard", "M", HUM, "Neutral", 5, "10 14 14 18 12 12", ac=15, saves="Int, Wis", skills="Arcana, History", lang="Common, and three other languages",
  traits=[("Armored Caster", "The wizard wears magic armor that doesn't hinder its spellcasting.")],
  attacks=[("Arcane Bolt", "s:int", "3d8", "Force", "", "120 ft.")], multi=2,
  actions=[("Spellcasting", "The wizard casts one of the following spells, using Intelligence as the spellcasting ability ({dc:int}). At will: Light, Mage Hand. 1/Day each: Fireball, Misty Step.")],
  react=[("Ward", "When the wizard is hit by an attack roll, it gains a +5 bonus to AC against that attack, possibly causing it to miss. (2/Day)")],
  desc="A mage who studied war, not theory. The army pays for three of them in each company.")),
(SC, M("Magister of the Arcane College", "M", HUM, "Lawful Neutral", 15, "10 14 16 22 18 16", ac=17, saves="Int, Wis", skills="Arcana*, History*, Insight", lang="Common, and six other languages",
  res=R(Resistances="Force, Psychic"),
  traits=[("Magic Resistance", "The magister has Advantage on saving throws against spells and other magical effects."),
          ("Indomitable (3/Day)", "If the magister fails a saving throw, it can reroll the save and must use the new roll.")],
  attacks=[("Lance of Force", "s:int", "5d10", "Force", "", "150 ft.")], multi=3,
  actions=[("Spellcasting", "The magister casts one of the following spells, using Intelligence as the spellcasting ability ({dc:int}). At will: Detect Magic, Mage Hand. 2/Day each: Counterspell, Dispel Magic. 1/Day each: Cone of Cold, Globe of Invulnerability, Teleport, Wall of Force.")],
  react=[("Arcane Rebuke (2/Day)", "When a creature within 60 feet casts a spell, the magister forces it to make a {dc:int} Constitution saving throw. On a failed save, the spell fails and is wasted.")],
  desc="The head of the great school of magic. It has forgotten more spells than most mages will ever learn.")),

# ================= WILDERNESS FOLK =================
(W, M("Trapper", "M", HUM, "Neutral", 0.5, "12 14 12 10 13 9", skills="Nature, Stealth, Survival", lang="Common",
  traits=[("Snares", "The trapper sets {1d4} snares near its camp. A creature that steps on one makes a {dc:wis} Dexterity saving throw or has the Restrained condition (escape {dc:wis}).")],
  attacks=[("Hatchet", "f", "1d6", "Slashing"), ("Shortbow", "r", "1d6", "Piercing")],
  desc="A loner who lives on pelts and knows every animal trail for a day's walk.")),

# ================= ASSASSINS AND DUELISTS =================
(A, M("Nightblade Master", "M", HUM, "Lawful Evil", 14, "14 22 16 16 18 14", ac=19, saves="Dex, Int, Wis", skills="Acrobatics, Deception, Perception*, Stealth*", lang="Common, Thieves' Cant, and two other languages",
  traits=[("Evasion", "If the master is subjected to an effect that allows a Dexterity saving throw to take only half damage, it takes no damage on a success and only half damage on a failure."),
          ("Sneak Attack (1/Turn)", "The master deals an extra {8d6} damage when it hits a target with a weapon attack and has Advantage on the attack roll, or when the target is within 5 feet of an ally of the master that doesn't have the Incapacitated condition.")],
  attacks=[("Blackened Blade", "f", "2d6", "Slashing", "plus {2d8} Poison damage"), ("Throwing Star", "r", "1d6", "Slashing", "plus {2d8} Poison damage", "30/90 ft.")], multi=3,
  bonus=[("Cunning Action", "The master takes the Dash, Disengage, or Hide action.")],
  react=[("Uncanny Dodge", "When an attacker that the master can see hits it with an attack roll, the master halves the damage.")],
  desc="The teacher of the order of night blades. Its students are the best killers in the world, and they are all afraid of it.")),
]
