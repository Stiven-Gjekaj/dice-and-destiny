# Original subclasses, part 1: Barbarian, Bard, Cleric, Druid
# Format: class -> list of (name, tagline, [(level, feature, text), ...])
SUBS = {}

SUBS["barbarian"] = [
("Path of the Ironbound", "Warriors who wrap their arms in chains and drag the battle wherever they want it.", [
 (3, "Chain Lash", "While your Rage is active, your melee weapon attacks with a weapon that has the Heavy or Versatile property have a reach of 10 feet. Once per turn when you hit a creature with such an attack, you can pull it up to 10 feet toward you."),
 (3, "Binding Grip", "When you hit a creature with a melee attack while raging, you can forgo the damage of that attack to grapple the target instead (escape DC 8 + your Strength modifier + your Proficiency Bonus). You can grapple creatures up to one size larger than you."),
 (6, "Anchor", "While raging, you can't be moved against your will, and you have Advantage on saving throws against being knocked Prone."),
 (10, "Shackle Breaker", "As a Bonus Action, you can end the Grappled or Restrained condition on yourself or on a willing creature within 5 feet of you. While raging, allies within 10 feet of you have Advantage on checks made to escape a grapple."),
 (14, "Iron Maelstrom", "As a Magic action while raging, you whirl your chains. Each creature of your choice within 15 feet of you makes a Strength saving throw (DC 8 + your Strength modifier + your Proficiency Bonus). On a failure, a creature takes 2d10 + your Strength modifier Bludgeoning damage and is pulled into an unoccupied space within 5 feet of you. On a success, it takes half as much damage only. Once you use this feature, you can't use it again until you finish a Short or Long Rest, unless you expend a use of your Rage to use it again."),
]),
("Path of the Hollow Hunger", "Barbarians possessed by a ravenous spirit that grows stronger with every wound.", [
 (3, "Gnashing Spirit", "While your Rage is active, you can make a special melee attack as a Bonus Action: a spectral bite that deals 1d8 + your Strength modifier Necrotic damage. On a hit, you gain Temporary Hit Points equal to your Rage Damage bonus."),
 (3, "Scent of Weakness", "You know whether any creature within 30 feet of you is Bloodied (at half its Hit Points or fewer). You have Advantage on Wisdom (Survival) checks to track a creature that has taken damage in the last 24 hours."),
 (6, "Feast of the Fallen", "When you reduce a creature to 0 Hit Points while raging, you can regain Hit Points equal to one roll of your Hit Die + your Constitution modifier. You can do so a number of times equal to your Constitution modifier (minimum once), regaining all uses when you finish a Long Rest."),
 (10, "Hungering Howl", "When you activate your Rage, each creature of your choice within 30 feet of you that can hear you makes a Wisdom saving throw (DC 8 + your Constitution modifier + your Proficiency Bonus). On a failure, the creature has the Frightened condition until the end of your next turn."),
 (14, "Insatiable", "Your Gnashing Spirit bite deals an extra 1d8 Necrotic damage, and the Temporary Hit Points it grants are doubled. In addition, when you would be reduced to 0 Hit Points while raging, you can expend one Hit Die to drop to 1 Hit Point instead and immediately make one Gnashing Spirit attack against a creature within reach (no action required). Once you use this benefit, you can't do so again until you finish a Long Rest."),
]),
("Path of the Mountain's Echo", "Rage drawn from the slow, crushing patience of stone.", [
 (3, "Bedrock Rage", "While raging, you have Tremorsense with a range of 15 feet, and when a creature you can see hits you with an attack, you can take a Reaction to reduce the damage by 1d8 + your Constitution modifier."),
 (3, "Stonestep", "Difficult terrain made of earth, stone or rubble doesn't cost you extra movement, and you have Advantage on Strength (Athletics) checks to climb natural rock."),
 (6, "Rockslide Shove", "When you shove a creature, you can push it up to 15 feet instead of 5. If it hits a solid surface or another creature before moving the full distance, it and that creature each take 1d10 Bludgeoning damage."),
 (10, "Avalanche Charge", "If you move at least 20 feet in a straight line toward a creature and then hit it with a melee attack on the same turn, it makes a Strength saving throw (DC 8 + your Strength modifier + your Proficiency Bonus) or takes an extra 2d10 Bludgeoning damage and has the Prone condition."),
 (14, "Unbroken Peak", "While raging, you have Resistance to all damage except Psychic damage, and the first time each turn you would be reduced to 0 Hit Points, you are reduced to 1 Hit Point instead if you have at least one Hit Die remaining; expend that Hit Die."),
]),
]

SUBS["bard"] = [
("College of Masks", "Performers who carry a different self for every occasion.", [
 (3, "Mask Repertoire", "You craft three ritual masks: the Hero, the Trickster and the Tyrant. As a Bonus Action you don or swap a mask; you wear only one at a time. Hero: when you give Bardic Inspiration, the target also gains Temporary Hit Points equal to your Charisma modifier + your Bard level. Trickster: you have Expertise in Deception, and a creature that receives your Bardic Inspiration gains +10 feet of Speed until the end of its next turn. Tyrant: when a creature fails a saving throw against one of your Enchantment spells, it takes extra Psychic damage equal to one roll of your Bardic die."),
 (3, "Quick Change", "You can alter your clothing, hair and voice in 1 minute to appear as a different person of your size. Creatures have Disadvantage on Wisdom (Insight or Perception) checks to see through it."),
 (6, "Second Face", "When you fail a Wisdom or Charisma saving throw, you can take a Reaction to swap masks and reroll the save, using the new roll. Once you use this feature, you can't use it again until you finish a Short or Long Rest."),
 (14, "Thousand Faces", "You can wear two masks at once and gain the benefits of both."),
]),
("College of Echoes", "Bards who weaponize resonance, silence and sound itself.", [
 (3, "Resonant Strike", "When you hit a creature with a weapon attack or deal damage to it with a cantrip, you can expend one use of Bardic Inspiration to add your Bardic die to the damage as Thunder damage. Each other creature of your choice within 5 feet of the target takes Thunder damage equal to half the number rolled."),
 (3, "Listening Ear", "You have Blindsight with a range of 10 feet, and Advantage on Wisdom (Perception) checks that rely on hearing."),
 (6, "Silencing Chord", "When a creature you can see within 60 feet casts a spell with a Verbal component, you can take a Reaction and expend one use of Bardic Inspiration. The creature makes a Constitution saving throw against your spell save DC. On a failure, the spell fails but the slot isn't expended. Once a creature succeeds on this save, it is immune to this feature for 24 hours."),
 (14, "Perfect Pitch", "Your spells that deal Thunder damage ignore Resistance to Thunder damage, and you add your Charisma modifier to one damage roll of each such spell."),
]),
("College of the Road", "Wandering minstrels whose songs keep travelers alive.", [
 (3, "Wayfarer's Tune", "When you and your allies finish a Short Rest, each creature that spends Hit Dice regains extra Hit Points equal to one roll of your Bardic die. In addition, your group can travel at a fast pace without penalties to Wisdom (Perception) checks."),
 (3, "Campfire Lore", "You learn two languages and gain proficiency in the Survival skill or with a musical instrument of your choice."),
 (6, "Rallying Verse", "When an ally you can see within 30 feet drops to 0 Hit Points, you can take a Reaction and expend one use of Bardic Inspiration. The ally regains Hit Points equal to your Bardic die roll + your Charisma modifier."),
 (14, "Song of the Long Road", "Allies within 30 feet of you gain +10 feet of Speed and have Advantage on saving throws against Exhaustion. You always have Teleport prepared and can cast it once without a spell slot, regaining that use when you finish a Long Rest."),
]),
]

SUBS["cleric"] = [
("Hearth Domain", "Gods of home, shelter and the shared table.", [
 (3, "Hearth Domain Spells", "Always prepared. Level 3: Heroism, Sanctuary, Aid, Calm Emotions; level 5: Create Food and Water, Protection from Energy; level 7: Guardian of Faith, Aura of Life; level 9: Hallow, Greater Restoration."),
 (3, "Warm Welcome", "As a Magic action you expend a use of Channel Divinity to fill a 30-foot Emanation with comforting warmth for 1 minute. Allies in it when you use this feature gain Temporary Hit Points equal to 1d6 + your Cleric level, and allies in it have Advantage on saving throws against the Frightened condition."),
 (3, "Blessed Meal", "During a Short Rest, you can prepare a simple meal. Each creature that eats it regains an extra 1d4 Hit Points for each Hit Die it spends during that rest."),
 (6, "Shield the Flock", "When an ally within 30 feet of you takes damage, you can take a Reaction to reduce the damage by 1d8 + your Wisdom modifier. You can use this feature a number of times equal to your Wisdom modifier (minimum once), regaining all uses when you finish a Long Rest."),
 (17, "Eternal Hearth", "Allies in your Warm Welcome emanation also have Resistance to all damage, and when you use Warm Welcome you regain one expended spell slot of level 5 or lower."),
]),
("Tide Domain", "Deities of the sea, the moon's pull and the patience of water.", [
 (3, "Tide Domain Spells", "Always prepared. Level 3: Fog Cloud, Create or Destroy Water, Gust of Wind, Hold Person; level 5: Water Breathing, Sleet Storm; level 7: Control Water, Freedom of Movement; level 9: Cone of Cold, Commune with Nature."),
 (3, "Undertow", "As a Magic action you expend a use of Channel Divinity. Each creature of your choice in a 15-foot Cone makes a Strength saving throw. On a failure, a creature takes Cold damage equal to 2d8 + your Cleric level, is pulled up to 10 feet toward you and has the Prone condition. On a success, it takes half damage only."),
 (3, "Saltborn", "You gain a Swim Speed equal to your Speed and can breathe water."),
 (6, "Ebb and Flow", "When you restore Hit Points to a creature with a spell, you can also move that creature up to 10 feet (no opportunity attacks) or push one hostile creature within 5 feet of it up to 10 feet away."),
 (17, "Tidal Avatar", "As a Bonus Action you become a churning column of water for 1 minute (once per Long Rest, or by expending a level 5+ spell slot). You gain a Fly Speed of 30 feet, Resistance to Bludgeoning, Piercing and Slashing damage, and each enemy that starts its turn within 10 feet of you takes 2d8 Cold damage."),
]),
("Ash Domain", "Gods of the pyre, of endings that make way for beginnings.", [
 (3, "Ash Domain Spells", "Always prepared. Level 3: Burning Hands, False Life, Gentle Repose, Scorching Ray; level 5: Revivify, Speak with Dead; level 7: Death Ward, Fire Shield; level 9: Flame Strike, Raise Dead."),
 (3, "Rekindle", "As a Magic action you expend a use of Channel Divinity and touch a creature that has 0 Hit Points. It regains Hit Points equal to 2d8 + your Cleric level and can stand up without spending movement."),
 (3, "Pyre's Mercy", "When a creature within 30 feet of you drops to 0 Hit Points, you can take a Reaction to deal Fire damage equal to your Wisdom modifier + your Proficiency Bonus to one hostile creature within 5 feet of it."),
 (6, "Ashen Veil", "When you cast a spell with a spell slot that deals Fire damage or restores Hit Points, you can wreathe yourself in drifting ash until the start of your next turn: attack rolls against you have Disadvantage."),
 (17, "Phoenix Rite", "When you drop to 0 Hit Points and don't die outright, you can burst into flame instead: you regain Hit Points equal to half your Hit Point maximum, and each creature of your choice within 20 feet takes 6d10 Fire damage (Dexterity save for half). Once you use this feature, you can't do so again until you finish a Long Rest."),
]),
]

SUBS["druid"] = [
("Circle of the Hive", "Druids who speak for bees, wasps and every humming swarm.", [
 (3, "Hive Mind", "As a Bonus Action you can expend a use of Wild Shape to surround yourself with a swarm of insects for 10 minutes instead of transforming. Any creature of your choice that ends its turn within 5 feet of you takes Piercing damage equal to 1d6 + your Wisdom modifier, and you gain a +1 bonus to AC."),
 (3, "Pollinator", "When you cast a spell that restores Hit Points, one creature of your choice within 10 feet of a target also regains 1d4 Hit Points."),
 (6, "Stinging Cloud", "While your swarm is active, you can take a Magic action to send it in a 15-foot Cube within 30 feet. Each creature there makes a Constitution save or takes 3d6 Piercing damage and has the Poisoned condition until the end of your next turn. Your swarm then returns."),
 (10, "Royal Jelly", "Once per Long Rest, during a Short Rest, you can produce honey equal to your Wisdom modifier in doses. A creature that eats a dose as a Bonus Action regains 2d8 Hit Points and ends the Poisoned condition. The honey loses its potency after 24 hours."),
 (14, "Endless Swarm", "Your swarm's damage becomes 2d6 + your Wisdom modifier, it extends to 10 feet, and while it's active you can't be Grappled and have Resistance to Piercing damage."),
]),
("Circle of Thorns", "Guardians who grow armor of bark and bramble.", [
 (3, "Thornhide", "As a Bonus Action you can expend a use of Wild Shape to cover yourself in bark and thorns for 10 minutes. Your AC becomes 13 + your Wisdom modifier if that's higher, and when a creature within 5 feet hits you with a melee attack, it takes Piercing damage equal to your Wisdom modifier."),
 (3, "Bramble Ward", "You always have Entangle and Barkskin prepared."),
 (6, "Bramble Step", "Plant-based difficult terrain doesn't cost you extra movement, and once per turn while within 5 feet of a plant you can teleport up to 30 feet to an unoccupied space within 5 feet of another plant you can see."),
 (10, "Rootbind", "When a creature within 30 feet of you fails a saving throw against one of your spells, roots grip it: its Speed becomes 0 until the end of its next turn."),
 (14, "Verdant Rebirth", "If you drop to 0 Hit Points while Thornhide is active, you instead drop to 1 Hit Point and gain Temporary Hit Points equal to five times your Druid level. Once you use this feature, you can't do so again until you finish a Long Rest."),
]),
("Circle of Bones", "Druids of the carrion cycle: scavengers, rot and return.", [
 (3, "Grave Shape", "When you use Wild Shape, you can make your beast form skeletal. While in it, you have Resistance to Necrotic and Poison damage and your attacks can deal Necrotic damage instead of their normal type."),
 (3, "Carrion Speech", "You can cast Speak with Dead without a spell slot, targeting only beasts, once per Long Rest. You always have Speak with Dead prepared."),
 (6, "Return to the Soil", "When a creature within 30 feet of you dies, you or an ally within 30 feet of it gains Temporary Hit Points equal to your Wisdom modifier + your Druid level (once per turn)."),
 (10, "Ossuary Guardian", "As a Magic action, expend a use of Wild Shape to raise a beast skeleton (statistics of a beast of CR 2 or lower that you've seen) for 1 hour. It obeys your commands and acts on your turn. It has the Undead type and disappears at 0 Hit Points."),
 (14, "Cycle Eternal", "You no longer age, and when you would die, you can instead rise 1 minute later with 1 Hit Point and one level of Exhaustion. Once you use this benefit, you can't do so again until you finish 1d4 Long Rests."),
]),
]
