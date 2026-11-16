"""The people with statblocks of The Dawnwatch, Book One, Act II (chapters 6 to 10).

The format is the same as in content/npcs: a pair (role, M(...)). The role is
one of the keys of ROLES in build/render_npcs.py. Each person is a Humanoid.
Sergeant Maud Kettle is a ghost, so she is in creatures_act2.py.
"""
from monster_engine import M
R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())
G, C, K = "Guards and Soldiers", "Criminals and Spies", "Cultists"
HUM = "Humanoid"


def legres(n):
    return (f"Legendary Resistance ({n}/Day)", "If the creature fails a saving throw, it can choose to succeed instead.")


NPCS = [
(C, M("Captain Ilse Varro", "M", HUM, "Lawful Neutral", 6, "12 18 14 14 14 16", ac=16, saves="Dex, Int",
  skills="Deception, Insight, Perception, Stealth*", lang="Common, and the trade speech of Corrantey",
  traits=[("Quiet Work", "Once on each of her turns, Ilse deals an extra {3d6} damage to a creature that she hits with a weapon attack "
                         "if she has Advantage on the attack roll, or if an ally of hers is within 5 feet of the target.")],
  attacks=[("Rapier", "f", "1d8", "Piercing"), ("Hand Crossbow", "r", "1d6", "Piercing", "", "30/120 ft.")], multi=3,
  bonus=[("Gaunt Training", "Ilse takes the Dash, Disengage, or Hide action."),
         ("Smoke Pellet (1/Day)", "Ilse throws a pellet at a point within 30 feet. Grey smoke fills a 10-foot-radius Sphere there. "
                                  "The area is Heavily Obscured for 1 minute or until a strong wind disperses it.")],
  react=[("Turn Aside", "When an attacker that Ilse can see hits her with an attack, she halves the damage that she takes from it.")],
  desc="The quiet hand of Marshal Gauntry in the city of Corrantey. She buys what she can, steals what she must, "
       "and keeps a list of the people who owe her.")),
(G, M("Marshal Ide Gauntry", "M", HUM, "Lawful Neutral", 8, "18 12 16 14 16 18", ac=19, saves="Str, Con, Wis",
  skills="Athletics, History, Insight, Intimidation", lang="Common, and the old speech of Ostrey",
  traits=[("Iron Will (2/Day)", "If the marshal fails a saving throw, she can reroll it, and she must use the new roll."),
          ("The Banner of Gaunt", "Allies within 30 feet of the marshal that can see her have Advantage on saving throws against the Frightened condition.")],
  attacks=[("Gauntry Longsword", "m", "2d8", "Slashing"),
           ("Shield Bash", "m", "1d6", "Bludgeoning", "and the target has the Prone condition if it is Large or smaller")], multi=3,
  bonus=[("Hold the Line", "Up to three allies within 30 feet that can hear the marshal each gain {2d6} Temporary Hit Points.")],
  react=[("Parry", "The marshal adds 3 to her AC against one melee attack that would hit her. To do so, she must see the attacker.")],
  desc="The ruler of Gaunt, in plain steel and a grey cloak. She has read every book about old Ostrey. "
       "She believes that a land needs a strong hand, and that her hand is the strongest.")),
(K, M("Mother Sallow, Unbound", "M", HUM, "Neutral Evil", 11, "10 14 16 16 20 18", ac=17, saves="Con, Wis, Cha",
  skills="Deception, Insight, Religion, Stealth", senses="Darkvision 120 ft.", lang="Common, and the old speech of Ostrey",
  res=R(Resistances="Necrotic, Psychic"),
  traits=[legres(2),
          ("Grey Sight", "Mother Sallow sees normally in Dim Light and in darkness, magical darkness included, out to 120 feet."),
          ("Unbound", "The first time Mother Sallow is Bloodied, darkness bursts from her. Each creature within 20 feet of her makes a {dc:wis} "
                      "Constitution saving throw, taking {4d10} Necrotic damage on a failed save or half as much on a success.")],
  attacks=[("Grey Knife", "f", "2d6", "Piercing", "plus {3d8} Necrotic damage"),
           ("Word of Ending", "s:wis", "4d10", "Psychic", "", "120 ft.")], multi=2,
  actions=[("Spellcasting", "Mother Sallow casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). "
                            "At will: Darkness, Thaumaturgy. 1/Day each: Blight, Dispel Magic, Hold Monster."),
           ("The Long Night (Recharge 5–6)", "Each creature of her choice in a 30-foot-radius Sphere centered on a point within 120 feet makes a "
                                             "{dc:wis} Wisdom saving throw. On a failed save, it takes {8d8} Psychic damage and has the Frightened condition "
                                             "until the end of its next turn. On a successful save, it takes half as much damage only.")],
  leg=[("Knife", "Mother Sallow makes one Grey Knife attack."),
       ("Fade", "Mother Sallow teleports up to 30 feet to an unoccupied space in Dim Light or darkness that she can see."),
       ("Snuff (Costs 2)", "Each light within 60 feet of Mother Sallow goes out, except sunlight and the pieces of the Dawnfire. "
                           "One creature that she can see within 60 feet makes a {dc:wis} Constitution saving throw or takes {3d10} Necrotic damage.")],
  desc="The leader of the Hush, at the end of her road. She drank the dark of the empty crystal, and now it drinks her. "
       "Use this statblock in place of Mother Sallow in the last chapter of Book One.")),
]
