"""Original coast monsters, added by a helper of the bestiary: tide pools, sea cliffs, fog banks, and wrecked harbors."""
from monster_engine import M
R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())
UNDEAD = "Charmed, Exhaustion, Frightened, Poisoned"
CONSTRUCT = "Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned"
LEGRES = ("Legendary Resistance ({n}/Day)", "If the creature fails a saving throw, it can choose to succeed instead.")


def legres(n):
    return (LEGRES[0].format(n=n), LEGRES[1])


SWARM = R(Resistances="Bludgeoning, Piercing, Slashing", Immunities="Charmed, Frightened, Grappled, Paralyzed, Petrified, Prone, Restrained, Stunned")
SWARM_TRAIT = ("Swarm", "The swarm can occupy another creature's space and vice versa, and it can move through any opening large enough for a Medium creature. The swarm can't regain Hit Points or gain Temporary Hit Points.")


MON = [
M("Tidepool Mimic", "S", "Monstrosity", "Unaligned", 1, "12 10 14 3 12 4", speed="10 ft., swim 20 ft.", senses="Tremorsense 30 ft.", skills="Stealth",
  traits=[("False Appearance", "While the mimic is motionless, it looks like a tide pool full of pretty shells."), ("Sticky", "A creature that touches the mimic has the Grappled condition (escape {dc:str}).")],
  attacks=[("Bite", "m", "2d6", "Piercing")],
  desc="A little rock pool with the brightest shells on the beach. Children are told never to put a hand in a pool that is warm."),
M("Skeleton Crew", "L", "Swarm of Medium Undead", "Chaotic Evil", 4, "14 14 14 6 8 8", speed="30 ft., swim 30 ft.", senses="Darkvision 60 ft.", lang="understands Common but can't speak", res=SWARM,
  traits=[SWARM_TRAIT, ("Heave Together", "The crew can pull a rope or row a boat as if it were twelve sailors.")],
  attacks=[("Rusty Cutlasses", "f", "4d6", "Slashing", "or {2d6} Slashing damage if the crew has half its Hit Points or fewer")], multi=2,
  desc="The dead crew of a ghost ship, still clattering at their stations. They come ashore at low tide for fresh hands."),
M("Dune-Shore Wurm", "H", "Monstrosity", "Unaligned", 6, "20 8 18 2 10 4", speed="30 ft., burrow 30 ft.", senses="Tremorsense 60 ft.",
  traits=[("Sand Burrower", "The wurm can burrow through sand and loose shingle without leaving a tunnel.")],
  attacks=[("Bite", "m", "3d8", "Piercing", "and if the target is Medium or smaller, it has the Grappled condition (escape {dc:str})", "10 ft")], multi=2,
  actions=[("Undertow Pull", "The wurm drags a creature Grappled by it 15 feet down into the sand. The creature has the Restrained condition and can't breathe until it escapes the grapple.")],
  desc="A pale worm that lives under the beaches of the north, where the dunes meet the tide. Beachcombers who dig too deep feel it move."),
M("Fogbank Elemental", "H", "Elemental", "Neutral", 9, "10 18 18 6 12 8", speed="0 ft., fly 50 ft. (hover)", senses="Blindsight 120 ft.", lang="Aquan, Auran",
  res=R(Resistances="Lightning; Bludgeoning, Piercing, Slashing", Immunities="Cold, Poison; Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious"),
  traits=[("Fog Body", "The elemental's space and a 30-foot Emanation around it are Heavily Obscured."), ("Lost in the Fog", "A creature that starts its turn in the elemental's fog makes a {dc:con} Wisdom saving throw or moves 10 feet in a random direction.")],
  attacks=[("Chilling Embrace", "f", "5d8", "Cold")], multi=2,
  actions=[("Drown in Mist (Recharge 5-6)", "Each creature in the fog makes a {dc:con} Constitution saving throw, taking {8d8} Cold damage and being unable to breathe until the end of its next turn on a failure, or half as much damage only on a success.")],
  desc="A fog bank that rolls in against the wind. Ships that sail into it come out with fewer sailors, or not at all."),
M("Undertow Horror", "H", "Aberration", "Chaotic Evil", 11, "22 14 20 12 14 10", speed="10 ft., swim 60 ft.", senses="Blindsight 60 ft., Darkvision 120 ft.", lang="telepathy 60 ft.",
  res=R(Resistances="Cold; Bludgeoning, Piercing, Slashing"), saves="Str, Con",
  traits=[legres(1), ("Amphibious", "The horror can breathe air and water."), ("Rip Current", "Water within 60 feet of the horror pulls toward it. A creature that starts its turn swimming there is pulled 15 feet toward the horror.")],
  attacks=[("Tentacle", "m", "3d10", "Bludgeoning", "and the target has the Grappled condition (escape {dc:str})", "20 ft")], multi=3,
  desc="The thing that lives at the bottom of a rip current, a mass of grey tentacles that pulls swimmers out to sea."),
M("Selkie Tide Queen", "M", "Fey", "Chaotic Neutral", 12, "14 18 16 16 18 22", speed="30 ft., swim 60 ft.", senses="Darkvision 120 ft.", lang="Common, Aquan, Sylvan", skills="Deception, Performance, Persuasion",
  res=R(Resistances="Cold"), saves="Dex, Wis, Cha",
  traits=[legres(2), ("Seal Skin", "As a Bonus Action, the queen takes the form of a great grey seal, or returns to her true form. In seal form her Speed is 10 feet and her Swim Speed is 90 feet.")],
  attacks=[("Pearl Blade", "f", "4d10", "Slashing", "plus {2d8} Cold damage")], multi=2,
  actions=[("Song of the Tide (Recharge 5-6)", "Each creature of the queen's choice within 60 feet of her that can hear her makes a {dc:cha} Wisdom saving throw. On a failure, it takes {8d10} Psychic damage and has the Charmed condition until the end of its next turn. On a success, it takes half as much damage only.")],
  desc="The queen of the seal people, who comes ashore once a year to dance. Whoever steals her skin may keep her for seven years. No one ever tried twice."),
M("Kraken Priest", "L", "Monstrosity", "Chaotic Evil", 14, "20 14 20 16 20 18", speed="30 ft., swim 50 ft.", senses="Darkvision 120 ft.", lang="Common, Aquan",
  res=R(Resistances="Cold, Lightning"), saves="Con, Wis, Cha",
  traits=[legres(2), ("Amphibious", "The priest can breathe air and water.")],
  attacks=[("Tentacle Beard", "m", "4d10", "Bludgeoning", "plus {2d8} Psychic damage", "10 ft")], multi=2,
  actions=[("Call of the Deep (Recharge 5-6)", "A wave of black water rolls from the priest in a 60-foot Cone. Each creature in it makes a {dc:wis} Strength saving throw. On a failure, it takes {9d10} Bludgeoning damage and is pulled 20 feet toward the priest. On a success, it takes half as much damage only.")],
  desc="A man who went down to pray to the thing under the sea and came back with tentacles where his beard was. His cult lights false beacons on the cliffs."),
M("Moon-Tide Behemoth", "G", "Monstrosity", "Unaligned", 15, "28 8 26 3 12 6", ac=19, speed="30 ft., swim 50 ft.", senses="Darkvision 60 ft.",
  res=R(Resistances="Cold"), saves="Str, Con",
  traits=[legres(2), ("Moon-Pulled", "During a full moon, the behemoth has Advantage on attack rolls and saving throws."), ("Siege Monster", "The behemoth deals double damage to objects and structures.")],
  attacks=[("Slam", "m", "5d12", "Bludgeoning", "", "15 ft")], multi=2,
  actions=[("Spring Tide (Recharge 5-6)", "The behemoth rears up and crashes down. Each creature within 40 feet of it makes a {dc:str} Dexterity saving throw. On a failure, it takes {10d10} Bludgeoning damage and has the Prone condition. On a success, it takes half as much damage only.")],
  desc="A beast like a whale with legs that climbs out of the sea only on the highest tides of the year, to lay its eggs in the harbor towns."),
M("The Last Lighthouse", "G", "Construct", "Lawful Good", 17, "26 4 26 14 20 16", ac=20, speed="20 ft.", senses="Truesight 300 ft.", lang="understands Common but can't speak",
  res=R(Resistances="Bludgeoning, Piercing, Slashing", Immunities="Fire, Poison, Psychic, Radiant; " + CONSTRUCT), saves="Con, Wis",
  traits=[legres(3), ("Beacon", "The lighthouse sheds Bright Light in a 300-foot radius. Creatures in the light can't benefit from the Invisible condition."), ("Siege Monster", "The lighthouse deals double damage to objects and structures.")],
  attacks=[("Stone Fist", "m", "4d12", "Bludgeoning", "", "20 ft"), ("Lamp Beam", "s:wis", "8d10", "Radiant", "", "300 ft")], multi=2,
  actions=[("Burning Light (Recharge 5-6)", "The lighthouse turns its lamp on a 120-foot Line that is 20 feet wide. Each creature in it makes a {dc:wis} Constitution saving throw. On a failure, it takes {12d10} Radiant damage and has the Blinded condition until the end of its next turn. On a success, it takes half as much damage only.")],
  leg=[("Sweep", "The lighthouse makes one Lamp Beam attack."), ("Step", "The lighthouse moves up to its Speed.")],
  desc="The lighthouse of a drowned city, which kept its light burning for five hundred years until it learned to walk and hunt the wreckers itself."),
M("Hurricane Lord", "G", "Elemental", "Chaotic Neutral", 19, "24 20 24 12 16 18", ac=20, speed="0 ft., fly 120 ft. (hover)", senses="Darkvision 120 ft.", lang="Auran, Aquan",
  res=R(Resistances="Cold; Bludgeoning, Piercing, Slashing", Immunities="Lightning, Poison, Thunder; Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious"), saves="Dex, Con, Wis",
  traits=[legres(3), ("Eye of the Storm", "The lord's space is calm. A 120-foot Emanation around it is a hurricane: Difficult Terrain, Heavily Obscured, and ranged attacks in it have Disadvantage.")],
  attacks=[("Gale Fist", "f", "4d10", "Bludgeoning", "plus {3d8} Lightning damage, and the target is pushed 20 feet away", "20 ft")], multi=3,
  actions=[("Storm Surge (Recharge 5-6)", "Lightning and wind strike each creature of the lord's choice within 120 feet. Each makes a {dc:con} Dexterity saving throw, taking {10d10} Lightning damage on a failed save or half as much on a successful one.")],
  leg=[("Gust", "The lord moves up to half its Fly Speed."), ("Gale Fist", "The lord makes one Gale Fist attack.")],
  desc="The spirit of the great autumn storm, which walks the coast once in a generation and takes the harbor walls with it."),
]

# The shared traits say "The creature". Put the name of each monster in its place.
for _m in MON:
    _m.traits = [(n, t.replace("If the creature", "If the " + _m.ref())) for n, t in _m.traits]
