# Original subclasses, part 11: the subclasses of the Apothecary
# Format: class -> list of (name, tagline, [(level, feature, text), ...])
# In a feature text, [[label]] shows the label in bold.
SUBS = {}

SUBS["apothecary"] = [
("Field Surgeon", "Apothecaries who work where the wounded fall, with steady hands and no time to waste.", [
 (3, "Triage", "When you stabilize a creature as a Bonus Action, it also regains Hit Points equal to one roll of your Brew Die + your Intelligence modifier."),
 (3, "Steady Hands", "When you feed a Healing Tonic to another creature, it regains extra Hit Points equal to one roll of your Brew Die."),
 (6, "Double Dose", "When you feed a Healing Tonic to a creature, a second creature of your choice within 5 feet of you also regains half as many Hit Points (round down)."),
 (10, "Stitch in Time", "When a creature within 5 feet of you drops to 0 Hit Points, you can take a Reaction to feed it a Healing Tonic."),
 (14, "Miracle Worker", "Your Revival Draught costs 1 Reagent instead of 2, and herbs worth 100 GP instead of 300 GP. Once per Long Rest, you can prepare a Revival Draught with no Reagent and no herbs."),
]),
("Grenadier", "Apothecaries who measure their work by the size of the crater.", [
 (3, "Bandolier", "When you prepare concoctions, you can prepare a number of extra bombs equal to your Intelligence modifier (minimum of one). These extra concoctions must be Fire Bombs or Smoke Bombs."),
 (3, "Careful Throw", "When you throw a bomb, you can choose a number of creatures up to your Intelligence modifier (minimum of one). They automatically succeed on their saving throws against it and take no damage from it."),
 (6, "Sticky Mix", "A creature that fails its saving throw against your Fire Bomb has its Speed halved until the end of its next turn."),
 (10, "Cluster Charge", "When you throw a bomb, you can throw a second bomb at the same time at a different point within range. Each creature makes only one saving throw if it is in both areas."),
 (14, "Grand Detonation", "Once per Long Rest, you can combine three bombs into one great bomb and throw it as an action. Each creature in a 30-foot-radius Sphere centered on the point makes a Dexterity saving throw, taking damage equal to two rolls of your Potency dice + your Intelligence modifier on a failed save, and having the Prone condition, or half as much damage only on a successful one."),
]),
("Hexbrewer", "Apothecaries who brew misfortune: slow poisons, bitter fumes, and draughts that make strong things weak.", [
 (3, "Bitter Vial", "You learn a new concoction. [[Bitter Vial:]] You throw it at a creature within 30 feet of you (the Utilize action, or a Bonus Action with Quick Hands). The creature makes a Constitution saving throw against your Apothecary save DC. On a failed save, it subtracts one roll of your Brew Die from its attack rolls and saving throws until the end of its next turn."),
 (3, "Envenom", "As a Bonus Action, you can coat a weapon or up to 10 pieces of ammunition with poison from a Bitter Vial or a Fire Bomb you made, instead of throwing it. For 1 minute, a creature hit by the weapon or the ammunition takes an extra 1d4 Poison damage (1d6 at Apothecary level 10)."),
 (6, "Lingering Fumes", "When you throw a Fire Bomb, its area fills with fumes until the end of your next turn. A creature that enters the area or starts its turn there makes a Constitution saving throw against your Apothecary save DC or has the Poisoned condition until the end of its next turn."),
 (10, "Toxic Mastery", "Your Poison damage ignores Resistance to Poison damage. Your Bitter Vial affects a creature even if it has Immunity to Poison damage or to the Poisoned condition."),
 (14, "Witch's Draught", "Once per Long Rest, you can prepare a Witch's Draught. You throw it at a creature within 30 feet of you as an action. The creature makes a Constitution saving throw against your Apothecary save DC. On a failed save, it has the Poisoned and Incapacitated conditions for 1 minute. It repeats the save at the end of each of its turns, ending the effect on itself on a success."),
]),
]
