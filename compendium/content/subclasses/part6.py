# Original subclasses, part 6: Edition 2, batch 3 (one for each SRD class)
# Format: class -> list of (name, tagline, [(level, feature, text), ...])
# In a feature text, [[label]] shows the label in bold.
SUBS = {}

SUBS["barbarian"] = [
("Path of the Cinder Heart", "Barbarians whose fury burns hot enough to scorch the air around them.", [
 (3, "Smoldering Rage", "While your Rage is active, your melee weapon attacks and Unarmed Strikes deal Fire damage instead of their normal type if you choose, and when a creature within 5 feet of you hits you with a melee attack, it takes Fire damage equal to your Rage Damage bonus."),
 (3, "Hearthborn", "You have Resistance to Fire damage while you aren't wearing Heavy armor, and you are naturally adapted to hot climates."),
 (6, "Fire Walker", "You can move through fire and lava-warmed ground without harm, and you can take a Bonus Action to set alight a flammable object you touch that isn't being worn or carried."),
 (10, "Flare", "When you activate your Rage, each creature of your choice within 10 feet of you makes a Dexterity saving throw (DC 8 + your Constitution modifier + your Proficiency Bonus), taking 2d10 Fire damage on a failed save or half as much on a successful one."),
 (14, "Pyre of Spite", "While your Rage is active, the Fire damage of your Smoldering Rage increases to twice your Rage Damage bonus, and when you are reduced to 0 Hit Points while raging, each creature of your choice within 10 feet of you takes 4d10 Fire damage. You can still make Death Saving Throws as normal."),
]),
]

SUBS["bard"] = [
("College of Lullabies", "Bards of the cradle-song, who soothe the hurt and send the angry off to sleep.", [
 (3, "Soothing Voice", "You learn the Sleep spell, and it counts as a Bard spell for you. It doesn't count against the number of spells you can prepare. When you cast Sleep, creatures have Disadvantage on the first saving throw against it."),
 (3, "Cradle Song", "During a Short Rest, you can sing for its whole length. Each ally who hears the song and spends one or more Hit Dice during the rest regains extra Hit Points equal to one roll of your Bardic Inspiration die."),
 (6, "Hush, Now", "When a creature you can see within 60 feet of you makes an attack roll, you can take a Reaction and expend one use of Bardic Inspiration. The creature makes a Wisdom saving throw against your spell save DC. On a failed save, it subtracts the number rolled on your Bardic Inspiration die from the attack roll, and it has the Incapacitated condition until the start of its next turn as a wave of drowsiness passes over it. Creatures that can't be Charmed are immune to this feature."),
 (14, "Endless Dream", "Once per Long Rest, you can cast Dream without a spell slot. In addition, creatures that are Unconscious because of your Sleep spell don't wake up when they take damage the first time."),
]),
]

SUBS["cleric"] = [
("Mountain Domain", "Gods of stone and summit: patient, unmoving, and older than any kingdom.", [
 (3, "Mountain Domain Spells", "Always prepared. Level 3: Shield of Faith, Earth Tremor, Shatter, Spiritual Weapon; level 5: Meld into Stone, Protection from Energy; level 7: Stone Shape, Stoneskin; level 9: Wall of Stone, Passwall."),
 (3, "Stand Like Stone", "As a Magic action, you expend a use of Channel Divinity. For 1 minute, you and a number of allies of your choice within 30 feet of you up to your Wisdom modifier (minimum of one) have Resistance to Bludgeoning, Piercing, and Slashing damage and can't be moved against your will or knocked Prone. The effect ends early on a creature that moves more than 30 feet from you."),
 (3, "Stonesense", "You gain proficiency with Mason's Tools. You have Tremorsense with a range of 10 feet while you are standing on stone or earth."),
 (6, "Rockfall", "When you deal damage to a creature with a Cleric spell, you can force it to make a Strength saving throw against your spell save DC. On a failed save, it has the Prone condition. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
 (17, "Living Mountain", "When you use Stand Like Stone, you and the allies it affects also gain Temporary Hit Points equal to your Cleric level, and it lasts for 10 minutes."),
]),
]

SUBS["druid"] = [
("Circle of Feathers", "Druids of the high air, who wear the shapes of hawk, owl, and storm-crow.", [
 (3, "Circle of Feathers Spells", "Always prepared. Level 3: Feather Fall, Gust of Wind, Find Traps, Hold Person; level 5: Fly, Wind Wall; level 7: Freedom of Movement, Locate Creature; level 9: Commune with Nature, Scrying."),
 (3, "Wings of the Circle", "When you use Wild Shape, you can take the form of a Beast that has a Fly Speed even if your level doesn't normally allow it, but its Challenge Rating can't be more than 1/4 (1/2 at Druid level 6, 1 at level 10). While you are in a form with a Fly Speed, you gain Temporary Hit Points equal to your Druid level."),
 (3, "Sky Sight", "You have Advantage on Wisdom (Perception) checks that rely on sight, and you can see clearly up to 1 mile away in clear weather."),
 (6, "Diving Strike", "While you are in a Wild Shape form that has a Fly Speed, when you move at least 20 feet straight down toward a creature and then hit it with an attack on the same turn, the attack deals an extra 2d8 damage, and the target makes a Strength saving throw against your spell save DC or has the Prone condition."),
 (10, "Feathered Escape", "When you take damage while in a Wild Shape form that has a Fly Speed, you can take a Reaction to fly up to half your Fly Speed without provoking Opportunity Attacks."),
 (14, "Thunderbird", "As a Magic action, you can expend two uses of Wild Shape to become a great storm bird for 1 minute. You use your own game statistics, but you are Large, you have a Fly Speed of 80 feet, and once on each of your turns you can call a bolt of lightning on a creature you can see within 120 feet: it makes a Dexterity saving throw against your spell save DC, taking 4d10 Lightning damage on a failed save or half as much on a successful one. You can cast spells in this form."),
]),
]

SUBS["fighter"] = [
("Outrider", "Fighters who live in the saddle, scouting ahead and striking before the enemy can form a line.", [
 (3, "Born to the Saddle", "You gain proficiency in the Animal Handling skill. Mounting or dismounting costs you only 5 feet of movement, and you have Advantage on saving throws to avoid falling off your mount."),
 (3, "Riding Strike", "Once on each of your turns when you hit a creature with a weapon attack while you are mounted or after you move at least 20 feet on that turn, the attack deals an extra 1d8 damage. When you gain the Fighter level 10 feature of this subclass, the extra damage increases to 2d8."),
 (7, "Scout Ahead", "You and your mount can take the Dash or Disengage action as a Bonus Action. While you ride, your mount uses your saving throw bonuses if they are higher than its own."),
 (10, "Shield Your Mount", "When your mount is hit by an attack, you can take a Reaction to make yourself the target of the attack instead. In addition, Riding Strike deals 2d8 extra damage."),
 (15, "Trample", "When you move through or next to a creature while mounted, you can force it to make a Strength saving throw (DC 8 + your Strength modifier + your Proficiency Bonus). On a failed save, it has the Prone condition and takes Bludgeoning damage equal to 1d10 + your Strength modifier. A creature can be affected by this only once per turn."),
 (18, "Unhorsed, Never Beaten", "When you or your mount drop to 0 Hit Points, you can take a Reaction to let the other one move up to its Speed without provoking Opportunity Attacks. While you aren't mounted, your Speed increases by 10 feet, and Riding Strike works after you move at least 10 feet."),
]),
]

SUBS["monk"] = [
("Warrior of the Long Staff", "Monks who trust a length of wood more than any blade.", [
 (3, "Staff Form", "The Quarterstaff counts as a Monk weapon for you, and when you hit with it you can use your Martial Arts die in place of its normal damage. While you hold a Quarterstaff in two hands, it has a reach of 10 feet for you."),
 (3, "Sweep", "When you hit a creature with a Quarterstaff as part of your Flurry of Blows, you can force it to make a Dexterity saving throw against your Focus save DC. On a failed save, it has the Prone condition."),
 (6, "Vault", "When you take the Step of the Wind, you can plant your staff and vault: your jump distance is tripled, and you can move over creatures without entering their spaces."),
 (11, "Whirling Guard", "While you hold a Quarterstaff, you can take a Reaction when a creature hits you with a ranged attack to reduce the damage by 1d10 + your Dexterity modifier + your Monk level. If you reduce the damage to 0, you knock the missile aside."),
 (17, "Thousand Strikes", "As a Magic action, you can spend 4 Focus Points to spin your staff into a blur. Make one Quarterstaff attack against each creature of your choice within 10 feet of you. On a hit, the attack deals an extra 3d10 Force damage, and you can impose the Sweep effect on the target."),
]),
]

SUBS["paladin"] = [
("Oath of Liberty", "Paladins who break chains, open cages, and stand between the weak and anyone who would own them.", [
 (3, "Liberty Oath Spells", "Always prepared. Level 3: Command, Expeditious Retreat; level 5: Knock, Misty Step; level 9: Dispel Magic, Haste; level 13: Freedom of Movement, Dimension Door; level 17: Passwall, Dispel Evil and Good."),
 (3, "Break the Chain", "As a Bonus Action, you expend a use of Channel Divinity. Each ally of your choice within 30 feet of you who has the Charmed, Frightened, Grappled, Paralyzed, or Restrained condition is freed from one of those conditions, and each ally you free can take a Reaction to move up to half its Speed without provoking Opportunity Attacks."),
 (7, "Aura of Freedom", "You and your allies in your Aura of Protection can't have your Speed reduced, and you have Advantage on ability checks and saving throws made to avoid or end the Grappled or Restrained condition."),
 (15, "Tyrant's Bane", "When a creature you can see causes an ally within 30 feet of you to gain the Charmed, Frightened, Grappled, or Restrained condition, you can take a Reaction to move up to your Speed toward that creature without provoking Opportunity Attacks and make one melee weapon attack against it."),
 (20, "Unconquered", "As a Bonus Action, you become an unstoppable force of freedom for 10 minutes. For the duration, you and your allies in your Aura of Protection have Immunity to the Charmed, Frightened, Grappled, Paralyzed, and Restrained conditions, and you can move through the spaces of hostile creatures. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a level 5 spell slot (no action required) to restore your use of it."),
]),
]

SUBS["ranger"] = [
("Reefstalker", "Rangers of coast, reef, and wreck, who hunt where the land ends.", [
 (3, "Reefstalker Spells", "Always prepared. Level 3: Create or Destroy Water; level 5: Fog Cloud; level 9: Water Breathing; level 13: Control Water; level 17: Commune with Nature."),
 (3, "Tidal Hunter", "You have a Swim Speed equal to your Speed, and you can hold your breath for 1 hour. Fighting underwater doesn't give you Disadvantage on attack rolls with spears, tridents, nets, and crossbows."),
 (3, "Harpoon Shot", "Once on each of your turns when you hit the target of your Hunter's Mark with an attack, you can pull it up to 10 feet toward you if it is Large or smaller."),
 (7, "Slippery", "You have Advantage on ability checks and saving throws made to avoid or end the Grappled or Restrained condition, and Difficult Terrain made of water, mud, or wet rock doesn't cost you extra movement."),
 (11, "Undertow", "When you pull a creature with Harpoon Shot, it also makes a Strength saving throw against your spell save DC. On a failed save, it has the Prone condition, or if it is in water, it is pulled under and can't breathe until the start of your next turn."),
 (15, "Riptide", "When a creature you can see within 30 feet of you moves away from you, you can take a Reaction to make one weapon attack against it. On a hit, its Speed becomes 0 until the end of the turn."),
]),
]

SUBS["rogue"] = [
("Bounty Hunter", "Rogues who bring them back alive, because a living prisoner pays twice.", [
 (3, "Wanted", "You gain proficiency in the Survival skill, or another skill of your choice if you already have it. You have Advantage on Wisdom (Survival) checks made to track a creature you have seen, and on Intelligence (Investigation) checks made to learn where it went."),
 (3, "Take Them Alive", "When you reduce a creature to 0 Hit Points with a melee attack, you can knock it out instead of killing it, even with a weapon. When you hit a creature with Sneak Attack, you can forgo the extra damage of one Sneak Attack die to give it the Grappled condition (escape DC equals your Cunning Strike DC), if it is no more than one size larger than you."),
 (9, "Manacles Ready", "You can apply Manacles to a creature Grappled by you, Incapacitated, or Restrained as a Bonus Action. You have Advantage on ability checks to see through a disguise or a false name."),
 (13, "No Escape", "A creature Grappled by you has Disadvantage on ability checks made to escape. When a creature you can see within 30 feet of you takes the Disengage or Dash action, you can take a Reaction to move up to your Speed toward it."),
 (17, "Dead or Alive", "Once on each of your turns when you hit a creature Grappled by you or Restrained, you can deal Sneak Attack damage to it even if you already used Sneak Attack this turn. The second Sneak Attack can't use Cunning Strike options. You can use this feature a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."),
]),
]

SUBS["sorcerer"] = [
("Crystalline Sorcery", "Gems grow in your bones, and your magic comes out bent and bright like light through a prism.", [
 (3, "Crystalline Spells", "Always prepared. Level 3: Color Spray, Shield, Mirror Image, Shatter; level 5: Daylight, Protection from Energy; level 7: Stoneskin, Fire Shield; level 9: Wall of Stone, Wall of Force."),
 (3, "Gem Skin", "Your Hit Point maximum increases by 3, and it increases by 1 again whenever you gain another Sorcerer level. Parts of your skin are covered in hard, smooth crystal."),
 (3, "Prism", "While your Innate Sorcery is active, when you cast a Sorcerer spell that deals damage, you can change its damage type to Fire, Cold, Lightning, Radiant, or Force."),
 (6, "Refraction", "When you cast a Sorcerer spell that targets one creature and deals damage, you can spend 2 Sorcery Points to split off a second beam. A second creature within 15 feet of the first takes half the damage that the first creature takes."),
 (14, "Diamond Body", "As a Reaction when you take damage, you can spend 3 Sorcery Points to have Resistance to that damage and to all damage of that type until the start of your next turn."),
 (18, "Living Prism", "As a Bonus Action, you can spend 5 Sorcery Points to become a shining crystal statue that moves and casts for 1 minute. For the duration, you shed Bright Light in a 30-foot radius, you have Resistance to all damage except Thunder damage, and when a creature hits you with a spell attack, you can take a Reaction to reflect a ray of light at it that deals 4d10 Radiant damage."),
]),
]

SUBS["warlock"] = [
("The Sleeping Titan", "Your patron is a giant older than the gods, buried under a mountain range and dreaming of the day it wakes.", [
 (3, "Sleeping Titan Spells", "Always prepared. Level 3: Earth Tremor, Thunderwave, Enlarge/Reduce, Shatter; level 5: Meld into Stone, Slow; level 7: Stone Shape, Stoneskin; level 9: Wall of Stone, Hold Monster."),
 (3, "Titan's Grip", "You have Advantage on Strength checks and Strength saving throws, and you count as one size larger when you determine your carrying capacity and the weight you can push, drag, or lift."),
 (3, "Stone Fist", "Once on each of your turns when you hit a creature with an attack roll, you can deal an extra 1d8 Bludgeoning damage and push it up to 10 feet away from you. The extra damage increases to 2d8 at Warlock level 10."),
 (6, "Earthen Hide", "While you aren't wearing armor, your base Armor Class equals 13 + your Dexterity modifier. You have Resistance to Bludgeoning damage from falls and falling objects."),
 (10, "Titan Shake", "As a Magic action, you stamp the ground. Each creature of your choice within 15 feet of you that is standing on the ground makes a Dexterity saving throw against your spell save DC. On a failed save, it takes 3d8 Bludgeoning damage and has the Prone condition. On a successful save, it takes half as much damage only. Once you use this feature, you can't use it again until you finish a Short or Long Rest."),
 (14, "The Titan Stirs", "As a Bonus Action, you grow to Huge size for 1 minute if there is room. For the duration, your reach increases by 10 feet, your Stone Fist deals an extra 4d8 Bludgeoning damage instead of its normal extra damage, and you have Resistance to Bludgeoning, Piercing, and Slashing damage. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a Pact Magic spell slot (no action required) to restore your use of it."),
]),
]

SUBS["wizard"] = [
("Chromaturge", "Wizards who study color as a force of its own, and paint the world in it.", [
 (3, "Palette", "Add Color Spray and Hypnotic Pattern to your spellbook for free. When you cast Color Spray, Hypnotic Pattern, Prismatic Spray, or Prismatic Wall, you can choose a number of creatures up to your Intelligence modifier (minimum of one) that the spell doesn't affect."),
 (3, "Paint the Foe", "When a creature fails a saving throw against one of your Wizard spells, you can splash it with a color for 1 minute or until you splash it again. [[Red:]] it takes an extra 1d6 Fire damage the first time you damage it on each of your turns. [[Blue:]] its Speed decreases by 10 feet. [[Gold:]] it sheds Bright Light in a 10-foot radius and can't benefit from the Invisible condition. You can use this feature a number of times equal to your Intelligence modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
 (6, "Fast Colors", "Your colors from Paint the Foe last until the creature finishes a Short or Long Rest, or until you splash it again. You can always see a creature you have painted if it is within 120 feet of you, even if it is Invisible, as long as it isn't behind total cover."),
 (10, "Mixed Colors", "A creature can carry two different colors from Paint the Foe at once, and splashing it with a second color doesn't end the first."),
 (14, "Masterpiece", "As a Magic action, you can paint the air with every color at once. Each creature of your choice in a 30-foot Cone makes a Wisdom saving throw against your spell save DC. On a failed save, it takes 8d8 Psychic damage, has the Blinded condition until the end of its next turn, and carries all three colors of Paint the Foe. On a successful save, it takes half as much damage only. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a spell slot of level 5 or higher (no action required) to restore your use of it."),
]),
]
