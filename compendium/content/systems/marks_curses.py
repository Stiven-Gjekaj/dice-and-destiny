"""Six Curses: Marks that the story puts on a character. They print in the Player's Compendium."""

_STORY = "The story. The GM decides, usually when you go near the thing that cursed you, or when you act against what the Curse demands."

MARKS = [
    dict(
        name="Curse of the Lone Path", kind="Curse", hidden=False,
        summary="Something old decided that you must walk alone. Your friends can stand beside you, but their hands pass through you like mist.",
        benefit="",
        cost="You can't benefit from the Help action. A spell or feature of another creature can't restore your Hit Points, give you Temporary Hit Points, "
             "or add a bonus to your d20 Tests. Potions, and your own spells and features, work as usual.",
        grows=_STORY,
        thresholds=[(2, "A spell of an ally that targets only you fails, and the spell slot is spent."),
                    (4, "An ally who touches you to stabilize you at 0 Hit Points must succeed on a DC 15 Wisdom (Medicine) check, not the usual DC 10.")],
        give_in="You accept the path. When you would drop to 0 Hit Points, you drop to 1 instead, once each Long Rest. You have Advantage on saving throws while no ally is within 30 feet of you. "
                "[[Key moments:]] when an ally offers to share your burden, the GM steers you to refuse.",
        scar="You learned to stand alone. You have Advantage on death saving throws.",
        ends="Find the place where the Curse was made, and let a friend carry you through it.",
        ends_after="As above, and the friend must take on the Curse for one day and one night while you carry them back.",
        secret="", blocks_bonds=True,
    ),
    dict(
        name="Liar's Curse", kind="Curse", hidden=False,
        summary="Every lie you tell sounds like the truth, even to you. It is very useful, until you can't remember what was true.",
        benefit="You have Advantage on Charisma (Deception) checks. Magic that detects lies doesn't detect your lies.",
        cost="After you tell a lie that matters, you must succeed on a DC 10 Wisdom saving throw or believe it yourself until you finish a Long Rest.",
        grows=_STORY,
        thresholds=[(2, "The saving throw becomes DC 13, and a lie that you believe lasts until someone proves it false to you."),
                    (4, "You can't tell which of your memories are true. Once each session, the GM can tell you that one thing you remember is not true.")],
        give_in="Once each Long Rest, you can cast Suggestion without a spell slot, and the target believes that the suggestion was its own idea. "
                "[[Key moments:]] when the truth would hurt you, the GM steers you to lie, and you believe the lie.",
        scar="You know the sound of a lie. You have Advantage on Wisdom (Insight) checks to tell if a creature is lying.",
        ends="Return what you took when the Curse began, and confess the theft, in your own words, to the one you stole from.",
        ends_after="As above, and you must also confess every lie that you told under the Curse to the person it hurt.",
        secret="", blocks_bonds=False,
    ),
    dict(
        name="Curse of the Stone Heart", kind="Curse", hidden=False,
        summary="Your skin is turning to stone, a little at a time. It is hard to hurt you now. It is also hard to feel anything.",
        benefit="You gain a +1 bonus to Armor Class.",
        cost="Your Speed decreases by 5 feet. You have Disadvantage on Dexterity (Stealth) checks, and you sink in water.",
        grows=_STORY,
        thresholds=[(2, "You have Resistance to Bludgeoning damage. You have Disadvantage on Dexterity saving throws."),
                    (4, "You don't need to eat or drink. Your Speed decreases by another 5 feet, and you have Disadvantage on Charisma checks to show feeling.")],
        give_in="You gain a +2 bonus to Armor Class, you keep the Resistance to Bludgeoning damage, and you have Immunity to the Petrified condition. "
                "[[Key moments:]] when someone asks you to feel something (to grieve, to forgive, to love), the GM steers your answer, and it is cold.",
        scar="One hand stays stone grey. You can't be knocked Prone against your will while you are standing on stone or earth.",
        ends="Weep honest tears for someone you lost. The tears break the stone.",
        ends_after="Weep honest tears for someone you lost, at the place where the Curse found you, before the eyes of everyone you call a friend.",
        secret="", blocks_bonds=False,
    ),
    dict(
        name="Curse of the Restless Dead", kind="Curse", hidden=False,
        summary="The dead have noticed you. They follow you, they whisper to you, and they want something.",
        benefit="You know the location of each Undead creature within 60 feet of you. You can understand the speech of the Undead.",
        cost="When you finish a Long Rest, roll a d6. On a 1, an Undead creature finds you during the next day.",
        grows=_STORY,
        thresholds=[(2, "Once each Long Rest, you can cast Gentle Repose without a spell slot. You roll a d4 at the end of a Long Rest, not a d6."),
                    (4, "Undead creatures have Advantage on attack rolls against you. You have Advantage on saving throws against the spells and the features of Undead creatures.")],
        give_in="Once each Long Rest, you can cast Speak with Dead without a spell slot, and you can call a ghost to serve you for 1 hour. It uses the stat block of a Specter, it obeys you, and it can't go more than 120 feet from you. "
                "[[Key moments:]] when a dead creature asks you for a favor, the GM steers your answer.",
        scar="Cold hands. You have Resistance to Necrotic damage.",
        ends="Find the dead creature who first cursed you, learn what it wants, and give it peace.",
        ends_after="Give peace to the first dead creature, and then to every ghost that served you while you gave in.",
        secret="", blocks_bonds=False,
    ),
    dict(
        name="Curse of the Forgotten Name", kind="Curse", hidden=False,
        summary="The world is forgetting you. People who meet you can't remember your face, and soon they won't remember your name.",
        benefit="You have Advantage on Dexterity (Stealth) checks. A creature that isn't hostile to you forgets that it saw you an hour after you leave it.",
        cost="Merchants, guards, and other people who aren't your friends forget your deals with them after a day. Written records of your name fade within a week.",
        grows=_STORY,
        thresholds=[(2, "Once each Long Rest, you can cast Invisibility on yourself without a spell slot."),
                    (4, "Your friends start to forget too. At the start of each session, each ally must remind the table of one thing that you did together, "
                        "or that ally has Disadvantage on Wisdom (Insight) checks about you until the end of the session.")],
        give_in="Once each Long Rest, you can cast Greater Invisibility on yourself without a spell slot, and Divination magic can't find you unless the caster knows your true name. "
                "[[Key moments:]] when someone calls you by your name, the GM steers you to deny it.",
        scar="You fade a little in the dark. You have Advantage on Dexterity (Stealth) checks made in dim light or darkness.",
        ends="Find someone who remembers your true name, and make them say it aloud where a crowd can hear it.",
        ends_after="As above, and your true name must also be carved into stone in the place you were born.",
        secret="", blocks_bonds=False,
    ),
    dict(
        name="Curse of Ill Fortune", kind="Curse", hidden=False,
        summary="Bad luck follows you like a black dog. You have learned how to send it after someone else.",
        benefit="Once each Long Rest, when a creature you can see within 30 feet makes a d20 Test, you can take a Reaction to make it reroll the d20 and use the lower roll.",
        cost="Once each Long Rest, the GM can make you reroll a d20 Test and use the lower roll. The GM must use it before you finish your next Long Rest.",
        grows=_STORY,
        thresholds=[(2, "You can use the benefit twice each Long Rest. The GM can use the cost twice each Long Rest."),
                    (4, "Once each Long Rest, when you roll a 1 on a d20 Test, you can choose an ally you can see: that ally rolls a 1 on its next d20 Test instead, and you reroll yours.")],
        give_in="You can use the benefit a number of times equal to your Proficiency Bonus each Long Rest, and the cost of the Curse ends. "
                "[[Key moments:]] when an ally is about to succeed at something that you wanted, the GM can steer your Curse onto them.",
        scar="Luck owes you one. Once each Long Rest, when you roll a 1 on a d20 Test, you can reroll it.",
        ends="Do a kindness for someone so unlucky that they have nothing left, and expect nothing in return.",
        ends_after="As above, and you must then go a month without using the benefit.",
        secret="", blocks_bonds=False,
    ),
]
