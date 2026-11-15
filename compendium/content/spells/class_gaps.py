# Original spells that fill thin class and level lists.
# Format: (name, level, school, classes, time, range, components, duration, concentration, ritual, desc, higher)
B, C, D, P, R, S, K, W = "Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Warlock", "Wizard"
SPELLS = [
# ---------- level 3
("Banner of the Unbroken", 3, "Evocation", [P, C], "Bonus Action", "Self (30-foot Emanation)", "V, S, M (a strip of cloth from a banner)", "1 minute", True, False,
 "A ghostly banner rises above you and snaps in a wind no one else feels. For the duration, whenever you or an ally in the Emanation hits a creature with a weapon attack, the attacker gains 1d6 Temporary Hit Points. You and your allies in the Emanation also have Advantage on saving throws to avoid or end the Frightened condition.",
 "The Temporary Hit Points increase by 1d6 for every two slot levels above 3."),
# ---------- level 4
("Fettering Smite", 4, "Evocation", [P], "Bonus Action, which you take immediately after hitting a target with a Melee weapon or an Unarmed Strike", "Self", "V", "1 minute", True, False,
 "Chains of light burst from the wound. The target takes an extra 4d6 Radiant damage from the attack and makes a Strength saving throw. On a failed save, it has the Restrained condition and can't teleport for the duration. It repeats the save at the end of each of its turns, ending the spell on a success.",
 "The damage increases by 1d6 per slot level above 4."),
("Hunter's Tether", 4, "Transmutation", [R, P], "Action", "90 feet", "V, S", "1 minute", True, False,
 "A spectral chain links you to a creature you can see. The target makes a Charisma saving throw. On a failed save, for the duration its Speed is halved, it can't teleport or leave its plane, it can't willingly move to a space more than 30 feet away from you, and your weapon attacks against it deal an extra 1d8 Force damage. It repeats the save at the end of each of its turns, ending the spell on a success.",
 "You can target one additional creature for every two slot levels above 4. Each target has its own chain."),
("Bursting Briar Shot", 4, "Conjuration", [R, D], "Bonus Action", "Self", "V", "1 minute", False, False,
 "The next time you hit a creature with a Ranged weapon attack before the spell ends, the ammunition bursts into a tangle of barbed vines. The target takes an extra 4d8 Piercing damage, and each other creature within 10 feet of it makes a Dexterity saving throw, taking 4d6 Piercing damage on a failed save or half as much on a successful one. The ground within 10 feet of the target becomes Difficult Terrain until the spell ends.",
 "The damage of both effects increases by 1d6 per slot level above 4."),
("Soul Siphon", 4, "Necromancy", [K, S, W], "Action", "60 feet", "V, S", "Instantaneous", False, False,
 "You hook a thread of life out of a creature you can see and pull. The target makes a Constitution saving throw, taking 6d8 Necrotic damage on a failed save or half as much on a successful one. You gain Temporary Hit Points equal to half the damage dealt. Undead and Constructs are unaffected.",
 "The damage increases by 1d8 per slot level above 4."),
# ---------- level 5
("Warden's Last Stand", 5, "Abjuration", [P, R], "Bonus Action", "Self", "V, S", "1 minute", True, False,
 "You plant your feet and refuse to fall back. For the duration, you have Resistance to Bludgeoning, Piercing, and Slashing damage, and you can't be moved against your will. When a creature within 10 feet of you makes an attack roll against a target other than you, you can take a Reaction to impose Disadvantage on the roll and then make one weapon attack against that creature.",
 None),
("Mantle of the Apex Beast", 5, "Transmutation", [R, D], "Bonus Action", "Self", "V, S, M (a tooth or claw from a predator)", "1 minute", True, False,
 "You take on the aspect of the greatest hunter of the land around you. For the duration, you gain a Climb Speed equal to your Speed, you have Advantage on Wisdom (Perception) checks that rely on smell or hearing, and your weapon attacks deal an extra 2d6 damage of the weapon's type. Once on each of your turns when you hit a creature with a weapon attack, you can force it to make a Strength saving throw. On a failed save, it has the Prone condition.",
 None),
# ---------- level 6
("Procession of Nightmares", 6, "Illusion", [B, K, W], "Action", "120 feet", "V, S", "1 minute", True, False,
 "A silent parade of every horror the targets have ever imagined marches through a 30-foot-radius Sphere centered on a point you choose. Each creature of your choice in the Sphere makes a Wisdom saving throw. On a failed save, a creature takes 8d6 Psychic damage and has the Frightened condition for the duration. On a successful save, it takes half as much damage only. A Frightened creature repeats the save at the end of each of its turns, ending the effect on itself on a success.",
 "The damage increases by 1d6 per slot level above 6."),
# ---------- level 7
("Final Rite", 7, "Necromancy", [C, K], "Action", "60 feet", "V, S, M (a pinch of grave dirt)", "Instantaneous", False, False,
 "You speak the last words over a creature you can see, whether it is ready or not. The target makes a Constitution saving throw, taking 10d10 Necrotic damage on a failed save or half as much on a successful one. Undead have Disadvantage on the save. If this damage reduces the target to 0 Hit Points, it dies and its soul passes beyond reach: it can't be returned to life except by True Resurrection or Wish, and it can never rise as an Undead.",
 None),
# ---------- level 8
("Gravity Collapse", 8, "Transmutation", [S, K, W], "Action", "120 feet", "V, S, M (a lodestone)", "Instantaneous", False, False,
 "Weight floods into a single point. Each creature in a 30-foot-radius Sphere centered on a point you choose makes a Strength saving throw. On a failed save, a creature takes 10d6 Force damage, is pulled straight toward the center of the Sphere to the nearest unoccupied space, has the Prone condition, and has the Restrained condition until the end of its next turn. On a successful save, it takes half as much damage only. Unsecured objects in the area are pulled to the center.",
 None),
("Toll of the Final Bell", 8, "Evocation", [C, B], "Action", "Self (60-foot Emanation)", "V, S, M (a small bronze bell)", "Instantaneous", False, False,
 "A great unseen bell tolls once, and the sound shakes every bone in range. Each creature of your choice in the Emanation makes a Constitution saving throw, taking 10d6 Thunder damage and having the Deafened and Incapacitated conditions until the end of its next turn on a failed save, or taking half as much damage only on a successful one. Undead and Fiends have Disadvantage on the save. Nonmagical glass and crystal in the area that isn't worn or carried shatters.",
 None),
# ---------- level 9
("Saga of the Undying", 9, "Enchantment", [B, C, D], "Action", "60 feet", "V, S", "10 minutes", True, False,
 "You sing the opening verse of a legend and name up to six creatures you can see as its heroes. For the duration, each of them gains 40 Temporary Hit Points when you cast the spell, has Advantage on saving throws, and has Immunity to the Charmed and Frightened conditions. The first time each hero would drop to 0 Hit Points before the spell ends, it drops to 1 Hit Point instead.",
 None),
]
