# Original subclasses, part 10: the subclasses of the Spiritbinder
# Format: class -> list of (name, tagline, [(level, feature, text), ...])
# In a feature text, [[label]] shows the label in bold.
SUBS = {}

SUBS["spiritbinder"] = [
("Bond of the Great Beast", "Your spirit grows into a hunter of legend, and it grows hungry.", [
 (3, "Mighty Spirit", "Your spirit's Hit Point maximum increases by twice your Spiritbinder level. Its Spirit Strike deals 1d10 instead of 1d6 (1d12 in Claw Form)."),
 (3, "Pack Sense", "While your spirit is within 30 feet of you, you and it have Advantage on Wisdom (Perception) checks, and neither of you can have the Surprised condition."),
 (6, "Grown Spirit", "Your spirit becomes Large. Its reach increases by 5 feet, and a creature of your size or smaller can ride it as a mount."),
 (10, "Rampage", "When your spirit reduces a creature to 0 Hit Points, it can move up to half its Speed and make one more Spirit Strike (no action required)."),
 (14, "Titan Soul", "Your spirit has Resistance to Bludgeoning, Piercing, and Slashing damage."),
]),
("Bond of the Twin Lights", "A second, smaller spirit follows you: a wisp of light that heals and guides.", [
 (3, "Wisp", "A Tiny wisp of light also follows you. It has AC 13 + your Proficiency Bonus, 1 Hit Point, a Fly Speed of 30 feet, and it can't attack. It sheds Bright Light in a 10-foot radius. It moves with your spirit on its turn. If it drops to 0 Hit Points, it returns when you finish a Short or Long Rest. When you command your spirit, the wisp can also take the Help action."),
 (3, "Carried Light", "When you use the Mend gift, it can target a creature within 30 feet of your wisp, and it restores extra Hit Points equal to your Charisma modifier."),
 (6, "Guiding Glow", "You and your allies within 10 feet of the wisp add 1 to their saving throws."),
 (10, "Soul Shelter", "When an ally within 30 feet of your wisp drops to 0 Hit Points, you can take a Reaction and spend 2 Bond Points to make it drop to 1 Hit Point instead."),
 (14, "Thousand Wisps", "As a Bonus Action, you can spend 3 Bond Points to scatter your wisp into a swarm of lights. Each ally of your choice within 30 feet of the wisp regains 2d8 + your Charisma modifier Hit Points and can end one of these conditions on itself: Blinded, Charmed, Frightened, Poisoned."),
]),
("Bond of the Spirit Mantle", "You don't fight beside your spirit. You wear it.", [
 (3, "Wear the Spirit", "As a Bonus Action, your spirit can wrap itself around you as a mantle while it is within 5 feet of you, or step out of you again into an unoccupied space within 5 feet of you. While you wear it, it doesn't take turns. Your AC equals the spirit's AC if that is higher than your own. When you take the Attack action, you can make Spirit Strikes with the spirit's attack bonus and damage in place of your weapon attacks, up to the number in the Spirit Attacks column; these are melee attacks with a reach of 5 feet. When you take damage, the spirit takes half of it (round up), and you take the rest. If the spirit drops to 0 Hit Points, it stops being worn and returns to your soul."),
 (3, "Mantle Training", "You gain training with Shields and proficiency with Martial weapons."),
 (6, "Mantle Step", "While you wear your spirit, your Speed increases by 10 feet, and once on each of your turns you can use the Pounce gift without spending a Bond Point."),
 (10, "Lashing Shroud", "While you wear your spirit, the reach of your Spirit Strikes is 10 feet, and when a creature you can see enters your reach, you can take a Reaction to make one Spirit Strike against it."),
 (14, "Spirit Fury", "While you wear your spirit, your Spirit Strikes score a Critical Hit on a roll of 19 or 20 on the d20, and once on each of your turns you can use the Unsettle gift without spending a Bond Point."),
]),
]
