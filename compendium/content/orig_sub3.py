# Original subclasses — part 3: Rogue, Sorcerer, Warlock, Wizard
SUBS = {}

SUBS["rogue"] = [
("Grifter", "Con artists who win fights before the first blade is drawn.", [
 (3, "Silver Tongue", "You gain Expertise in Deception and Persuasion. If you succeeded on a Charisma (Deception) check against a creature within the last minute, you can apply Sneak Attack to it on your first hit each turn even without Advantage."),
 (3, "Read the Mark", "As a Bonus Action, make a Wisdom (Insight) check contested by a creature's Charisma (Deception). On a success you learn its highest and lowest saving throw modifiers and your next attack against it this turn has Advantage."),
 (9, "The Long Con", "You can spend 1 hour establishing a false identity in a community. Until you abandon it, creatures there treat you as that person, and magic that reads thoughts or detects lies reveals only what fits the identity."),
 (13, "Patsy", "When a creature you can see attacks you, you can take a Reaction to choose another creature within 5 feet of you; the attack targets that creature instead if its AC is equal to or lower than yours. Once per Short Rest."),
 (17, "The Big Score", "Once per Long Rest, when you hit a creature you deceived within the last minute, the hit is a Critical Hit and the target has the Stunned condition until the end of your next turn."),
]),
("Venomblade", "Rogues who distill death into a few precious drops.", [
 (3, "Toxin Crafting", "You gain proficiency with the Poisoner's Kit. During a Long Rest you can brew doses of venom equal to your Proficiency Bonus. Applying one to a weapon or three pieces of ammunition is a Bonus Action; it lasts 1 minute."),
 (3, "Envenom", "When you hit with a coated weapon, the target takes extra Poison damage equal to your Rogue level and makes a Constitution save (8 + Dexterity modifier + Proficiency Bonus) or has the Poisoned condition for 1 minute (save ends at end of each of its turns)."),
 (9, "Inured Blood", "You have Resistance to Poison damage and Immunity to the Poisoned condition."),
 (13, "Lingering Toxin", "Your Envenom ignores Resistance to Poison damage, and Immunity to Poison damage becomes Resistance against it."),
 (17, "Death Bloom", "When a creature Poisoned by your Envenom drops to 0 Hit Points, it releases a 10-foot cloud: each creature of your choice there makes a Constitution save or takes 6d6 Poison damage and is Poisoned."),
]),
("Rooftop Runner", "Acrobats who fight on walls, ledges and chimneys.", [
 (3, "Freerunning", "You gain a Climb Speed equal to your Speed, your long and high jump distances double, and you reduce falling damage you take by five times your Rogue level."),
 (3, "Dazzling Vault", "You can move through the space of any creature larger than Tiny. The first time each turn you do so, your next attack against that creature this turn has Advantage."),
 (9, "Ricochet", "When you hit with a thrown weapon, you can bounce it to a second creature within 15 feet of the first and make an attack against it with the same weapon (no Sneak Attack unless the first missed)."),
 (13, "Untouchable Momentum", "If you've moved at least 20 feet this turn, Opportunity Attacks against you have Disadvantage and you have Advantage on Dexterity saving throws until the start of your next turn."),
 (17, "Final Flourish", "Once per turn when you hit after moving at least 30 feet, roll your Sneak Attack dice twice and use either total."),
]),
]

SUBS["sorcerer"] = [
("Starborn Sorcery", "Your power fell from the sky — the light of a dying star lives in you.", [
 (3, "Starlit Spells", "Always prepared — level 3: Guiding Bolt, Faerie Fire, Moonbeam, See Invisibility; level 5: Daylight, Fly; level 7: Guardian of Faith, Dimension Door; level 9: Wall of Force, Scrying."),
 (3, "Twinkling Aura", "While Innate Sorcery is active, you shed Bright Light in a 10-foot radius and the first creature you hit with a spell each turn takes extra Radiant damage equal to your Charisma modifier."),
 (6, "Constellations", "After each Long Rest choose one: The Archer (+2 to spell attack rolls), The Shield (+1 AC and Advantage on Concentration saves), or The Lantern (allies within 10 feet have Advantage on saving throws against Frightened and Blinded)."),
 (14, "Supernova", "As a Magic action you spend 6 Sorcery Points: each creature of your choice within 30 feet makes a Constitution save, taking 8d10 Radiant damage and having the Blinded condition until the end of its next turn on a failure, or half damage on a success."),
 (18, "Falling Star", "Once per Long Rest, you can cast Meteor Swarm without a spell slot, its damage fully Radiant."),
]),
("Frostblood Sorcery", "Winter in your veins: your magic freezes everything it touches.", [
 (3, "Cold Heart", "You have Resistance to Cold damage, and you are unaffected by extreme cold. Always prepared — level 3: Ray of Frost, Hold Person; level 5: Sleet Storm; level 7: Ice Storm; level 9: Cone of Cold."),
 (3, "Rime Spells", "When you deal Cold damage to a creature with a spell, its Speed is reduced by 10 feet until the start of your next turn."),
 (6, "Glacier Skin", "As a Reaction when you take damage, spend 2 Sorcery Points to gain Temporary Hit Points equal to 2d8 + your Sorcerer level."),
 (14, "Shatterpoint", "When a creature whose Speed you've reduced takes Cold damage from you, it takes an extra 2d8 Cold damage. If this reduces it to 0 Hit Points, it shatters into ice."),
 (18, "Avatar of Winter", "For 1 minute (once per Long Rest), you have Immunity to Cold damage, your Cold damage ignores Resistance and Immunity, and enemies within 15 feet of you have their Speed halved."),
]),
("Bloodsong Sorcery", "Magic carried in your heartbeat — and paid for in blood.", [
 (3, "Vital Font", "As a Bonus Action you can lose Hit Points equal to 1d6 per Sorcery Point to regain that many Sorcery Points (maximum equal to your Proficiency Bonus per Long Rest). These Hit Points can't be reduced in any way. Always prepared — level 3: False Life, Ray of Sickness, Hold Person; level 5: Vampiric Touch; level 7: Blight; level 9: Contagion."),
 (3, "Crimson Spells", "When a creature fails a saving throw against one of your spells, it also takes Necrotic damage equal to your Charisma modifier."),
 (6, "Hemocraft", "When you deal Necrotic damage with a spell, you can regain Hit Points equal to half the damage dealt, once per turn."),
 (14, "Sanguine Shield", "When you're hit by an attack, spend 3 Sorcery Points as a Reaction to gain +5 AC against it and all attacks until the start of your next turn."),
 (18, "Bloodstorm", "Once per Long Rest as a Magic action, every creature of your choice within 60 feet makes a Constitution save, taking 10d10 Necrotic damage on a failure (half on a success); you regain Hit Points equal to half the total damage dealt."),
]),
]

SUBS["warlock"] = [
("The Drowned King", "Your patron is a dead monarch who rules the bottom of the sea.", [
 (3, "Drowned King Spells", "Always prepared — level 3: Fog Cloud, Hold Person, Create or Destroy Water; level 5: Water Breathing, Sleet Storm; level 7: Control Water, Black Tentacles; level 9: Cone of Cold, Insect Plague."),
 (3, "Tidebound", "You gain a Swim Speed equal to your Speed and can breathe water."),
 (3, "Drowning Grasp", "Once per turn when you hit a creature with a spell attack, you can force it to make a Strength save or be pulled 10 feet toward you and have its Speed reduced to 0 until the start of your next turn."),
 (6, "Brine Ward", "You have Resistance to Cold damage, and when a creature within 10 feet hits you, you can take a Reaction to drench it: it has Disadvantage on its next attack roll."),
 (10, "Abyssal Pressure", "Creatures that start their turn Grappled or Restrained by you or your spells take 2d10 Bludgeoning damage."),
 (14, "Call of the Deep", "Once per Long Rest as a Magic action, each creature of your choice within 30 feet makes a Charisma save or is dragged to a drowning dream until the end of your next turn: it is Incapacitated and takes 10d6 Cold damage (half and not Incapacitated on a success)."),
]),
("The Hungry Library", "A sentient archive that trades forbidden knowledge for more knowledge.", [
 (3, "Library Spells", "Always prepared — level 3: Identify, Comprehend Languages, Detect Thoughts; level 5: Tongues, Clairvoyance; level 7: Arcane Eye, Locate Creature; level 9: Legend Lore, Scrying."),
 (3, "Marginalia", "You gain Expertise in two of Arcana, History, Nature and Religion."),
 (3, "Borrowed Words", "After each Long Rest choose one cantrip from any class's spell list. You know it until your next Long Rest; it counts as a Warlock spell for you."),
 (6, "Overdue Notice", "When a creature you can see casts a spell, you can take a Reaction to learn its name and level. Once per Long Rest, you can also cast that spell once within the next minute using a Pact Magic slot, if its level is no higher than your slot level."),
 (10, "Index of Souls", "Whenever you learn a creature's true name, you have Advantage on attack rolls against it and it has Disadvantage on saving throws against your spells."),
 (14, "Restricted Section", "Once per Long Rest you can cast any spell of level 6 or lower from any class's list without a spell slot."),
]),
("The Wild Gambler", "A patron of luck, risk and impossible odds.", [
 (3, "Gambler Spells", "Always prepared — level 3: Bane, Bless, Blur; level 5: Bestow Curse, Haste; level 7: Freedom of Movement, Confusion; level 9: Mislead, Dream."),
 (3, "Loaded Dice", "After each Long Rest roll three d20s and record the results. Once per turn, you can replace an attack roll, ability check or saving throw made by you or a creature you can see with one of these results; you must do so before the roll. Unused results vanish on your next Long Rest."),
 (6, "Double or Nothing", "When you cast a spell with a Pact Magic slot, you can roll a d6. On a 4 or higher, you regain the slot. On a 1, you take Psychic damage equal to twice the slot's level × 5. Once per Short Rest."),
 (10, "Stack the Deck", "You roll four d20s for Loaded Dice instead of three."),
 (14, "Jackpot", "When you roll a 20 on any d20 Test, you regain one expended Pact Magic slot and gain Heroic Inspiration."),
]),
]

SUBS["wizard"] = [
("Cartomancer", "Wizards who draw maps so precise the world bends to match them.", [
 (3, "Living Map", "You can spend 10 minutes mapping a location you're in. While you carry the map, you can't get lost there and can cast Misty Step without a spell slot a number of times equal to your Intelligence modifier per Long Rest while in that location."),
 (3, "Survey", "You gain proficiency in the Cartographer's Tools and Survival skill. Teleportation spells you cast have twice their normal range."),
 (6, "Fold the Page", "When you cast a spell of level 1 or higher, you can also teleport one willing creature you can see within 30 feet to another space you can see within 30 feet."),
 (10, "Marked Territory", "You can draw a circle on your map up to 1 mile across. You always know the location of creatures of a type you name within it, and you can cast Teleport to return to it once per Long Rest without a slot."),
 (14, "Cartographer's Dominion", "Once per Long Rest, redraw the battlefield: up to 6 creatures you can see within 120 feet make a Charisma save (willing creatures can fail) or are teleported to unoccupied spaces of your choice within that range."),
]),
("Golemancer", "Wizards who sculpt servants of clay, iron and stone.", [
 (3, "Clay Servant", "You craft a Medium construct companion during a Long Rest. It uses your Proficiency Bonus for attacks, has AC 13 + PB, Hit Points equal to 5 × your Wizard level, Speed 30 ft, and a Slam (+your spell attack, 1d8 + PB Bludgeoning). It acts on your turn; if you don't command it, it takes the Dodge action."),
 (3, "Artisan's Hands", "You gain proficiency with Mason's Tools and Smith's Tools, and you can repair 2d8 Hit Points to your servant during a Short Rest."),
 (6, "Spell Conduit", "When you cast a spell with a range of Touch, your servant can deliver it as if it had cast it."),
 (10, "Iron Frame", "Your servant becomes Large, gains Resistance to Bludgeoning, Piercing and Slashing damage, and its Slam deals 2d8 + PB."),
 (14, "Grand Golem", "Once per Long Rest your servant can become Huge for 1 minute: its reach becomes 15 feet, it makes two Slams per turn, and each Slam can knock the target Prone (Strength save against your spell save DC)."),
]),
("Mnemonist", "Wizards who study memory — their own and everyone else's.", [
 (3, "Memory Palace", "You can prepare two additional Wizard spells. You have perfect recall of anything you've seen or heard in the last month."),
 (3, "Steal Memory", "As a Magic action, a creature you touch makes an Intelligence save or forgets the last 10 minutes; you learn what it forgot. Once per Long Rest, or by expending a level 2+ spell slot."),
 (6, "Forgotten Face", "As a Bonus Action you can make a creature you can see forget your presence until the end of its next turn (Intelligence save negates): you're Invisible to it."),
 (10, "Echo Casting", "When you cast a spell of level 1–3, you can store it. Once before your next Long Rest you can cast it again without a slot."),
 (14, "Total Recall", "Once per Long Rest you can cast any spell you've seen cast within the last 24 hours, as if you had prepared it, using a spell slot of its level or higher."),
]),
]
