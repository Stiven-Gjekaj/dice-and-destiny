"""The new creatures of The Dawnwatch, Book One, Act II (chapters 6 to 10).

The format is the same as in content/monsters. The engine in
build/monster_engine.py calculates AC, Hit Points, attack bonuses, and save DCs.
"""
from monster_engine import M
R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())
UNDEAD = "Charmed, Exhaustion, Frightened, Poisoned"
GHOST = "Charmed, Exhaustion, Frightened, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained"
CONSTRUCT = "Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned"
GREY_SIGHT = ("Grey Sight", "The creature sees normally in Dim Light and in Darkness, magical Darkness included, out to 30 feet.")
INCORPOREAL = ("Incorporeal Movement", "The creature can move through other creatures and objects as if they were Difficult Terrain. "
               "It takes {1d10} Force damage if it ends its turn inside an object.")


def legres(n):
    return (f"Legendary Resistance ({n}/Day)", "If the creature fails a saving throw, it can choose to succeed instead.")


MON = [
# ================= THE HUSH =================
M("Hush Night Warden", "M", "Humanoid", "Lawful Evil", 4, "16 12 16 10 12 11", ac=17, skills="Perception, Stealth",
  lang="Common, Hush Sign", traits=[GREY_SIGHT],
  attacks=[("Grey Mace", "m", "1d8", "Bludgeoning", "plus {1d6} Necrotic damage"),
           ("Light Crossbow", "r", "1d8", "Piercing", "", "80/320 ft.")], multi=2,
  bonus=[("Snuff", "The warden pinches its fingers. One nonmagical flame or light that it can see within 30 feet goes out: "
                   "a torch, a candle, a lantern, or a campfire. A magical light flickers but stays lit.")],
  react=[("Close the Ranks", "When an ally within 5 feet of the warden is hit by an attack roll, the warden adds 2 to that ally's AC "
                             "against the attack, possibly causing it to miss.")],
  desc="The soldiers of the Hush wear grey mail with no badge. They do not shout in battle. "
       "They put out the lights first, and then they come."),
M("Hush Grey Choir", "L", "Swarm of Medium Humanoids", "Lawful Evil", 6, "12 10 14 10 14 14", ac=13,
  lang="Common, Hush Sign", res=R(Resistances="Bludgeoning, Piercing, Slashing",
                       Immunities="Charmed, Frightened, Grappled, Paralyzed, Petrified, Prone, Restrained, Stunned"),
  traits=[GREY_SIGHT,
          ("Swarm", "The choir is a crowd of grey-robed singers who move as one. It can occupy another creature's space and vice versa, "
                    "and it can move through any opening large enough for a Medium creature. It can't regain Hit Points or gain Temporary Hit Points."),
          ("Song of the Long Night", "The choir sings with closed mouths. Bright Light within 30 feet of the choir becomes Dim Light, "
                                     "and creatures within 30 feet of it have Disadvantage on Constitution saving throws to keep Concentration.")],
  attacks=[("Knives and Cudgels", "f", "4d6", "Slashing", "or {2d6} Slashing damage if the choir has half its Hit Points or fewer")],
  actions=[("Hymn of Quiet (Recharge 5–6)", "Each creature of the choir's choice within 30 feet of it makes a {dc:cha} Wisdom saving throw. "
                                            "On a failed save, the creature takes {6d8} Psychic damage and can't speak until the end of its next turn. "
                                            "On a successful save, it takes half as much damage only.")],
  desc="Twenty grey robes, twenty hoods, one hum. The choir walks in front of the Hush and sings the light away."),
M("Hush Dusk Priest", "M", "Humanoid", "Lawful Evil", 7, "10 14 14 13 18 15", ac=14, saves="Wis, Cha",
  skills="Insight, Religion", lang="Common, Hush Sign", traits=[GREY_SIGHT],
  attacks=[("Word of Night", "s:wis", "3d10", "Psychic", "", "120 ft."),
           ("Iron Censer", "m", "1d6", "Bludgeoning", "plus {2d6} Necrotic damage")], multi=2,
  actions=[("Spellcasting", "The priest casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). "
                            "At will: Thaumaturgy. 1/Day each: Darkness, Hold Person, Silence."),
           ("Snuff the Sun (Recharge 5–6)", "The priest closes a fist. Each creature in a 20-foot-radius Sphere centered on a point within 60 feet "
                                            "makes a {dc:wis} Constitution saving throw, taking {5d8} Necrotic damage on a failed save or half as much on a success. "
                                            "Each light in the Sphere goes out, and magical light in it is suppressed until the end of the priest's next turn.")],
  react=[("Dim the Flame", "When a creature that the priest can see within 60 feet makes an attack roll that would deal Radiant damage, "
                           "the priest gives the roll Disadvantage.")],
  desc="The priests of the Hush lead the prayers of the cult: long silences, broken by one word. "
       "Each priest believes that the sun is dying. Each one is partly right."),

# ================= CHAPTER 6: CORRANTEY =================
M("Brass Lamp Warden", "L", "Construct", "Unaligned", 5, "18 10 18 3 10 1", ac=17, speed="25 ft.",
  senses="Darkvision 60 ft.", lang="understands Common but can't speak",
  res=R(Resistances="Fire", Immunities="Poison, Psychic; " + CONSTRUCT),
  traits=[("Lamp Heart", "A flame burns in the chest of the warden. It sheds Bright Light in a 20-foot radius and Dim Light for 20 feet more."),
          ("Maker's Mark", "The warden doesn't attack a creature that carries Wick, the talking lantern of Haskel Orme, "
                           "unless that creature attacks it first. It knows Wick as the work of its own maker."),
          ("Constructed Nature", "The warden doesn't need air, food, drink, or sleep.")],
  attacks=[("Brass Fist", "m", "2d8", "Bludgeoning")], multi=2,
  actions=[("Flare (Recharge 5–6)", "The flame in the warden's chest roars out in a 15-foot Cone. Each creature in the Cone makes a {dc:con} Dexterity saving throw. "
                                    "On a failed save, it takes {6d6} Fire damage and has the Blinded condition until the end of its next turn. "
                                    "On a successful save, it takes half as much damage only.")],
  desc="A brass figure eight feet tall, with a lamp where its heart should be. Haskel Orme made six of them "
       "to guard the hall that his apprentices would build. Each one carries a small stamp on its heel: a sun inside a square."),

# ================= CHAPTER 8: FENNICK =================
M("Fennick Drowned", "M", "Undead", "Neutral Evil", 2, "15 8 16 6 8 5", ac=11, speed="20 ft., swim 30 ft.",
  senses="Darkvision 60 ft.", res=R(Immunities="Poison; " + UNDEAD),
  traits=[("Waterlogged", "The drowned doesn't need to breathe. It has Advantage on attack rolls against a creature that is underwater and isn't a swimmer by nature."),
          ("Still Here", "If damage reduces the drowned to 0 Hit Points while it is in water, it makes a Constitution saving throw with a DC of 5 plus the damage taken, "
                         "unless the damage is Radiant or from a Critical Hit. On a success, it drops to 1 Hit Point instead.")],
  attacks=[("Clutching Hands", "m", "2d6", "Bludgeoning", "and the target has the Grappled condition (escape {dc:str}). "
                                                         "While the target is Grappled and underwater, the drowned can swim with it at half Speed")],
  desc="The people of Fennick, two hundred years under the water. They still walk to the market. They still go to church. "
       "They want company."),
M("Grief of Fennick", "L", "Undead", "Neutral", 8, "6 14 18 12 16 20", ac=14, speed="0 ft., fly 40 ft. (hover), swim 40 ft.",
  saves="Wis, Cha", senses="Darkvision 120 ft.", lang="understands Common but speaks only with the voices of the drowned",
  res=R(Resistances="Acid, Fire, Lightning, Thunder; Bludgeoning, Piercing, Slashing",
        Immunities="Cold, Necrotic, Poison; " + GHOST),
  traits=[INCORPOREAL,
          ("The Bell", "While the grief is within 300 feet of the bell of Fennick, it regains 10 Hit Points at the start of each of its turns. "
                       "If the bell is rung three times in one round, the grief loses this trait until it finishes a Long Rest."),
          ("Many Faces", "The grief is the sorrow of a whole town. It has Advantage on saving throws against the Charmed and Frightened conditions, "
                         "and it can't be turned or destroyed by the Turn Undead feature.")],
  attacks=[("Cold Hand", "f", "3d8", "Cold", "and the target's Speed is halved until the end of its next turn")], multi=2,
  actions=[("Wail of the Drowned (Recharge 5–6)", "Each creature within 30 feet of the grief that can hear it makes a {dc:cha} Wisdom saving throw. "
                                                  "On a failed save, the creature takes {6d10} Psychic damage and has the Frightened condition until the end of its next turn. "
                                                  "On a successful save, it takes half as much damage only.")],
  bonus=[("Call the Drowned", "One Fennick Drowned that the grief can see within 60 feet moves up to its Speed and makes one Clutching Hands attack. "
                              "The drowned uses its Reaction to do so.")],
  desc="When the water came, the whole town screamed at once. The scream never stopped. It became this: a cold grey shape in the drowned church, "
       "with a hundred faces that come and go in it like bubbles."),
M("Sergeant Maud Kettle", "M", "Undead", "Lawful Good", 5, "16 14 14 10 14 12", ac=17, speed="30 ft., fly 30 ft. (hover)",
  saves="Str, Con", skills="Athletics, Insight, Intimidation", senses="Darkvision 60 ft.", lang="Common (the old speech of Ostrey)",
  res=R(Resistances="Acid, Fire, Lightning, Thunder; Bludgeoning, Piercing, Slashing", Immunities="Cold, Necrotic, Poison; " + GHOST),
  traits=[INCORPOREAL,
          ("Bound to the Tower", "Maud can't go more than 1 mile from the bell tower of Fennick. If she is destroyed while her duty is not done, "
                                 "she forms again in the tower at the next dusk."),
          ("Old Drill", "Maud uses Techniques as a character does. She has 3 technique points and regains them when she finishes a Short Rest. "
                        "She knows Driving Strike and Turn the Blade (both in the Techniques chapter of the Player's Compendium). Her techniques use {dc:str}."),
          ("Only Sparring", "When Maud reduces a creature to 0 Hit Points in a fight that she calls a drill, the creature drops to 1 Hit Point instead.")],
  attacks=[("Ghostly Halberd", "m", "1d10", "Slashing", "plus {1d8} Cold damage", "10 ft.")], multi=2,
  bonus=[("On Your Feet", "Maud barks an order at one creature within 60 feet that can hear her. If it has the Prone condition, it can stand up "
                          "without spending movement, and it has Advantage on its next attack roll before the end of its next turn.")],
  desc="A sergeant of the last garrison of the king in Fennick, in the Grey Winter. She died on the bell tower, ringing the bell as the water came. "
       "She has drilled her drowned squad every morning for two hundred years. They are not getting any better."),

# ================= CHAPTER 10: KINGSHOLM =================
M("The Unlit Knight", "M", "Undead", "Lawful Neutral", 12, "22 12 20 14 16 18", ac=20, saves="Str, Con, Wis",
  skills="Athletics, Perception", senses="Darkvision 120 ft., Truesight 30 ft.", lang="Common (the old speech of Ostrey)",
  res=R(Resistances="Cold, Psychic", Immunities="Necrotic, Poison; " + UNDEAD),
  traits=[legres(2),
          ("Unlit", "Bright Light within 30 feet of the knight becomes Dim Light. Sunlight is not affected."),
          ("Last Words", "When the knight drops to 0 Hit Points, its armor falls empty, and a voice in it says the old motto of the Dawnwatch: "
                         "\"We watch so that the dawn can wake.\"")],
  attacks=[("Black Greatsword", "m", "2d10", "Slashing", "plus {2d8} Necrotic damage")], multi=3,
  actions=[("Eclipse (Recharge 5–6)", "Darkness pours out of the knight's visor. Each creature within 30 feet of it makes a {dc:con} Constitution saving throw. "
                                      "On a failed save, the creature takes {8d8} Necrotic damage and can't regain Hit Points until the start of the knight's next turn. "
                                      "On a successful save, it takes half as much damage only.")],
  bonus=[("Dark Step", "The knight teleports up to 30 feet to an unoccupied space in Dim Light or Darkness that it can see.")],
  react=[("Parry", "The knight adds 4 to its AC against one melee attack that would hit it. To do so, it must see the attacker.")],
  leg=[("Strike (Costs 2)", "The knight makes one Black Greatsword attack."),
       ("Advance", "The knight moves up to half its Speed. It doesn't provoke Opportunity Attacks."),
       ("Night Falls (Costs 2)", "Each creature of the knight's choice within 30 feet of it makes a {dc:cha} Wisdom saving throw. "
                                 "On a failed save, it has the Blinded condition until the end of its next turn.")],
  desc="A suit of old plate, black as wet slate, that stands guard at the foot of an empty crystal. There is no one inside it. "
       "There is only the dark that the sleeper left behind, and the habit of a knight who kept watch."),
]
