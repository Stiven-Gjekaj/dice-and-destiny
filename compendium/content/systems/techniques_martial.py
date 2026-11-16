"""Techniques, first set: stances and maneuvers for weapons and bodies. They print in the Player's Compendium."""


def _t(name, type_, cost, level, timing, text):
    return dict(name=name, type=type_, cost=cost, level=level, timing=timing, text=text)


_ON_HIT = "When you hit with a weapon attack"
_ON_MELEE = "When you hit with a melee weapon attack"

TECHNIQUES = [
    # Stances.
    _t("Iron Root Stance", "Stance", 1, 1, "Bonus Action",
       "You sink your weight into the ground. You have Advantage on saving throws and Strength checks against being pushed, pulled, "
       "or knocked Prone. While you are in this stance, your Speed is halved."),
    _t("Flowing Water Stance", "Stance", 1, 1, "Bonus Action",
       "You never stand still. Your Speed increases by 10 feet, and Opportunity Attacks against you have Disadvantage. "
       "While you are in this stance, you can't gain the benefit of a Shield."),
    _t("Hawk's Eye Stance", "Stance", 1, 1, "Bonus Action",
       "You settle and take aim. Your ranged weapon attacks ignore Half Cover, and attacking at long range doesn't impose Disadvantage on them. "
       "While you are in this stance, you can't move more than half your Speed on your turn."),
    _t("Guardian's Stance", "Stance", 1, 1, "Bonus Action",
       "You plant yourself between your friends and harm. Each creature within 5 feet of you has Disadvantage on attack rolls against creatures other than you. "
       "While you are in this stance, you can't take the Dash action."),
    _t("Turtle Stance", "Stance", 1, 1, "Bonus Action",
       "You tuck in behind your guard. You gain a +2 bonus to Armor Class. While you are in this stance, you can make only one attack on each of your turns, "
       "even if a feature lets you attack more than once."),
    _t("Serpent Stance", "Stance", 1, 1, "Bonus Action",
       "You coil and slip away. When a creature misses you with a melee attack, you can move up to 5 feet without provoking Opportunity Attacks. "
       "This movement doesn't use your Speed or your Reaction."),
    _t("Spellguard Stance", "Stance", 1, 1, "Bonus Action",
       "You guard your focus as a fighter guards a flank. You have Advantage on Constitution saving throws to keep Concentration. "
       "While you are in this stance, your Speed decreases by 10 feet."),
    _t("Tiger Stance", "Stance", 2, 5, "Bonus Action",
       "You fight with your whole body and no thought of defense. Once on each of your turns, when you hit with a melee weapon attack, "
       "the attack deals an extra 1d6 damage of its type. While you are in this stance, you take a -2 penalty to Armor Class."),
    _t("Storm Stance", "Stance", 2, 11, "Bonus Action",
       "Each fall is the start of the next blow. Once on each of your turns, when you score a Critical Hit with a weapon or reduce a creature to 0 Hit Points with one, "
       "you can make one more attack with the same weapon as part of the same action."),
    _t("Mountain Stance", "Stance", 3, 11, "Bonus Action",
       "You become a wall. You have Resistance to Bludgeoning, Piercing, and Slashing damage. While you are in this stance, "
       "your Speed is halved and you can't take Reactions."),

    # Maneuvers.
    _t("Driving Strike", "Maneuver", 1, 1, _ON_MELEE,
       "The target must succeed on a Strength saving throw against your technique DC or be pushed up to 15 feet straight away from you. "
       "A creature more than one size larger than you succeeds automatically."),
    _t("Hamstring", "Maneuver", 1, 1, _ON_MELEE,
       "You cut low. The attack deals an extra 1d4 damage, and the target's Speed decreases by 15 feet until the start of your next turn."),
    _t("Read the Opening", "Maneuver", 1, 1, "Bonus Action",
       "Choose a creature you can see within 30 feet. Make a Wisdom (Insight) check against its Charisma (Deception) check. "
       "If you win, you have Advantage on attack rolls against it until the end of your turn."),
    _t("Shield Rattle", "Maneuver", 1, 1, "When you hit with a melee attack while you hold a Shield",
       "You slam the rim of your shield into the target. It must succeed on a Dexterity saving throw against your technique DC or be unable to take Reactions "
       "until the start of its next turn."),
    _t("Grit Your Teeth", "Maneuver", 1, 1, "Bonus Action",
       "You refuse to feel it. Spend one of your Hit Point Dice: roll it and add your Constitution modifier. You regain that many Hit Points."),
    _t("Turn the Blade", "Maneuver", 1, 1, "Reaction, when a melee attack would hit you",
       "You gain a +2 bonus to Armor Class against that attack, possibly causing it to miss you."),
    _t("Covering Fire", "Maneuver", 1, 1, "Reaction, when a creature you can see moves toward an ally",
       "If the creature is within the normal range of a ranged weapon you hold, make one ranged attack with that weapon against it."),
    _t("Snap Out of It", "Maneuver", 1, 1, "Bonus Action",
       "You shout the name of an ally who can hear you within 30 feet. If the ally has the Charmed or Frightened condition, it can repeat the saving throw "
       "against that condition now, with Advantage."),
    _t("Tackle", "Maneuver", 1, 1, "When you take the Attack action, in place of one attack",
       "You move up to 10 feet straight toward a creature, then try to grapple or shove it. You have Advantage on the attempt. This movement doesn't provoke Opportunity Attacks."),
    _t("Pinning Shot", "Maneuver", 1, 1, "When you hit with a ranged weapon attack",
       "You pin the target's cloak, boot, or tail. Its Speed becomes 0 until the start of your next turn, unless it uses its action to pull free."),
    _t("Duck and Roll", "Maneuver", 1, 1, "Reaction, before you make a Dexterity saving throw",
       "You have Advantage on the saving throw. After the effect, you can move up to 5 feet without provoking Opportunity Attacks."),
    _t("Draw Their Eye", "Maneuver", 1, 1, "Bonus Action",
       "You taunt a creature you can see within 30 feet. It must succeed on a Wisdom saving throw against your technique DC, or until the start of your next turn "
       "it has Disadvantage on attack rolls against creatures other than you."),
    _t("Low Blow", "Maneuver", 1, 1, _ON_MELEE,
       "You strike where it hurts. The target must succeed on a Constitution saving throw against your technique DC or be unable to take Reactions "
       "and have Disadvantage on its next attack roll before the end of its next turn."),
    _t("Blinding Dust", "Maneuver", 1, 1, "Bonus Action",
       "You throw grit at the eyes of a creature within 5 feet of you. It must succeed on a Dexterity saving throw against your technique DC "
       "or have the Blinded condition until the start of your next turn. A creature without eyes succeeds automatically."),
    _t("Set Against the Charge", "Maneuver", 1, 1, "Reaction, when a creature moves at least 10 feet straight toward you and enters your reach",
       "Make one melee weapon attack against the creature. If it hits, the attack deals an extra 1d8 damage, and the creature is pushed 5 feet away from you."),
    _t("Mighty Throw", "Maneuver", 1, 1, "When you make a ranged attack with a Thrown weapon",
       "The weapon's normal and long ranges double for this attack. If it hits, it deals an extra 1d6 damage."),
    _t("Study the Foe", "Maneuver", 1, 1, "Bonus Action",
       "Choose a creature you can see within 60 feet. The GM tells you its Immunities, Resistances, and Vulnerabilities, "
       "and which of its saving throws has the lowest bonus."),
    _t("Steel Your Mind", "Maneuver", 1, 1, "Reaction, when you fail an Intelligence, Wisdom, or Charisma saving throw",
       "Roll 1d6 and add it to the saving throw, possibly turning it into a success."),
    _t("Finish Them", "Maneuver", 2, 5, _ON_HIT + " against a Bloodied creature",
       "The attack deals an extra 2d8 damage of its type."),
    _t("Thunderous Charge", "Maneuver", 2, 5, _ON_MELEE + " after you move at least 20 feet straight toward the target on this turn",
       "The attack deals an extra 2d6 damage, and the target must succeed on a Strength saving throw against your technique DC or have the Prone condition."),
    _t("Refuse to Fall", "Maneuver", 3, 11, "Reaction, when you are reduced to 0 Hit Points but not killed outright",
       "You drop to 1 Hit Point instead."),
    _t("Unstoppable", "Maneuver", 3, 11, "Bonus Action",
       "The Grappled and Restrained conditions end on you. Until the start of your next turn, you can't gain either condition, "
       "difficult terrain doesn't slow you, and your Speed increases by 10 feet."),
    _t("Perfect Strike", "Maneuver", 3, 17, "When you make a weapon attack roll, before you roll",
       "Everything you have learned goes into one blow. If the attack hits, it is a Critical Hit."),
]
