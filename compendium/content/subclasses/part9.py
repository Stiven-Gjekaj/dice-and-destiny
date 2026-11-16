# Original subclasses, part 9: the subclasses of the Shaper
# Format: class -> list of (name, tagline, [(level, feature, text), ...])
# In a feature text, [[label]] shows the label in bold.
SUBS = {}

SUBS["shaper"] = [
("Wallwarden", "Shapers who raise their element as a wall between their friends and harm.", [
 (3, "Bulwark Training", "You gain training with Medium armor and Shields."),
 (3, "Shared Ward", "When a creature you can see within 30 feet of you is hit by an attack roll, you can use your Ward Surge on that creature instead of on yourself. The +5 bonus to AC goes to that creature."),
 (6, "Shaped Cover", "As a Bonus Action, you can take 1 Strain to raise a pillar of your element, 5 feet wide and 10 feet tall, in an unoccupied space you can see within 30 feet of you. It lasts for 1 minute or until it is destroyed. It gives Total Cover, has AC 15 and Hit Points equal to 10 + your Shaper level, and has Immunity to your element damage and to Poison and Psychic damage."),
 (10, "Standing Wall", "Once per Long Rest, you can use your Wall Surge without taking Strain."),
 (14, "Bastion", "When a creature you can see within 30 feet of you takes damage, you can take a Reaction to reduce the damage by 3d10 + your Wisdom modifier. You can use this feature a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."),
]),
("Bladeshaper", "Shapers who hold their element in the shape of a blade and fight up close.", [
 (3, "Blade Training", "You gain training with Medium armor and Shields."),
 (3, "Element Blade", "As a Bonus Action, you can form a blade of your element in your hand. It lasts until you dismiss it (no action required) or it leaves your hand. It is a Simple Melee weapon with the Finesse and Light properties for you. You use your Wisdom modifier for its attack and damage rolls, and on a hit it deals 1d8 + your Wisdom modifier element damage. When you take the Magic action for your Elemental Bolt, you can replace any number of the Bolts with attacks with your Element Blade against creatures within 5 feet of you. The rider of your element works with the blade as it does with a Bolt."),
 (6, "Surge Strike", "When you hit a creature with your Element Blade, you can take 1 Strain to deal an extra 2d8 element damage to it."),
 (10, "Blade Dance", "When you use a Surge as a Magic action, you can make one attack with your Element Blade as a Bonus Action."),
 (14, "Edge of the World", "Your attack rolls with the Element Blade score a Critical Hit on a roll of 19 or 20 on the d20. When you use Surge Strike, you can take up to 3 Strain, and the strike deals an extra 2d8 element damage for each Strain."),
]),
("Weatherworker", "Shapers who stop bending one flame or one stone, and start bending the sky.", [
 (3, "Read the Sky", "You always know what the weather will be in your area for the next 24 hours, unless magic changes it. As a Magic action, you can take 2 Strain to change the weather within 1 mile of you over 10 minutes: bring rain, fog, snow, or a strong wind, or clear the sky. The change lasts for 8 hours."),
 (3, "Squall", "You learn a Tier 1 Surge. [[Squall:]] Each creature of your choice in a 15-foot-radius Sphere centered on a point within 60 feet of you makes a Strength saving throw. On a failed save, it is pushed up to 15 feet straight away from the center of the Sphere. Until the start of your next turn, ranged attack rolls that pass through the area have Disadvantage."),
 (6, "Pressure Front", "When a creature fails its saving throw against one of your Surges that affects an area, you can push it up to 10 feet in a direction of your choice. Difficult Terrain that your Surges make doesn't affect your allies."),
 (10, "Season in a Circle", "When you finish a Long Rest, choose one season for a 30-foot Emanation originating from you. It lasts until you choose again. [[Rain:]] You and your allies in the Emanation have Resistance to Fire damage. [[Snow:]] An enemy that starts its turn in the Emanation has its Speed reduced by 10 feet until the start of its next turn. [[Wind:]] The first ranged attack roll against each of you and your allies in the Emanation on each turn has Disadvantage."),
 (14, "Eye of the Hurricane", "As a Bonus Action, you can take 3 Strain to call a hurricane in a 30-foot Emanation originating from you for 1 minute (Concentration). The area is Difficult Terrain for your enemies, and ranged attack rolls into or out of it have Disadvantage. At the start of each of your turns, choose one creature in the area. It makes a Strength saving throw against your shaping save DC. On a failed save, it takes 3d8 Bludgeoning damage and is pulled up to 15 feet toward you, or pushed up to 15 feet away from you (your choice)."),
]),
]
