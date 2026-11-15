# Original subclasses, part 7: Edition 2, batch 4 (one for each SRD class)
# Format: class -> list of (name, tagline, [(level, feature, text), ...])
# In a feature text, [[label]] shows the label in bold.
SUBS = {}

SUBS["barbarian"] = [
("Path of the Still Storm", "Barbarians whose rage is cold and quiet, and far more dangerous for it.", [
 (3, "Cold Fury", "While your Rage is active, you can choose to keep a cold head. If you do, you can concentrate on spells and maintain Concentration (but you still can't cast spells), and once on each of your turns, when you miss with a melee attack, you can reroll the attack roll and must use the new roll."),
 (3, "Calm Eye", "You have Advantage on Wisdom (Insight) and Wisdom (Perception) checks while your Rage isn't active."),
 (6, "Measured Breath", "When you activate your Rage, you can end the Charmed or Frightened condition on yourself. While your Rage is active, you have Advantage on Wisdom saving throws."),
 (10, "Eye of the Storm", "While your Rage is active, when a creature you can see within your reach misses you with a melee attack, you can take a Reaction to make one melee weapon attack against it."),
 (14, "The Storm Breaks", "Once per turn while your Rage is active, when you hit a creature that missed you since the end of your last turn, the attack deals an extra 3d8 damage of the weapon's type. In addition, the reroll from Cold Fury works on any attack roll you make, not only melee attacks."),
]),
]

SUBS["bard"] = [
("College of Riddles", "Bards who ask the question no one can answer, and win the fight while the enemy thinks.", [
 (3, "Riddler", "You gain proficiency in the Investigation skill and with one Gaming Set of your choice."),
 (3, "Riddle Me This", "As a Bonus Action, you can expend one use of Bardic Inspiration to pose a riddle to a creature within 60 feet of you that can hear and understand you. It makes an Intelligence saving throw against your spell save DC. On a failed save, it is lost in thought until the start of your next turn: it can't take Reactions, and it subtracts one roll of your Bardic Inspiration die from the first attack roll it makes. A creature with an Intelligence score of 3 or lower is immune."),
 (6, "The Answer Was Obvious", "When you or an ally you can see within 60 feet of you makes an Intelligence, Wisdom, or Charisma saving throw, you can take a Reaction and expend one use of Bardic Inspiration to add your Intelligence modifier (minimum of +1) and one roll of your Bardic Inspiration die to the save."),
 (14, "Unanswerable", "When a creature fails its save against Riddle Me This, it also has the Incapacitated condition until the start of your next turn. A creature that succeeds on that save against you has Disadvantage on its next save against it for the next 24 hours."),
]),
]

SUBS["cleric"] = [
("Plague Domain", "Gods of the sickness and the cure, who know that the two are never far apart.", [
 (3, "Plague Domain Spells", "Always prepared. Level 3: Ray of Sickness, Detect Poison and Disease, Lesser Restoration, Ray of Enfeeblement; level 5: Bestow Curse, Stinking Cloud; level 7: Blight, Death Ward; level 9: Contagion, Greater Restoration."),
 (3, "Fever and Cure", "As a Magic action, you expend a use of Channel Divinity and choose one effect. [[Fever:]] Each creature of your choice in a 20-foot Emanation originating from you makes a Constitution saving throw against your spell save DC. On a failed save, it takes Poison damage equal to 2d6 + your Cleric level and has the Poisoned condition until the end of its next turn. On a successful save, it takes half as much damage only. [[Cure:]] Each creature of your choice in the Emanation regains Hit Points equal to 1d6 + your Cleric level, and you end the Poisoned condition and one disease on each of them."),
 (3, "Plague Doctor", "You gain proficiency with the Herbalism Kit and the Poisoner's Kit. You have Resistance to Poison damage."),
 (6, "Immune Response", "You and each ally within 30 feet of you have Advantage on saving throws against diseases and against the Poisoned condition. When you cast a spell that ends a disease or the Poisoned condition, the target also gains Temporary Hit Points equal to your Wisdom modifier + your Cleric level."),
 (17, "Plague Lord", "You have Immunity to Poison damage and the Poisoned condition. When you use Fever and Cure, you can choose both effects at once, choosing which creatures receive each one."),
]),
]

SUBS["druid"] = [
("Circle of the Glacier", "Druids of the ice that moves slowly, carves valleys, and never forgives.", [
 (3, "Circle of the Glacier Spells", "Always prepared. Level 3: Ice Knife, Fog Cloud, Hold Person, Spike Growth; level 5: Sleet Storm, Slow; level 7: Ice Storm, Fire Shield; level 9: Cone of Cold, Wall of Stone."),
 (3, "Rime Armor", "As a Bonus Action, you can expend a use of Wild Shape to cover yourself in ice for 10 minutes instead of changing shape. For the duration, you gain Temporary Hit Points equal to three times your Druid level, you have Resistance to Cold damage, and when a creature within 5 feet of you hits you with a melee attack, its Speed decreases by 10 feet until the start of its next turn."),
 (6, "Frozen Ground", "When you cast a Druid spell that deals Cold damage, you can make the ground in a 10-foot radius around one target icy until the end of your next turn. It is Difficult Terrain, and a creature that enters it for the first time on a turn makes a Dexterity saving throw against your spell save DC or has the Prone condition."),
 (10, "Heart of Winter", "You have Immunity to Cold damage, and you are naturally adapted to cold climates. While your Rime Armor is active, you can't be moved against your will."),
 (14, "Glacial Advance", "As a Magic action while your Rime Armor is active, you can send a wall of ice grinding forward in a 60-foot Line that is 10 feet wide. Each creature in the Line makes a Strength saving throw against your spell save DC. On a failed save, it takes 8d8 Cold damage, is pushed to the end of the Line, and has the Prone condition. On a successful save, it takes half as much damage only. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a spell slot of level 4 or higher (no action required) to restore your use of it."),
]),
]

SUBS["fighter"] = [
("Duelist", "Fighters who want one opponent, one blade, and nobody else in the way.", [
 (3, "Challenge", "As a Bonus Action, you can challenge a creature you can see within 30 feet of you for 1 minute, or until you challenge another creature. While you are within 5 feet of your challenged foe and no other creature is within 5 feet of you, you have a +2 bonus to AC against its attacks, and your melee weapon attacks against it deal an extra 1d6 damage."),
 (3, "Parry", "When the creature you have challenged hits you with a melee attack while you hold a melee weapon, you can take a Reaction to add your Proficiency Bonus to your AC against that attack, which can turn the hit into a miss."),
 (7, "Footwork", "When the creature you have challenged moves, you can take a Reaction to move up to half your Speed toward it. This movement doesn't provoke Opportunity Attacks."),
 (10, "Read the Blade", "You have Advantage on saving throws against the abilities and spells of the creature you have challenged, and when you finish a Short Rest, you regain one expended use of Second Wind."),
 (15, "Flawless Riposte", "When the creature you have challenged misses you with a melee attack, you can make one melee weapon attack against it as part of the same Reaction you used for Parry, or as a Reaction if you didn't use Parry."),
 (18, "Final Lesson", "The extra damage of Challenge increases to 3d6, and your weapon attacks against the creature you have challenged score a Critical Hit on a roll of 19 or 20 on the d20."),
]),
]

SUBS["monk"] = [
("Warrior of the Thunderclap", "Monks who strike so fast the air itself cracks.", [
 (3, "Thunder Palm", "When you hit a creature with an Unarmed Strike, you can change the damage type to Thunder. Once on each of your turns when you do so, you can push the target up to 10 feet away from you."),
 (3, "Clap", "As a Magic action, you can spend 1 Focus Point to clap your hands. Each creature in a 15-foot Cone makes a Constitution saving throw against your Focus save DC. On a failed save, it takes Thunder damage equal to two rolls of your Martial Arts die and has the Deafened condition until the end of your next turn. On a successful save, it takes half as much damage only. You can take this action in place of the Magic action of Flurry of Blows."),
 (6, "Rolling Thunder", "When you push a creature with Thunder Palm into another creature or a solid object, both take Thunder damage equal to one roll of your Martial Arts die."),
 (11, "Sound Barrier", "When you take the Dash action, your Speed increases by an extra 20 feet until the end of the turn, and creatures you move past within 5 feet take Thunder damage equal to your Wisdom modifier (once per creature per turn)."),
 (17, "Thunderclap", "When you use Clap, you can spend 3 more Focus Points to make it a 30-foot Cone. A creature that fails its save takes an extra 6d10 Thunder damage and has the Stunned condition until the end of your next turn."),
]),
]

SUBS["paladin"] = [
("Oath of Truth", "Paladins who will not lie, and who make lies very hard to tell anywhere near them.", [
 (3, "Truth Oath Spells", "Always prepared. Level 3: Detect Evil and Good, Heroism; level 5: Zone of Truth, See Invisibility; level 9: Clairvoyance, Tongues; level 13: Locate Creature, Banishment; level 17: Legend Lore, Dispel Evil and Good."),
 (3, "Unveil", "As a Magic action, you expend a use of Channel Divinity. For 1 minute, you can see invisible creatures and objects within 30 feet of you, you know if a creature within 30 feet of you is under the effect of an illusion or a shapechanging effect, and you can see its true form. Creatures in the area can't benefit from the Invisible condition against your allies who can see you."),
 (7, "Aura of Candor", "When a creature of your choice enters your Aura of Protection or starts its turn there, it makes a Charisma saving throw against your spell save DC. On a failed save, it can't speak a deliberate lie until the start of its next turn, and it knows that it failed. You and your allies in the aura have Advantage on saving throws against illusions and on Wisdom (Insight) checks."),
 (15, "Mark the Liar", "When a creature you can see tells a deliberate lie or attacks you while it has the Invisible condition, you can take a Reaction to mark it for 1 minute. The marked creature sheds Bright Light in a 10-foot radius, can't benefit from the Invisible condition, and takes an extra 2d8 Radiant damage the first time you hit it on each of your turns."),
 (20, "Light of Truth", "As a Bonus Action, you become a blazing witness for 10 minutes. You shed Bright Light in a 30-foot radius, and illusions and shapechanging effects of level 5 or lower end on enemies in the light. Enemies in your Aura of Protection have Disadvantage on Charisma (Deception) checks and on saving throws against your spells and Channel Divinity. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a level 5 spell slot (no action required) to restore your use of it."),
]),
]

SUBS["ranger"] = [
("Thornwarden", "Rangers who grow their arrows, their armor, and their snares from living briar.", [
 (3, "Thornwarden Spells", "Always prepared. Level 3: Entangle; level 5: Spike Growth; level 9: Plant Growth; level 13: Blight; level 17: Tree Stride."),
 (3, "Briar Shot", "Once on each of your turns when you hit the target of your Hunter's Mark with a weapon attack, thorns sprout in the wound. Until the start of your next turn, the target takes Piercing damage equal to your Wisdom modifier each time it moves 5 feet or more willingly."),
 (3, "Bark Hide", "While you aren't wearing armor, your base Armor Class equals 13 + your Dexterity modifier. You can use a Shield and still gain this benefit."),
 (7, "Snaring Growth", "When a creature takes damage from your Briar Shot, it also makes a Strength saving throw against your spell save DC. On a failed save, it has the Restrained condition until the start of your next turn. A creature can fail this save only once per turn."),
 (11, "Thicket", "As a Bonus Action, you can make thorny growth fill a 15-foot-radius circle centered on a point you can see within 60 feet of you for 1 minute. The area is Difficult Terrain for your enemies, and an enemy that enters it or starts its turn there takes 2d6 Piercing damage. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
 (15, "Crown of Thorns", "When a creature within 10 feet of you hits you with an attack, you can take a Reaction to give yourself Resistance to that damage and deal 2d8 Piercing damage to the attacker. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
]),
]

SUBS["rogue"] = [
("Chameleon", "Rogues who blend into any crowd, any wall, and any role.", [
 (3, "Blend In", "You can take the Hide action while you are only Lightly Obscured, and while you don't move on your turn, you have Advantage on Dexterity (Stealth) checks."),
 (3, "Borrowed Face", "You gain proficiency with the Disguise Kit. You can make a disguise with it in 1 minute, and creatures have Disadvantage on checks to see through it."),
 (9, "Color Shift", "As a Bonus Action, you can take the colors of your surroundings for 1 minute. For the duration, attack rolls against you from more than 30 feet away have Disadvantage, and you can hide in plain sight, even while a creature can see you, if you don't move on that turn. You can use this feature a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."),
 (13, "Mimic", "You can mimic the voice of any creature you have heard speak for at least 1 minute. When you hit a creature that can't see you with Sneak Attack, it can't tell where the attack came from, and you can take the Hide action as part of the same action."),
 (17, "Never Seen", "When you finish a Short or Long Rest, you gain the Invisible condition until you make an attack roll, deal damage, or cast a spell. If you lose it this way during combat, you regain it at the start of your next turn if you are Heavily Obscured or behind total cover."),
]),
]

SUBS["sorcerer"] = [
("Ghostblood Sorcery", "An ancestor's ghost rides in your blood and whispers advice, warnings, and spells.", [
 (3, "Ghostblood Spells", "Always prepared. Level 3: Protection from Evil and Good, False Life, Augury, See Invisibility; level 5: Speak with Dead, Spirit Guardians; level 7: Death Ward, Arcane Eye; level 9: Contact Other Plane, Legend Lore."),
 (3, "Ancestral Whisper", "You can add your Charisma modifier (minimum of +1) to Intelligence (History) and Intelligence (Religion) checks. While your Innate Sorcery is active, you have Advantage on Wisdom saving throws."),
 (3, "Ghostly Hand", "While your Innate Sorcery is active, you can cast your Sorcerer spells with a range of Touch from a point within 30 feet of you, as your ancestor's hand reaches out."),
 (6, "Possessed Defense", "When a creature you can see hits you with an attack roll, you can spend 2 Sorcery Points and take a Reaction to let your ancestor take the blow. You have Resistance to the damage, and the attacker takes Necrotic damage equal to your Charisma modifier + your Sorcerer level."),
 (14, "Step Through the Veil", "As a Bonus Action, you can spend 3 Sorcery Points to become partly a ghost until the start of your next turn. You can move through creatures and objects as if they were Difficult Terrain, and you have Resistance to Bludgeoning, Piercing, and Slashing damage. If you end your turn inside an object, you take 1d10 Force damage."),
 (18, "The Ancestor Rises", "As a Bonus Action, you can spend 5 Sorcery Points to call your ancestor out of your blood for 1 minute. It appears in an unoccupied space within 30 feet of you, uses your AC, and can't be targeted. At the end of each of your turns, it touches one creature within 5 feet of it: the creature makes a Wisdom saving throw against your spell save DC, taking 5d10 Necrotic damage and having the Frightened condition until the end of your next turn on a failed save, or half as much damage only on a successful one. As a Bonus Action, you can move the ancestor up to 30 feet."),
]),
]

SUBS["warlock"] = [
("The Lady of Locks", "Your patron keeps every key, guards every threshold, and remembers every door you have ever opened.", [
 (3, "Lady of Locks Spells", "Always prepared. Level 3: Alarm, Arcane Lock, Knock, Hold Person; level 5: Glyph of Warding, Nondetection; level 7: Dimension Door, Secret Chest; level 9: Passwall, Teleportation Circle."),
 (3, "Keyholder", "You can cast Knock without expending a spell slot a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest. You have Advantage on Dexterity (Sleight of Hand) checks made to pick locks."),
 (3, "Lock Them In", "Once on each of your turns when you hit a creature with a spell attack, you can lock it in place. It makes a Strength saving throw against your spell save DC or its Speed is 0 until the start of your next turn."),
 (6, "Doorway", "As a Bonus Action, you can touch a door, gate, or window frame and teleport to the other side of another door, gate, or window frame you can see within 60 feet of you, or that you have passed through in the last 24 hours within 1 mile. Once you use this feature, you can't use it again until you finish a Short or Long Rest."),
 (10, "Closed to You", "When a creature you can see within 60 feet of you casts a spell to teleport or travel to another plane, you can take a Reaction to make it make a Charisma saving throw against your spell save DC. On a failed save, the spell fails and is wasted. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a Pact Magic spell slot (no action required) to restore your use of it."),
 (14, "The Last Door", "As a Magic action, you open a door to your patron's endless hall behind a creature you can see within 60 feet of you. It makes a Charisma saving throw against your spell save DC. On a failed save, it is shut in the hall until the end of your next turn, then returns to the space it left (or the nearest unoccupied space) and takes 8d10 Psychic damage. On a successful save, it takes half as much damage only. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a Pact Magic spell slot (no action required) to restore your use of it."),
]),
]

SUBS["wizard"] = [
("Familiarist", "Wizards whose greatest work is the small, clever creature on their shoulder.", [
 (3, "Bound Familiar", "Add Find Familiar to your spellbook for free, and you can cast it as a Bonus Action. Your familiar's Hit Point maximum equals its normal maximum + three times your Wizard level, and it adds your Proficiency Bonus to its AC, attack rolls, and saving throws. As a Bonus Action, you can command it to make one attack, using your spell attack modifier. On a hit, the attack deals 1d4 + your Intelligence modifier Force damage."),
 (3, "Shared Senses", "While your familiar is within 1 mile of you, you can see through its eyes and hear through its ears as a Bonus Action, and when you cast a spell with a range of Touch through it, the familiar doesn't need to take a Reaction."),
 (6, "Familiar Shield", "When your familiar is within 5 feet of you and you are hit by an attack, you can take a Reaction to have the familiar take the damage instead. If this reduces the familiar to 0 Hit Points, it vanishes as normal, and you can recast Find Familiar without a spell slot once per Long Rest."),
 (10, "Spell Carrier", "When you cast a spell with a range of 5 feet or more, you can cast it as if you were in your familiar's space if the familiar is within 100 feet of you. Your familiar has Resistance to damage from your spells."),
 (14, "Greater Familiar", "Your familiar becomes Medium if you choose, its Hit Point maximum increases by your Wizard level, and once on each of your turns when you cast a Wizard spell of level 1 or higher, the familiar can take a Reaction to make one attack. On a hit, the attack deals an extra 3d8 Force damage."),
]),
]
