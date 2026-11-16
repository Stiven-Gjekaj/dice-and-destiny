# Original species from the moors, the libraries, the plague towns, and the ruins of old empires.
# Format: (name, size, speed, description, [(trait, text), ...])

SPELL_ABILITY = ("Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells "
                 "(choose when you select this species).")
USES = ("You can use this trait a number of times equal to your Proficiency Bonus, "
        "and you regain all expended uses when you finish a Long Rest.")

SPECIES = [
("Cairnborn", "Medium (about 6–7 feet tall)", "30 feet",
 "On the windswept moors stand rings of old stones, and over a century some of those stones wake. The Cairnborn who step out of them are broad, gray, and patient, with lichen in the creases of their skin. Each one remembers the names of everyone buried under its home ring. They value their lineage, and they make decisions slowly, because they keep them forever.",
 [("Creature Type", "You are a Humanoid."),
  ("Darkvision", "You have Darkvision with a range of 60 feet."),
  ("Weight of Ages", "You count as one size larger when you determine your carrying capacity and the weight you can push, drag, or lift. You have Advantage on Strength checks that you make to push, pull, or lift."),
  ("Long Memory", "You have proficiency in the History skill."),
  ("Standing Stone", "At the end of a turn in which you didn't move at all (you used none of your Speed, and no creature or effect moved you), you can set like stone. Until the start of your next turn, you have Resistance to Bludgeoning, Piercing, and Slashing damage. " + USES)]),

("Foldfolk", "Medium (about 5–6 feet tall) or Small (about 3–4 feet tall), chosen when you select this species", "30 feet",
 "Long ago, an order of scribes folded people out of paper and ink to keep its libraries when the scribes were gone. The order is forgotten, but the Foldfolk remain. Their bodies are layers of paper, their veins are lines of ink, and their skin carries faded text in a hundred hands. They are not soldiers or servants. They are keepers, and they value knowledge that is kept, copied, and passed on.",
 [("Creature Type", "You are a Humanoid."),
  ("Paper Body", "You have Vulnerability to Fire damage. You have Resistance to Psychic damage, because a mind written in ink is hard to smudge."),
  ("Living Text", "When you finish a Long Rest, you can rewrite the text on your skin to learn one language of your choice. You know that language until you finish your next Long Rest."),
  ("Fold Flat", "As an Action, you fold yourself to the thickness of a book. While folded, you can move through a gap as narrow as 1 inch, you have Advantage on Dexterity (Stealth) checks, and you can't make attack rolls or cast spells. You can unfold as a Bonus Action."),
  ("Scribe's Gift", "You know the Mending cantrip. At level 3, you can cast Comprehend Languages once without a spell slot; at level 5, Locate Object. You regain the ability to cast each of these spells this way when you finish a Long Rest, and you can also cast them using spell slots you have. " + SPELL_ABILITY)]),

("Feverblooded", "Medium (about 5–6 feet tall)", "30 feet",
 "Generations ago, a great plague burned through the land, and the Feverblooded are the children of those who lived. The sickness still sleeps in their blood, and it shows as a flush of color on the cheeks and hands that never fades. They live in walled towns that still remember the plague years. They value care for the sick, cleanliness, and the hard discipline that kept their ancestors alive.",
 [("Creature Type", "You are a Humanoid."),
  ("Plague Survivor", "You can't contract diseases, and you have Resistance to Poison damage."),
  ("Plague Nurse", "You have proficiency in the Medicine skill."),
  ("Burning Blood", "When you fail a Constitution saving throw, you can succeed instead. Once you use this trait, you can't use it again until you finish a Long Rest."),
  ("Draw the Fever", "As an Action, you touch a creature and draw its sickness into your blood. Choose the Poisoned condition or one disease on the creature. That condition or disease ends on the creature, and the creature regains Hit Points equal to your Proficiency Bonus. The sickness you draw in sleeps in your blood and has no effect on you. " + USES)]),

("Relicborn", "Medium (about 5–6 feet tall)", "30 feet",
 "Relicborn live among the ruins of a fallen empire, in the shells of its cities and the halls of its vaults. The old wards and magic of that empire soaked into their families over the centuries, and now faint lines of light trace their skin when they near anything enchanted. They are salvagers and scholars. They value the warnings of history, and their first rule is to never repeat the mistakes that ended the empire.",
 [("Creature Type", "You are a Humanoid."),
  ("Darkvision", "You have Darkvision with a range of 60 feet."),
  ("Ruin Sense", "You can cast Detect Magic without a spell slot. " + USES),
  ("Trapwise", "You have Advantage on saving throws against traps, and on Wisdom (Perception) and Intelligence (Investigation) checks that you make to find traps."),
  ("Old Blood", "You can attune to a magic item in 1 minute, instead of during a Short Rest."),
  ("Relic Gift", "You know the Light cantrip. At level 3, you can cast Identify once without a spell slot; at level 5, Arcane Lock. You regain the ability to cast each of these spells this way when you finish a Long Rest, and you can also cast them using spell slots you have. " + SPELL_ABILITY)]),
]
