"""Original NPCs, the last batch: cults, ships, the underworld, and the court."""
from monster_engine import M
R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())
N, C, CU, S, A = "Nobles and Officials", "Criminals and Spies", "Cultists", "Sailors and Pirates", "Assassins and Duelists"
HUM = "Humanoid"

NPCS = [
# ================= CULTISTS =================
(CU, M("Hooded Torchbearer", "M", HUM, "Chaotic Evil", 0.5, "12 12 12 10 10 12", ac=12, lang="Common",
  traits=[("Sacred Flame Bearer", "While the torchbearer holds its torch, it sheds Bright Light in a 20-foot radius, and its attacks deal an extra {1d4} Fire damage.")],
  attacks=[("Burning Torch", "m", "1d6", "Bludgeoning")],
  desc="A hooded cultist who carries the torches in the night procession. It doesn't ask what the fire is for.")),
(CU, M("Ash Priest of the Burned God", "M", HUM, "Chaotic Evil", 5, "12 12 16 12 16 16", ac=14, skills="Intimidation, Religion", lang="Common, Ignan",
  res=R(Resistances="Fire"),
  traits=[("Smoke Veil", "The priest's space is Lightly Obscured.")],
  attacks=[("Ember Rod", "m", "1d6", "Bludgeoning", "plus {3d8} Fire damage")], multi=2,
  actions=[("Burning Hymn (Recharge 5–6)", "Each creature of the priest's choice within 20 feet makes a {dc:wis} Dexterity saving throw, taking {6d8} Fire damage on a failed save or half as much damage on a successful one."),
           ("Spellcasting", "The priest casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). 1/Day each: Flame Strike, Scorching Ray.")],
  desc="A priest with ash on its face and hands, who teaches that everything must burn to be pure.")),
(CU, M("Voice of the Abyss", "M", HUM, "Chaotic Evil", 14, "14 16 18 18 18 22", ac=18, saves="Con, Wis, Cha", skills="Arcana, Deception, Persuasion, Religion", lang="Common, Abyssal, Infernal; telepathy 60 ft.",
  res=R(Resistances="Fire, Necrotic, Psychic", Immunities="Charmed, Frightened"),
  traits=[("Indomitable (3/Day)", "If the voice fails a saving throw, it can reroll the save and must use the new roll."),
          ("Demon Pact (1/Day)", "When the voice drops to 0 Hit Points, a Hezrou from the SRD appears in an unoccupied space within 30 feet of it and acts on its own Initiative, and the voice regains 30 Hit Points instead of dropping to 0. When you build an encounter, count the Hezrou as a separate monster.")],
  attacks=[("Abyssal Lash", "s:cha", "6d10", "Necrotic", "", "120 ft.")], multi=2,
  actions=[("Word of Ruin (Recharge 5–6)", "Each creature of the voice's choice within 60 feet that can hear it makes a {dc:cha} Wisdom saving throw. On a failed save, a creature takes {10d8} Psychic damage and has the Frightened condition until the end of its next turn. On a successful save, it takes half as much damage only."),
           ("Spellcasting", "The voice casts one of the following spells, using Charisma as the spellcasting ability ({dc:cha}). 1/Day each: Dominate Person, Plane Shift, Wall of Fire.")],
  desc="The grandmaster of a demon cult, who has spoken with the abyss so long that the abyss now speaks through it.")),

# ================= SAILORS AND PIRATES =================
(S, M("Powder Monkey", "S", HUM, "Chaotic Neutral", 0.125, "8 13 10 10 11 10", skills="Acrobatics, Stealth", speed="30 ft., climb 30 ft.", lang="Common",
  traits=[("Quick Climber", "The powder monkey can climb ropes and rigging at full Speed.")],
  attacks=[("Knife", "f", "1d4", "Piercing")],
  desc="The youngest of the crew, who runs powder and messages across the deck in battle. Faster than anyone, and braver than they should be.")),
(S, M("Ship's Surgeon", "M", HUM, "Neutral Good", 2, "10 14 12 15 15 10", skills="Medicine*, Nature", speed="30 ft., swim 30 ft.", lang="Common, and one other language",
  traits=[("Sea Medicine", "During a Short Rest, each ally that the surgeon tends regains an extra {1d8} Hit Points when it spends Hit Point Dice.")],
  attacks=[("Bone Saw", "f", "1d6", "Slashing")], multi=2,
  bonus=[("Quick Bandage", "One creature within 5 feet regains {2d6} Hit Points. (3/Day)")],
  desc="The crew's healer, who pulls teeth, sets bones, and keeps a bottle of rum for the pain, mostly their own.")),
(S, M("Admiral of the Black Fleet", "M", HUM, "Neutral Evil", 11, "16 18 16 14 14 18", ac=18, saves="Dex, Wis, Cha", skills="Athletics, Intimidation, Perception", speed="30 ft., swim 30 ft.", lang="Common, and the languages of five ports",
  traits=[("Black Flag", "Pirate allies within 60 feet of the admiral that can see its flag have Advantage on saving throws against being Frightened."),
          ("Feared Name", "The admiral has Advantage on Charisma (Intimidation) checks against sailors and merchants.")],
  attacks=[("Cutlass", "f", "2d10", "Slashing"), ("Pistol Crossbow", "r", "2d8", "Piercing", "", "60/180 ft.")], multi=3,
  actions=[("Broadside (Recharge 5–6)", "The admiral's ship fires. Each creature in a 60-foot-long, 20-foot-wide Line beside the ship makes a {dc:cha} Dexterity saving throw, taking {8d10} Bludgeoning damage on a failed save or half as much damage on a successful one. This works only while the admiral is on its ship.")],
  bonus=[("Swing on the Rigging", "The admiral moves up to its Speed without provoking Opportunity Attacks.")],
  react=[("Parry", "The admiral adds 4 to its AC against one melee attack that would hit it. To do so, the admiral must see the attacker.")],
  desc="The lord of a pirate fleet that rules a whole sea. Kings pay it not to raid, and it raids anyway.")),

# ================= CRIMINALS AND SPIES =================
(C, M("Tunnel Smuggler", "S", HUM, "Neutral", 0.5, "10 15 12 11 13 10", skills="Perception, Stealth*", lang="Common, Thieves' Cant",
  traits=[("Tunnel Rat", "The smuggler can squeeze through a space as narrow as 1 foot wide without slowing down.")],
  attacks=[("Short Sword", "f", "1d6", "Piercing"), ("Sling", "r", "1d4", "Bludgeoning", "", "30/120 ft.")],
  desc="A small, quick runner who moves goods through the old sewers under the city wall.")),
(C, M("Blackmailer", "M", HUM, "Lawful Evil", 2, "9 14 12 16 16 15", ac=13, skills="Deception, Insight*, Investigation", lang="Common, Thieves' Cant, and two other languages",
  traits=[("Insurance", "The blackmailer has left letters with a friend. If it dies or disappears, the letters go to the people who would be hurt by them.")],
  attacks=[("Hidden Pistol Crossbow", "r", "1d8", "Piercing", "", "30/120 ft.")], multi=2,
  actions=[("I Know Your Secret (Recharge 5–6)", "One creature within 30 feet that can hear the blackmailer makes a {dc:int} Wisdom saving throw. On a failed save, it has the Charmed condition for 1 hour and won't harm the blackmailer. The effect ends if the blackmailer or its allies harm the target.")],
  desc="A polite person with a ledger of other people's secrets. They never threaten. They only remind.")),

# ================= NOBLES AND OFFICIALS =================
(N, M("Old Duke", "M", HUM, "Lawful Neutral", 7, "14 10 14 16 18 18", ac=17, saves="Wis, Cha", skills="History, Insight*, Intimidation, Persuasion", lang="Common, and three other languages",
  traits=[("Household Guard", "The duke is guarded by {1d4+2} Line Pikemen and one Shield-Wall Captain. When you build an encounter, count them as separate monsters."),
          ("Old Fox", "The duke can't be surprised, and it has Advantage on saving throws against being Charmed.")],
  attacks=[("Sword Cane", "f", "1d8", "Piercing", "plus {3d6} Poison damage")], multi=2,
  actions=[("Command the House (Recharge 5–6)", "Up to four allies within 60 feet that can hear the duke can each use a Reaction to move up to their Speed and make one weapon attack.")],
  desc="A noble who has outlived three kings, two wars, and every rival at court. It is in no hurry.")),

# ================= ASSASSINS AND DUELISTS =================
(A, M("Veiled Courier", "M", HUM, "Neutral", 4, "10 18 12 12 14 12", ac=15, skills="Acrobatics, Insight, Stealth*", lang="Common, Thieves' Cant",
  traits=[("Sealed Message", "The courier carries one message that it must deliver. It has Advantage on saving throws against being Charmed or Frightened while it carries the message.")],
  attacks=[("Twin Daggers", "f", "1d4", "Piercing", "plus {2d6} Poison damage")], multi=2,
  bonus=[("Slip Away", "The courier takes the Dash, Disengage, or Hide action.")],
  desc="A messenger of the assassins' guild, who delivers contracts and sometimes carries them out.")),
]
