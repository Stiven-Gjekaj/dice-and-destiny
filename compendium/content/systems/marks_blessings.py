"""The seven Blessings: one virtue for each Sin. They print in the Player's Compendium."""

_ZEAL = "Even a virtue can own you. "

MARKS = [
    dict(
        name="Blessing of Humility", kind="Blessing", hidden=False,
        summary="You don't need the credit. Others shine brighter with you beside them, and they rarely notice why.",
        benefit="You can take the Help action as a Bonus Action.",
        cost="You can't take credit for a deed. You have Disadvantage on Charisma (Intimidation) checks, and on checks to impress someone with your name or your deeds.",
        grows="When you let someone else take the credit, the reward, or the glory for something that you did, and it costs you something real.",
        thresholds=[(2, "When you take the Help action to aid an attack, the attack also deals extra damage equal to your Proficiency Bonus if it hits."),
                    (4, "Creatures that aren't hostile to you forget your face after a day, unless you tell them your name.")],
        give_in="When you take the Help action, the ally also adds your Proficiency Bonus to the d20 Test. " + _ZEAL +
                "[[Key moments:]] when you are offered praise, a title, or a reward, the GM steers you to give it away.",
        scar="You stand in the background easily. You have Advantage on Dexterity (Stealth) checks to go unnoticed in a crowd.",
        ends="Accept a great honor in public, for a deed that was truly yours.",
        ends_after="Accept a great honor in public, and keep it for a year without giving it away.",
        secret="", blocks_bonds=False,
    ),
    dict(
        name="Blessing of Charity", kind="Blessing", hidden=False,
        summary="What you have is not only yours. When you give, something gives back.",
        benefit="Once each Long Rest, you can touch a creature as a Bonus Action and spend Hit Point Dice up to your Proficiency Bonus. "
                "Roll them: the creature regains that many Hit Points.",
        cost="At the end of each Long Rest in a settlement, you give away a tenth of your coins to someone who needs them more than you.",
        grows="When you give away something of real value to someone who needs it, and nobody pays you back.",
        thresholds=[(2, "You can use the benefit twice each Long Rest. You give away a fifth of your coins, not a tenth."),
                    (4, "When you use the benefit, the creature also ends one of these conditions on itself: Blinded, Deafened, Poisoned.")],
        give_in="You can use the benefit a number of times equal to your Proficiency Bonus each Long Rest, and you can use it on a creature within 30 feet. " + _ZEAL +
                "[[Key moments:]] when someone asks you for help or for an item that you own, the GM steers your answer.",
        scar="The poor know your face. In any settlement, you can find a free meal and a safe place to sleep for you and up to four friends.",
        ends="Refuse to give, once, when the giving would hurt someone you love.",
        ends_after="Take back something that you gave, and use it to save the life of someone you love.",
        secret="", blocks_bonds=False,
    ),
    dict(
        name="Blessing of Patience", kind="Blessing", hidden=False,
        summary="The right moment always comes. You have learned to wait for it.",
        benefit="When you take the Ready action, the readied action has Advantage on its d20 Test. If it is an attack, it deals extra damage equal to your Proficiency Bonus if it hits.",
        cost="You never strike first. In the first round of a fight, you can't attack a creature that hasn't attacked or harmed you or your allies.",
        grows="When you keep your temper, and wait, at a moment when anger or haste would have been easier.",
        thresholds=[(2, "You can take the Ready action as a Bonus Action. You can't take the Dash action in the first round of a fight."),
                    (4, "You have Advantage on saving throws to avoid or end the Charmed and Frightened conditions.")],
        give_in="Your readied attacks deal extra damage equal to twice your Proficiency Bonus, and they score a Critical Hit on a roll of 19 or 20. " + _ZEAL +
                "[[Key moments:]] when your friends want to act now, the GM can steer you to tell them to wait.",
        scar="You don't startle. You don't have Disadvantage on Initiative rolls when you are surprised.",
        ends="Strike first, in anger, for a cause that you know is right.",
        ends_after="Strike first, in anger, against someone you were told to wait for.",
        secret="", blocks_bonds=False,
    ),
    dict(
        name="Blessing of Kindness", kind="Blessing", hidden=False,
        summary="Another's joy is yours. When your friends do well, you are filled with it.",
        benefit="When an ally you can see scores a Critical Hit or succeeds on a saving throw, you can take a Reaction to gain Temporary Hit Points equal to 1d6 plus your Proficiency Bonus.",
        cost="You can't deal damage to a creature that has surrendered, or to a creature that is Incapacitated and can't fight back.",
        grows="When you help a rival or an enemy succeed, or when you are glad for someone who got what you wanted.",
        thresholds=[(2, "When you gain the Temporary Hit Points, the ally gains the same number."),
                    (4, "You have Disadvantage on attack rolls against a creature that is Bloodied, unless it attacked you this turn.")],
        give_in="The Temporary Hit Points become 2d6 plus your Proficiency Bonus, and you can give yours to a different ally you can see. " + _ZEAL +
                "[[Key moments:]] when an enemy begs for mercy, the GM steers your answer.",
        scar="Strangers trust you a little more. You have Advantage on Wisdom (Insight) checks to tell if a creature means you harm.",
        ends="Refuse to forgive, once, someone who has truly earned your anger.",
        ends_after="Refuse to forgive someone who asks for it with tears, because forgiving them would put others in danger.",
        secret="", blocks_bonds=False,
    ),
    dict(
        name="Blessing of Devotion", kind="Blessing", hidden=False,
        summary="One heart, one cause. You have given yourself to it, and it gives you strength.",
        benefit="Choose one person you love or one cause you serve. Once each Long Rest, when that person takes damage within 30 feet of you, "
                "you can take a Reaction to teleport to an unoccupied space within 5 feet of them and take the damage instead.",
        cost="When the person or the cause is in danger and you can reach it, you must go to it first. To go elsewhere first, you must succeed on a DC 12 Wisdom saving throw.",
        grows="When you put the person or the cause before your own safety or your own desire.",
        thresholds=[(2, "You can use the benefit twice each Long Rest. When you take the damage, you reduce it by your Proficiency Bonus."),
                    (4, "You know the direction and the distance to the person you chose while they are on the same plane as you. The saving throw becomes DC 15.")],
        give_in="You can use the benefit a number of times equal to your Proficiency Bonus each Long Rest, and you have Resistance to the damage that you take with it. " + _ZEAL +
                "[[Key moments:]] when the person or the cause asks something of you, the GM steers your answer.",
        scar="You keep your word. A creature that can see your face knows when you make a promise that you mean.",
        ends="Leave the person or the cause, with their blessing, for a good reason.",
        ends_after="Leave the person or the cause without their blessing, because staying would hurt them.",
        secret="", blocks_bonds=False,
    ),
    dict(
        name="Blessing of Temperance", kind="Blessing", hidden=False,
        summary="Enough is enough. You take only what you need, and your body and mind are clear because of it.",
        benefit="You have Advantage on saving throws to avoid or end the Charmed and Poisoned conditions.",
        cost="You can't benefit from more than one potion between Short Rests. Strong drink has no effect on you, good or bad.",
        grows="When you refuse a pleasure, a comfort, or a power that you could have taken, and nobody makes you refuse it.",
        thresholds=[(2, "You need only half the usual food and water each day."),
                    (4, "You have Immunity to the Poisoned condition. You can't benefit from a potion other than a potion of healing.")],
        give_in="You have Immunity to the Charmed and Poisoned conditions, and to Poison damage. " + _ZEAL +
                "[[Key moments:]] when your friends feast, celebrate, or take a reward, the GM steers you to refuse it, and to tell them why.",
        scar="Your mind stays clear. You have Advantage on saving throws to avoid or end the Poisoned condition.",
        ends="Join a great feast or celebration, and enjoy it fully, with the people who gave it.",
        ends_after="Join a great feast, then take a power or a reward that you once refused.",
        secret="", blocks_bonds=False,
    ),
    dict(
        name="Blessing of Diligence", kind="Blessing", hidden=False,
        summary="The work is its own reward. Your hands never stop, and they rarely fail.",
        benefit="Once each Long Rest, when you fail an ability check that uses a tool or a skill, you can reroll it and use the new roll. "
                "Crafting, training, and research in downtime take you three quarters of the usual time.",
        cost="Idle hours are hard for you. You gain the benefits of a Short Rest only if you spend part of it on a task, such as mending, cleaning, or standing watch.",
        grows="When you finish a long, hard task that others gave up on.",
        thresholds=[(2, "You can use the reroll twice each Long Rest. You need only 4 hours of sleep in a Long Rest; you spend the rest working."),
                    (4, "Downtime tasks take you half the usual time. You must succeed on a DC 12 Wisdom saving throw to stop a task before it is finished.")],
        give_in="You can use the reroll a number of times equal to your Proficiency Bonus each Long Rest. Once each Long Rest, you gain Heroic Inspiration when you finish a Short Rest. " + _ZEAL +
                "[[Key moments:]] when a task is left unfinished, the GM steers you back to it.",
        scar="Your hands remember. You gain proficiency with one tool of your choice.",
        ends="Leave an important task unfinished, on purpose, to spend the time with someone who needs you.",
        ends_after="Leave the most important work of your life unfinished, and let someone else complete it.",
        secret="", blocks_bonds=False,
    ),
]
