"""The seven Taints: the Sins as hidden Marks. They print in the Game Master's Compendium."""

_SIN_HEARS = "The Sin hears you."

MARKS = [
    dict(
        name="Taint of Envy", kind="Taint", hidden=True,
        summary="Someone else always has it better. The Sin of Envy makes sure you notice, and gives you the strength to make them pay for it.",
        benefit="When an ally you can see scores a Critical Hit, reduces a creature to 0 Hit Points, or succeeds on a saving throw that you failed, "
                "your next hit with an attack before the end of your next turn deals an extra 1d6 damage of the attack's type.",
        cost="You can't take the Help action to aid an ally with a check that you also tried and failed. "
             "When an ally is praised in front of you, you have Disadvantage on your next Charisma check before the end of the scene.",
        grows="When you deal the extra damage of the benefit.",
        thresholds=[(1, "The extra damage becomes 1d8."),
                    (3, _SIN_HEARS + " The extra damage becomes 2d6, but the benefit now also triggers when an ally is healed, praised, or rewarded "
                        "in front of you, and you can't choose to hold the extra damage back.")],
        give_in="The extra damage becomes 3d6, and you can deal it once on each of your turns while an ally has done better than you this scene. "
                "The Sin whispers to you. [[Key moments:]] when an ally gets a reward, an honor, or a love that you wanted, the GM steers your next action toward taking it.",
        scar="A fleck of green stays in one of your eyes. Once each Long Rest, when an ally succeeds where you failed, you gain Temporary Hit Points equal to your Proficiency Bonus, "
             "because you have learned to be glad for them.",
        ends="Give the thing you envy most to the person you envy, freely, and tell them why.",
        ends_after="As above, but the gift must cost you something that you can't get back: a treasured item, a title, or a chance you will never have again.",
        secret="Envy usually comes through a gift: a stone, a ring, or an ember that glows when someone near you is happy. "
               "At 3, the one who gave the gift (a witch, a fey, or the Sin itself) can hear what you say near it. "
               "At 5, it can whisper to you once each day, and it uses the whispers to turn you against your closest friend.",
        blocks_bonds=False,
    ),
    dict(
        name="Taint of Pride", kind="Taint", hidden=True,
        summary="You were always better than this. The Sin of Pride agrees, and it will not let the world forget it.",
        benefit="Once each Long Rest, when you fail a saving throw, you can reroll it and use the new roll.",
        cost="You can't take the Help action for a task you think you could do alone, and you have Disadvantage on Charisma checks "
             "to apologize, to ask for aid, or to admit a mistake.",
        grows="When you use the reroll, or when you refuse help that you clearly need.",
        thresholds=[(2, "You have Advantage on Charisma (Intimidation) checks. When an ally's spell or feature would restore your Hit Points while you have 1 or more, "
                        "you must succeed on a DC 10 Wisdom saving throw to accept it."),
                    (4, "You can use the reroll twice each Long Rest. The saving throw to accept healing becomes DC 15.")],
        give_in="Once each Long Rest, you can turn a failed saving throw into a success. You keep the reroll of the benefit, twice each Long Rest. "
                "[[Key moments:]] when someone challenges your worth, gives you an order, or forgives you in front of others, the GM steers your answer.",
        scar="You keep a straight back and an even voice. You have Advantage on saving throws to avoid or end the Frightened condition.",
        ends="Ask for help, honestly and in front of others, from someone you thought was beneath you, and accept it.",
        ends_after="Serve someone you scorned, at their command, for a full month of downtime or until they release you.",
        secret="Each time you use the reroll, you hear applause that nobody else hears. "
               "At 4, the healing saving throw also applies to healing from potions that an ally gives you. "
               "At 5, if you give in, the Sin asks for one public act of contempt each month. If you refuse, the full power fails until you perform one.",
        blocks_bonds=False,
    ),
    dict(
        name="Taint of Greed", kind="Taint", hidden=True,
        summary="There is always more. The Sin of Greed shows you where it is hidden, and then it asks you why you should share it.",
        benefit="You have Advantage on Wisdom (Perception) and Intelligence (Investigation) checks to find hidden treasure, and you know the value of a coin, gem, "
                "or art object by touch. Once each Long Rest, when you search a room or a small area, the GM tells you whether something valuable is hidden there.",
        cost="When the party divides treasure, you must take a full share. To give away coins or an item of value, you must succeed on a DC 12 Wisdom saving throw.",
        grows="When you use the benefit to find something, or when you take more than your share.",
        thresholds=[(2, "You can feel gold and gems through stone: you know the direction of the largest store of them within 120 feet. The saving throw to give becomes DC 15."),
                    (4, "You can use the search benefit twice each Long Rest. You can't sell an item for less than its full price, and you can't lend an item at all.")],
        give_in="Once each Long Rest, you can cast Locate Object without a spell slot, and you know the location of every coin and gem within 120 feet. "
                "[[Key moments:]] when treasure is in reach and nobody is watching, the GM steers your hands.",
        scar="Your fingers keep a merchant's touch. You know the value of any coin, gem, or art object by holding it.",
        ends="Give away half of everything you own to people who need it more than you do.",
        ends_after="Give away everything you own, keeping only what you can carry in your two hands.",
        secret="At 2, the coins you touch feel warm, and you start to dream about them. "
               "At 4, items that you take without a fair share bring bad luck: the GM can make an ally reroll one d20 Test each day and take the lower roll. "
               "At 5, if you give in, one item you carry always calls a thief to you.",
        blocks_bonds=False,
    ),
    dict(
        name="Taint of Wrath", kind="Taint", hidden=True,
        summary="Every wound is an insult, and every insult must be paid back. The Sin of Wrath gives you the strength to do it.",
        benefit="When a creature damages you, your next hit against that creature before the end of your next turn deals extra damage equal to your Proficiency Bonus.",
        cost="While you are Bloodied, you can't take the Disengage or Dodge action, and you have Disadvantage on Charisma (Persuasion) checks.",
        grows="When you deal the extra damage of the benefit to a creature that has 10 or fewer Hit Points left.",
        thresholds=[(2, "The extra damage becomes 1d6 plus your Proficiency Bonus. When you are Bloodied, you must attack a creature that damaged you this turn if you can."),
                    (4, "When you are Bloodied, you have Advantage on attack rolls, and attack rolls against you have Advantage.")],
        give_in="The extra damage becomes 1d6 plus twice your Proficiency Bonus, and you can deal it once on each of your turns against a creature that damaged you this scene. "
                "You have Immunity to the Frightened condition while you are Bloodied. "
                "[[Key moments:]] when a creature insults you or hurts someone you love, the GM steers your next action against it.",
        scar="A thin red line stays on your knuckles. Once each Long Rest, when you are Bloodied, you can take the Dodge action as a Bonus Action.",
        ends="Spare a creature that hurt you badly, and let it walk away.",
        ends_after="Spare a creature that hurt you badly, then protect it from someone else's revenge until it is safe.",
        secret="At 2, the forced attack can't target an ally unless that ally damaged you this turn. Tell the player only that they \"feel the pull of the fight\". "
               "At 4, you no longer notice when an enemy surrenders: the GM tells you about a surrender only if you succeed on a DC 12 Wisdom (Insight) check. "
               "At 5, if you give in, the Sin keeps a count of the creatures you spare. When the count reaches three, it offers you more power in exchange for one life taken in anger. You can refuse; the Sin waits, and asks again.",
        blocks_bonds=False,
    ),
    dict(
        name="Taint of Lust", kind="Taint", hidden=True,
        summary="You want, and you are wanted. The Sin of Lust makes your desire into a kind of magic, and it makes you its servant.",
        benefit="Once each Long Rest, you can cast Charm Person without a spell slot. Charisma is your spellcasting ability for it.",
        cost="Choose a thing you desire: a person, a pleasure, or a kind of luxury. When it is near and in reach, you must succeed on a DC 12 Wisdom saving throw "
             "to leave it or to refuse it.",
        grows="When you cast the spell of the benefit, or when you put your desire before the needs of your friends.",
        thresholds=[(2, "You can cast the spell twice each Long Rest. A creature you charm with it doesn't know that you charmed it when the spell ends. The saving throw becomes DC 15."),
                    (4, "Once each Long Rest, you can cast Suggestion without a spell slot. Your desire begins to choose for you: on a failed saving throw, the GM says what you do to get closer to it.")],
        give_in="You keep Charm Person twice and Suggestion once each Long Rest, and you can cast Suggestion as a Bonus Action. "
                "[[Key moments:]] when the thing you desire is offered to you at a price, the GM steers your answer.",
        scar="A warmth stays in your voice. You have Advantage on Charisma (Persuasion) checks against a creature that is your friend.",
        ends="Give up the thing you desire, in a way that you can't take back.",
        ends_after="As above, and also free each creature you charmed with the Mark from any promise it made to you.",
        secret="At 2, the Sin begins to want through you: the thing you desire grows more beautiful, and more expensive, each month. "
               "At 4, the creatures you charmed with the Mark start to want you too, and they follow you. "
               "At 5, if you give in, one of them becomes a servant of the Sin and works against your friends.",
        blocks_bonds=False,
    ),
    dict(
        name="Taint of Gluttony", kind="Taint", hidden=True,
        summary="You are always hungry, and the hunger makes you strong. The Sin of Gluttony eats with you.",
        benefit="When you drink a potion that restores Hit Points, you regain extra Hit Points equal to twice your Proficiency Bonus. "
                "You have Advantage on saving throws against poison that you eat or drink.",
        cost="You need twice the usual food and water each day. At the end of a day when you get less, you gain 1 Exhaustion level.",
        grows="When you use the extra healing, or when you eat or drink what others needed.",
        thresholds=[(2, "When you eat a meal, you gain Temporary Hit Points equal to your Proficiency Bonus. They last until you finish a Long Rest. "
                        "You need three times the usual food and water."),
                    (4, "You can eat things that are not food: you can bite a creature as an Unarmed Strike that deals 1d6 Piercing damage, "
                        "and you regain Hit Points equal to half the damage. You must succeed on a DC 12 Wisdom saving throw to stop eating while food is in reach.")],
        give_in="The extra healing from potions becomes three times your Proficiency Bonus. Your bite deals 1d10 Piercing damage, and you regain Hit Points equal to the damage. "
                "[[Key moments:]] when you are hungry and food or a wounded creature is in reach, the GM steers your next action.",
        scar="You can always find a meal. You need only half the usual food and water each day.",
        ends="Fast for three days while you give your food to people who are starving.",
        ends_after="Fast for seven days, and feed a whole village through a winter or a famine.",
        secret="At 2, food that you eat no longer tastes of anything, and only blood tastes good. "
               "At 4, beasts flee from you, and the smell of a wounded creature makes you hungry. "
               "At 5, if you give in, a creature that you bite to 0 Hit Points can't be raised from the dead by any spell below level 7.",
        blocks_bonds=False,
    ),
    dict(
        name="Taint of Sloth", kind="Taint", hidden=True,
        summary="Why hurry? The Sin of Sloth teaches you how to rest, and how to let others do the work.",
        benefit="When you spend Hit Point Dice during a Short Rest, you regain the maximum number of Hit Points for each die.",
        cost="You have Disadvantage on Initiative rolls. A task that you start in downtime takes a quarter longer.",
        grows="When you use the benefit, or when you leave work or danger to others that you could have faced yourself.",
        thresholds=[(2, "You regain 1 spent Hit Point Die at the end of each Short Rest. You can't take the Dash action."),
                    (4, "You can finish a Short Rest in 10 minutes once each Long Rest. You fall asleep easily: when you are bored or alone, "
                        "you must succeed on a DC 12 Constitution saving throw or fall asleep for 1 hour.")],
        give_in="You can finish a Short Rest in 10 minutes twice each Long Rest, and you regain the maximum on each Hit Point Die. "
                "[[Key moments:]] when you are asked to stand watch, to work, or to hurry, the GM steers your answer.",
        scar="You learned the value of rest. When you finish a Long Rest, you regain all spent Hit Point Dice, not only half.",
        ends="Do a long, hard task alone, for others, without rest and without reward, until it is complete.",
        ends_after="As above, and the task must take at least a month of downtime.",
        secret="At 2, you start to forget small promises, and the GM can say that you forgot one each session. "
               "At 4, the sleep is not natural: if you fall asleep on watch, a creature that hunts you can find you. "
               "At 5, if you give in, the Sin can make you fall asleep once each month at the moment it chooses.",
        blocks_bonds=False,
    ),
]
