"""The new creatures of chapter 1 of Beyond the Western Sea, "The Wreck of the Good Intent".

The sea lice live in the sand of Farholm and on the back of the Grandam, as lice live on a whale.
The giant conger lives in the flooded hold of the wreck.
The chapter is for level 1. Keep the armor class at 16 or less and each save DC at 15 or less.
"""
from monster_engine import M

R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())

AMPHIBIOUS = ("Amphibious", "The creature can breathe air and water.")
SWARM = R(Resistances="Bludgeoning, Piercing, Slashing",
          Immunities="Charmed, Frightened, Grappled, Paralyzed, Petrified, Prone, Restrained, Stunned")
SWARM_TRAIT = ("Swarm", "The swarm can occupy another creature's space and vice versa, and it can move through any "
               "opening large enough for a Tiny creature. The swarm can't regain Hit Points or gain Temporary Hit Points.")
HEAT = ("Drawn to Heat", "The {name} knows where each fire within 120 feet of it is, also through sand and turf. "
        "It moves toward the nearest fire, and it attacks the creatures near that fire first.")

MON = [
M("Giant Sea Louse", "S", "Beast", "Unaligned", 0.25, "12 13 13 1 10 3", ac=14, speed="30 ft., burrow 10 ft., swim 30 ft.",
  senses="Tremorsense 30 ft.",
  traits=[AMPHIBIOUS,
          (HEAT[0], HEAT[1].format(name="louse")),
          ("Under the Sand", "While the louse is buried in sand and doesn't move, it looks like a flat grey stone. "
           "A creature notices it only with a successful DC 13 Wisdom (Perception) check.")],
  attacks=[("Hooked Legs", "m", "1d6", "Piercing",
            "and the target has the Grappled condition (escape {dc:str}) if it is Medium or smaller. "
            "The louse can grapple only one creature at a time")],
  desc="A flat grey thing as long as a dog, with a shell like a roof of slates and too many hooked legs. "
       "It lives in the sand of Farholm and nowhere else in the world. The colonists call it a scrab, and they say that it comes out after every storm. "
       "A whaler from the land would know its shape at once: the lice that live on the back of a whale look just like it, only smaller."),
M("Swarm of Sea Lice", "M", "Swarm of Tiny Beasts", "Unaligned", 0.5, "6 13 12 1 10 2", ac=12, speed="20 ft., burrow 5 ft., swim 20 ft.",
  senses="Tremorsense 30 ft.", res=SWARM,
  traits=[AMPHIBIOUS, SWARM_TRAIT, (HEAT[0], HEAT[1].format(name="swarm"))],
  attacks=[("Bites", "f", "2d4", "Piercing", "or {1d4} Piercing damage if the swarm has half its Hit Points or fewer")],
  bonus=[("Into the Sand", "The swarm burrows into sand or loose turf in its space. Until it moves, attack rolls against it have Disadvantage.")],
  desc="A thousand grey lice, each as big as a thumb, that boil up out of warm sand. A fire on the bare ground of Farholm brings them in minutes."),
M("Giant Conger", "L", "Beast", "Unaligned", 1, "16 14 14 1 10 3", ac=13, speed="5 ft., swim 40 ft.", senses="Darkvision 60 ft.",
  skills="Stealth",
  traits=[("Water Breathing", "The conger can breathe only underwater. Out of the water, it can live for 1 hour."),
          ("Hole Dweller", "While the conger is in a hole, a gap in a hull, or another narrow space, it has Half Cover.")],
  attacks=[("Bite", "m", "2d6", "Piercing",
            "and the target has the Grappled condition (escape {dc:str}) if it is Medium or smaller. "
            "While the target is grappled, the conger can't bite another creature")],
  bonus=[("Drag Down", "The conger moves up to 10 feet in the water with the creature that it grapples. "
          "If the creature is a Medium or smaller creature that can't breathe water, it must hold its breath.")],
  desc="A grey-black eel as long as a ship's boat and as thick as a man's leg, with a mouth that opens farther than seems right. "
       "It lives in the dark of a wreck, and it does not like visitors."),
]
