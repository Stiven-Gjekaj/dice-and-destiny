# Edition 2, items batch 10: wondrous items, potions, rings, and weapons.
# (name, category, rarity, attunement, text)
A = "Requires Attunement"
AS = "Requires Attunement by a Spellcaster"
W = "Wondrous Item"
ITEMS = [
# ================= WONDROUS ITEMS =================
("Homing Button", W, "Common", None, "Sew this brass button onto a garment. If the garment is ever lost or stolen, you know the direction to it, as long as it is within 1 mile of you."),
("Sleeper's Earplugs", W, "Common", None, "While you wear these wax earplugs, you can't hear anything except your own name, which you hear clearly when someone says it within 30 feet of you."),
("Patchwork Bedroll", W, "Common", None, "This quilted bedroll stays dry and warm. Sleeping on it on hard or cold ground is as comfortable as sleeping in a good bed."),
("Damp-Day Flint", W, "Common", None, "A spark struck from this flint lights wet wood, damp tinder, or a soaked wick on the first try. The flint never wears down."),
("Hamper of the Long Road", W, "Uncommon", None, "Once per dawn, you can open this wicker hamper to find a hot meal and fresh water for up to six creatures. Food taken from the hamper spoils after 1 hour."),
("Archer's Bracer", W, "Uncommon", A, "While wearing this leather bracer, your ranged weapon attacks at long range don't have Disadvantage."),
("Scholar's Cap", W, "Uncommon", A, "While wearing this felt cap, you have Advantage on Intelligence (History) checks. Once per dawn, you can ask the GM one question about the history of a place, a person, or an object in front of you, and learn one true fact about it."),
("Climbing Claws", W, "Uncommon", A, "While wearing these iron claws over your hands, you have a Climb Speed of 20 feet. You can't hold anything else in a hand that wears a claw."),
("Lens of the Second Glance", W, "Uncommon", None, "Once per dawn, you can look through this amber lens to cast Detect Evil and Good from it."),
("Paired Courier Satchels", W, "Uncommon", None, "These two leather satchels come as a pair. Once per dawn, you can put an object of up to 10 pounds into one satchel and speak the command word. If the other satchel is within 10 miles, the object moves into it."),
("Mask of the Long Breath", W, "Uncommon", A, "While wearing this leather mask, you can hold your breath for up to 1 hour."),
("Torch of Revealing Ink", W, "Uncommon", None, "This torch burns with a pale blue flame. Writing in its light shows invisible ink, hidden marks, and words written with Illusory Script, as long as you can read the language."),
("Cape of the Diving Hawk", W, "Rare", A, "While wearing this feathered cape, you fall at a rate of 60 feet per round, and you can move up to 2 feet horizontally for every 1 foot you fall. Once per turn, when you fall at least 30 feet onto a creature and hit it with a melee attack at the end of the fall, the attack deals an extra 3d6 damage."),
("Sash of the River Dancer", W, "Rare", A, "While wearing this blue silk sash, you have a Swim Speed of 40 feet, and you can breathe underwater."),
("Thunderclap Gauntlet", W, "Rare", A, "Once per dawn, you can strike this steel gauntlet against your other hand as a Magic action. Each creature in a 15-foot Cone makes a DC 15 Constitution save. On a failed save, a creature takes 3d8 Thunder damage and is pushed 10 feet away from you. On a successful save, it takes half as much damage only."),
("Eye of the Watchful Owl", W, "Rare", A, "While wearing this amber brooch, you have Advantage on Wisdom (Perception) checks that rely on sight, and you can see Invisible creatures and objects within 10 feet of you. Once per dawn, you can cast See Invisibility from it."),
("Wardstone of the Hidden Camp", W, "Rare", None, "Once per dawn, you can set this flat black stone on the ground to cast Private Sanctum from it, without material components. The sanctum is centered on the stone."),
("Beastmaster's Whistle", W, "Rare", A, "Once per dawn, you can blow this bone whistle to cast Dominate Beast (save DC 15) from it."),
("Quiver of the Steady Rain", W, "Rare", A, "This quiver holds up to 60 arrows, and arrows in it weigh nothing. Once per dawn, as a Bonus Action, you can wake the quiver for 1 minute. While it is awake, arrows you draw from it deal an extra 1d6 Force damage on a hit."),
("Glove of the Far Reach", W, "Very Rare", A, "Once per dawn, you can cast Telekinesis (save DC 17) from this grey silk glove."),
("Crystals of the Shared Mind", W, "Very Rare", None, "This set of eight small crystals is worn on cords. Once per dawn, while you wear one of them, you can cast Telepathic Bond from it, targeting up to seven other creatures who wear the other crystals."),
("Dragon Egg Pendant", W, "Very Rare", A, "This pendant holds a tiny scaled egg. Once per dawn, you can cast Summon Dragon from it, without material components."),
("Mask of the Second Self", W, "Legendary", AS, "Once per 30 days, you can cast Simulacrum from this white porcelain mask, without the costly materials. The simulacrum wears a copy of the mask. If you cast it again, the earlier simulacrum melts away."),
("Chalk of the Final Sign", W, "Legendary", None, "This stick of black chalk has 3 uses. Once per 7 days, you can use it to cast Symbol (save DC 19), without the costly materials. When the last use is spent, the chalk crumbles."),
# ================= POTIONS =================
("Potion of the Garden Scent", "Potion", "Common", None, "For 24 hours after you drink this potion, you smell faintly of roses and fresh grass, and creatures that track by scent can't follow your trail during that time."),
("Potion of the Borrowed Face", "Potion", "Uncommon", None, "When you drink this potion, you gain the effect of the Disguise Self spell for 1 hour."),
("Dragonfire Tonic", "Potion", "Uncommon", None, "For 1 hour after you drink this tonic, you can take a Bonus Action once to exhale fire in a 15-foot Cone. Each creature in the Cone makes a DC 13 Dexterity save, taking 3d6 Fire damage on a failed save or half as much on a successful one."),
("Potion of the Gentle Rest", "Potion", "Uncommon", None, "When you drink this potion, you fall into a deep sleep for up to 8 hours. While you sleep, you appear dead to all examination, short of magic. You wake when the time ends, when you take damage, or when someone shakes you hard. If you sleep for at least 8 hours, you gain the benefits of a Long Rest."),
("Potion of the Bear's Form", "Potion", "Rare", None, "When you drink this potion, you transform into a Brown Bear for up to 1 hour, as if by the Polymorph spell. The effect doesn't require Concentration, and you can end it as a Bonus Action."),
("Potion of the Steady Mind", "Potion", "Rare", None, "For 1 hour after you drink this potion, you have Immunity to the Frightened condition, and you have Advantage on Wisdom saving throws."),
("Potion of the New Body", "Potion", "Very Rare", None, "When you pour this potion over the remains of a Humanoid that died within the last 10 days, you cast Reincarnate on it, without material components."),
("Potion of the True Shape", "Potion", "Legendary", None, "When you drink this potion, you can transform into any creature whose CR is equal to or less than your level, as if by the True Polymorph spell targeting only you. The effect lasts for 1 hour, doesn't require Concentration, and you can end it as a Bonus Action."),
# ================= RINGS =================
("Ring of Three Darts", "Ring", "Uncommon", A, "This ring has 3 charges and regains all expended charges daily at dawn. While wearing it, you can expend 1 charge to cast Magic Missile from it."),
("Ring of the Charming Smile", "Ring", "Rare", A, "Once per dawn, you can cast Charm Monster (save DC 15) from this ring."),
("Ring of the Called Blade", "Ring", "Very Rare", A, "You can bind one object of up to 10 pounds to this ring by touching the object with it for 1 minute. Once per dawn, you can crush a tiny sapphire that grows on the ring each dawn to cast Instant Summons from it, calling the bound object, without other material components."),
("Ring of the Closed Mind", "Ring", "Legendary", A, "Once per dawn, you can cast Mind Blank from this ring, targeting only yourself."),
# ================= WEAPONS =================
("Boomerang Handaxe", "Weapon (Handaxe)", "Uncommon", None, "You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon. When you throw it, it flies back to your hand after the attack."),
("Flamebrand Scimitar", "Weapon (Scimitar)", "Rare", A, "You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. As a Bonus Action, you can set the blade on fire. While it burns, it sheds Bright Light in a 10-foot radius and Dim Light for an additional 10 feet, and it deals Fire damage instead of Slashing damage."),
("Rapier of the Mad Dance", "Weapon (Rapier)", "Very Rare", A, "You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, when you hit a creature with it, you can cast Irresistible Dance (save DC 17) on that creature from the rapier."),
("Greataxe of the Sundered Ward", "Weapon (Greataxe)", "Legendary", A, "You gain a +3 bonus to attack rolls and damage rolls made with this magic weapon. Damage you deal with the axe's own attacks ignores Resistance, and a creature with Immunity to that damage takes half damage instead. This doesn't apply to other damage, such as spells."),
]
