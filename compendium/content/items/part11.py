# Edition 2, items batch 8: weapons, wands, rings, and rods, with spells that no item used before.
# (name, category, rarity, attunement, text)
A = "Requires Attunement"
AS = "Requires Attunement by a Spellcaster"
ITEMS = [
# ================= WEAPONS =================
("Cobbler's Hammer", "Weapon (Light Hammer)", "Common", None, "A nail struck with this small hammer sinks in with a single tap and never bends. Shoes you mend with it last twice as long."),
("Herbalist's Sickle", "Weapon (Sickle)", "Common", None, "Herbs and flowers you cut with this silver sickle stay fresh for a week. While holding it, you can cast Druidcraft from it at will."),
("Lantern Pole", "Weapon (Quarterstaff)", "Common", None, "A brass hook on the end of this quarterstaff holds a cold, clear light. On command, the hook sheds Bright Light in a 20-foot radius and Dim Light for an additional 20 feet, or goes dark."),
("Rapier of the Quick Riposte", "Weapon (Rapier)", "Uncommon", A, "You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, when a creature within 5 feet of you misses you with a melee attack, you can take a Reaction to make one attack with the rapier against that creature."),
("Moon-Edge Scimitar", "Weapon (Scimitar)", "Uncommon", A, "Its blade sheds Dim Light in a 5-foot radius. While holding it, you can cast Starry Wisp (+5 to hit) from it at will. The cantrip's damage grows with your level as normal."),
("Mace of the Sacred Flame", "Weapon (Mace)", "Uncommon", A, "While holding it, you can cast Sacred Flame (save DC 13) from it at will. The cantrip's damage grows with your level as normal."),
("Spear of the Grasping Root", "Weapon (Spear)", "Uncommon", None, "You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, you can cast Ensnaring Strike (save DC 13) from it."),
("Crossbow of the Guiding Light", "Weapon (Light Crossbow)", "Uncommon", None, "You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, you can cast Guiding Bolt (+5 to hit) from it."),
("Blade of the Searing Oath", "Weapon (Longsword)", "Rare", A, "You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, you can cast Searing Smite (save DC 15) from it."),
("Sleepthorn Shortsword", "Weapon (Shortsword)", "Rare", A, "You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, you can cast Sleep (save DC 15) from it."),
("Hammer of Making", "Weapon (Warhammer)", "Rare", A, "You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, you can cast Fabricate from it."),
("Dagger of the Piercing Thought", "Weapon (Dagger)", "Rare", A, "You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon. When you throw it, it flies back to your hand after the attack. Once per dawn, you can cast Mind Spike (save DC 15) from it."),
("Longbow of the Ice Knife", "Weapon (Longbow)", "Rare", A, "You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. It has 3 charges and regains all expended charges daily at dawn. When you fire it, you can expend 1 charge to cast Ice Knife (save DC 15) from it instead of making a normal attack."),
("Greatsword of the Watchful Spirit", "Weapon (Greatsword)", "Very Rare", A, "You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, you can cast Guardian of Faith (save DC 17) from it."),
("Maul of the Giant's Grip", "Weapon (Maul)", "Very Rare", A, "You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, as a Bonus Action, you can cast Enlarge/Reduce from it, targeting only yourself and choosing Enlarge. The effect lasts 1 minute and doesn't require Concentration."),
("Flail of Confusion", "Weapon (Flail)", "Very Rare", A, "You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, you can cast Confusion (save DC 17) from it."),
("Lance of the Faithful Steed", "Weapon (Lance)", "Very Rare", A, "You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, you can cast Find Steed from it. A steed you summon this way has a Fly Speed equal to its Speed."),
("Blade of the Divine Word", "Weapon (Longsword)", "Legendary", A, "You gain a +3 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, you can raise it and cast Divine Word (save DC 19) from it."),
("Crossbow of the Slow Fuse", "Weapon (Heavy Crossbow)", "Legendary", A, "You gain a +3 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, you can fire a glowing bolt from it to cast Delayed Blast Fireball (save DC 19), with the bead at the point where the bolt lands."),
("Whip of the Beast Lord", "Weapon (Whip)", "Legendary", A, "You gain a +3 bonus to attack rolls and damage rolls made with this magic weapon. Once per dawn, you can crack it at a creature you can see within 60 feet to cast Dominate Monster (save DC 19) from it."),
# ================= WANDS =================
("Wand of Minor Illusions", "Wand", "Common", None, "While holding this wand, you can cast Minor Illusion from it at will."),
("Wand of the Chromatic Orb", "Wand", "Uncommon", AS, "This wand has 7 charges and regains 1d6 + 1 expended charges daily at dawn. While holding it, you can expend 1 charge to cast Chromatic Orb (+5 to hit) from it. For each additional charge you expend, the spell's level increases by 1, to a maximum of level 3."),
("Wand of Sleet Storms", "Wand", "Rare", AS, "This wand has 7 charges and regains 1d6 + 1 expended charges daily at dawn. While holding it, you can expend 3 charges to cast Sleet Storm (save DC 15) from it."),
("Wand of Enthralling Words", "Wand", "Rare", AS, "This wand has 7 charges and regains 1d6 + 1 expended charges daily at dawn. While holding it, you can expend 1 charge to cast Charm Person (save DC 15) from it, or 2 charges to cast Enthrall (save DC 15) from it."),
("Wand of the Restless Grave", "Wand", "Very Rare", AS, "This wand of black iron has 7 charges and regains 1d6 + 1 expended charges daily at dawn. While holding it, you can expend 3 charges to cast Animate Dead from it, or 6 charges to cast Create Undead from it, without material components. Undead made with the wand crumble to dust 24 hours after they rise, and casting a spell from the wand again doesn't extend that time."),
("Wand of the Sevenfold Wall", "Wand", "Legendary", AS, "This wand of rainbow glass has 7 charges and regains 1d6 + 1 expended charges daily at dawn. While holding it, you can expend 7 charges to cast Prismatic Wall (save DC 18) from it."),
# ================= RINGS =================
("Ring of Small Wonders", "Ring", "Common", None, "While wearing this ring, you can cast Thaumaturgy from it at will."),
("Ring of the Mage's Skin", "Ring", "Uncommon", A, "Once per dawn, you can cast Mage Armor from this ring, targeting only yourself."),
("Ring of the Stubborn Heart", "Ring", "Uncommon", A, "While wearing this ring, you have Advantage on Death Saving Throws. Once per dawn, you can cast False Life from it, targeting only yourself."),
("Ring of Many Tongues", "Ring", "Rare", A, "Once per dawn, you can cast Tongues from this ring, targeting only yourself."),
("Ring of the Bright Bubble", "Ring", "Rare", A, "Once per dawn, you can cast Resilient Sphere (save DC 15) from this ring, without material components."),
("Ring of the Waiting Spell", "Ring", "Very Rare", AS, "Once per 7 days, you can cast Contingency through this ring, without material components. The ring takes the place of the statuette, and the contingent spell must be of level 5 or lower. The contingency ends if you take off the ring."),
("Ring of the Wandering Soul", "Ring", "Legendary", A, "Once per 7 days, you can cast Astral Projection from this ring, targeting only yourself and without material components."),
# ================= RODS =================
("Rod of the Messenger Bird", "Rod", "Uncommon", None, "This rod has 3 charges and regains all expended charges daily at dawn. While holding it, you can expend 1 charge to cast Animal Messenger from it."),
("Rod of the Hidden Trail", "Rod", "Rare", A, "Once per dawn, you can cast Nondetection from this rod, without material components. While you hold it, you leave no tracks."),
("Rod of the Unseen Chest", "Rod", "Rare", A, "This rod has a small hollow in its head. Once per dawn, you can cast Secret Chest from it, using the hollow as the replica instead of the costly materials. The hidden chest returns when you use the rod again."),
("Rod of the Living Tools", "Rod", "Very Rare", A, "Once per dawn, you can cast Animate Objects from this rod."),
("Rod of the Long Road Home", "Rod", "Very Rare", A, "When you finish a Long Rest, you can touch this rod to the ground to mark the place. Once per dawn, you can cast Word of Recall from the rod, returning to the marked place instead of a sanctuary."),
("Rod of the Shunned Ground", "Rod", "Legendary", A, "Once per dawn, you can cast Antipathy/Sympathy (save DC 19) from this rod, without material components."),
("Rod of the Empty Mind", "Rod", "Legendary", A, "Once per dawn, you can cast Befuddlement (save DC 19) from this rod."),
]
