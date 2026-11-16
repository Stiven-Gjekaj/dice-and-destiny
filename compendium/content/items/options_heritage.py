# Original heritage items of the original species. Anyone can use them, unless the text says otherwise.
# Format: (name, category, rarity, attunement, text)
A = "Requires Attunement"
ITEMS = [
# ---------- Lumen
("Starglass Pendant", "Wondrous Item", "Common", None,
 "This pendant holds a sliver of a fallen star. On command, it sheds Dim Light in a 10-foot radius, and it always points toward the brightest star in the night sky, even under clouds."),
("Lumen Choir Harp", "Wondrous Item", "Rare", A,
 "When you play this small harp as a Magic action, each ally within 30 feet of you who can hear it gains Temporary Hit Points equal to 1d8 plus your Charisma modifier. A Lumen who plays it also ends the Frightened condition on those allies. Once used, the harp can't be used again until the next dawn."),
# ---------- Hollowborn
("Grave-Bell Ring", "Ring", "Uncommon", A,
 "While you wear this black iron ring, you have Advantage on Death Saving Throws. A Hollowborn who wears it also knows when any creature within 60 feet of them dies."),
("Shroud of the Second Death", "Wondrous Item", "Rare", A,
 "This gray burial cloth has 1 charge and regains it at dawn. When you drop to 0 Hit Points but don't die outright, you can expend the charge to drop to 1 Hit Point instead. It doesn't work if you are killed outright, and you can't use it in the same turn as Relentless Endurance, Second Death, or a similar trait. A Hollowborn who uses it also gains Temporary Hit Points equal to their Proficiency Bonus."),
# ---------- Brinewrought
("Salt-Crust Gauntlets", "Wondrous Item", "Uncommon", A,
 "These gauntlets are crusted with sea salt that never washes away. While you wear them, you have Advantage on Strength (Athletics) checks to grapple or to climb wet surfaces, and your Unarmed Strikes deal 1d6 Bludgeoning damage."),
("Tide Horn", "Wondrous Item", "Rare", None,
 "When you blow this conch shell as a Magic action, you can cast Fog Cloud or Gust of Wind from it, without spell components. A Brinewrought can also call the tide: water within 60 feet rises or falls by up to 3 feet for 1 hour. Once used, the horn can't be used again until the next dawn."),
# ---------- Kilnborn
("Kiln-Fired Hammer", "Weapon (Light Hammer)", "Uncommon", None,
 "You have a +1 bonus to attack and damage rolls made with this magic weapon. A Kilnborn who wields it can make it glow red-hot as a Bonus Action; until the end of the turn, a hit with it deals an extra 1d6 Fire damage."),
("Ashen Apron", "Wondrous Item", "Common", None,
 "While you wear this heavy apron, you have Resistance to Fire damage from forges, kilns, and other nonmagical fires, and sparks and splashes of molten metal don't harm you."),
# ---------- Sporekin
("Spore Lantern", "Wondrous Item", "Common", None,
 "This lantern holds glowing fungus instead of a flame. It sheds Dim Light in a 20-foot radius forever, and creatures that rely on light to find prey don't notice it."),
("Memory Cap", "Wondrous Item", "Rare", A,
 "This soft cap is grown from a Sporekin colony. While you wear it, you gain proficiency in one skill of your choice, which you can change when you finish a Long Rest. A Sporekin who wears it can also store one memory of up to 1 minute in the cap and let another creature who wears it live that memory."),
# ---------- Glassborn
("Dune Glass Lens", "Wondrous Item", "Common", None,
 "While you look through this lens of fused sand, bright sun and glare don't hinder your sight, and you can see heat shimmer that shows where a creature passed in the last hour."),
("Mirage Cloak", "Wondrous Item", "Rare", A,
 "This cloak shimmers like hot air over sand. As a Reaction when a creature you can see makes an attack roll against you, you can give the roll Disadvantage. A Glassborn can use this property twice. You regain all uses at dawn."),
# ---------- Windkin
("Aerie Feather Cloak", "Wondrous Item", "Uncommon", A,
 "While you wear this cloak, you fall at 60 feet per round and take no damage from falling. A Windkin who wears it can also glide 3 feet horizontally for every 1 foot they descend."),
("Wind Chime of the High Peaks", "Wondrous Item", "Uncommon", None,
 "When this chime rings by itself, a storm will reach your location within 24 hours. As a Magic action, you can ring it to cast Gust of Wind from it. Once used this way, it can't be used again until the next dawn."),
# ---------- Hoarfolk
("Frost-Bead Necklace", "Wondrous Item", "Common", None,
 "While you wear this necklace of blue beads, you are comfortable in cold down to the coldest winter night, and your breath doesn't freeze or show in the cold."),
("Storyteller's Fire Stone", "Wondrous Item", "Uncommon", None,
 "When you place this round stone on the ground and speak a word, it burns with a warm smokeless fire for 8 hours. Creatures that finish a Long Rest beside it have Advantage on their next saving throw against Exhaustion. A Hoarfolk who tells a story by this fire can make each listener remember the story word for word."),
# ---------- Oathborn
("Witness Quill", "Wondrous Item", "Uncommon", None,
 "Words written with this quill can't be changed or erased by any nonmagical means. If a creature signs a contract written with it and then knowingly breaks the contract, the signature glows red, and the writer of the contract learns of it."),
("Seal of the Kept Word", "Ring", "Rare", A,
 "While you wear this signet ring, you have Advantage on saving throws against the Charmed condition. As a Magic action, you can press it into wax on a promise; for 30 days, you know if the creature who made the promise breaks it. An Oathborn can have two such promises at a time; anyone else can have one."),
# ---------- Rootkin
("Seed of the Mother Tree", "Wondrous Item", "Uncommon", None,
 "When you plant this seed and water it, a tree grows from it in 1 minute and gives shade and shelter for up to eight creatures for 8 hours, then becomes an ordinary tree. A Rootkin who plants it can speak with the tree for as long as it lives."),
("Barkskin Bracers", "Wondrous Item", "Rare", A,
 "While you wear these bracers of living bark, your AC can't be lower than 15, whatever armor you wear. A Rootkin who wears them also regains 1 Hit Point at the start of each of their turns while they stand in sunlight and have at least 1 Hit Point."),
# ---------- Peatborn
("Bog Ancestor's Charm", "Wondrous Item", "Uncommon", A,
 "This charm holds a lock of hair from a preserved ancestor. Once per day, you can ask it for advice and gain Advantage on one Intelligence or Wisdom check. A Peatborn can ask it a yes-or-no question about the swamp where it was made, and it answers truly."),
("Mire Boots", "Wondrous Item", "Uncommon", None,
 "While you wear these boots, mud, bogs, and swamp water aren't Difficult Terrain for you, and you can walk on the surface of mud and wet sand as if it were firm ground."),
# ---------- Rillfolk
("Ferryman's Coin", "Wondrous Item", "Common", None,
 "When you drop this coin into a river, it shows you the safest place to cross within 1 mile, by glinting at that spot. It then returns to your hand."),
("River Ring", "Ring", "Uncommon", A,
 "While you wear this ring, you have a Swim Speed equal to your Speed, and you can hold your breath for twice as long as normal. A Rillfolk who wears it can also swim at twice their Swim Speed when they move with the current."),
# ---------- Sunrunner
("Horse-Tail Fetish", "Wondrous Item", "Common", None,
 "A mount whose bridle has this charm tied to it doesn't tire from a forced march, and it never panics from loud noises or fire."),
("Saddle of the Endless Steppe", "Wondrous Item", "Rare", None,
 "A mount that wears this saddle has its Speed increased by 20 feet, and it can travel for 12 hours a day without risking Exhaustion. A Sunrunner who rides it can take the Dash action for the mount as a Bonus Action."),
# ---------- Hushfolk
("Silence Stone", "Wondrous Item", "Uncommon", None,
 "When you squeeze this smooth black stone, sound can't leave a 10-foot-radius Sphere centered on it for 10 minutes, though sound can enter it. Once used, the stone can't be used again until the next dawn."),
("Echo Cloak", "Wondrous Item", "Rare", A,
 "While you wear this cloak, you make no sound when you move, and you have Advantage on Dexterity (Stealth) checks that rely on silence. A Hushfolk who wears it also gains Blindsight with a range of 30 feet."),
# ---------- Dreamborn
("Dreamcatcher of Soft Nights", "Wondrous Item", "Common", None,
 "A creature that sleeps beneath this dreamcatcher can't be harmed or contacted by magic that enters dreams, such as the Dream spell."),
("Pillow of Shared Dreams", "Wondrous Item", "Rare", None,
 "Up to four creatures who sleep within 10 feet of this pillow share one dream that the pillow's owner shapes. They can talk and plan in the dream, and each remembers it on waking. A Dreamborn who shapes the dream can also reach one sleeping creature they know within 100 miles and bring it into the dream for a short time."),
# ---------- Gloamkin
("Dusk Lantern", "Wondrous Item", "Uncommon", None,
 "This lantern sheds no light. Instead, it fills a 20-foot radius with Dim Light, even in bright sunlight. A Gloamkin can use Shadow Step to and from this area as if it were dim by nature."),
("Shadow-Silk Gloves", "Wondrous Item", "Rare", A,
 "While you wear these gloves, you can take the Hide action as a Bonus Action while you are in Dim Light or Darkness. A Gloamkin who wears them can also step through one shadow into another within 60 feet once per Short Rest, as a Bonus Action."),
# ---------- Cairnborn
("Cairn Stone", "Wondrous Item", "Common", None,
 "This flat stone remembers names. When you place it on a grave and speak the name of the one buried there, anyone who touches the stone later hears the name and one sentence about that person."),
("Standing-Stone Shield", "Armor (Shield)", "Rare", A,
 "You have a +1 bonus to AC while you hold this heavy shield of gray stone. If you don't move on your turn, the bonus becomes +2 until the start of your next turn. A Cairnborn who holds it can't be moved against their will while Standing Stone is active."),
# ---------- Foldfolk
("Fireproof Wax Coat", "Wondrous Item", "Uncommon", A,
 "While you wear this coat of waxed paper, you have Resistance to Fire damage. For a Foldfolk, this Resistance and their Vulnerability to Fire damage cancel out, so they take normal Fire damage."),
("Book of Living Pages", "Wondrous Item", "Rare", None,
 "This book has 100 blank pages. When you touch a page to written text, the page copies it perfectly. A Foldfolk can also fold one page into a small paper messenger, which flies up to 10 miles to a creature they know and delivers a message of up to 25 words. Once used this way, the book can't make another messenger until the next dawn."),
# ---------- Feverblooded
("Plague Nurse's Kit", "Wondrous Item", "Uncommon", None,
 "This kit has 10 uses. As a Utilize action, you can expend one use to end the Poisoned condition or one disease on a creature. A Feverblooded who uses it also restores Hit Points equal to their Proficiency Bonus to that creature."),
("Ward Bell of the Walled Town", "Wondrous Item", "Rare", None,
 "When you ring this bell, it keeps disease out of a 100-foot radius for 24 hours. Creatures in the area can't contract diseases, and they have Advantage on saving throws against the Poisoned condition. Once used, the bell can't be used again until the next dawn."),
# ---------- Relicborn
("Ruin Compass", "Wondrous Item", "Uncommon", None,
 "This compass points toward the nearest magic item within 1 mile that isn't carried by a creature. A Relicborn can also name a kind of item, such as a weapon or a ring, and the compass points to the nearest one of that kind."),
("Imperial Ward Circlet", "Wondrous Item", "Rare", A,
 "While you wear this old circlet, you have Advantage on saving throws against traps and against spells cast by Constructs and by magic items. A Relicborn who wears it can also cast Dispel Magic from it once, regaining the ability at dawn."),
]
