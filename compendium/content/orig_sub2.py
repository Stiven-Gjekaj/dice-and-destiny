# Original subclasses, part 2: Fighter, Monk, Paladin, Ranger
SUBS = {}

SUBS["fighter"] = [
("Emberblade", "Warriors who conjure blades of fire from a bonded hilt and weave flame into swordplay.", [
 (3, "Spellcasting", "You learn to cast spells from the Wizard list, using Intelligence as your spellcasting ability and your weapon or an obsidian hilt as a Spellcasting Focus. Cantrips: 2 at level 3, 3 at level 10. Prepared spells by Fighter level (level: spells): 3: 3, 4–6: 4, 7: 5, 8: 6, 9: 6, 10: 7, 11–12: 8, 13: 9, 14–15: 10, 16: 11, 19: 12, 20: 13. Spell slots by Fighter level (level: slots): 3: two 1st; 4–6: three 1st; 7–9: four 1st, two 2nd; 10–12: four 1st, three 2nd; 13–15: +two 3rd; 16–18: +three 3rd; 19–20: +one 4th. Whenever you finish a Long Rest you can replace one prepared spell."),
 (3, "Obsidian Hilt", "You bond with a weapon hilt over a 1-hour ritual during a Short or Long Rest. As a Bonus Action, flame erupts from it as a blade: it counts as a longsword you're proficient with that deals Fire damage instead of Slashing and sheds Bright Light in a 10-foot radius. You can't be disarmed of the hilt unless you're Incapacitated, and you can call it to your hand from up to 1 mile as a Bonus Action."),
 (7, "Kindled Guard", "When a creature within 5 feet of you hits you with an attack, you can take a Reaction to deal Fire damage to it equal to 1d8 + your Intelligence modifier. You also have Resistance to Fire damage."),
 (10, "Flame Lash", "When you take the Attack action, you can lengthen your flame blade: until the end of the turn your attacks with it have a reach of 15 feet. You can use this feature a number of times equal to your Intelligence modifier (minimum once), regaining all uses on a Long Rest."),
 (15, "Phoenix Step", "When you cast a spell using a spell slot, you can teleport up to 20 feet to an unoccupied space you can see. Each creature of your choice within 5 feet of the space you left takes Fire damage equal to your Intelligence modifier."),
 (18, "Heart of the Forge", "You have Immunity to Fire damage, your Fire damage ignores Resistance, and when you roll Initiative you regain one expended spell slot of level 2 or lower."),
]),
("Warden of the Line", "Shield-bearers who make themselves the wall their friends stand behind.", [
 (3, "Hold the Line", "When a creature provokes an Opportunity Attack from you and you hit, its Speed becomes 0 for the rest of the turn. Creatures provoke Opportunity Attacks from you when they move 5 feet or more while within your reach, even if they don't leave it."),
 (3, "Interpose", "When a creature you can see attacks an ally within 5 feet of you, you can take a Reaction to swap places with the ally; you become the target of the attack."),
 (7, "Unyielding", "You have Advantage on saving throws against being pushed, pulled or knocked Prone, and while you hold a Shield, allies within 5 feet of you gain a +1 bonus to AC."),
 (10, "Rallying Stand", "When you use Second Wind, each ally within 10 feet of you gains Temporary Hit Points equal to your Fighter level."),
 (15, "Immovable Object", "When you take the Dodge action, you can also make one weapon attack as part of it, and creatures within 5 feet of you have Disadvantage on attack rolls against targets other than you until the start of your next turn."),
 (18, "Last Bastion", "When an ally within 30 feet would drop to 0 Hit Points, you can take a Reaction to move up to your Speed to a space within 5 feet of it and take the damage instead. If this drops you to 0 Hit Points, you drop to 1 instead. Once per Long Rest."),
]),
("Gladiator", "Fighters who learned their craft before a roaring crowd.", [
 (3, "Crowd Pleaser", "When you score a Critical Hit or reduce a creature to 0 Hit Points, you gain Heroic Inspiration, and each ally within 30 feet who can see you gains Temporary Hit Points equal to your Proficiency Bonus."),
 (3, "Showboat", "You gain proficiency in Performance. As a Bonus Action you can taunt a creature within 30 feet that can hear you: it makes a Wisdom saving throw (DC 8 + your Strength or Charisma modifier + your Proficiency Bonus) or has Disadvantage on attack rolls against creatures other than you until the end of its next turn."),
 (7, "Arena Footwork", "Your Speed increases by 10 feet, and when a creature misses you with a melee attack you can move up to half your Speed as a Reaction without provoking Opportunity Attacks."),
 (10, "Thumbs Down", "When you hit a creature that is Bloodied, you can deal extra damage equal to your Fighter level. Once per turn; uses equal to your Proficiency Bonus per Long Rest."),
 (15, "Champion of the Pit", "When you use Action Surge, you also gain Advantage on all attack rolls until the end of the turn."),
 (18, "Undying Legend", "When you drop to 0 Hit Points and don't die, you can stand back up with Hit Points equal to half your maximum and immediately use Showboat for free. Once per Long Rest."),
]),
]

SUBS["monk"] = [
("Warrior of the Iron Bell", "Monks whose strikes ring like temple bells.", [
 (3, "Ringing Blow", "When you hit a creature with an Unarmed Strike, you can spend 1 Focus Point to deal extra Thunder damage equal to one roll of your Martial Arts die. The target has the Deafened condition and can't take Reactions until the start of your next turn."),
 (3, "Bell Stance", "While you are not wearing armor or wielding a Shield, you have Resistance to Thunder damage and Advantage on saving throws against the Deafened and Stunned conditions."),
 (6, "Resonant Body", "When you take Bludgeoning or Thunder damage from a creature within 5 feet, you can take a Reaction to deal Thunder damage to it equal to your Martial Arts die + your Wisdom modifier."),
 (11, "Toll for the Fallen", "As a Magic action you spend 3 Focus Points to ring out a toll: each creature of your choice within 20 feet makes a Constitution save or takes 6d8 Thunder damage and has the Stunned condition until the end of your next turn (half damage and no Stun on a success)."),
 (17, "The Great Bell", "Your Ringing Blow no longer costs Focus Points once per turn, and creatures Deafened by it have Disadvantage on saving throws against your Stunning Strike."),
]),
("Warrior of the Paper Crane", "Light-footed monks who fold their bodies like paper and ride the wind.", [
 (3, "Folded Steps", "When you use Step of the Wind, you can glide: you don't fall while moving that turn and take no falling damage. Your jump distance is tripled instead of doubled."),
 (3, "Paper Cuts", "Your Unarmed Strikes can deal Slashing damage. Once per turn when you hit, the target loses 1d4 Hit Points at the start of its next turn from fine bleeding cuts."),
 (6, "Crane Form", "When you use Step of the Wind, you gain a Fly Speed equal to your Speed until the end of the turn."),
 (11, "Thousand Cranes", "As a Magic action you spend 3 Focus Points to release a storm of paper birds in a 20-foot Sphere within 60 feet for 1 minute (Concentration). Creatures of your choice that start their turn there take 4d6 Slashing damage, and the area is Heavily Obscured to everyone but you."),
 (17, "Unfolding", "You have Resistance to Bludgeoning, Piercing and Slashing damage while your Fly Speed from Crane Form is active, and Crane Form lasts until the end of your next turn."),
]),
("Warrior of the Mirror Lake", "Monks who still themselves until every attack returns to its sender.", [
 (3, "Still Water", "Your Deflect Attacks can reduce damage from spell attacks. When you reduce an attack's damage with it, your next attack roll before the end of your next turn has Advantage."),
 (3, "Reflection", "As a Bonus Action you spend 1 Focus Point to create an illusory double in your space until the start of your next turn. The first attack made against you during that time has Disadvantage."),
 (6, "Mirror Guard", "When you succeed on a saving throw against a spell that deals damage, you take no damage, and you can take a Reaction to deal the caster half the damage the spell would have dealt you (no save)."),
 (11, "Clear Surface", "You can't be Charmed or Frightened, and you have Advantage on Wisdom (Insight) checks."),
 (17, "Shattered Moon", "As a Magic action you spend 4 Focus Points to split into four mirror images for 1 minute. Attack rolls against you have Disadvantage; each time an attack misses you, one image shatters, dealing 2d10 Force damage to the attacker. The effect ends when all images are gone."),
]),
]

SUBS["paladin"] = [
("Oath of the Lantern", "Paladins sworn to guide the lost and light the dark places.", [
 (3, "Lantern Oath Spells", "Always prepared. Level 3: Faerie Fire, Guiding Bolt; level 5: See Invisibility, Find Traps; level 9: Daylight, Beacon of Hope; level 13: Guardian of Faith, Locate Creature; level 17: Commune, Flame Strike."),
 (3, "Beacon", "As a Magic action you expend a use of Channel Divinity to make your holy symbol blaze for 1 minute: Bright Light in a 30-foot radius. Hostile creatures in the light can't benefit from the Invisible condition or hide, and allies in it have Advantage on saving throws against the Frightened condition."),
 (3, "Wayfinder", "You and companions traveling with you can't become lost except by magical means."),
 (7, "Aura of the Way", "You and allies in your Aura of Protection gain +10 feet of Speed and Advantage on saving throws against being Charmed."),
 (15, "Unquenchable", "You can't be Blinded, and when you use Divine Smite the target also has the Blinded condition until the start of your next turn unless it succeeds on a Constitution save."),
 (20, "Dawnbringer", "As a Bonus Action you become a pillar of dawn for 10 minutes (once per Long Rest, or by expending a level 5 spell slot): your aura sheds Bright Light 60 feet, enemies in your aura take 10 Radiant damage at the start of their turns, and allies in it regain 10 Hit Points at the start of theirs if they have at least 1 Hit Point."),
]),
("Oath of the Unbroken Chain", "Paladins who hold the wicked to account for every promise broken.", [
 (3, "Unbroken Chain Spells", "Always prepared. Level 3: Command, Hunter's Mark; level 5: Hold Person, Zone of Truth; level 9: Bestow Curse, Counterspell; level 13: Banishment, Compulsion; level 17: Geas, Hold Monster."),
 (3, "Bind Oath", "As a Magic action you expend a use of Channel Divinity and choose a creature within 30 feet. It makes a Wisdom save or is spiritually chained to you for 1 minute: it can't willingly move more than 30 feet away from you and has Disadvantage on attack rolls against creatures other than you."),
 (3, "Truthsense", "You always know if you hear a lie, though not what the truth is."),
 (7, "Aura of Accountability", "When an enemy in your Aura of Protection hits one of your allies, the enemy takes Radiant damage equal to your Charisma modifier."),
 (15, "Unbreakable Word", "You can't be Charmed, and creatures under your Bind Oath also take 2d8 Radiant damage whenever they end a turn more than 30 feet from you."),
 (20, "Judge Absolute", "For 1 minute (once per Long Rest, or a level 5 spell slot), your weapon attacks against creatures under Bind Oath score Critical Hits on 18–20, and such creatures can't regain Hit Points."),
]),
("Oath of the Shield-Sibling", "Paladins who vow that no companion will fall while they stand.", [
 (3, "Shield-Sibling Spells", "Always prepared. Level 3: Shield of Faith, Sanctuary; level 5: Aid, Warding Bond; level 9: Protection from Energy, Revivify; level 13: Death Ward, Aura of Life; level 17: Mass Cure Wounds, Greater Restoration."),
 (3, "Take the Blow", "As a Bonus Action you expend a use of Channel Divinity. For 1 minute, when an ally within 10 feet of you is hit by an attack, you can take a Reaction to become the target instead; you gain Resistance to that attack's damage."),
 (3, "Sibling's Vow", "When you use Lay On Hands on another creature, you also gain Temporary Hit Points equal to the amount restored."),
 (7, "Aura of Shared Burden", "When an ally in your aura takes damage, you can choose to take half of it instead (no action required). Damage you take this way can't be reduced."),
 (15, "Undying Devotion", "When an ally in your aura drops to 0 Hit Points, you can expend 5 points from Lay On Hands to restore 5 × your Charisma modifier Hit Points to it instead, no matter the distance in your aura."),
 (20, "Living Rampart", "For 1 minute (once per Long Rest, or a level 5 spell slot), allies in your aura have Resistance to all damage and can't be reduced below 1 Hit Point while you are conscious."),
]),
]

SUBS["ranger"] = [
("Spirit Tracker", "Rangers who hunt the restless dead and things from beyond.", [
 (3, "Spirit Tracker Spells", "Always prepared. Level 3: Protection from Evil and Good; level 5: See Invisibility; level 9: Speak with Dead; level 13: Banishment; level 17: Dispel Evil and Good."),
 (3, "Haunt Sense", "As a Bonus Action you sense the location of any Undead, Fiend or Celestial within 60 feet for 1 minute. Your Hunter's Mark deals Radiant damage instead of Force when you choose."),
 (3, "Spectral Arrows", "Your weapon attacks can hit creatures on the Ethereal Plane and ignore Resistance to nonmagical damage."),
 (7, "Veil Step", "As a Bonus Action you step partly into the Ethereal Plane until the start of your next turn: you can move through creatures and objects as difficult terrain and attacks against you have Disadvantage. Uses equal to your Wisdom modifier per Long Rest."),
 (11, "Exorcist's Shot", "When you hit a creature marked by your Hunter's Mark, you can force it to make a Charisma save (your spell save DC). On a failure it takes an extra 4d8 Radiant damage, and if it is possessing a creature, it is expelled. Once per turn."),
 (15, "Last Rites", "Undead you reduce to 0 Hit Points can't rise again by any means short of a Wish spell, and you have Advantage on saving throws against effects created by Undead and Fiends."),
]),
("Trapper", "Patient hunters who make the land itself fight for them.", [
 (3, "Snare Kit", "As a Bonus Action you set a hidden snare in an unoccupied 5-foot space within 5 feet. The first creature to enter it makes a Dexterity save (your spell save DC) or has the Restrained condition (escape DC equals your spell save DC). You can have snares up to your Wisdom modifier at once."),
 (3, "Lay of the Land", "You know the location of difficult terrain, cover and hiding places within 60 feet, and you have Advantage on checks to find or disarm traps."),
 (7, "Tripwire Sense", "You can't be surprised, and when a creature becomes Restrained by one of your snares you can make a weapon attack against it as a Reaction."),
 (11, "Killing Field", "Your attacks have Advantage against Restrained creatures, and when you hit one, it takes an extra 2d8 damage of the weapon's type."),
 (15, "Master Trapper", "Your snares can now be set at range (60 feet), are invisible, and a creature caught in one also takes 4d8 Piercing damage."),
]),
("Deep Roads Wayfarer", "Rangers of caves, tunnels and the lightless world below.", [
 (3, "Lightless Sight", "You gain Darkvision 60 feet, or if you already have it, its range increases by 60 feet. You can see through magical Darkness to a range of 10 feet."),
 (3, "Tunnel Fighter", "While you are within 5 feet of a wall or in a space no wider than 10 feet, you have Advantage on Opportunity Attacks and creatures have Disadvantage on Opportunity Attacks against you."),
 (7, "Stone Whisper", "You can cast Stone Shape and Meld into Stone without expending a spell slot once each per Long Rest, and you always have them prepared."),
 (11, "Burrow Strike", "You gain a Burrow Speed of 10 feet through loose earth. When you emerge from the ground and hit a creature on the same turn, the hit deals an extra 3d8 damage and the target has the Prone condition."),
 (15, "Lord Under Stone", "Once per Long Rest as a Magic action, you bring down the ceiling or cliff above a 20-foot-radius area within 120 feet: each creature there makes a Dexterity save or takes 8d10 Bludgeoning damage and is Restrained by rubble (half damage, not Restrained, on a success)."),
]),
]
