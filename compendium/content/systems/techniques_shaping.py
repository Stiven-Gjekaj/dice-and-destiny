"""Techniques, second set: spell shapings, and maneuvers for skills and movement. They print in the Player's Compendium."""


def _t(name, type_, cost, level, timing, text):
    return dict(name=name, type=type_, cost=cost, level=level, timing=timing, text=text)


_CAST = "When you cast a spell with a spell slot"

TECHNIQUES = [
    # Spell Shapings.
    _t("Wider Weave", "Shaping", 1, 1, _CAST + " that has an area of effect",
       "One size of the area grows: a Sphere, Cylinder, or Emanation's radius grows by 5 feet, or a Cone, Cube, or Line's length grows by 10 feet."),
    _t("Focused Beam", "Shaping", 1, 1, _CAST + " that creates a Cone",
       "You squeeze the cone into a beam. The spell creates a Line 5 feet wide and twice as long as the Cone, in place of the Cone."),
    _t("Spell Armor", "Shaping", 1, 1, _CAST,
       "Leftover magic clings to you. You gain Temporary Hit Points equal to the slot's level plus your Proficiency Bonus."),
    _t("Blink Cast", "Shaping", 1, 1, _CAST,
       "You step through the spell as it forms. Before or after you cast it, you teleport up to 10 feet to an unoccupied space that you can see."),
    _t("Second Spark", "Shaping", 1, 1, "When you miss with the spell attack of a cantrip",
       "This shaping works on cantrips. You reroll the attack roll and must use the new roll."),
    _t("Spill the Cup", "Shaping", 1, 1, _CAST + " that restores Hit Points",
       "The healing overflows. One creature of your choice within 5 feet of a target also regains Hit Points equal to the slot's level plus your spellcasting ability modifier."),
    _t("Binding Word", "Shaping", 2, 5, _CAST + " that forces a saving throw",
       "Choose one creature that fails its saving throw against the spell. Its Speed becomes 0 until the end of its next turn."),
    _t("Shatter Focus", "Shaping", 2, 5, _CAST + " that forces a saving throw",
       "Choose one creature that fails its saving throw against the spell. Until the end of its next turn, it has Disadvantage on Constitution saving throws "
       "to keep Concentration."),
    _t("Held Breath", "Shaping", 2, 5, _CAST + " that has an area of effect and an instant duration",
       "You hold the spell for a heartbeat. It takes effect at the start of your next turn, not now. When it does, you can move its point of origin "
       "up to 30 feet, within the spell's range. If you have the Incapacitated condition before then, the spell is lost."),
    _t("Lingering Ground", "Shaping", 2, 5, _CAST + " that has an area of effect on the ground",
       "The area stays torn, frozen, or charged after the spell. Until the end of your next turn, the area is Difficult Terrain."),
    _t("Push the Weave", "Shaping", 3, 11, _CAST,
       "You pour more of yourself into the spell. It is cast as if you used a spell slot one level higher. This can't raise it above level 9."),

    # Maneuvers for skills and movement.
    _t("Wall Run", "Maneuver", 1, 1, "When you move on your turn",
       "You can move up to half your Speed along a vertical surface or across a gap no longer than that distance, without falling. "
       "If you end your turn on the wall, you fall."),
    _t("Vault", "Maneuver", 1, 1, "When you jump",
       "Your jump distances double for this jump, and you don't need a running start."),
    _t("Tumble Through", "Maneuver", 1, 1, "When you move on your turn",
       "Until the end of the turn, you can move through the spaces of hostile creatures. Their spaces aren't Difficult Terrain for you, "
       "but you can't end your move in one."),
    _t("Burst of Speed", "Maneuver", 1, 1, "At the start of your turn",
       "Your Speed increases by 15 feet until the end of the turn."),
    _t("Look Again", "Maneuver", 1, 1, "When you fail a Wisdom (Perception) or Intelligence (Investigation) check",
       "You reroll the check and must use the new roll."),
    _t("Silver Tongue", "Maneuver", 1, 1, "When you make a Charisma check",
       "Roll 1d6 and add it to the check. You can decide after you see the d20, but before the GM says whether the check succeeds."),
    _t("Heave", "Maneuver", 1, 1, "When you make a Strength (Athletics) check to lift, push, pull, or break something",
       "You have Advantage on the check, and your carrying capacity doubles for it."),
    _t("Ready Blade", "Maneuver", 1, 1, "When you roll Initiative",
       "Roll 1d6 and add it to the Initiative roll."),
    _t("Listen Closely", "Maneuver", 1, 1, "Bonus Action",
       "You close your eyes for a moment. Until the end of your next turn, you know the location of each creature within 15 feet of you "
       "that isn't hidden by magic, even if it is invisible."),
    _t("Catch", "Maneuver", 1, 1, "Reaction, when a creature within 5 feet of you falls or is pushed",
       "You grab it. It stops falling or moving and stays in a space within 5 feet of you. A creature larger than you pulls you along "
       "unless you succeed on a Strength (Athletics) check against DC 15."),
    _t("Roll With the Fall", "Maneuver", 1, 1, "Reaction, when you take damage from a fall",
       "You take half the damage, and you don't land Prone."),
    _t("Spur On", "Maneuver", 1, 1, "Bonus Action, while you ride a mount",
       "Your mount's Speed increases by 20 feet until the end of your turn, and its movement doesn't provoke Opportunity Attacks this turn."),
    _t("Spell Ward", "Maneuver", 1, 1, "Reaction, before you make a saving throw against a spell",
       "You brace against the magic. Add your Proficiency Bonus to the saving throw."),
    _t("Shake It Off", "Maneuver", 2, 5, "Bonus Action",
       "End one of these conditions on yourself: Charmed, Frightened, or Poisoned."),
    _t("Untouchable Passage", "Maneuver", 3, 11, "At the start of your turn",
       "Until the end of your turn, your movement doesn't provoke Opportunity Attacks, you can move through the spaces of other creatures, "
       "and Difficult Terrain doesn't slow you."),
]
