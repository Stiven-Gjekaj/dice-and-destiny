"""Original NPCs of the towns, the courts, the temples, and the docks."""
from monster_engine import M
R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())
G, N, P, T = "Guards and Soldiers", "Nobles and Officials", "Priests and the Faithful", "Merchants and Townsfolk"
C, CU, S = "Criminals and Spies", "Cultists", "Sailors and Pirates"
HUM = "Humanoid"

NPCS = [
# ================= MERCHANTS AND TOWNSFOLK =================
(T, M("Innkeeper", "M", HUM, "Neutral Good", 0.125, "13 10 14 11 13 13", skills="Insight, Persuasion", lang="Common, and one other language",
  traits=[("Heard It All", "The innkeeper knows the local rumors. A creature that buys a drink and asks can learn one useful rumor.")],
  attacks=[("Rolling Pin", "m", "1d4", "Bludgeoning")])),
(T, M("Farmhand Militia", "M", HUM, "Neutral", 0.125, "13 10 12 9 11 9", lang="Common",
  traits=[("Strength in Numbers", "The militia member has Advantage on saving throws against being Frightened while an ally is within 5 feet of it.")],
  attacks=[("Pitchfork", "m", "1d6", "Piercing", "", "10 ft.")])),
(T, M("Street Performer", "M", HUM, "Chaotic Good", 0.25, "10 15 11 11 12 15", skills="Acrobatics, Performance*, Sleight of Hand", lang="Common, and one other language",
  attacks=[("Juggling Knife", "f", "1d4", "Piercing", "", "20/60 ft.")],
  actions=[("Distracting Show", "Each creature of the performer's choice within 30 feet that can see it makes a {dc:cha} Wisdom saving throw or has Disadvantage on Wisdom (Perception) checks until the end of its next turn.")],
  desc="A juggler, a singer, or a fire-eater on the market square. Their friends in the crowd are the ones with quick hands.")),
(T, M("Master Smith", "M", HUM, "Lawful Good", 2, "18 10 16 11 12 10", ac=14, skills="Athletics", lang="Common",
  res=R(Resistances="Fire"),
  traits=[("Forge Arm", "The smith has Advantage on Strength checks and on saving throws against the Prone condition.")],
  attacks=[("Smith's Hammer", "m", "1d8", "Bludgeoning")], multi=2,
  desc="The person who makes the town's swords, plows, and horseshoes, and who knows exactly how strong each one is.")),

# ================= GUARDS AND SOLDIERS =================
(G, M("Mounted Lancer", "M", HUM, "Lawful Neutral", 3, "16 12 14 10 12 11", ac=18, skills="Animal Handling, Athletics", lang="Common",
  traits=[("Mounted", "The lancer rides a Warhorse from the SRD. While mounted, it has Advantage on melee attack rolls against creatures that are Medium or smaller and on foot. When you build an encounter, count the warhorse as a separate monster.")],
  attacks=[("Lance", "m", "1d12", "Piercing", "", "10 ft."), ("Longsword", "m", "1d8", "Slashing")], multi=2,
  desc="A light cavalry soldier who rides the border roads. A troop of lancers can break a bandit camp in one charge.")),
(G, M("Royal Guard", "M", HUM, "Lawful Neutral", 6, "17 14 16 11 14 12", ac=19, saves="Str, Con", skills="Athletics, Insight, Perception", lang="Common",
  traits=[("Sworn Protector", "While the guard's charge is within 5 feet of the guard and the guard doesn't have the Incapacitated condition, a creature that the guard can see has Disadvantage on attack rolls against the charge.")],
  attacks=[("Halberd", "m", "1d10", "Slashing", "", "10 ft.")], multi=3,
  react=[("Take the Blow", "When the guard's charge within 5 feet of the guard is hit by an attack roll, the guard takes the damage instead.")],
  desc="One of the picked soldiers who guard the royal family. They have sworn to die first, and some have.")),

# ================= NOBLES AND OFFICIALS =================
(N, M("Young Lordling", "M", HUM, "Lawful Neutral", 0.25, "10 13 11 12 9 14", ac=14, skills="Persuasion", lang="Common, and one other language",
  traits=[("Important Family", "A creature that harms the lordling has trouble with the lordling's family. The GM decides what kind.")],
  attacks=[("Dress Sword", "f", "1d6", "Piercing")],
  desc="The second son or third daughter of a great house, who wants adventure and has a guard who wants a quiet day.")),
(N, M("Baron of the Borderlands", "M", HUM, "Lawful Neutral", 5, "17 12 16 12 14 15", ac=18, saves="Str, Wis", skills="Athletics, Insight, Intimidation", lang="Common, and one other language",
  traits=[("Lord of the Keep", "In its own keep, the baron and its soldiers have Advantage on Initiative rolls.")],
  attacks=[("Longsword", "m", "2d8", "Slashing")], multi=2,
  bonus=[("Rally the Garrison", "Each ally within 30 feet that can hear the baron gains {1d8} Temporary Hit Points. (2/Day)")],
  desc="A rough noble who holds a castle at the edge of the realm. It cares more about walls than about court manners.")),

# ================= PRIESTS AND THE FAITHFUL =================
(P, M("Exorcist", "M", HUM, "Lawful Good", 5, "12 12 14 14 18 14", ac=15, saves="Wis, Cha", skills="Insight, Religion*", lang="Common, Celestial, Infernal",
  res=R(Resistances="Necrotic, Psychic"),
  traits=[("Holy Ward", "Fiends and Undead have Disadvantage on attack rolls against the exorcist.")],
  attacks=[("Blessed Censer", "m", "1d6", "Bludgeoning", "plus {3d8} Radiant damage")], multi=2,
  actions=[("Banishing Rite (Recharge 5–6)", "One Fiend or Undead within 30 feet makes a {dc:wis} Charisma saving throw. On a failed save, it takes {6d10} Radiant damage and has the Incapacitated condition until the end of its next turn. On a successful save, it takes half as much damage only."),
           ("Spellcasting", "The exorcist casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). 1/Day each: Dispel Evil and Good, Protection from Evil and Good, Remove Curse.")],
  desc="The temple's answer to a haunted house, a cursed child, or a demon in the cellar.")),
(P, M("Oracle of the Shrine", "M", HUM, "Neutral", 8, "9 12 14 14 20 16", ac=14, saves="Wis, Cha", skills="Insight*, Religion", lang="Common, Celestial",
  traits=[("Foresight", "The oracle can't be surprised, and attack rolls against it don't have Advantage unless it has the Incapacitated condition.")],
  attacks=[("Vision Ray", "s:wis", "4d8", "Psychic", "", "120 ft.")], multi=2,
  actions=[("Spellcasting", "The oracle casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). At will: Guidance. 1/Day each: Augury, Divination, Scrying.")],
  react=[("I Saw It Coming", "When the oracle is hit by an attack roll, it imposes Disadvantage on that roll, possibly causing it to miss. It can do this once each round.")],
  desc="A seer at a mountain shrine who answers one question for each pilgrim. The answer is always true and rarely useful.")),

# ================= CRIMINALS AND SPIES =================
(C, M("Forger", "M", HUM, "Neutral", 0.5, "9 15 11 15 12 13", skills="Deception, Investigation, Sleight of Hand*", lang="Common, Thieves' Cant, and two other languages",
  traits=[("Perfect Copy", "Given 1 day and a model, the forger can copy a document, a seal, or a signature. A creature tells the difference only with a successful {dc:int} Intelligence (Investigation) check.")],
  attacks=[("Stiletto", "f", "1d4", "Piercing")])),
(C, M("Spymaster of the Crown", "M", HUM, "Lawful Evil", 10, "10 16 14 20 18 18", ac=16, saves="Dex, Int, Wis", skills="Deception*, Insight*, Investigation, Persuasion", lang="Common, Thieves' Cant, and four other languages",
  traits=[("Web of Eyes", "The spymaster has a spy in every town of the realm. It learns about any public event within a day."),
          ("Contingency", "If the spymaster drops to 0 Hit Points, a hidden ally carries its papers to its successor.")],
  attacks=[("Sword Cane", "f", "2d6", "Piercing", "plus {3d6} Poison damage")], multi=2,
  actions=[("Turn an Agent (Recharge 5–6)", "One creature within 30 feet that can hear the spymaster makes a {dc:int} Wisdom saving throw. On a failed save, it takes {6d8} Psychic damage and has the Charmed condition until the end of its next turn. On a successful save, it takes half as much damage only.")],
  bonus=[("Signal", "Up to two allies within 60 feet that can see the spymaster can each use a Reaction to make one attack.")],
  desc="The quiet official who knows every secret in the kingdom. The queen reigns, but the spymaster knows why.")),

# ================= CULTISTS =================
(CU, M("Plague Preacher", "M", HUM, "Chaotic Evil", 6, "12 12 18 12 16 18", ac=14, skills="Deception, Medicine, Religion", lang="Common, Abyssal",
  res=R(Resistances="Necrotic, Poison", Immunities="Poisoned"),
  traits=[("Carrier", "A creature that starts its turn within 10 feet of the preacher makes a {dc:con} Constitution saving throw or has the Poisoned condition until the start of its next turn.")],
  attacks=[("Rotting Touch", "m", "2d6", "Necrotic", "plus {2d6} Poison damage")], multi=2,
  actions=[("Sermon of Rot (Recharge 5–6)", "Each creature of the preacher's choice within 30 feet that can hear it makes a {dc:cha} Constitution saving throw. On a failed save, a creature takes {6d8} Poison damage and has the Poisoned condition for 1 minute. It repeats the save at the end of each of its turns, ending the Poisoned condition on itself on a success. On a successful save, it takes half as much damage only."),
           ("Spellcasting", "The preacher casts one of the following spells, using Charisma as the spellcasting ability ({dc:cha}). 1/Day each: Contagion, Stinking Cloud.")],
  desc="A cult preacher who walks into plague towns and promises the sick a cure. Its god wants more sick.")),

# ================= SAILORS AND PIRATES =================
(S, M("Navigator", "M", HUM, "Neutral", 1, "10 14 12 15 15 11", skills="Nature, Perception, Survival", speed="30 ft., swim 30 ft.", lang="Common, and two other languages",
  traits=[("Star Reader", "On a clear night, the navigator always knows where the ship is, to within 10 miles.")],
  attacks=[("Brass Sextant Club", "m", "1d6", "Bludgeoning"), ("Light Crossbow", "r", "1d8", "Piercing")], multi=2,
  desc="The person with the charts, the stars, and the captain's ear. A ship without a navigator is a raft with a sail.")),
]
