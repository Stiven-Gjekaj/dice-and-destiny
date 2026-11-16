# Original species from the swamps, rivers, steppes, deep cities, and the edges of other planes.
# Format: (name, size, speed, description, [(trait, text), ...])

SPELL_ABILITY = ("Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells "
                 "(choose when you select this species).")
USES = ("You can use this trait a number of times equal to your Proficiency Bonus, "
        "and you regain all expended uses when you finish a Long Rest.")

SPECIES = [
("Peatborn", "Medium (about 5–6 feet tall)", "30 feet",
 "Peatborn come from the great fens and black-water swamps, where the bog keeps everything it swallows. Their skin is dark and leathery, their eyes are amber, and they age slowly, as if the bog preserves them too. They lay their dead to rest in the peat and visit them for advice, so they value memory, patience, and the old ways.",
 [("Creature Type", "You are a Humanoid."),
  ("Darkvision", "You have Darkvision with a range of 60 feet."),
  ("Bog Hide", "You have Resistance to Acid damage, and you can hold your breath for 1 hour."),
  ("Fenwalker", "Difficult Terrain made of mud, shallow water, or swamp plants doesn't cost you extra movement."),
  ("Preserved", "You have Advantage on Death Saving Throws."),
  ("Bog Grasp", "As a Bonus Action, you call hands of mud up from the ground under a creature you can see within 30 feet of you. It makes a Strength saving throw (DC 8 plus your Constitution modifier and Proficiency Bonus). On a failed save, its Speed is 0 until the end of its next turn. " + USES)]),

("Rillfolk", "Medium (about 5–6 feet tall)", "30 feet",
 "Rillfolk live along the great rivers, in stilt towns, on barges, and at every ferry crossing. They are lean and quick, with slick dark hair and webbing between their fingers. They carry news and cargo from one town to the next, and they hold that a fair trade leaves both sides richer and that no one should stay in one place too long.",
 [("Creature Type", "You are a Humanoid."),
  ("River Swimmer", "You have a Swim Speed equal to your Speed, and you can hold your breath for 15 minutes."),
  ("River Trader", "You have proficiency in the Insight skill and with Water Vehicles."),
  ("Slip Away", "When you would gain the Grappled or Restrained condition, you can take a Reaction to slip free and avoid the condition. You can then move up to half your Speed without provoking Opportunity Attacks. " + USES),
  ("Current's Gift", "You know the Message cantrip. At level 3, you can cast Expeditious Retreat once without a spell slot; at level 5, Misty Step. You regain the ability to cast each of these spells this way when you finish a Long Rest, and you can also cast them using spell slots you have. " + SPELL_ABILITY)]),

("Sunrunner", "Medium (about 5–7 feet tall)", "35 feet",
 "Sunrunners follow the herds across the endless grass seas of the steppe. Their homes are tents and wagons, their children ride before they walk, and they measure wealth in horses and in friends. They value speed, open sky, and freedom, and they think a wall is a strange thing to build.",
 [("Creature Type", "You are a Humanoid."),
  ("Horizon Eyes", "In Bright Light, you can see clearly out to 1 mile. You have Advantage on Wisdom (Perception) checks to see creatures and objects that are more than 60 feet away from you."),
  ("Born to the Saddle", "You have proficiency in the Animal Handling skill, and you have Advantage on saving throws to avoid falling off a mount."),
  ("Hard Rider", "When you would gain a level of Exhaustion from a forced march, from hunger, or from thirst, you can choose to not gain it. Once you use this trait, you can't use it again until you finish a Long Rest."),
  ("Windrun", "As a Bonus Action, you take the Dash action, and Difficult Terrain doesn't cost you extra movement until the end of the turn. " + USES)]),

("Hushfolk", "Medium (about 5–6 feet tall)", "30 feet",
 "Hushfolk build their cities in vast caverns deep under the earth, where a careless shout can bring the roof down. They speak in whispers and hand signs, move without a sound, and see with their ears as much as with their eyes. They value silence, care, and fine stonework, and they find surface people unbearably loud.",
 [("Creature Type", "You are a Humanoid."),
  ("Darkvision", "You have Darkvision with a range of 60 feet."),
  ("Echo Sense", "You have Blindsight with a range of 10 feet. You can't use this Blindsight while you have the Deafened condition."),
  ("Soft Step", "You have proficiency in the Stealth skill."),
  ("Carrying Whisper", "You can whisper to one creature you can see within 60 feet of you. Only that creature hears you."),
  ("Hush", "As a Bonus Action, you still the air around you. For 1 minute, no sound can be created within a 10-foot Emanation that comes from you, and no sound can pass through it. A creature entirely inside the Emanation has the Deafened condition, and a spell that has a Verbal component can't be cast there. Once you use this trait, you can't use it again until you finish a Long Rest.")]),

("Dreamborn", "Medium (about 5–6 feet tall) or Small (about 3–4 feet tall), chosen when you select this species", "30 feet",
 "Some children are born on nights when the wall between waking and dreaming wears thin. These Dreamborn are never quite all here: their outlines blur at the edges, their eyes change color with their mood, and they remember places they have never been. They gather in misty valleys and at old shrines where the dream lies close, and they value imagination, kindness, and a good story.",
 [("Creature Type", "You are a Humanoid."),
  ("Half Awake", "You have Advantage on saving throws to avoid or end the Frightened condition, and magic can't put you to sleep."),
  ("Dream Message", "When you finish a Long Rest, you can send a message of up to 25 words into the dreams of a creature you know that is on the same plane of existence. It receives the message the next time it sleeps and knows that it came from you. Once you use this trait, you can't use it again until you finish a Long Rest."),
  ("Fade", "As a Bonus Action, you fade halfway into the dream. You have the Invisible condition until the start of your next turn, or until you make an attack roll, deal damage, or cast a spell. " + USES),
  ("Dream Gift", "You know the Dancing Lights cantrip. At level 3, you can cast Sleep once without a spell slot; at level 5, Invisibility. You regain the ability to cast each of these spells this way when you finish a Long Rest, and you can also cast them using spell slots you have. " + SPELL_ABILITY)]),

("Gloamkin", "Medium (about 5–6 feet tall)", "30 feet",
 "Gloamkin are the children of the twilight lands, where the world lies close to the plane of shadow. Their skin is ash gray, and their shadows move a moment late. They live in deep valleys, ruined cities, and other places of long dusk, and they value secrets kept, debts honored, and help given without witnesses.",
 [("Creature Type", "You are a Humanoid."),
  ("Darkvision", "You have Darkvision with a range of 120 feet."),
  ("Child of Dusk", "You have Advantage on Dexterity (Stealth) checks that you make while you are in Dim Light or Darkness."),
  ("Shadow Step", "As a Bonus Action while you are in Dim Light or Darkness, you teleport up to 30 feet to an unoccupied space you can see that is also in Dim Light or Darkness. " + USES),
  ("Gloom Gift", "You know the Chill Touch cantrip. At level 3, you can cast Dissonant Whispers once without a spell slot; at level 5, Darkness. You regain the ability to cast each of these spells this way when you finish a Long Rest, and you can also cast them using spell slots you have. " + SPELL_ABILITY)]),
]
