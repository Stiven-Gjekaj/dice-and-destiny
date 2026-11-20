"""The new creatures of the last chapter of Beyond the Western Sea, "Storm Season".

The great lamprey lives on the flank of the Grandam, as a lamprey lives on a whale.
It rises with her in the storm season and meets the boats in the lane.
The flukes live in the warm passages under the Grandam's Well.
They find their prey by light, noise, and movement. A creature that stays still in the dark is safe from them.
The chapter is for level 5. Keep the armor class at 16 or less and each save DC at 15 or less.
"""
from monster_engine import M

R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())

SWARM = R(Resistances="Bludgeoning, Piercing, Slashing",
          Immunities="Charmed, Frightened, Grappled, Paralyzed, Petrified, Prone, Restrained, Stunned")

MON = [
M("Great Lamprey", "L", "Beast", "Unaligned", 4, "17 12 16 1 10 3", ac=13, speed="5 ft., swim 40 ft.",
  senses="Blindsight 30 ft., Darkvision 60 ft.",
  traits=[("Water Breathing", "The lamprey can breathe only underwater."),
          ("Drawn to Light", "The lamprey knows where each light on or near the water within 1 mile of it is. "
           "It swims toward the brightest one, and it attacks the creatures nearest that light first.")],
  attacks=[("Round Mouth", "m", "2d10", "Piercing",
            "and the lamprey attaches to the target, which has the Grappled condition (escape {dc:str}). "
            "While it is attached, the lamprey can't use Round Mouth against another creature, and the target takes "
            "{2d6} Necrotic damage at the start of each of the lamprey's turns"),
           ("Tail", "m", "1d8", "Bludgeoning", "", "10 ft")],
  multi=2,
  bonus=[("Rock the Boat", "The lamprey strikes the hull of a boat within 5 feet of it. Each creature standing on that boat "
          "makes a {dc:str} Dexterity saving throw. On a failed save, a creature has the Prone condition, and a creature "
          "at the rail falls into the water.")],
  desc="A grey eel-thing as long as a ship's boat, with no jaw, only a round mouth ringed with hooked teeth. "
       "In the deep, it clings to the side of something very large and drinks from it. When that thing rises, the lamprey "
       "lets go and comes up to look at the lights."),
M("Swarm of Flukes", "M", "Swarm of Tiny Beasts", "Unaligned", 2, "6 14 14 1 8 1", ac=12,
  speed="10 ft., climb 10 ft., swim 30 ft.", senses="Blindsight 60 ft. (blind beyond this radius)", res=SWARM,
  traits=[("Swarm", "The swarm can occupy another creature's space and vice versa, and it can move through any opening "
           "large enough for a Tiny creature. The swarm can't regain Hit Points or gain Temporary Hit Points."),
          ("Light, Noise, and Movement", "The swarm notices a creature only if the creature carries a light, made a sound "
           "louder than a whisper since the end of the swarm's last turn, or moved more than 5 feet since then. "
           "It ignores each other creature, and it moves away from a creature that it ignores."),
          ("Warm Water", "The swarm can breathe air and water. It takes {1d6} Cold damage at the end of each of its turns "
           "in cold air or cold water.")],
  attacks=[("Bites", "f", "4d4", "Piercing", "or {2d4} Piercing damage if the swarm has half its Hit Points or fewer")],
  desc="A slick mass of pale flat worms, each as long as a finger, that pours over the warm walls deep under the island like "
       "spilled milk. Each worm is blind. Together, they feel each footstep and each lantern in the dark."),
]
