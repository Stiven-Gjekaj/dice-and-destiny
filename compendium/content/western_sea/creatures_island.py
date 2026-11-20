"""The new creatures of the island in Beyond the Western Sea (chapter 2).

The format is the same as in content/monsters. The engine in
build/monster_engine.py calculates AC, Hit Points, attack bonuses, and save DCs.
Keep the armor class at 16 or less and each save DC at 15 or less.

The Rib Louse and the Louse Mother live on the back of the Grandam. They are a clue:
they are the lice of a living thing, not crabs of the shore.
"""
from monster_engine import M

R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())

NO_LIGHT = ("No Light at Night", "The Well Watch carries no fire after dark. The watchman has Advantage on Wisdom (Perception) checks "
            "and Dexterity (Stealth) checks in Dim Light.")

MON = [
M("Bonxie", "S", "Beast", "Unaligned", 0.25, "8 15 12 3 12 6", ac=13, speed="10 ft., fly 60 ft.", skills="Perception",
  traits=[("Flyby", "The bonxie doesn't provoke an Opportunity Attack when it flies out of an enemy's reach."),
          ("Dive", "If the bonxie flies at least 20 feet straight toward a target and then hits it with a Beak attack in the same turn, "
           "the target takes an extra {1d4} Piercing damage.")],
  attacks=[("Beak", "f", "1d6", "Piercing")],
  desc="A big brown sea bird with a hooked beak and a temper. It robs the gulls of their fish, and it dives at the head of any climber "
       "who comes near its nest. The Tey egg climbers wear a hat with a stick on top, so that the bonxie hits the stick."),
M("Rib Louse", "M", "Monstrosity", "Unaligned", 0.5, "14 12 14 1 10 3", ac=14, speed="30 ft., climb 30 ft.",
  senses="Blindsight 30 ft.", skills="Stealth",
  traits=[("Bog Lurker", "The louse has Advantage on Dexterity (Stealth) checks while it is in fog or in bog water."),
          ("Spider Climb", "The louse can climb difficult surfaces, including along ceilings, without an ability check.")],
  attacks=[("Mandibles", "m", "1d8", "Piercing",
            "If the target is a Medium or smaller creature, it has the Grappled condition (escape {dc:str}). The louse can grapple only one creature at a time")],
  desc="A pale, flat thing as big as a sheep, with a shell like old horn and too many legs. It lives in the black bogs between the Ribs "
       "and eats the dead grey crust of the stone. Its shell has no barnacle and no weed on it. It is not a creature of the sea."),
M("Louse Mother", "L", "Monstrosity", "Unaligned", 3, "17 8 16 2 11 5", ac=15, speed="20 ft., climb 20 ft.",
  senses="Blindsight 60 ft.", res=R(Resistances="Piercing"),
  traits=[("Spider Climb", "The louse mother can climb difficult surfaces, including along ceilings, without an ability check."),
          ("Brood", "When a Rib Louse within 30 feet of the louse mother drops to 0 Hit Points, the louse mother has Advantage "
           "on its next attack roll before the end of its next turn.")],
  attacks=[("Mandibles", "m", "1d10", "Piercing"),
           ("Leg", "m", "1d8", "Bludgeoning", "If the target is a Large or smaller creature, it has the Prone condition", "10 ft")],
  multi=2,
  actions=[("Brood Call (1/Day)", "The louse mother clicks and scrapes. Two Rib Lice crawl out of the cracks of the stone or the timbers "
            "in unoccupied spaces within 30 feet of her. They act right after her in the order of turns.")],
  desc="A louse as big as a cart, white and slow, with a shell scarred by three hundred years of growth. She has made her nest "
       "in the dark of a place that nobody visits, and her young live all round her."),
M("Scalding Eel", "M", "Beast", "Unaligned", 1, "13 15 12 2 10 4", ac=13, speed="5 ft., swim 40 ft.",
  senses="Blindsight 30 ft.", res=R(Immunities="Fire"),
  traits=[("Hot Water", "The eel can breathe only in hot water. It can stay out of the water for 1 minute."),
          ("Steam Cloud", "While the eel is in a pool, the steam gives it Half Cover against attacks from creatures that are not in the pool.")],
  attacks=[("Bite", "f", "1d8", "Piercing", "plus {1d6} Fire damage")],
  actions=[("Scald (Recharge 5–6)", "The eel spits boiling water in a 15-foot Cone. Each creature in the Cone makes a {dc:con} Dexterity "
            "saving throw. On a failed save, a creature takes {2d6} Fire damage. On a successful save, it takes half as much damage.")],
  desc="A thick yellow eel as long as a man, that lives in the hottest pools of the Kettles and nowhere else on the island. "
       "Its skin is too hot to touch. The colonists cook their eggs in its pools, with a long spoon and a quick hand."),
M("Well Watchman", "M", "Humanoid", "Lawful Neutral", 0.5, "13 14 12 10 13 10", ac=13, skills="Perception, Stealth, Survival", lang="Common",
  traits=[NO_LIGHT],
  attacks=[("Seal Spear", "m", "1d8", "Piercing"), ("Harpoon", "t", "1d6", "Piercing", "", "20/60 ft")],
  bonus=[("Smother", "The watchman puts out one nonmagical flame within 5 feet of it with its cloak or its hand.")],
  desc="A man or woman of the Tey bank in sealskin, with a spear, a harpoon on a line, and no lantern. The Well Watch keeps outsiders "
       "away from the Grandam's Well and keeps an eye on the Corrin Light. Its members do not want to hurt anybody. They will."),
M("The Ghost of John Pascoe", "M", "Undead", "Neutral", 2, "8 14 12 12 14 15", ac=12, speed="0 ft., fly 30 ft. (hover)",
  senses="Darkvision 60 ft.", lang="Common",
  res=R(Resistances="Bludgeoning, Piercing, Slashing",
        Immunities="Cold, Necrotic, Poison; Charmed, Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained"),
  traits=[("Incorporeal Movement", "The ghost can move through other creatures and objects as if they were Difficult Terrain. "
           "It takes {1d10} Force damage if it ends its turn inside an object."),
          ("Master of the Hopewell", "Each Drowned Sailor within 30 feet of the ghost that can see it has Advantage on attack rolls."),
          ("Bound to the Wreck", "The ghost can't move more than 300 feet from the name board of the Hopewell. If the board is carried "
           "out of the Boneyard, the ghost follows it. If the ghost drops to 0 Hit Points, it comes back at the next high tide, "
           "unless the board lies on Founders' Hill.")],
  attacks=[("Drowning Hand", "f", "2d8", "Cold", "and the target can't breathe until the start of the ghost's next turn")],
  actions=[("The Last Wave (Recharge 5–6)", "Cold sea water pours out of the ghost. Each creature in a 15-foot Emanation from it makes a "
            "{dc:cha} Constitution saving throw. On a failed save, a creature takes {3d6} Cold damage and has the Prone condition. "
            "On a successful save, it takes half as much damage only.")],
  desc="A young man in a blue coat, wet to the skin, with weed in his hair and a lantern that gives no light. He was the master of the "
       "Hopewell. He still sails her, each night, out through the gap in the Wall that closed a hundred and fifty years ago."),
]
