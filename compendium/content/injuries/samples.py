"""The first injuries of the d20 Injury table."""

INJURIES = [
    dict(
        name="Ringing Ears", roll=1, severity="Minor",
        effect="You have Disadvantage on Wisdom (Perception) checks that rely on hearing.",
        treatment="It heals when you finish a Long Rest.",
        scar=("Battle-Deaf", "You have Advantage on saving throws against the Deafened condition."),
    ),
    dict(
        name="Twisted Ankle", roll=4, severity="Minor",
        effect="Your Speed decreases by 10 feet.",
        treatment="It heals when you finish a Long Rest after someone tends it: one use of a Healer's Kit, or a successful DC 10 Wisdom (Medicine) check.",
        scar=("Steady Feet", "You have Advantage on saving throws to avoid the Prone condition."),
    ),
    dict(
        name="Cut Above the Eye", roll=8, severity="Minor",
        effect="Blood runs into your eye. You have Disadvantage on the first attack roll you make in each combat.",
        treatment="It heals when you finish a Long Rest after someone tends it: one use of a Healer's Kit, or a successful DC 10 Wisdom (Medicine) check.",
        scar=("Dueling Scar", "You have Advantage on Charisma (Intimidation) checks against creatures that can see your face."),
    ),
    dict(
        name="Cracked Ribs", roll=11, severity="Serious",
        effect="Each breath hurts. You have Disadvantage on Constitution saving throws to keep Concentration, and you can't take the Dash action.",
        treatment="It heals after three Long Rests, each one after someone tends it (a use of a Healer's Kit, or a successful DC 15 Wisdom (Medicine) check). A Lesser Restoration spell or any stronger healing magic ends it at once.",
        scar=("Knit Bone", "You have a +1 bonus to Constitution saving throws to keep Concentration."),
    ),
    dict(
        name="Deep Gash", roll=13, severity="Serious",
        effect="The wound keeps opening. When you spend a Hit Point Die, you regain 1 fewer Hit Point for each die (minimum of 1 for each die).",
        treatment="It heals after three Long Rests, each one after someone tends it (a use of a Healer's Kit, or a successful DC 15 Wisdom (Medicine) check). A Lesser Restoration spell or any stronger healing magic ends it at once.",
        scar=("Old Wound", "Once per Long Rest, when you spend Hit Point Dice, you regain extra Hit Points equal to your Proficiency Bonus."),
    ),
    dict(
        name="Broken Arm", roll=16, severity="Serious",
        effect="Choose an arm. You can't use it to hold a Shield, to wield a weapon, or to cast a spell with a Somatic component, and you have Disadvantage on Strength checks.",
        treatment="It heals after seven Long Rests with the arm in a sling, after someone sets the bone (a successful DC 15 Wisdom (Medicine) check). A Lesser Restoration spell or any stronger healing magic ends it at once.",
        scar=("Set Bone", "You have Advantage on ability checks to keep hold of an object or to keep a creature Grappled."),
    ),
    dict(
        name="Shattered Knee", roll=18, severity="Lasting",
        effect="Your Speed decreases by 10 feet, and you can't take the Dash action.",
        treatment="It heals after 30 days of rest (a downtime activity), with a successful DC 15 Wisdom (Medicine) check by a healer at the end. A Greater Restoration spell, a Heal spell, or a Regenerate spell ends it at once.",
        scar=("Iron Knee", "You have Advantage on saving throws against the Restrained condition."),
    ),
    dict(
        name="Lost Eye", roll=20, severity="Lasting",
        effect="The player chooses: the eye is lost for good, or it is a deep wound that can heal. Either way, you have Disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls against targets more than 30 feet away.",
        treatment="A deep wound heals after 30 days of rest (a downtime activity), with a successful DC 15 Wisdom (Medicine) check by a healer at the end. A lost eye returns only with a Regenerate spell. A Greater Restoration spell or a Heal spell ends the deep wound at once. If the player chose to lose the eye, the character gains the scar when they finish their next Long Rest, and the effect stays until a Regenerate spell.",
        scar=("One-Eyed Glare", "You have Advantage on Charisma (Intimidation) checks, and you have Advantage on saving throws against the Blinded condition."),
    ),
]
