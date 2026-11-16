# Edition 2, items batch 9: wondrous items (mostly Common and Uncommon), staffs, ammunition, scrolls, and armor.
# (name, category, rarity, attunement, text)
A = "Requires Attunement"
AS = "Requires Attunement by a Spellcaster"
W = "Wondrous Item"
ITEMS = [
# ================= WONDROUS ITEMS =================
("Pocket Spring", W, "Common", None, "This smooth river stone is always wet. Once per dawn, you can squeeze it over a container to fill it with up to 1 gallon of clean, cold water."),
("Bootblack Tin", W, "Common", None, "Boots polished with the black wax in this tin stay clean and shiny for a week, and they never squeak. The tin refills itself at each new moon."),
("Weatherwise Harmonica", W, "Common", None, "When you play this harmonica outdoors for 1 minute, the tune it plays tells you what the weather will be for the next 24 hours, as well as a local farmer could guess it."),
("Lucky Copper", W, "Common", None, "When you flip this worn copper coin and call the side, it lands on the side you call. It has no effect on dice or other games of chance."),
("Kitchen Spirit Doll", W, "Common", None, "Set this small straw doll beside a cooking pot. While it sits there, the pot stirs itself, and food in it never burns or boils over."),
("Signet of the Unbroken Seal", W, "Common", None, "Wax seals stamped with this ring glow faintly red if the seal has been broken and closed again, even if a careful hand repaired it."),
("Shepherd's Bell", W, "Common", None, "When you ring this little brass bell, domestic animals within 300 feet that belong to you or your companions come toward the sound, if they can."),
("Familiar's Perch", W, "Uncommon", AS, "This silver perch is shaped like a branch. Once per dawn, you can cast Find Familiar from it, without material components. While your familiar sits on the perch, it can't be harmed by effects that it can't see coming."),
("Wayside Prayer Beads", W, "Uncommon", None, "Once per dawn, you can tell these wooden beads as a Magic action to cast Prayer of Healing from them."),
("Satchel of Restoration", W, "Uncommon", None, "This leather satchel holds clean bandages and bitter herbs that never run out. It has 2 charges and regains all expended charges daily at dawn. You can expend 1 charge to cast Lesser Restoration from it."),
("Rope of the Hidden Room", W, "Uncommon", None, "Once per dawn, you can throw this 60-foot silk rope into the air and cast Rope Trick from it."),
("Grease Pot", W, "Uncommon", None, "This clay pot has 3 charges and regains all expended charges daily at dawn. As a Magic action, you can expend 1 charge to throw a glob of grease and cast Grease (save DC 13) from it."),
("Brazier of the Wayfarer's Rest", W, "Rare", None, "Once per dawn, you can light this small iron brazier as a Magic action to cast Tiny Hut from it. The dome is centered on the brazier, and it ends early if the brazier is moved or goes out."),
("Jar of the Giant Bee", W, "Rare", A, "This honey jar holds a single sleeping bee. Once per dawn, you can open it as a Magic action to cast Giant Insect from it."),
("Bell of Hallowed Ground", W, "Very Rare", None, "Once per 7 days, you can ring this large bronze bell for 24 hours to cast Hallow from it, without material components. The bell must hang within the area of the spell."),
# ================= STAFFS =================
("Druid's Walking Staff", "Staff", "Uncommon", "Requires Attunement by a Druid or Ranger", "This knotted staff can be wielded as a Quarterstaff. While holding it, you can cast Shillelagh and Guidance from it at will."),
("Staff of the Swift Dragon", "Staff", "Rare", AS, "This staff can be wielded as a Quarterstaff. It has 7 charges and regains 1d6 + 1 expended charges daily at dawn. While holding it, you can expend 2 charges to cast Dragon's Breath (save DC 15) from it, or 3 charges to cast Haste from it."),
("Staff of the Crooked Will", "Staff", "Rare", AS, "This twisted staff can be wielded as a Quarterstaff. It has 7 charges and regains 1d6 + 1 expended charges daily at dawn. While holding it, you can expend charges to cast one of the following spells from it (save DC 15): Bane (1 charge), Ray of Enfeeblement (2 charges), or Compulsion (4 charges)."),
("Staff of the Awakened Wood", "Staff", "Very Rare", "Requires Attunement by a Druid", "This staff of living wood is a magic Quarterstaff that grants a +2 bonus to attack rolls and damage rolls made with it. It has 10 charges and regains 1d6 + 4 expended charges daily at dawn. While holding it, you can expend charges to cast one of the following spells from it, without material components: Commune with Nature (5 charges), Awaken (5 charges), or Conjure Fey (6 charges)."),
("Staff of Planar Binding", "Staff", "Very Rare", AS, "This staff is a magic Quarterstaff that grants a +2 bonus to attack rolls and damage rolls made with it. It has 10 charges and regains 1d6 + 4 expended charges daily at dawn. While holding it, you can expend charges to cast one of the following spells from it (save DC 17), without material components: Planar Binding (5 charges) or Planar Ally (6 charges)."),
("Staff of the Celestial Choir", "Staff", "Legendary", "Requires Attunement by a Cleric or Paladin", "This white staff is a magic Quarterstaff that grants a +3 bonus to attack rolls and damage rolls made with it. It has 20 charges and regains 2d8 + 4 expended charges daily at dawn. While holding it, you can expend charges to cast one of the following spells from it: Prayer of Healing (2 charges), Conjure Celestial (7 charges), or Power Word Heal (9 charges)."),
# ================= AMMUNITION =================
("Chalk-Tipped Arrow", "Ammunition", "Common", None, "This blunt arrow deals no damage. Instead, it leaves a bright chalk mark of the color you choose on whatever it hits. The mark can't be washed off for 1 day. Found in bundles of 1d6 + 2."),
("Arrow of the Sure Path", "Ammunition", "Uncommon", None, "Wind doesn't affect this arrow, and an attack made with it ignores Half Cover. Found in bundles of 1d4 + 1."),
("Bolt of Sickness", "Ammunition", "Uncommon", None, "On a hit, the target takes an extra 2d8 Poison damage and makes a DC 13 Constitution save. On a failed save, it has the Poisoned condition until the end of its next turn. Found in bundles of 1d4."),
("Arrow of the Long Pull", "Ammunition", "Rare", None, "On a hit, a Large or smaller target makes a DC 15 Strength save. On a failed save, it is pulled up to 30 feet in a straight line toward you. Found in bundles of 1d4."),
("Bolt of Compulsion", "Ammunition", "Rare", None, "On a hit, the target makes a DC 15 Wisdom save. On a failed save, on its next turn it must use all its movement to move in a direction you choose when you hit, by the safest route. It doesn't have to move into obvious danger. The bolt then crumbles."),
("Arrow of Harm", "Ammunition", "Very Rare", None, "On a hit, the target makes a DC 17 Constitution save, as if it were the target of the Harm spell, instead of taking the arrow's normal damage. The arrow is then destroyed."),
("Arrow of the Burning Cloud", "Ammunition", "Legendary", None, "When this arrow hits a creature or a point within the weapon's range, it bursts into an Incendiary Cloud (save DC 19) centered on that point. The cloud lasts for 1 minute and doesn't require Concentration. The arrow is destroyed."),
# ================= SCROLLS =================
("Scroll of the Last Watch", "Scroll", "Common", None, "As a Bonus Action, you read this scroll over a creature that has 0 Hit Points and isn't dead. The creature becomes Stable. The scroll then turns to dust."),
("Scroll of the Honest Hour", "Scroll", "Uncommon", None, "As a Magic action, you read this scroll aloud to cast Zone of Truth (save DC 13). The scroll then turns to dust."),
("Scroll of the Water-Kin", "Scroll", "Rare", None, "As a Magic action, you read this scroll aloud. For 24 hours, you and up to nine willing creatures within 30 feet of you can breathe underwater, as if from the Water Breathing spell. The scroll then turns to dust."),
("Scroll of the Binding Oath", "Scroll", "Very Rare", None, "As a Magic action, you read this scroll aloud and name a creature you can see within 60 feet to cast Geas (save DC 17) on it. The scroll then turns to dust."),
("Scroll of the Guarded House", "Scroll", "Very Rare", None, "Reading this scroll aloud takes 1 hour. When you finish, you cast Guards and Wards, without material components. The scroll then turns to dust."),
("Scroll of the Second Body", "Scroll", "Legendary", None, "Reading this scroll aloud takes 1 hour. When you finish, you cast Clone. You still need a cubic inch of the creature's flesh, but no other materials and no vessel: the scroll becomes the vessel, rolled around the growing body."),
# ================= ARMOR =================
("Tidy Traveler's Leathers", "Armor (Leather)", "Common", None, "Dust, mud, and rain slide off this leather armor, and it always looks freshly oiled."),
("Heraldic Shield", "Armor (Shield)", "Common", None, "As a Bonus Action, you can change the coat of arms painted on this shield to any design you have seen or can describe."),
("Chain Mail of the Faithful", "Armor (Chain Mail)", "Uncommon", A, "You have a +1 bonus to AC while wearing this armor. Once per dawn, you can cast Divine Favor from it."),
("Half Plate of the Living Aura", "Armor (Half Plate)", "Rare", A, "You have a +1 bonus to AC while wearing this armor. Once per dawn, you can cast Aura of Life from it."),
("Plate of the Untouched", "Armor (Plate)", "Very Rare", A, "You have a +2 bonus to AC while wearing this armor. Once per dawn, you can cast Antilife Shell from it."),
("Studded Leather of the Ghost Step", "Armor (Studded Leather)", "Legendary", A, "You have a +3 bonus to AC while wearing this armor. Once per dawn, you can cast Etherealness from it, targeting only yourself."),
]
