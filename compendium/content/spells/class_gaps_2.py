# Original spells that fill thin class and level lists (second batch).
# Format: (name, level, school, classes, time, range, components, duration, concentration, ritual, desc, higher)
B, C, D, P, R, S, K, W = "Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Warlock", "Wizard"
SPELLS = [
# ---------- level 2
("Anthem of Iron", 2, "Enchantment", [B, P], "Bonus Action", "30 feet", "V", "Instantaneous", False, False,
 "You sing a short, hard verse. Up to three creatures of your choice that can hear you within range each gain Temporary Hit Points equal to 1d8 plus your spellcasting ability modifier, and each has Advantage on the next saving throw it makes before the end of your next turn.",
 "You can target one additional creature for each slot level above 2."),
("Interposing Step", 2, "Conjuration", [P, C], "Reaction, which you take when a creature you can see within 30 feet of you is hit by an attack roll", "Self", "V", "Instantaneous", False, False,
 "You teleport to an unoccupied space within 5 feet of the triggering creature, and the attack hits you instead. You take the damage and any other effects of the hit, and the creature takes none. You have Resistance to the damage of that attack.",
 None),
# ---------- level 3
("Shattering Chord", 3, "Evocation", [B, S, W], "Action", "Self (30-foot Cone)", "V, S", "Instantaneous", False, False,
 "You strike a chord that no instrument should be able to play. Each creature in the Cone makes a Constitution saving throw, taking 5d8 Thunder damage and having the Deafened condition until the end of its next turn on a failed save, or taking half as much damage only on a successful one. Nonmagical glass and crystal objects in the Cone that aren't worn or carried shatter.",
 "The damage increases by 1d8 for each slot level above 3."),
# ---------- level 4
("Masquerade", 4, "Illusion", [B, K, W], "Action", "30 feet", "V, S, M (a feathered mask)", "1 hour", False, False,
 "You and up to three willing creatures you can see within range take on new illusory faces, voices, and clothing of your choice. Each creature can be made to look up to 1 foot taller or shorter and seem thinner or heavier, but it keeps its basic body shape. The illusion holds up to touch. A creature that takes a Study action to examine a disguised creature can make an Intelligence (Investigation) check against your spell save DC to see through the disguise.",
 "The duration becomes 8 hours with a level 5 or higher slot."),
("Wolfpack Hunt", 4, "Transmutation", [R, D], "Action", "Self (30-foot Emanation)", "V, S, M (a wolf's tooth)", "1 minute", True, False,
 "Choose up to five creatures in the Emanation, which can include you. For the duration, each of them has its Speed increased by 10 feet, and each has Advantage on attack rolls against a creature if another chosen creature is within 5 feet of that creature and doesn't have the Incapacitated condition.",
 None),
# ---------- level 5
("Grand Finale", 5, "Evocation", [B, S], "Action", "60 feet", "V, S", "Instantaneous", False, False,
 "Light, sound, and color burst in a 20-foot-radius Sphere centered on a point you choose within range. Each creature of your choice in the Sphere makes a Dexterity saving throw, taking 7d8 Radiant damage and having the Blinded condition until the end of its next turn on a failed save, or taking half as much damage only on a successful one. Each other creature of your choice in the Sphere gains 2d8 Temporary Hit Points.",
 "The damage and the Temporary Hit Points increase by 1d8 for each slot level above 5."),
# ---------- level 6
("Stampede of Spirits", 6, "Conjuration", [D], "Action", "Self (100-foot Line)", "V, S, M (a tuft of fur from a herd animal)", "Instantaneous", False, False,
 "A herd of spectral beasts thunders out from you in a Line 100 feet long and 20 feet wide. Each creature in the Line makes a Dexterity saving throw. On a failed save, it takes 8d10 Bludgeoning damage and has the Prone condition. On a successful save, it takes half as much damage only.",
 "The damage increases by 1d10 for each slot level above 6."),
("Prism Lance", 6, "Evocation", [S, W], "Action", "Self (120-foot Line)", "V, S, M (a prism)", "Instantaneous", False, False,
 "A beam of split light lances out from you in a Line 120 feet long and 5 feet wide. Choose Acid, Cold, Fire, Lightning, or Thunder for each creature in the Line. Each creature in the Line makes a Dexterity saving throw, taking 10d8 damage of the chosen type on a failed save or half as much damage on a successful one.",
 "The damage increases by 1d8 for each slot level above 6."),
# ---------- level 7
("Swallowing Earth", 7, "Transmutation", [D, C, S], "Action", "90 feet", "V, S", "Instantaneous", False, False,
 "The ground opens like a mouth under a creature you can see that is standing on earth or stone. The target makes a Dexterity saving throw. On a failed save, it takes 10d10 Bludgeoning damage and is buried: it has the Restrained condition and can't breathe until it escapes. A buried creature, or a creature within 5 feet of it, can take an action to make a Strength (Athletics) check against your spell save DC, freeing the creature on a success. On a successful save, the target takes half as much damage only.",
 None),
# ---------- level 8
("Storm of Glass", 8, "Evocation", [S, D, W], "Action", "150 feet", "V, S, M (a handful of sand)", "1 minute", True, False,
 "A howling wind full of glass shards fills a 40-foot-radius, 40-foot-high Cylinder centered on a point you choose within range. The area is Heavily Obscured. A creature takes 8d6 Slashing damage when it enters the Cylinder for the first time on a turn or starts its turn there. It makes a Constitution saving throw, taking half as much damage on a successful one.",
 None),
# ---------- level 9
("Absolute Zero", 9, "Evocation", [S, K, W], "Action", "150 feet", "V, S", "Instantaneous", False, False,
 "All heat leaves a 40-foot-radius Sphere centered on a point you choose within range. Each creature in the Sphere makes a Constitution saving throw. On a failed save, a creature takes 20d6 Cold damage, its Speed becomes 0, and it has the Incapacitated condition until the end of its next turn. On a successful save, it takes half as much damage only. A creature that this damage reduces to 0 Hit Points freezes solid and dies. Water in the area freezes to a depth of 10 feet.",
 None),
]
