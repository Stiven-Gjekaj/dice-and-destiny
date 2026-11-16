# Original spells for the last gaps in the class lists.
# Format: (name, level, school, classes, time, range, components, duration, concentration, ritual, desc, higher)
B, C, D, P, R, S, K, W = "Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Warlock", "Wizard"
SPELLS = [
# ---------- cantrips (Paladins and Rangers can learn these through a Fighting Style that grants cantrips)
("Warden's Call", 0, "Enchantment", [P, R, C, D], "Action", "30 feet", "V", "1 round", False, False,
 "You call out a challenge to a creature you can see within range. It makes a Wisdom saving throw. On a failed save, it has Disadvantage on attack rolls against creatures other than you until the end of its next turn.",
 None),
("Snapping Vine", 0, "Conjuration", [R, D, W], "Action", "60 feet", "V, S", "Instantaneous", False, False,
 "A thorny vine lashes up from the ground under a creature you can see. Make a ranged spell attack. On a hit, it takes 1d8 Piercing damage, and its Speed is reduced by 10 feet until the start of your next turn.",
 "The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8)."),
# ---------- level 6
("Shadow Road", 6, "Conjuration", [K, W], "1 minute", "Self", "V, S", "Instantaneous", False, False,
 "You and up to eight willing creatures within 10 feet of you step into a shadow and out of another one. You arrive at a shadow within 500 miles that you have seen before, or from which you hold an object, in an unoccupied space in Dim Light or Darkness that is as close to it as possible. The spell fails if you start in Bright Light. Unlike Teleportation Circle or Teleport, there is no mishap, but you can only arrive where there is shadow.",
 None),
# ---------- level 7
("Heroic Anthem", 7, "Enchantment", [B], "Action", "60 feet", "V, S", "1 minute", True, False,
 "You sing a song of heroes. Up to six creatures of your choice within range that can hear you each gain the following benefits for the duration: they have Immunity to the Frightened condition, and they can add 1d6 to their attack rolls and saving throws.",
 None),
("Living Forest", 7, "Conjuration", [D], "Action", "Self (60-foot Emanation)", "V, S, M (an acorn)", "1 minute", True, False,
 "Trees burst from the ground around you and move at your will. For the duration, the Emanation is Difficult Terrain for your enemies, and you and your allies there have Half Cover. Each enemy that starts its turn in the Emanation makes a Strength saving throw. On a failed save, it has the Restrained condition until the start of its next turn.",
 None),
# ---------- level 8
("Masterwork Illusion", 8, "Illusion", [B, W], "10 minutes", "120 feet", "V, S, M (paints and jade dust worth 1,000 GP)", "Until dispelled", False, False,
 "You create an illusion of a place, an object, or a crowd of creatures that fills up to a 120-foot Cube within range. It has sound, smell, temperature, and texture, and it holds up to touch. Illusory creatures act as you planned when you cast the spell, but they can't harm anyone. A creature that studies the illusion and suspects it can take a Study action to make an Intelligence (Investigation) check against your spell save DC to see through it.",
 None),
]
