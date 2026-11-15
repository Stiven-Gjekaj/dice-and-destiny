# Original species from many regions of a large world.
# Format: (name, size, speed, description, [(trait, text), ...])

SPELL_ABILITY = ("Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells "
                 "(choose when you select this species).")

SPECIES = [
("Brinewrought", "Medium (about 5–6 feet tall)", "30 feet",
 "The Brinewrought come from tide-cut coasts and storm-beaten islands, where generations of salt and spray have worked into their blood. Pale salt crystals crust their brows and knuckles, and their voices carry over the surf. They prize a steady hand, an honest read of the weather, and debts paid before the next tide.",
 [("Creature Type", "You are a Humanoid."),
  ("Amphibious", "You can breathe air and water, and you have a Swim Speed equal to your Speed."),
  ("Salt Blood", "You have Advantage on saving throws to avoid or end the Poisoned condition, and you can drink salt water as if it were fresh."),
  ("Undertow", "When you hit a Large or smaller creature with a melee attack roll, you can pull at it like a falling tide. It makes a Strength saving throw (DC 8 plus your Constitution modifier and Proficiency Bonus). On a failed save, you pull it up to 10 feet toward you, and its Speed is 0 until the start of your next turn. You can use this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."),
  ("Tidecaller", "You know the Elementalism cantrip. At level 3, you can cast Fog Cloud once without a spell slot; at level 5, Water Walk. You regain the ability to cast each of these spells this way when you finish a Long Rest, and you can also cast them using spell slots you have. " + SPELL_ABILITY)]),

("Kilnborn", "Medium (about 5–7 feet tall)", "30 feet",
 "Kilnborn live on the slopes of fire mountains and across the black ash plains below them. Their skin is the color and texture of fired clay, crossed with fine cracks that glow when they are angry or afraid. They are makers above all, and a Kilnborn judges a life by the work that outlasts it.",
 [("Creature Type", "You are a Humanoid."),
  ("Darkvision", "You have Darkvision with a range of 60 feet."),
  ("Fired Clay", "You have Resistance to Fire damage. You are naturally adapted to hot climates, and you can handle hot coals and fresh-forged metal without harm."),
  ("Maker's Hands", "You gain proficiency with one type of Artisan's Tools of your choice."),
  ("Kiln Flare", "As a Bonus Action, you let the fire inside you blaze through the cracks in your skin for 1 minute. For the duration, you shed Bright Light in a 10-foot radius and Dim Light for an additional 10 feet, and when a creature within 5 feet of you hits you with a melee attack, it takes Fire damage equal to your Proficiency Bonus. You can use this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."),
  ("Forge Gift", "You know the Produce Flame cantrip. At level 3, you can cast Heat Metal once without a spell slot, and you regain the ability to cast it this way when you finish a Long Rest. You can also cast it using spell slots you have. " + SPELL_ABILITY)]),

("Sporekin", "Medium (about 4–6 feet tall)", "30 feet",
 "Sporekin grow in the deep caverns, in lightless forests of fungus that stretch for miles beneath the surface. Fine pale threads run through their bodies, and they drift a faint haze of spores when they speak. A Sporekin colony shares its memories through those spores, so the Sporekin value patience, consensus, and the slow, careful choice that every member can live with.",
 [("Creature Type", "You are a Humanoid."),
  ("Darkvision", "You have Darkvision with a range of 120 feet."),
  ("Spore Speech", "You can speak telepathically to any creature you can see within 30 feet of you. You don't need to share a language with it, but it must know at least one language to understand you. It can't reply telepathically."),
  ("Fungal Body", "You have Resistance to Poison damage, and you can't contract diseases."),
  ("Colony Memory", "When you finish a Long Rest, you gain proficiency in one skill of your choice, drawn from the memories of your colony. The proficiency lasts until you finish your next Long Rest."),
  ("Spore Burst", "As a Bonus Action, you release a cloud of spores. Each creature of your choice within 10 feet of you makes a Constitution saving throw (DC 8 plus your Constitution modifier and Proficiency Bonus). On a failed save, it has the Poisoned condition until the end of your next turn. You can use this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.")]),

("Glassborn", "Medium (about 5–6 feet tall)", "30 feet",
 "Glassborn come from the deep deserts, where lightning strikes the dunes and fuses the sand to glass. A fine glitter of glass covers their skin, and in strong sun they shimmer like heat over the road. Most are nomads. They hold that water is always shared, and that a guest under your tent is under your protection until sunrise.",
 [("Creature Type", "You are a Humanoid."),
  ("Storm-Fused", "You have Resistance to Lightning damage."),
  ("Desert Born", "You need only half the water that other creatures need, and you are naturally adapted to hot climates. You have Advantage on saving throws to avoid or end the Blinded condition."),
  ("Mirage", "When a creature you can see makes an attack roll against you, you can take a Reaction to bend the light around you, giving that roll Disadvantage. You can use this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."),
  ("Shimmer Gift", "You know the Minor Illusion cantrip. At level 3, you can cast Blur once without a spell slot, and you regain the ability to cast it this way when you finish a Long Rest. You can also cast it using spell slots you have. " + SPELL_ABILITY)]),

("Windkin", "Medium (about 5–6 feet tall)", "30 feet",
 "Windkin live on the high peaks, in aeries cut into cliffs where the air is thin and the wind never stops. They are light of bone, and a membrane of skin stretches from each wrist to the hip. They build no walls they can't leave, and they say that a promise made on the ground weighs nothing in the sky.",
 [("Creature Type", "You are a Humanoid."),
  ("Gliding Membranes", "When you fall and you aren't Incapacitated, you can spread your membranes. You then descend at 60 feet per round, you take no damage from the fall, and you can move up to 2 feet horizontally for every 1 foot you descend."),
  ("Mountain Lungs", "You are naturally adapted to high altitude and to cold climates, and you can hold your breath for 10 minutes."),
  ("Keen Sight", "You have proficiency in the Perception skill."),
  ("Ride the Wind", "As a Bonus Action, you leap up to 20 feet in any direction, including straight up, without provoking Opportunity Attacks. You can use this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."),
  ("Updraft", "Starting at character level 5, you can take a Bonus Action to catch a rising wind. For 10 minutes, you have a Fly Speed equal to your Speed. Once you use this trait, you can't use it again until you finish a Long Rest.")]),

("Hoarfolk", "Medium (about 5–7 feet tall)", "30 feet",
 "Hoarfolk herd and hunt across the frozen steppes and the ice-bound coasts at the edge of the world. Their hair is white or pale blue, and frost forms on their lashes when they breathe. Their winters are long and dark, and they fill them with stories, so a Hoarfolk remembers every kindness and every insult for a lifetime. No traveler is turned away from a Hoarfolk fire.",
 [("Creature Type", "You are a Humanoid."),
  ("Darkvision", "You have Darkvision with a range of 60 feet."),
  ("Winter Blood", "You have Resistance to Cold damage, and you are naturally adapted to cold climates."),
  ("Snow-Eyed", "Snow, sleet, mist, and fog don't make an area Lightly Obscured for you."),
  ("Breath of Winter", "As a Bonus Action, you exhale a freezing gust in a 15-foot Cone. Each creature in the Cone makes a Constitution saving throw (DC 8 plus your Constitution modifier and Proficiency Bonus). On a failed save, its Speed is halved and it can't take Reactions until the end of your next turn. You can use this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.")]),

("Oathborn", "Medium (about 5–6 feet tall)", "30 feet",
 "The first Oathborn stepped out of the great oaths sworn when the oldest cities were founded, and they still carry those words on their skin as lines of script that shift and rewrite themselves. They are found wherever promises matter: in courts, guildhalls, and temple archives, as witnesses, judges, and keepers of contracts. To an Oathborn, a broken promise is a wound in the world.",
 [("Creature Type", "You are a Humanoid."),
  ("Living Script", "You gain proficiency in one skill of your choice, and you know one extra language of your choice."),
  ("Unbending Word", "You have Advantage on saving throws to avoid or end the Charmed condition."),
  ("Witness", "As a Bonus Action, you open your senses to the weight of words for 1 minute. For the duration, you know when a creature within 30 feet of you that you can hear speaks a deliberate lie, though you don't learn the truth. Once you use this trait, you can't use it again until you finish a Long Rest."),
  ("Call to Account", "When a creature you can see within 30 feet of you damages you or an ally, you can take a Reaction to brand it with a glowing sigil until the end of your next turn. Your next attack roll against it before then has Advantage, and if that attack hits, it deals extra Force damage equal to your Proficiency Bonus. You can use this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.")]),

("Rootkin", "Small (about 3–4 feet tall)", "30 feet",
 "Rootkin grow from seeds that fall from the oldest trees in the deep forests. Bark patches their skin, and their leafy hair turns from green to gold to bare as the seasons pass. They are slow to anger and slower to forget, and they see themselves as the keepers of the groves that bore them.",
 [("Creature Type", "You are a Humanoid."),
  ("Deep Roots", "You have Advantage on saving throws to avoid being moved against your will or knocked Prone."),
  ("Sunfed", "If you spend at least 4 hours of a day in sunlight, you need only half the food that other creatures need. Once per Short Rest, when you spend Hit Point Dice to regain Hit Points, you regain extra Hit Points equal to your Proficiency Bonus."),
  ("Grasping Roots", "As a Bonus Action, you call roots up from the ground around you. For 1 minute, the ground within 10 feet of you is Difficult Terrain for creatures of your choice, and the roots move with you. You can use this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."),
  ("Grove Gift", "You know the Druidcraft cantrip. At level 3, you can cast Barkskin once without a spell slot; at level 5, Speak with Plants. You regain the ability to cast each of these spells this way when you finish a Long Rest, and you can also cast them using spell slots you have. " + SPELL_ABILITY)]),
]
