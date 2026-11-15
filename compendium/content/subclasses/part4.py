# Original subclasses, part 4: Edition 2, batch 1 (one for each SRD class)
# Format: class -> list of (name, tagline, [(level, feature, text), ...])
SUBS = {}

SUBS["barbarian"] = [
("Path of the Tempered Scar", "Barbarians who keep every wound as a lesson and grow harder where they were hurt.", [
 (3, "Scar Memory", "While your Rage is active, when you take damage of a type other than Bludgeoning, Piercing, or Slashing, you can mark that damage type as your Scar. You have Resistance to your Scar's damage type while your Rage lasts. You can have only one Scar; marking a new one replaces the old one, and your Scar fades when your Rage ends."),
 (3, "Read the Wound", "You have Advantage on Wisdom (Medicine) checks. Once per Short Rest, when you spend Hit Dice to regain Hit Points, you regain extra Hit Points equal to your Constitution modifier."),
 (6, "Scar Tissue", "Your Hit Point maximum increases by 3, and it increases by 1 again whenever you gain a Barbarian level after this one. In addition, you can have two Scars at once."),
 (10, "Wounds Returned", "While raging, when a creature within 30 feet of you deals damage to you of your Scar's type, you can take a Reaction to make it take 2d6 + your Constitution modifier damage of that same type."),
 (14, "Living Monument", "You can have three Scars at once. Your Scars no longer fade when your Rage ends; they last until you finish a Short or Long Rest, and you keep their Resistances while you aren't raging. The damage of Wounds Returned increases to 4d6 + your Constitution modifier."),
]),
]

SUBS["bard"] = [
("College of the Loom", "Bards who tie threads of fate between people and pull them tight when it matters.", [
 (3, "Weaver's Craft", "You gain proficiency with Weaver's Tools and in one skill of your choice."),
 (3, "Fateful Thread", "As a Bonus Action, you can expend one use of Bardic Inspiration to tie an invisible thread between two creatures you can see within 60 feet of you. The thread lasts for 1 minute, until either creature is more than 120 feet from the other, or until you tie another thread. Choose the kind of thread when you tie it. [[Kin Thread (two willing creatures):]] When one of them regains Hit Points from a spell, the other regains Hit Points equal to one roll of your Bardic Inspiration die. [[Snare Thread (one willing creature and one other creature):]] When the other creature hits the willing one with an attack, the attacker takes Psychic damage equal to one roll of your Bardic Inspiration die."),
 (6, "Pull the Thread", "When a creature tied by your thread is hit by an attack, you can take a Reaction to make the attack hit the other creature on the thread instead, if that creature is within 30 feet of the attacker. The attack uses the same roll against the new target's AC; if the roll doesn't hit the new target, the attack misses. You can use this feature a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
 (14, "Tapestry", "Tying a thread with Fateful Thread no longer expends a use of Bardic Inspiration, and you can keep two threads at once."),
]),
]

SUBS["cleric"] = [
("Harvest Domain", "Gods of the field and the sickle: growth, plenty, and the reaping that feeds the year.", [
 (3, "Harvest Domain Spells", "Always prepared. Level 3: Goodberry, Entangle, Barkskin, Lesser Restoration; level 5: Plant Growth, Revivify; level 7: Blight, Aura of Life; level 9: Greater Restoration, Insect Plague."),
 (3, "Reap and Sow", "As a Magic action, you expend a use of Channel Divinity and choose a creature you can see within 30 feet of you. It makes a Constitution saving throw against your spell save DC, taking Necrotic damage equal to 2d8 + your Cleric level on a failed save or half as much on a successful one. Then one creature of your choice within 30 feet of you regains Hit Points equal to the damage dealt. This feature has no effect on Undead or Constructs."),
 (6, "Bountiful Hand", "When you cast a spell with a spell slot that restores Hit Points, you can also end one of these conditions on one creature that regains Hit Points from the spell: Blinded, Deafened, or Poisoned. In addition, each berry you create with Goodberry restores 1d4 + your Wisdom modifier Hit Points instead of 1."),
 (17, "Year of Plenty", "When you use Reap and Sow, you can target each creature of your choice in a 30-foot Emanation originating from you instead of one creature. Add up the damage dealt, and divide that number of Hit Points as you choose among any creatures of your choice in the Emanation."),
]),
]

SUBS["druid"] = [
("Circle of the Deep Mire", "Druids of bogs and fens, where the ground itself swallows the unwary.", [
 (3, "Circle of the Deep Mire Spells", "Always prepared. Level 3: Grease, Fog Cloud, Spike Growth, Ray of Sickness; level 5: Stinking Cloud, Water Breathing; level 7: Black Tentacles, Freedom of Movement; level 9: Cloudkill, Contagion."),
 (3, "Sucking Mud", "As a Bonus Action, you can expend a use of Wild Shape to turn the ground in a 20-foot-radius circle centered on a point within 60 feet of you into deep mud. The mud lasts for 1 minute or until you use this feature again. It is Difficult Terrain for creatures other than you and allies you choose when you create it. When a creature you didn't choose enters the mud for the first time on a turn or starts its turn there, it makes a Strength saving throw against your spell save DC. On a failed save, its Speed is 0 until the end of the current turn."),
 (3, "Bog Born", "You have a Swim Speed equal to your Speed, you can hold your breath for 1 hour, and mud, bogs, and quicksand never cause you to sink."),
 (6, "Marsh Gas", "When a creature fails its saving throw against your Sucking Mud, it also has the Poisoned condition until the end of its next turn."),
 (10, "Fen Ward", "You have Immunity to the Poisoned condition and Resistance to Acid and Poison damage."),
 (14, "The Mire Takes", "A creature that fails its saving throw against your Sucking Mud has the Restrained condition until the end of the current turn instead of having a Speed of 0. In addition, once per Long Rest, you can cast Black Tentacles without a spell slot, centered on a point inside your mud."),
]),
]

SUBS["fighter"] = [
("Siegebreaker", "Fighters trained to bring down walls, gates, and anyone who hides behind them.", [
 (3, "Sunder", "Once on each of your turns when you hit a creature with a melee weapon attack, you can dent its armor or hide. Its AC decreases by 1 until the start of your next turn. A creature can be affected by only one Sunder at a time."),
 (3, "Wall Breaker", "Your weapon attacks deal double damage to objects and structures, and you have Advantage on Strength checks made to break or force open doors, gates, chests, and chains."),
 (7, "Unstoppable Advance", "Difficult Terrain made of rubble, debris, or broken objects doesn't cost you extra movement. While you wear Heavy armor, Opportunity Attacks against you have Disadvantage."),
 (10, "Crack the Shell", "A creature affected by your Sunder loses its Resistance to Bludgeoning, Piercing, and Slashing damage against your attacks until the start of your next turn."),
 (15, "Earthshaker", "Once on each of your turns when you score a Critical Hit with a melee weapon attack or reduce a creature to 0 Hit Points with one, each creature of your choice within 10 feet of you makes a Dexterity saving throw (DC 8 + your Strength modifier + your Proficiency Bonus). On a failed save, it has the Prone condition."),
 (18, "Battering Ram", "Your Sunder decreases a creature's AC by 2 instead of 1. Once on each of your turns, when you hit a creature that is affected by your Sunder, it takes an extra 2d8 damage of the weapon's type."),
]),
]

SUBS["monk"] = [
("Warrior of the Hidden Needle", "Monks who learned where the body keeps its secrets, and how to press them.", [
 (3, "Pressure Points", "Whenever you hit a creature with one of the attacks granted by your Flurry of Blows, you can impose one of the following effects on that target. [[Numb:]] The target has Disadvantage on the next attack roll it makes before the start of your next turn. [[Hobble:]] The target must succeed on a Constitution saving throw or its Speed is 0 until the start of your next turn. [[Hush:]] The target must succeed on a Constitution saving throw or it can't speak until the start of your next turn. While it can't speak, it can't cast spells that have a Verbal component."),
 (3, "Needle Sense", "You have Advantage on Wisdom (Medicine) checks, and you can take the Help action to stabilize a creature as a Bonus Action."),
 (6, "Counterpoint", "When a creature within your reach hits you with an attack, you can take a Reaction and spend 1 Focus Point to reduce the damage by one roll of your Martial Arts die + your Wisdom modifier. The attacker is then affected by Numb from your Pressure Points."),
 (11, "Twin Needles", "When you hit a creature with an attack granted by your Flurry of Blows, you can impose two different effects of your Pressure Points instead of one."),
 (17, "Hundred Needles", "As a Magic action, you can spend 5 Focus Points to strike every nerve within reach. Each creature of your choice within 15 feet of you makes a Constitution saving throw against your Focus save DC. On a failed save, a creature has the Stunned condition until the end of your next turn. On a successful save, its Speed is halved until the end of your next turn."),
]),
]

SUBS["paladin"] = [
("Oath of the Last Rite", "Paladins who give the dead their rest: by prayer if they can, and by the blade if they must.", [
 (3, "Last Rite Oath Spells", "Always prepared. Level 3: Protection from Evil and Good, Bless; level 5: Gentle Repose, Lesser Restoration; level 9: Speak with Dead, Revivify; level 13: Death Ward, Banishment; level 17: Dispel Evil and Good, Raise Dead."),
 (3, "Rite of Rest", "As a Magic action, you expend a use of Channel Divinity. Each Undead of your choice in a 30-foot Emanation originating from you makes a Wisdom saving throw against your spell save DC. On a failed save, it takes Radiant damage equal to 2d10 + your Paladin level, and it can't willingly move closer to you for 1 minute or until it takes damage again. On a successful save, it takes half as much damage only."),
 (7, "Aura of the Threshold", "You and your allies have Advantage on Death Saving Throws and Resistance to Necrotic damage while in your Aura of Protection."),
 (15, "Not Yet", "When an ally you can see in your Aura of Protection would drop to 0 Hit Points, you can take a Reaction to make it drop to 1 Hit Point instead. You can use this feature a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
 (20, "Keeper of the Gate", "As a Bonus Action, you take on the form of a guide of souls for 10 minutes. You gain a Fly Speed of 60 feet and can hover. Enemies in your Aura of Protection can't regain Hit Points, and a creature that dies in your aura can't be raised as an Undead. Your allies in the aura who start their turns with 0 Hit Points regain 10 Hit Points. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a level 5 spell slot (no action required) to restore your use of it."),
]),
]

SUBS["ranger"] = [
("Peakwarden", "Rangers of high passes and storm-bitten ridges, where lightning is a hunting partner.", [
 (3, "Peakwarden Spells", "Always prepared. Level 3: Thunderwave; level 5: Gust of Wind; level 9: Call Lightning; level 13: Freedom of Movement; level 17: Cone of Cold."),
 (3, "Mountain Born", "You have a Climb Speed equal to your Speed and Resistance to Cold damage, and you suffer no ill effects from high altitude."),
 (3, "Storm-Marked", "When you cast Hunter's Mark, you can make its extra damage Lightning or Thunder damage. In addition, once on each of your turns when you deal Hunter's Mark damage to a creature, you can force it to make a Strength saving throw against your spell save DC. On a failed save, it is pushed up to 10 feet straight away from you."),
 (7, "Updraft", "When you fall, you can take a Reaction to take no damage from the fall and land on your feet. Opportunity Attacks against you have Disadvantage."),
 (11, "Forked Strike", "When you deal Hunter's Mark damage to a creature, you can also deal that extra damage to a second creature you can see within 10 feet of the first one."),
 (15, "Eye of the Storm", "When you take damage, you can take a Reaction to give yourself Resistance to that damage. Then each creature of your choice within 10 feet of you makes a Constitution saving throw against your spell save DC, taking 2d8 Thunder damage on a failed save or half as much on a successful one. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
]),
]

SUBS["rogue"] = [
("Saboteur", "Rogues who win by breaking things: locks, bridges, plans, and the gear of their foes.", [
 (3, "Tinkerer", "You gain proficiency with Tinker's Tools. If you already have it, you gain proficiency with another type of Artisan's Tools of your choice."),
 (3, "Quick Charges", "You carry small charges that you build from scraps. As a Bonus Action, you can throw a charge at a point within 30 feet of you. Choose one kind: [[Smoke:]] A 10-foot-radius Sphere around the point is Heavily Obscured until the end of your next turn. [[Flash:]] One creature within 5 feet of the point makes a Constitution saving throw (DC 8 + your Dexterity modifier + your Proficiency Bonus). On a failed save, it has the Blinded condition until the end of its next turn. [[Snap:]] Each creature in a 5-foot-radius Sphere around the point makes a Dexterity saving throw against the same DC, taking 2d6 Fire damage on a failed save or half as much on a successful one. You can throw a number of charges equal to your Proficiency Bonus, and you regain all expended charges when you finish a Long Rest."),
 (9, "Break Their Toys", "You gain a new Cunning Strike option. [[Sunder Gear (Cost: 2d6):]] A nonmagical weapon or Shield that the target holds breaks. The target can't use it until it is repaired. This option has no effect on natural weapons. In addition, you can spend 1 minute to quietly ruin a nonmagical object that a creature will use later (a crossbow, a saddle, a wagon wheel, a rope bridge). The next time a creature uses the object, it fails. A creature notices your work with a successful Intelligence (Investigation) check against your Cunning Strike DC."),
 (13, "Chain Reaction", "When you throw a Quick Charge, you can throw two charges instead of one, at the same point or at different points. Your Snap charge deals 4d6 Fire damage instead of 2d6."),
 (17, "Grand Charge", "You can spend 1 minute to set a large charge on a point you touch. As a Bonus Action within 1 hour, while you are within 120 feet of the charge, you can set it off. Each creature in a 20-foot-radius Sphere centered on the charge makes a Dexterity saving throw against your Cunning Strike DC, taking 10d6 Fire damage on a failed save or half as much on a successful one. Nonmagical objects and structures in the area take double damage. Once you set off a Grand Charge, you can't set another until you finish a Long Rest."),
]),
]

SUBS["sorcerer"] = [
("Quicksilver Sorcery", "Living metal flows in your blood: heavy as lead one moment, quick as a thrown knife the next.", [
 (3, "Quicksilver Spells", "Always prepared. Level 3: Shield, Expeditious Retreat, Blur, Heat Metal; level 5: Haste, Protection from Energy; level 7: Stoneskin, Fabricate; level 9: Animate Objects, Passwall."),
 (3, "Silver Skin", "While you aren't wearing armor, your base Armor Class equals 12 + your Dexterity modifier. You can use a Shield and still gain this benefit."),
 (3, "Run Like Mercury", "While your Innate Sorcery is active, your Speed increases by 10 feet, and you can take the Disengage action as a Bonus Action."),
 (6, "Molten Edge", "You have Resistance to Fire damage. Once on each of your turns when you deal Fire or Force damage with a Sorcerer spell, you can add your Charisma modifier to one damage roll of that spell."),
 (14, "Mercurial Step", "As a Bonus Action, you can spend 2 Sorcery Points to turn into a flash of liquid silver and teleport up to 60 feet to an unoccupied space you can see. Until the start of your next turn, you have Resistance to Bludgeoning, Piercing, and Slashing damage."),
 (18, "Living Alloy", "As a Bonus Action, you can turn your body into shining metal for 1 minute. For the duration, you have Resistance to Bludgeoning, Piercing, and Slashing damage, your AC increases by 2, and when a creature within 5 feet of you hits you with a melee attack, it takes 2d8 Slashing damage. Once you use this feature, you can't use it again until you finish a Long Rest unless you spend 5 Sorcery Points (no action required) to restore your use of it."),
]),
]

SUBS["warlock"] = [
("The Moth Queen", "A pale queen of night insects who loves every light that burns, and every soul that flutters toward one.", [
 (3, "Moth Queen Spells", "Always prepared. Level 3: Faerie Fire, Sleep, Calm Emotions, Phantasmal Force; level 5: Hypnotic Pattern, Daylight; level 7: Confusion, Giant Insect; level 9: Dream, Insect Plague."),
 (3, "Moth Dust", "Once on each of your turns when you hit a creature with a spell attack, or a creature fails a saving throw against one of your Warlock spells, you can cover it in pale dust. It has Disadvantage on the next attack roll it makes before the start of your next turn, and it sheds Dim Light in a 5-foot radius for that time."),
 (3, "Night Eyes", "You have Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 30 feet."),
 (6, "Flutter Away", "When a creature you can see hits you with an attack roll, you can take a Reaction to burst into a cloud of moths. The attack roll has Disadvantage against you, which can turn the hit into a miss. Then you teleport up to 15 feet to an unoccupied space you can see. You can use this feature a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."),
 (10, "Wings of Dust", "You grow soft gray wings. While you are in Bright Light or Dim Light and aren't wearing Heavy armor, you have a Fly Speed equal to your Speed."),
 (14, "The Queen's Lantern", "As a Magic action, you can light a pale lantern of your patron's flame. For 1 minute (Concentration), the light fills a 30-foot Emanation originating from you. When an enemy enters the Emanation for the first time on a turn or starts its turn there, it makes a Wisdom saving throw against your spell save DC. On a failed save, it takes 3d10 Psychic damage, and it has the Charmed condition and a Speed of 0 until the start of its next turn. On a successful save, it takes half as much damage only. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a Pact Magic spell slot (no action required) to restore your use of it."),
]),
]

SUBS["wizard"] = [
("Weatherwright", "Wizards who read the sky like a book, and rewrite a page when it suits them.", [
 (3, "Sky Reader", "Choose two of these spells: Fog Cloud, Gust of Wind, Thunderwave, Ice Knife. Add them to your spellbook for free. They count as Wizard spells for you. In addition, you always know what the weather will be in your area for the next 24 hours, unless magic changes it."),
 (3, "Pressure Shift", "When you cast a spell that deals Cold, Lightning, or Thunder damage, you can push or pull each creature that takes damage from the spell up to 10 feet."),
 (6, "Lightning Rod", "You have Resistance to Cold, Lightning, and Thunder damage."),
 (10, "Gathering Storm", "When you cast a Wizard spell with a spell slot that deals Cold, Lightning, or Thunder damage, you can add your Intelligence modifier to one damage roll of that spell."),
 (14, "Storm Crown", "As a Bonus Action, you call a small storm to hover above you for 1 minute. For the duration, you have a Fly Speed of 30 feet and can hover, and at the start of each of your turns you can call down a bolt on one creature you can see within 120 feet of you. It makes a Dexterity saving throw against your spell save DC, taking 4d10 Lightning damage on a failed save or half as much on a successful one. Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a spell slot of level 5 or higher (no action required) to restore your use of it."),
]),
]
