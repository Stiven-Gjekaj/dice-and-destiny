"""The four kinds of Bond. They print in the Player's Compendium, in the order of this list."""

BONDS = [
    dict(
        name="Friend",
        summary="You trust each other with your lives, and you have the scars to prove it.",
        special=("I've Got You",
                 "When an attack hits your friend, you can take a Reaction to move up to half your Speed to a space within 5 feet of your friend "
                 "and become the target instead. The attack hits you, and you take its damage and its effects."),
        strain="Leaving your friend in danger when you could help, lying to your friend about something that matters, or siding with their enemy.",
        example="An ogre's club comes down on Pell, who has 3 Hit Points left. Bryn, his Friend, shouts \"I've got you!\", "
                "steps in front of him, and takes the blow on her shield. Neither of them can spend the Bond again until they rest.",
    ),
    dict(
        name="Rival",
        summary="You push each other further than any friend could. You want to win, and you want to win fair.",
        special=("Not to Be Outdone",
                 "When your rival succeeds on a d20 Test that you can see, roll the bond die. Add the number to your next d20 Test before the end of your next turn."),
        strain="Cheating to beat your rival, refusing a fair challenge, or letting your rival fail at something that matters just to come out ahead.",
        example="Kesh hits the troll with a perfect arrow. Her Rival, Dov, can't let that stand: he spends the Bond, rolls a 6 on their d8, "
                "and adds it to his next attack roll.",
    ),
    dict(
        name="Debt",
        summary="One of you owes the other something big: a life, a fortune, a secret kept. Both of you know it.",
        special=("Called In",
                 "Once each adventure, the partner who is owed can call in the debt and name one task. This doesn't spend the shared use of the Bond. The partner who owes adds the bond die "
                 "to each d20 Test for that task until the end of the scene. If the one who owes refuses a fair task, the Bond strains. "
                 "When the debt is fully paid, the two can change the Bond to a Friend or a Rival, and keep the die."),
        strain="The one who owes refuses a fair call, or the one who is owed asks for something cruel or dishonorable.",
        example="Years ago, the smuggler Ilse pulled Corvin from a river. Tonight she calls in the debt: \"Get me into that vault.\" "
                "Corvin adds their d6 to each check to pick the locks and slip past the guards until the scene ends.",
    ),
    dict(
        name="Oath",
        summary="You swore it together: to protect a village, to find a lost child, to bring down a tyrant. The oath binds you to each other.",
        special=("Sworn Purpose",
                 "As a Bonus Action, either partner can spend the Bond. Until the start of that partner's next turn, both partners have Advantage on d20 Tests "
                 "that directly serve the oath. When the oath is fulfilled, the bond die grows one step, and the two can swear a new oath or change the Bond to a Friend."),
        strain="Breaking the oath, giving up on it, or putting something else first when the oath needs you.",
        example="Arlo and Sela swore to bring the warlord to justice. When they finally corner him, Arlo spends the Bond: for a moment, "
                "both of them fight with Advantage, because this is what they swore to do.",
    ),
]
