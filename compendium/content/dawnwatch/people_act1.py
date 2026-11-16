"""The people of Act I of The Dawnwatch, Book One (chapters 2 to 5).

A person who fights is a pair (role, M(...)). A person with no statblock is a pair (role, "Name").
Chapters 7, 9, and 10 use some of these people again, by name.
"""
from monster_engine import M

R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())

NPCS = [
# ================= THE PEOPLE WITH STATBLOCKS =================
("A priest of the Church of the Five Sleepers who thinks that the party are impostors. Chapters 3, 4, and 9.",
 M("Brother Cade", "M", "Humanoid", "Lawful Good", 2, "14 10 14 13 16 11", ac=16, saves="Wis", skills="Insight, Religion", lang="Common",
   traits=[("Plain Speech", "Cade has Advantage on Wisdom (Insight) checks to tell if a creature is lying.")],
   attacks=[("Mace", "m", "1d6", "Bludgeoning", "plus {1d6} Radiant damage")], multi=2,
   actions=[("Spellcasting", "Cade casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). "
             "At will: Light, Thaumaturgy. 1/Day each: Bless, Cure Wounds, Zone of Truth.")],
   react=[("Stand Between", "When a creature that Cade can see attacks an ally within 5 feet of him, Cade imposes Disadvantage on the attack roll.")],
   desc="A broad, tired priest with ink on his fingers and a mace on his belt. He has seen a hundred false saints, and he believes in the true ones too much to let a fake one pass.")),
("The enforcer of Mother Sallow. Big, and he does not speak. Chapters 4 and 7.",
 M("Osk", "L", "Humanoid", "Lawful Evil", 4, "19 10 18 6 12 7", ac=15, saves="Str, Con", skills="Athletics", lang="understands Common and Hush Sign but doesn't speak",
   senses="Darkvision 60 ft.",
   traits=[("Silent", "Osk makes no sound when he moves, and he has Advantage on Dexterity (Stealth) checks in Darkness.")],
   attacks=[("Iron Maul", "m", "2d6", "Bludgeoning")], multi=2,
   bonus=[("Carry Off", "One Medium or smaller creature within 5 feet of Osk makes a {dc:str} Strength or Dexterity saving throw. "
           "On a failed save, the creature has the Grappled condition (escape {dc:str}). "
           "While Osk grapples a creature this way, he moves at his full Speed.")],
   react=[("Her Shield", "When a creature that Osk can see hits Mother Sallow within 5 feet of him with an attack, Osk becomes the target of the attack instead.")],
   desc="A grey giant of a man, eight feet tall, with a shaved head and a sewn-up mouth. Nobody knows if the Hush did it, or if he did it himself.")),
("The leader of the Hush, the cult of the Unlit King. She escapes at the end of Act I. Chapters 4, 7, and 10.",
 M("Mother Sallow", "M", "Humanoid", "Lawful Evil", 5, "9 12 14 14 18 16", ac=14, saves="Wis, Cha", skills="Deception, Insight, Religion", lang="Common, Hush Sign",
   senses="Darkvision 60 ft.",
   traits=[("Eyes of the Unlit", "Magical Darkness doesn't stop Mother Sallow's Darkvision."),
           ("The Quiet Faith", "Each member of the Hush within 30 feet of Mother Sallow has Advantage on saving throws against the Charmed and Frightened conditions.")],
   attacks=[("Grey Hand", "s:wis", "2d8", "Cold", "", "60 ft.")], multi=2,
   actions=[("Spellcasting", "Mother Sallow casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). "
             "At will: Chill Touch, Thaumaturgy. 1/Day each: Darkness, Hold Person, Silence.")],
   bonus=[("Put Out the Light", "Each nonmagical flame within 30 feet of Mother Sallow goes out. A magical light in that area that comes from a spell of level 3 or lower, or from a creature or an object that is not an Artifact, "
           "sheds only Dim Light until the end of her next turn.")],
   react=[("Into the Dark (1/Day)", "When Mother Sallow takes damage while she is in Dim Light or Darkness, she teleports up to 90 feet to an unoccupied space in Dim Light or Darkness that she can see.")],
   desc="A small grey woman with a kind face and cold hands. She speaks softly, like a nurse at a sickbed, and she believes every word she says. The sun is dying. Only the king can save it.")),
("The ruler of Gaunt, who wants the Dawnwatch as banners for her army. Chapters 5 and 9.",
 M("Marshal Ide Gauntry", "M", "Humanoid", "Lawful Neutral", 8, "17 12 16 14 15 17", ac=18, saves="Str, Con, Wis", skills="Athletics, History, Insight, Intimidation", lang="Common",
   traits=[("Gauntry Command", "Each ally of the marshal within 30 feet of her that can see her has Advantage on saving throws against the Frightened condition.")],
   attacks=[("Longsword", "m", "2d6", "Slashing", "plus {1d8} Slashing damage if the marshal has Advantage on the attack roll")], multi=3,
   bonus=[("Orders", "One ally that the marshal can see within 30 feet of her can take a Reaction to move up to half its Speed or to make one weapon attack.")],
   react=[("Parry", "The marshal adds 3 to her AC against one melee attack roll that would hit her. She must see the attacker and hold a weapon.")],
   desc="A tall woman of sixty with grey braids and a soldier's back. She has ruled Gaunt for twenty years, and she has never lost a battle. She does not intend to start now.")),

# ================= THE PEOPLE WITH NO STATBLOCK =================
("The old ferry woman at Brannock's Ford. Kind, and she asks too many questions. Chapter 2.", "Tamsin"),
("A pedlar who sells \"bones of the Five Sleepers\" to pilgrims. Chapters 2 and 3.", "Dace"),
("An antiquary from Corrantey who buys old things of Ostrey. Chapters 2 and 3.", "Corvin Lisle"),
("The head of the Church in Saint Ivo's. She wants the party as living saints. Chapters 3 and 9.", "Abbess Merrow"),
("The leader of a troupe of actors who play the Dawnwatch. Chapter 3.", "Garret Pell"),
("The son of Marshal Ide Gauntry. He does not want a war. Chapters 5 and 9.", "Tobin Gauntry"),
("The first war mage of Gaunt, who teaches a \"Dawnwatch spell\" that is wrong. Chapter 5.", "Magister Aud Brennet"),
]
