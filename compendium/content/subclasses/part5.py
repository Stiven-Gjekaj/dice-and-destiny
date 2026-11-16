# Original subclasses, part 5: Edition 2, batch 2 (one for each SRD class)
# Format: class -> list of (name, tagline, [(level, feature, text), ...])
# In a feature text, [[label]] shows the label in bold.
SUBS = {}

SUBS["barbarian"] = [
("Path of the War Drum", "Barbarians whose heartbeat becomes a war drum that every ally can hear.", [
 (3, "Battle Rhythm", "When you activate your Rage, choose a number of allies up to your Constitution modifier (minimum of one) within 30 feet of you who can hear you. Until your Rage ends, once on each of its turns while it is within 30 feet of you, each chosen ally adds your Rage Damage bonus to the damage of one weapon attack or Unarmed Strike that hits."),
 (3, "Thunderous Lungs", "You gain proficiency in the Performance skill. Your shout, drumming, or chant can be heard clearly up to 300 feet away."),
 (6, "Steady Beat", "While your Rage is active, you have Immunity to the Frightened condition, and allies chosen for your Battle Rhythm have Advantage on saving throws against it."),
 (10, "Call and Answer", "While your Rage is active, you can take a Bonus Action to let one ally chosen for your Battle Rhythm take a Reaction to make one weapon attack or Unarmed Strike. You can use this feature a number of times equal to your Constitution modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
 (14, "Thunder of the Host", "When you activate your Rage, each ally you choose for your Battle Rhythm gains Temporary Hit Points equal to your Barbarian level, and you can choose a number of allies up to your Constitution modifier plus 2."),
]),
]

SUBS["bard"] = [
("College of the Quill", "Chroniclers whose written words have a way of coming true.", [
 (3, "Chronicler", "You gain proficiency with Calligrapher's Supplies and in the History skill. You can write as fast as a person can speak."),
 (3, "Written Fate", "When you finish a Long Rest, you can write a number of lines in a journal equal to your Charisma modifier (minimum of one). Each line names a creature and one kind of D20 Test: attack rolls, ability checks, or saving throws. Until you finish your next Long Rest, when that creature fails a D20 Test of that kind, it can spend the line to roll your Bardic Inspiration die and add the number rolled to the d20, which can turn the failure into a success. Spending a line doesn't expend a use of Bardic Inspiration."),
 (6, "Edit the Record", "When you or an ally you can see within 60 feet of you fails a saving throw, you can take a Reaction to strike the failure from the record. The creature rerolls the save and must use the new roll. Once you use this feature, you can't use it again until you finish a Short or Long Rest."),
 (14, "The Last Chapter", "You write two more lines with Written Fate. When a creature spends one of your lines, it rolls your Bardic Inspiration die twice and adds both numbers."),
]),
]

SUBS["cleric"] = [
("Crossroads Domain", "Gods of the road between: of choices, chance meetings, and the luck of the traveler.", [
 (3, "Crossroads Domain Spells", "Always prepared. Level 3: Bless, Longstrider, Misty Step, Augury; level 5: Clairvoyance, Tongues; level 7: Dimension Door, Freedom of Movement; level 9: Teleportation Circle, Legend Lore."),
 (3, "Which Way?", "As a Magic action, you expend a use of Channel Divinity. You and a number of willing creatures up to your Proficiency Bonus within 30 feet of you each teleport up to 30 feet to an unoccupied space you can see."),
 (3, "Traveler's Luck", "You and your companions can't become lost except by magical means, and you have Advantage on Wisdom (Survival) checks to find a road, a ford, or a pass."),
 (6, "Fork in the Road", "When a creature you can see attacks an ally within 30 feet of you, you can take a Reaction before the attack roll to make that ally and another willing creature within 30 feet of you swap places by teleporting. The attack targets the creature in the space instead, if it is still in range. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
 (17, "All Roads Meet", "The range of Which Way? increases to 60 feet. In addition, once per Long Rest, you can cast Teleport without a spell slot."),
]),
]

SUBS["druid"] = [
("Circle of the Turning Year", "Druids who carry the four seasons inside them, and change with them.", [
 (3, "Circle of the Turning Year Spells", "Always prepared. Level 3: Healing Word, Ice Knife, Flaming Sphere, Barkskin; level 5: Plant Growth, Sleet Storm; level 7: Ice Storm, Fire Shield; level 9: Tree Stride, Mass Cure Wounds."),
 (3, "Heart of the Season", "As a Bonus Action, you can expend a use of Wild Shape to take on the power of a season for 10 minutes. Choose one. [[Spring:]] When you cast a spell that restores Hit Points, one creature that regains Hit Points from it regains an extra 1d8. [[Summer:]] Once on each of your turns when you deal damage with a Druid spell, you can add your Wisdom modifier to one damage roll as Fire damage. [[Autumn:]] When a creature fails a saving throw against one of your Druid spells, its Speed is halved until the end of its next turn. [[Winter:]] You gain Temporary Hit Points equal to twice your Druid level, and you have Resistance to Cold damage."),
 (6, "The Wheel Turns", "While your Heart of the Season is active, you can take a Bonus Action to change to a different season without expending a use of Wild Shape. Winter's Temporary Hit Points don't return when you change to it again."),
 (10, "Weathered", "While your Heart of the Season is active, you have Resistance to Cold and Fire damage, and you have Advantage on saving throws against the Frightened condition."),
 (14, "A Year in a Moment", "As a Magic action, you call all four seasons at once into a 30-foot Emanation originating from you. Each creature of your choice in it makes a Constitution saving throw against your spell save DC. On a failed save, it takes 6d8 Cold or Fire damage (your choice) and has the Restrained condition until the end of its next turn. On a successful save, it takes half as much damage only. Each other creature of your choice in the Emanation regains 4d8 Hit Points. Once you use this feature, you can't use it again until you finish a Long Rest."),
]),
]

SUBS["fighter"] = [
("Javelineer", "Fighters who never run out of something to throw.", [
 (3, "Hurler", "The normal range of your thrown weapons increases by 20 feet, and their long range increases by 60 feet. Being within 5 feet of an enemy doesn't give you Disadvantage on attack rolls with thrown weapons."),
 (3, "Pinning Throw", "Once on each of your turns when you hit a creature with a thrown weapon, you can force it to make a Strength saving throw (DC 8 + the ability modifier you used for the attack + your Proficiency Bonus). On a failed save, its Speed is 0 until the start of your next turn."),
 (7, "Ricochet", "Once on each of your turns when you miss with a thrown weapon, you can make the attack roll again against a different creature within 10 feet of the first target."),
 (10, "Hail of Steel", "As a Bonus Action, you can make one attack with a thrown weapon against each of up to a number of creatures equal to your Proficiency Bonus in a 30-foot Cone. Once you use this feature, you can't use it again until you finish a Short or Long Rest."),
 (15, "Deadeye", "Your attack rolls with thrown weapons score a Critical Hit on a roll of 19 or 20 on the d20."),
 (18, "First Throw", "When you roll Initiative, you can make one attack with a thrown weapon (no action required). In addition, you can use Pinning Throw twice on each of your turns."),
]),
]

SUBS["monk"] = [
("Warrior of the Coiled Serpent", "Monks who wrap, bind, and squeeze until the fight is over.", [
 (3, "Serpent's Coil", "The escape DC of your grapples equals your Focus save DC. You can grapple a creature with your legs and keep your hands free. While a creature is Grappled by you, your Unarmed Strikes against it deal extra damage equal to your Wisdom modifier."),
 (3, "Shed Skin", "You have Advantage on ability checks made to escape a grapple, and you can try to escape as a Bonus Action."),
 (6, "Constrict", "As a Bonus Action, you can spend 1 Focus Point to squeeze a creature Grappled by you. It makes a Constitution saving throw against your Focus save DC. On a failed save, it has the Restrained condition until the start of your next turn."),
 (11, "Twin Fangs", "You can grapple two creatures at once. Moving a creature Grappled by you doesn't cost you extra movement."),
 (17, "Crushing Embrace", "As a Magic action, you can spend 3 Focus Points to crush a creature Grappled by you. It makes a Constitution saving throw against your Focus save DC. On a failed save, it takes 8d10 Bludgeoning damage and has the Stunned condition until the end of your next turn. On a successful save, it takes half as much damage only."),
]),
]

SUBS["paladin"] = [
("Oath of the Wyrmsbane", "Paladins sworn to hunt the great dragons, and every tyrant who hoards what is not theirs.", [
 (3, "Wyrmsbane Oath Spells", "Always prepared. Level 3: Shield of Faith, Hunter's Mark; level 5: Hold Person, Warding Bond; level 9: Protection from Energy, Fly; level 13: Freedom of Movement, Stoneskin; level 17: Hold Monster, Wall of Force."),
 (3, "Stand Against the Fire", "When you or an ally within 30 feet of you must make a saving throw against an effect that targets an area, you can take a Reaction and expend a use of Channel Divinity. Each creature of your choice within 10 feet of you has Advantage on that saving throw and Resistance to the damage of that effect."),
 (7, "Aura of Defiance", "You and your allies have Advantage on saving throws against the Frightened condition while in your Aura of Protection. In addition, when you finish a Long Rest, choose Acid, Cold, Fire, Lightning, or Poison. You and your allies have Resistance to that damage type while in your aura."),
 (15, "Scale Splitter", "When you use Divine Smite against a creature that is Large or larger, the target takes an extra 2d8 Radiant damage, and the damage of the smite ignores Resistance."),
 (20, "Dragonslayer", "As a Bonus Action, you can take up the mantle of the dragonslayer for 10 minutes. For the duration, you have Resistance to damage from area effects, your weapon attacks against Large or larger creatures score a Critical Hit on a roll of 19 or 20 on the d20, and when an enemy in your Aura of Protection uses an area effect, you can take a Reaction to move up to your Speed toward it without provoking Opportunity Attacks. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a level 5 spell slot (no action required) to restore your use of it."),
]),
]

SUBS["ranger"] = [
("Dune Strider", "Rangers of salt flats and sand seas, who move like heat haze and strike like the noon sun.", [
 (3, "Dune Strider Spells", "Always prepared. Level 3: Create or Destroy Water; level 5: Blur; level 9: Wind Wall; level 13: Fire Shield; level 17: Insect Plague."),
 (3, "Desert Born", "You have Resistance to Fire damage, you are naturally adapted to hot climates, and you need only half the water a creature of your size normally needs."),
 (3, "Heat Haze", "As a Bonus Action, you can make the air around you shimmer. Until the start of your next turn, attack rolls against you have Disadvantage. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
 (7, "Sunstroke", "When you deal Hunter's Mark damage, you can make it Fire damage. Once on each of your turns when you deal this damage to a creature, it can't take Reactions until the start of its next turn."),
 (11, "Scorching Volley", "When you hit the target of your Hunter's Mark with an attack, each other creature of your choice within 5 feet of the target takes Fire damage equal to your Wisdom modifier."),
 (15, "Mirage Twin", "When a creature hits you with an attack roll, you can take a Reaction to reveal that it struck a mirage. The attack misses, and you teleport up to 10 feet to an unoccupied space you can see. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
]),
]

SUBS["rogue"] = [
("Contrabandist", "Rogues who move what should not be moved, past people who should have noticed.", [
 (3, "Hidden Pockets", "You gain proficiency with Water Vehicles and with the Forgery Kit. Creatures have Disadvantage on ability checks made to find objects that you hide on your body or in your gear."),
 (3, "Slip the Net", "When a creature you can see ends its turn within 5 feet of you, you can take a Reaction to move up to half your Speed without provoking Opportunity Attacks."),
 (9, "Grease the Wheels", "You have Advantage on Charisma checks made to deal with guards, customs officers, and other officials. You can take the Influence action as a Bonus Action."),
 (13, "Never Caught", "When you would gain the Grappled or Restrained condition, you can take a Reaction to avoid it. When you fail a Dexterity saving throw, you can reroll it and must use the new roll. Once you reroll a save in this way, you can't do so again until you finish a Short or Long Rest."),
 (17, "Vanishing Act", "As a Bonus Action, you can gain the Invisible condition until the end of your next turn and move up to your Speed without provoking Opportunity Attacks. Your next attack roll before the end of your next turn has Advantage. Once you use this feature, you can't use it again until you finish a Short or Long Rest."),
]),
]

SUBS["sorcerer"] = [
("Verdant Sorcery", "Sap runs with your blood, and flowers open where you sleep.", [
 (3, "Verdant Spells", "Always prepared. Level 3: Entangle, Cure Wounds, Barkskin, Spike Growth; level 5: Plant Growth, Speak with Plants; level 7: Blight, Freedom of Movement; level 9: Tree Stride, Awaken."),
 (3, "Thorned Skin", "When a creature within 5 feet of you hits you with a melee attack, it takes Piercing damage equal to your Charisma modifier (minimum of 1)."),
 (3, "Bloom", "While your Innate Sorcery is active, when you cast a Sorcerer spell with a spell slot, one creature of your choice within 30 feet of you regains Hit Points equal to the slot's level + your Charisma modifier."),
 (6, "Strangling Roots", "When a creature fails a saving throw against one of your Sorcerer spells, you can spend 1 Sorcery Point to make roots burst from the ground. The creature has the Restrained condition until the end of its next turn. In addition, Difficult Terrain made of plants doesn't cost you extra movement."),
 (14, "Living Grove", "As a Bonus Action, you can spend 3 Sorcery Points to grow a grove in a 15-foot Emanation originating from you for 1 minute. The Emanation is Difficult Terrain for your enemies, and each ally of your choice that starts its turn in it regains 1d6 Hit Points."),
 (18, "Heart of the Old Tree", "When you are reduced to 0 Hit Points and not killed outright, you can drop to a number of Hit Points equal to half your Hit Point maximum instead. Roots erupt around you: each creature of your choice within 15 feet of you makes a Strength saving throw against your spell save DC or has the Restrained condition for 1 minute. A Restrained creature repeats the save at the end of each of its turns, ending the effect on itself on a success. Once you use this feature, you can't use it again until you finish a Long Rest."),
]),
]

SUBS["warlock"] = [
("The Ninth Bell", "A bell that rings once for every ending. Your patron is the last sound anyone hears.", [
 (3, "Ninth Bell Spells", "Always prepared. Level 3: Bane, False Life, Silence, Ray of Enfeeblement; level 5: Bestow Curse, Speak with Dead; level 7: Death Ward, Blight; level 9: Hold Monster, Contagion."),
 (3, "Toll the Hour", "As a Bonus Action, you can make a bell toll in the mind of a creature you can see within 60 feet of you. It makes a Wisdom saving throw against your spell save DC. On a failed save, it has Disadvantage on the next saving throw it makes before the end of your next turn. You can use this feature a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."),
 (6, "Not Your Hour", "You have Resistance to Necrotic damage. When you are reduced to 0 Hit Points and not killed outright, you can drop to 1 Hit Point instead. Once you use this benefit, you can't use it again until you finish a Long Rest."),
 (10, "The Silence After", "A creature that fails its saving throw against your Toll the Hour also can't take Reactions until the start of its next turn."),
 (14, "The Ninth Stroke", "As a Magic action, you ring the ninth bell for a creature you can see within 60 feet of you. It makes a Constitution saving throw against your spell save DC, taking 10d10 Necrotic damage on a failed save or half as much on a successful one. If this damage reduces it to 0 Hit Points, it can't be raised from the dead by any spell of level 5 or lower. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a Pact Magic spell slot (no action required) to restore your use of it."),
]),
]

SUBS["wizard"] = [
("Mirrormancer", "Wizards who study reflections, and the worlds that wait behind the glass.", [
 (3, "Mirror Savant", "Add Mirror Image and Silent Image to your spellbook for free. They count as Wizard spells for you."),
 (3, "Glass Double", "As a Bonus Action, you can create an illusory reflection of yourself in an unoccupied space you can see within 30 feet of you. It lasts for 1 minute, until it takes any damage, or until you create another. It has your AC and can't take actions. When you cast a spell, you can cast it as if you were in the reflection's space. You can use this feature a number of times equal to your Intelligence modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
 (6, "Glass Step", "As a Bonus Action, you can swap places with your Glass Double by teleporting."),
 (10, "Return to Sender", "When you succeed on a saving throw against a spell of level 5 or lower that targets only you, or the spell attack roll of such a spell misses you, you can take a Reaction to send the spell back. The caster makes a saving throw against your spell save DC, using the ability the spell uses for its save (Dexterity for a spell attack). On a failed save, the caster suffers the spell's effects as if you had cast it on the caster. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a spell slot of level 3 or higher (no action required) to restore your use of it."),
 (14, "Hall of Mirrors", "You can have two Glass Doubles at once. When you cast a spell of level 1 to 3 that targets only one creature, you can target a second creature that is within range of one of your Glass Doubles. You can use this benefit a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."),
]),
]
