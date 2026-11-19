"""The treasures of Act I of The Dawnwatch, Book One (chapters 2 to 5).

Each entry is (name, category, rarity, attunement, text), as in content/items/.
The black stone carries a Mark. Chapter 4 teaches the Mark with the Marks rules of the Compendiums.
"""
A = "Requires Attunement"
W = "Wondrous Item"

ITEMS = [
("The Black Stone", W, "Artifact", None,
 "A smooth black stone as big as a plum. It is always cold, and it hums against the skin. It is a piece of the crystal of the Unlit King. "
 "It hums louder when a member of the Hush is within 300 feet. Very rarely, the Unlit King speaks through it. "
 "The Mark. A creature that carries the stone for one day takes the open Taint of the Black Stone, with its track at 0. "
 "Benefit. You have Darkvision out to 60 feet, or 30 feet more if you already have it. As a Bonus Action, you can draw on the stone for 1 minute. "
 "For that time, your weapon attacks and your cantrips deal an extra 1d6 Necrotic damage on a hit, and magical Darkness doesn't stop your Darkvision. "
 "You can do this once, and you regain the use when you finish a Short or Long Rest. "
 "Cost. The stone is a lamp in the dark for the Unlit King, and the Hush can feel it too: a member of the Hush within 1 mile of you knows the direction to you. "
 "You have Disadvantage on saving throws against the Charmed and Frightened conditions from a member of the Hush. "
 "A piece of the Dawnfire burns you: when you touch one, you take 1d6 Radiant damage. "
 "Grows. Each time you draw on the stone. "
 "Thresholds. At 2, you dream of cold crystal each night. Once between Long Rests, you can hold the stone and learn the direction to the nearest piece of the Dawnfire within 10 miles. "
 "The extra damage becomes 1d8. At 4, your shadow falls a moment late. A member of the Hush thinks that you are one of them until you attack it, "
 "and you have Disadvantage on attack rolls while you are in the Bright Light of a piece of the Dawnfire. "
 "Crisis. At 5, you choose. Give in: you can draw on the stone twice between rests, the extra damage becomes 2d8, and as a Bonus Action while you draw on it, "
 "you can teleport up to 30 feet from a space in Dim Light or Darkness to another space in Dim Light or Darkness that you can see. "
 "Key moments: when a piece of the Dawnfire is in your reach and no ally can see you, the GM steers you to cover it or to carry it into the dark. "
 "Break free: the stone cracks across its middle, and the Mark ends. The scar: a thin grey line in one eye. You keep the Darkvision of the benefit. "
 "Ending. Hold the stone in the light of a piece of the Dawnfire from dusk to dawn. You take the Radiant damage of the cost at the start of each hour, and this damage can't be reduced. "
 "At dawn, the Mark ends. After you give in, an ally must hold the stone with you for the full night, and that ally takes the same damage. "
 "The stone stays whole and cold, and the next creature to carry it for a day takes the Mark with its track at 0."),
("The Ember of Saint Ivo", W, "Artifact", A,
 "A coal as big as a walnut, in a cage of old gold on a chain. It never goes cold, and it never burns the hand that holds it, unless that hand carries the black stone. "
 "It is a piece of the Dawnfire. The Church of the Five Sleepers keeps it as a holy relic and does not know what it does. "
 "The Ember sheds Bright Light in a 20-foot radius and Dim Light for 20 feet more. Nothing can put the light out except the rite of the Hush (chapter 4). "
 "While you are attuned to the Ember, you gain these benefits. "
 "Dawn Warmth. You and each ally within its Bright Light have Advantage on saving throws against the Frightened condition. "
 "Ward of the Fire. Magical Darkness can't exist inside its Bright Light. A creature of the Hush that starts its turn in the Bright Light has Disadvantage on attack rolls until the start of its next turn. "
 "Kindle. Once, as a Magic action, you can cast Lesser Restoration or Daylight from the Ember. You regain the use at dawn. "
 "The Wick in the Fire. When the Ember is within 5 feet of Wick, the two flames lean toward each other, and Wick feels very warm and cannot say why."),
("Compass of the Old Road", W, "Uncommon", None,
 "A brass compass of Ostrey, green with age, with a sun on its lid. Its needle points north, except on a road that Ostrey built. On such a road, it points along the road toward the nearest town of Ostrey, "
 "even if that town is now a ruin. While you hold the compass, you have Advantage on Wisdom (Survival) checks to keep your way. "
 "Once, when the party is lost, you can open the compass and know at once the way back to the last road that you traveled. You regain the use at dawn."),
("Mask of the Fifth Sleeper", W, "Uncommon", A,
 "A painted mask of wood and gold leaf, made for a play about the Dawnwatch. A thousand pilgrims touched it for luck, and some of their faith stayed in it. "
 "While you wear it, you have Advantage on Charisma (Performance) checks, and you can cast Disguise Self from it once, with no spell slot. You regain the use at dawn. "
 "When you take the mask off, the face of the person who wore it last is on the inside for a moment, and then it is gone."),
("Kell Warden's Shield", "Armor (Shield)", "Uncommon", None,
 "A round shield of oak and bronze with a rising sun on its face, from the shrine at Kell. While you hold this shield, you have a +1 bonus to Armor Class. "
 "This bonus is in addition to the shield's normal bonus to AC. When a member of the Hush is within 60 feet of you, the sun on the shield sheds Dim Light in a 5-foot radius."),
("Gauntry War Banner", W, "Rare", A,
 "A red banner on a black pole, with the iron gauntlet of the house of Gauntry. While you hold it, each ally within 30 feet of you that can see it has Advantage on saving throws against the Frightened condition. "
 "Once, as a Bonus Action, you can plant the banner in the ground. You and each ally within 30 feet of it gain Temporary Hit Points equal to 2d6 plus your Proficiency Bonus. "
 "You regain the use at dawn."),
]
