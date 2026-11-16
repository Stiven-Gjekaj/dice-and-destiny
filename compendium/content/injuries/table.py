"""The other injuries of the d20 Injury table, so that each d20 result has its own injury."""

MINOR_CARE = "It heals when you finish a Long Rest after someone tends it: one use of a Healer's Kit, or a successful DC 10 Wisdom (Medicine) check."
SERIOUS_CARE = ("It heals after three Long Rests, each one after someone tends it (a use of a Healer's Kit, or a successful DC 15 "
                "Wisdom (Medicine) check). A Lesser Restoration spell or any stronger healing magic ends it at once.")
LASTING_CARE = ("It heals after 30 days of rest (a downtime activity), with a successful DC 15 Wisdom (Medicine) check by a healer at "
                "the end. A Greater Restoration spell, a Heal spell, or a Regenerate spell ends it at once.")

INJURIES = [
    dict(
        name="Split Lip", roll=2, severity="Minor",
        effect="Talking hurts. You have Disadvantage on Charisma (Performance) and Charisma (Persuasion) checks.",
        treatment="It heals when you finish a Long Rest.",
        scar=("Crooked Smile", "You have Advantage on Charisma (Deception) checks to hide what you feel."),
    ),
    dict(
        name="Bruised Knuckles", roll=3, severity="Minor",
        effect="You have Disadvantage on ability checks that use tools.",
        treatment="It heals when you finish a Long Rest.",
        scar=("Calloused Knuckles", "Your Unarmed Strikes deal 1 extra damage."),
    ),
    dict(
        name="Winded", roll=5, severity="Minor",
        effect="You can't take the Dash action on your first turn of each combat.",
        treatment="It heals when you finish a Long Rest.",
        scar=("Deep Lungs", "You can hold your breath for twice as long as normal."),
    ),
    dict(
        name="Pulled Shoulder", roll=6, severity="Minor",
        effect="You have Disadvantage on Strength (Athletics) checks, and you can't throw a weapon farther than its normal range.",
        treatment=MINOR_CARE,
        scar=("Strong Shoulder", "The normal range of your thrown weapons increases by 10 feet."),
    ),
    dict(
        name="Black Eye", roll=7, severity="Minor",
        effect="You have Disadvantage on Wisdom (Perception) checks that rely on sight.",
        treatment="It heals when you finish a Long Rest.",
        scar=("Seen Worse", "You have Advantage on Wisdom (Insight) checks to tell whether a creature is about to attack."),
    ),
    dict(
        name="Gashed Leg", roll=9, severity="Minor",
        effect="Your Speed decreases by 5 feet, and you have Disadvantage on Dexterity (Acrobatics) checks.",
        treatment=MINOR_CARE,
        scar=("Hard Calves", "Your long jump distance increases by 5 feet, and your high jump distance increases by 1 foot."),
    ),
    dict(
        name="Concussion", roll=10, severity="Minor",
        effect="Your head spins. You have Disadvantage on Intelligence checks.",
        treatment=MINOR_CARE,
        scar=("Thick Skull", "You have Advantage on saving throws against the Stunned condition."),
    ),
    dict(
        name="Torn Muscle", roll=12, severity="Serious",
        effect="You have Disadvantage on Strength checks and Strength saving throws.",
        treatment=SERIOUS_CARE,
        scar=("Knotted Muscle", "You have Advantage on Strength checks to escape a grapple."),
    ),
    dict(
        name="Burned Hands", roll=14, severity="Serious",
        effect="You have Disadvantage on attack rolls with weapons and on ability checks that use tools.",
        treatment=SERIOUS_CARE,
        scar=("Fire-Kissed", "When you take Fire damage, reduce it by an amount equal to your Proficiency Bonus."),
    ),
    dict(
        name="Infected Wound", roll=15, severity="Serious",
        effect="You don't regain Hit Points when you spend Hit Point Dice.",
        treatment=SERIOUS_CARE,
        scar=("Hardy Blood", "You have Advantage on saving throws against diseases."),
    ),
    dict(
        name="Dislocated Hip", roll=17, severity="Serious",
        effect="Your Speed is halved.",
        treatment=SERIOUS_CARE,
        scar=("Loose Joints", "You have Advantage on Dexterity (Acrobatics) checks to escape a grapple."),
    ),
    dict(
        name="Crushed Hand", roll=19, severity="Lasting",
        effect="Choose a hand. The player chooses: the fingers are lost for good, or it is a deep wound that can heal. Either way, you have Disadvantage on attack rolls with a weapon held in that hand, and you can't use tools with it.",
        treatment=LASTING_CARE + " Lost fingers return only with a Regenerate spell. If the player chose to lose the fingers, the character gains the scar when they finish their next Long Rest, and the effect stays until a Regenerate spell.",
        scar=("Hand of Iron", "Your Unarmed Strikes with that hand deal 1d6 Bludgeoning damage instead of their normal damage."),
    ),
]
