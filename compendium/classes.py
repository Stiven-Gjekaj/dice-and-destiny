"""Class reference pages for the Player's Binder.
Level/feature data comes from the SRD 5.2 (2024) class JSON in ../data.
Descriptions are short summaries written for this binder."""
import json, re, html

import os
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
ORDER = "barbarian bard cleric druid fighter monk paladin ranger rogue sorcerer warlock wizard".split()

SUB_LEVELS = {
    "barbarian": [3, 6, 10, 14], "bard": [3, 6, 14], "cleric": [3, 6, 17],
    "druid": [3, 6, 10, 14], "fighter": [3, 7, 10, 15, 18], "monk": [3, 6, 11, 17],
    "paladin": [3, 7, 15, 20], "ranger": [3, 7, 11, 15], "rogue": [3, 9, 13, 17],
    "sorcerer": [3, 6, 14, 18], "warlock": [3, 6, 10, 14], "wizard": [3, 6, 10, 14],
}
FIX_NAMES = {"Studdied Attacks": "Studied Attacks", "Unarmoed Movement": "Unarmored Movement",
             "Cleric Subclasses": "Cleric Subclass", "Magic Cunning": "Magical Cunning"}
EXTRA = {  # features the API stores without a level
    "bard": [(3, "Bard Subclass")], "monk": [(3, "Deflect Attacks")],
}
SKIP = {"Bard Spell List", "Cleric Spell List", "Druid Spell List", "Paladin Spell List",
        "Ranger Spell List", "Sorcerer Spell List", "Warlock Spell List", "Wizard Spell List",
        "Cantrips Known"}

INFO = {
"barbarian": dict(
    tag="A primal warrior who channels rage into raw, unstoppable force.",
    role="Front-line tank &amp; damage", diff="Easy",
    play="Run at the biggest threat, Rage, and hit hard. You have the most HP in the game and resist physical damage while raging, so you're meant to be in the thick of it. Reckless Attack gives you advantage — at the cost of enemies getting advantage on you.",
    build="Strength 15, Constitution 14, Dexterity 13. Greataxe. Background: Soldier. Take Great Weapon Fighting… no wait — Barbarians don't get Fighting Styles; just swing.",
    feats={
        "Rage": "Bonus action, no heavy armor. Lasts until end of your next turn and is extended by attacking or forcing a save (up to 10 minutes). While raging: resistance to Bludgeoning/Piercing/Slashing, +Rage Damage on Strength attacks, advantage on Strength checks and saves, no spellcasting or concentration.",
        "Unarmored Defense": "No armor: AC = 10 + Dex mod + Con mod (shield allowed).",
        "Weapon Mastery": "Use the mastery property of a number of weapon types (see the Weapons chapter).",
        "Danger Sense": "Advantage on Dexterity saving throws unless Incapacitated.",
        "Reckless Attack": "On your first attack of a turn, choose to get advantage on Strength attacks this turn; attacks against you have advantage until your next turn.",
        "Primal Knowledge": "One extra Barbarian skill. While raging, Acrobatics, Intimidation, Perception, Stealth and Survival checks can use Strength.",
        "Extra Attack": "Attack twice with the Attack action.",
        "Fast Movement": "+10 ft Speed without heavy armor.",
        "Feral Instinct": "Advantage on initiative.",
        "Instinctive Pounce": "Move up to half your Speed as part of entering Rage.",
        "Brutal Strike": "When using Reckless Attack, give up advantage on one attack; on a hit it deals +1d10 and either pushes the target 15 ft or reduces its Speed by 15 ft.",
        "Relentless Rage": "Drop to 0 HP while raging: DC 10 Con save to stay at HP equal to twice your Barbarian level. DC rises by 5 each use.",
        "Improved Brutal Strike": "New Brutal Strike options: Staggering Blow (disadvantage on next save, no opportunity attacks) and Sundering Blow (next attack by someone else gets +5).",
        "Persistent Rage": "Regain all Rage uses when rolling initiative (once per long rest). Rage lasts 10 minutes without needing to extend it.",
        "Improved Brutal Strike (Enhanced)": "Brutal Strike deals +2d10 and you can apply two different effects.",
        "Indomitable Might": "If a Strength check or save totals less than your Strength score, use the score instead.",
        "Primal Champion": "Strength and Constitution +4 (max 25).",
    },
    sub=("Path of the Berserker", "Pure fury.", [
        (3, "Frenzy", "While raging and using Reckless Attack, your first Strength hit each turn deals extra d6s equal to your Rage Damage bonus."),
        (6, "Mindless Rage", "Immune to Charmed and Frightened while raging."),
        (10, "Retaliation", "When a creature within 5 ft damages you, use your reaction to make a melee attack against it."),
        (14, "Intimidating Presence", "Bonus action: creatures of your choice within 30 ft make a Wisdom save or are Frightened for 1 minute."),
    ]),
    other="Other subclasses in the Player's Handbook: Path of the Wild Heart, World Tree, Zealot.",
),
"bard": dict(
    tag="A magical performer whose words and music inspire allies and unravel foes.",
    role="Support, social face, versatile caster", diff="Medium",
    play="You're the party's best talker and a full spellcaster. Hand out Bardic Inspiration every round you can, lead conversations, and pick spells that control the battlefield or heal. Expertise and Jack of All Trades make you good at almost any skill.",
    build="Charisma 15, Dexterity 14, Constitution 13. Rapier or dagger, leather armor. Spells: Vicious Mockery, Healing Word, Dissonant Whispers.",
    feats={
        "Bardic Inspiration": "Bonus action: give a creature within 60 ft a Bardic die (d6, grows with level). Within the next hour, when it fails a d20 Test, it can add the die. Uses = Charisma modifier per long rest.",
        "Spellcasting": "Full caster using Charisma. Prepare spells from the Bard list; you can swap one prepared spell when you gain a level. Use a musical instrument as a focus.",
        "Expertise": "Double proficiency bonus on two skills (two more at level 9).",
        "Jack of All Trades": "Add half your proficiency bonus to ability checks with skills you're not proficient in.",
        "Font of Inspiration": "Bardic Inspiration recharges on a short rest too; you can spend a spell slot to regain a use.",
        "Countercharm": "Reaction: when you or an ally within 30 ft fails a save against being Charmed or Frightened, reroll it with advantage.",
        "Magical Secrets": "Whenever you prepare new spells, choose them from the Bard, Cleric, Druid or Wizard lists.",
        "Superior Inspiration": "When you roll initiative, regain Bardic Inspiration up to two uses.",
        "Words of Creation": "Always have Power Word Heal and Power Word Kill prepared, and can target a second creature with them.",
    },
    sub=("College of Lore", "Scholarship and cutting wit.", [
        (3, "Bonus Proficiencies", "Proficiency in three skills of your choice."),
        (3, "Cutting Words", "Reaction: subtract your Bardic die from a creature's attack roll, check or damage roll."),
        (6, "Magical Discoveries", "Learn two spells from the Cleric, Druid or Wizard lists; they're always prepared."),
        (14, "Peerless Skill", "When you fail an ability check or attack roll, add a Bardic die (not spent if it still fails)."),
    ]),
    other="Other subclasses in the Player's Handbook: College of Dance, Glamour, Valor.",
),
"cleric": dict(
    tag="A divine champion who channels the power of a god to heal, protect and smite.",
    role="Healer, support, sturdy caster", diff="Medium",
    play="You're the party's best healer and a strong spellcaster in medium or heavy armor. Don't spend every turn healing — a well-timed Bless or Spirit Guardians prevents more damage than healing restores. Healing Word lets you pick up downed allies as a bonus action.",
    build="Wisdom 15, Constitution 14, Strength 13. Mace, shield, chain shirt. Divine Order: Protector. Spells: Bless, Healing Word, Guiding Bolt, Sacred Flame.",
    feats={
        "Spellcasting": "Full caster using Wisdom. Prepare spells from the Cleric list after each long rest. Use a holy symbol as a focus.",
        "Divine Order": "Choose: Protector (martial weapons, heavy armor) or Thaumaturge (extra cantrip, add Wis mod to Arcana/Religion).",
        "Channel Divinity": "Uses per rest (regain one on a short rest, all on a long). Divine Spark: heal or deal Radiant/Necrotic damage (d8s based on level). Turn Undead: undead nearby make a Wis save or are Frightened and must flee.",
        "Cleric Subclass": "Choose your divine domain.",
        "Sear Undead": "Turn Undead also deals Radiant damage to the undead that fail.",
        "Blessed Strikes": "Choose: Divine Strike (+1d8 Radiant/Necrotic on a weapon hit, once per turn) or Potent Spellcasting (add Wis mod to cantrip damage).",
        "Divine Intervention": "Magic action, once per long rest: cast any Cleric spell of 5th level or lower for free.",
        "Improved Blessed Strikes": "Divine Strike becomes 2d8, or Potent Spellcasting also grants temporary HP.",
        "Greater Divine Intervention": "Divine Intervention can cast Wish (then unusable for 2d4 long rests).",
    },
    sub=("Life Domain", "The ultimate healer.", [
        (3, "Disciple of Life", "Healing spells restore extra HP equal to 2 + the spell's level."),
        (3, "Life Domain Spells", "Always-prepared spells: Aid, Bless, Cure Wounds, Lesser Restoration, then more at 5, 7, 9."),
        (3, "Preserve Life", "Channel Divinity: split healing equal to 5 × Cleric level among creatures within 30 ft (up to half their max HP)."),
        (6, "Blessed Healer", "When you heal others with a slot spell, you heal 2 + spell level too."),
        (17, "Supreme Healing", "Healing dice always roll their maximum."),
    ]),
    other="Other subclasses in the Player's Handbook: Light Domain, Trickery Domain, War Domain.",
),
"druid": dict(
    tag="A priest of nature who commands the elements and takes the shape of beasts.",
    role="Controller, utility, shapeshifter", diff="Hard",
    play="You're a full caster with nature magic: entangling roots, summoned storms, healing. Wild Shape lets you become an animal for scouting or combat. Strong but complex — lots of options to learn. Druids traditionally won't wear metal armor.",
    build="Wisdom 15, Constitution 14, Dexterity 13. Shield, leather armor. Spells: Produce Flame, Entangle, Healing Word, Faerie Fire.",
    feats={
        "Spellcasting": "Full caster using Wisdom. Prepare spells from the Druid list each long rest. Use a druidic focus.",
        "Druidic": "Know the secret Druidic language; always have Speak with Animals prepared.",
        "Primal Order": "Choose: Magician (extra cantrip, bonus to Arcana/Nature) or Warden (martial weapons, medium armor).",
        "Wild Shape": "Bonus action: transform into a beast form you know (limited by CR). You keep your mind; you get temporary HP equal to your Druid level. Uses recharge partly on short rests.",
        "Wild Companion": "Spend a slot or Wild Shape use to cast Find Familiar (a fey spirit animal).",
        "Druid Subclass": "Choose your Druid circle.",
        "Wild Resurgence": "Trade spell slots for Wild Shape uses and vice versa (limited).",
        "Elemental Fury": "Choose: Potent Spellcasting (add Wis to cantrip damage) or Primal Strike (+1d8 elemental damage on weapon/beast hits once per turn).",
        "Improved Elemental Fury": "Cantrips gain 300 ft range, or Primal Strike becomes 2d8.",
        "Beast Spells": "Cast spells while in Wild Shape.",
        "Archdruid": "Regain Wild Shape on initiative; convert Wild Shape into spell slots; you age very slowly.",
    },
    sub=("Circle of the Land", "Magic of a chosen landscape.", [
        (3, "Circle of the Land Spells", "After each long rest choose arid, polar, temperate or tropical land; gain that land's always-prepared spells."),
        (3, "Land's Aid", "Spend Wild Shape: flowers and thorns in a 10-ft sphere deal Necrotic damage to foes and heal one ally."),
        (6, "Natural Recovery", "Cast one circle spell free per long rest; recover spell slots on a short rest once per day."),
        (10, "Nature's Ward", "Immune to Poisoned; resistance to the damage type of your chosen land."),
        (14, "Nature's Sanctuary", "Spend Wild Shape to create spectral trees giving half cover and your resistance to allies."),
    ]),
    other="Other subclasses in the Player's Handbook: Circle of the Moon, Sea, Stars.",
),
"fighter": dict(
    tag="A master of weapons and armor, at home in any battle.",
    role="Versatile damage &amp; defense", diff="Easy — best first class",
    play="You get the most attacks in the game, heavy armor, and simple, reliable features. Pick a weapon style (big two-hander, sword and shield, or bow) and focus on positioning. Action Surge is your 'big moment' button — save it for when it matters.",
    build="Strength 15, Constitution 14, Dexterity 13. Greatsword or longsword + shield, chain mail. Fighting Style: Defense or Great Weapon Fighting.",
    feats={
        "Fighting Style": "Gain a Fighting Style feat (Defense, Great Weapon Fighting, Archery, Dueling, etc.). Can swap it on level up.",
        "Second Wind": "Bonus action: heal 1d10 + Fighter level. Limited uses; regain one on a short rest, all on a long rest.",
        "Weapon Mastery": "Use the mastery property of several weapon types (see the Weapons chapter).",
        "Action Surge": "Once per short rest: take one extra action on your turn (not Magic). Twice per rest at level 17.",
        "Tactical Mind": "When you fail an ability check, spend a Second Wind use to add 1d10 instead of healing.",
        "Fighter Subclass": "Choose your martial archetype.",
        "Ability Score Improvement": "Fighters get extra ASIs/feats at levels 6 and 14.",
        "Extra Attack": "Attack twice with the Attack action.",
        "Tactical Shift": "When you use Second Wind, move half Speed without opportunity attacks.",
        "Indomitable": "Reroll a failed save with a bonus equal to your Fighter level. 1/2/3 uses per long rest at 9/13/17.",
        "Tactical Master": "Swap any weapon's mastery property for Push, Sap or Slow on an attack.",
        "Two Extra Attacks": "Attack three times with the Attack action.",
        "Studied Attacks": "If you miss a creature, you have advantage on your next attack against it.",
        "Three Extra Attacks": "Attack four times with the Attack action.",
    },
    sub=("Champion", "Simple, brutal excellence.", [
        (3, "Improved Critical", "Critical hits on a 19 or 20."),
        (3, "Remarkable Athlete", "Advantage on initiative and Athletics checks; move half speed after a crit."),
        (7, "Additional Fighting Style", "Gain a second Fighting Style feat."),
        (10, "Heroic Warrior", "In combat, gain Heroic Inspiration at the start of your turn if you don't have it."),
        (15, "Superior Critical", "Critical hits on 18–20."),
        (18, "Survivor", "Advantage on death saves; regain 5 + Con mod HP each turn while bloodied."),
    ]),
    other="Other subclasses in the Player's Handbook: Battle Master, Eldritch Knight, Psi Warrior.",
),
"monk": dict(
    tag="A martial artist who channels inner focus into lightning-fast strikes.",
    role="Mobile skirmisher", diff="Medium",
    play="You're fast and hit many times per turn with fists or light weapons. Spend Focus Points on Flurry of Blows (extra strikes), Patient Defense (dodge) or Step of the Wind (dash/disengage). Stunning Strike can lock down a dangerous enemy. No armor — your AC comes from Dex and Wis.",
    build="Dexterity 15, Wisdom 14, Constitution 13. Spear or shortsword plus unarmed strikes.",
    feats={
        "Martial Arts": "Use Dex for unarmed strikes and Monk weapons; damage uses your Martial Arts die. Bonus action: make an unarmed strike. Grapple/shove can use Dex.",
        "Unarmored Defense": "No armor or shield: AC = 10 + Dex mod + Wis mod.",
        "Monk's Focus": "Focus Points (= Monk level) recharge on a short rest. Flurry of Blows (2 unarmed strikes as bonus action), Patient Defense (Disengage + Dodge), Step of the Wind (Disengage + Dash, jump distance doubled).",
        "Unarmored Movement": "+10 ft Speed without armor, growing with level (up to +30 ft).",
        "Uncanny Metabolism": "On initiative, regain all Focus Points and heal once per long rest.",
        "Deflect Attacks": "Reaction: reduce damage from an attack by 1d10 + Dex mod + Monk level; if reduced to 0, spend 1 Focus to redirect it.",
        "Monk Subclass": "Choose your monastic tradition.",
        "Slow Fall": "Reaction: reduce falling damage by 5 × Monk level.",
        "Extra Attack": "Attack twice with the Attack action.",
        "Stunning Strike": "Once per turn on a hit, spend 1 Focus: target makes a Con save or is Stunned until your next turn (on a success its Speed is halved and next attack against it has advantage).",
        "Empowered Strikes": "Unarmed strikes can deal Force damage.",
        "Evasion": "Dex save for half damage: take none on a success, half on a failure.",
        "Acrobatic Movement": "Run up walls and across water during your move.",
        "Heightened Focus": "Flurry makes 3 strikes; Patient Defense and Step of the Wind give temporary HP / carry an ally.",
        "Self-Restoration": "End Charmed, Frightened or Poisoned on yourself each turn; no exhaustion from hunger.",
        "Deflect Energy": "Deflect Attacks works on any damage type.",
        "Disciplined Survivor": "Proficiency in all saving throws; spend 1 Focus to reroll a failed save.",
        "Perfect Focus": "On initiative, regain Focus Points up to 4.",
        "Superior Defense": "Spend 3 Focus: resistance to all damage except Force for 1 minute.",
        "Body and Mind": "Dexterity and Wisdom +4 (max 25).",
    },
    sub=("Warrior of the Open Hand", "Master of unarmed combat.", [
        (3, "Open Hand Technique", "Flurry of Blows hits can Addle (no reactions), Push (15 ft) or Topple (Prone)."),
        (6, "Wholeness of Body", "Bonus action: heal Martial Arts die + Wis mod, Wis mod times per long rest."),
        (11, "Fleet Step", "Use Step of the Wind for free after another bonus action."),
        (17, "Quivering Palm", "Spend 4 Focus on a hit; later, end it to force a Con save for 10d12 Force damage."),
    ]),
    other="Other subclasses in the Player's Handbook: Warrior of Mercy, Shadow, the Elements.",
),
"paladin": dict(
    tag="A holy knight bound by a sacred oath, wielding divine power alongside steel.",
    role="Tank, burst damage, support aura", diff="Easy–Medium",
    play="Heavy armor, a big weapon, and Divine Smite to turn a hit into a devastating blow. Lay On Hands heals in a pinch. From level 6 your aura adds your Charisma to allies' saves — stay close to the party. Your oath gives roleplay direction.",
    build="Strength 15, Charisma 14, Constitution 13. Longsword + shield, chain mail. Spells: Bless, Cure Wounds, Shield of Faith.",
    feats={
        "Lay On Hands": "Healing pool of 5 × Paladin level HP per long rest. Bonus action: touch to heal, or spend 5 points to cure Poisoned.",
        "Spellcasting": "Half caster using Charisma. Prepare spells from the Paladin list each long rest.",
        "Weapon Mastery": "Use the mastery property of two weapon types.",
        "Fighting Style": "Gain a Fighting Style feat, or Blessed Warrior (two Cleric cantrips).",
        "Paladin's Smite": "Always have Divine Smite prepared; cast it once per long rest without a slot. Divine Smite: after hitting, bonus action, +2d8 Radiant (more with higher slots).",
        "Channel Divinity": "Divine Sense (detect celestials, fiends, undead within 60 ft) plus oath options.",
        "Paladin Subclass": "Swear your sacred oath.",
        "Extra Attack": "Attack twice with the Attack action.",
        "Faithful Steed": "Always have Find Steed prepared; cast it once free per long rest.",
        "Aura of Protection": "You and allies within 10 ft add your Charisma modifier to saving throws.",
        "Abjure Foes": "Channel Divinity: frighten enemies (Wis save) and limit their actions.",
        "Aura of Courage": "You and allies in your aura can't be Frightened.",
        "Radiant Strikes": "Melee weapon hits deal +1d8 Radiant damage.",
        "Restoring Touch": "Lay On Hands can also end Blinded, Charmed, Deafened, Frightened, Paralyzed or Stunned.",
        "Aura Expansion": "Your aura grows to 30 ft.",
    },
    sub=("Oath of Devotion", "The classic knight in shining armor.", [
        (3, "Oath of Devotion Spells", "Always-prepared spells: Protection from Evil and Good, Shield of Faith, then more at 5, 9, 13, 17."),
        (3, "Sacred Weapon", "Channel Divinity: add Cha mod to attack rolls with a weapon for 10 minutes; it sheds light and can deal Radiant damage."),
        (7, "Aura of Devotion", "You and allies in your aura can't be Charmed."),
        (15, "Smite of Protection", "When you cast Divine Smite, allies in your aura gain half cover."),
        (20, "Holy Nimbus", "Bonus action, 10 minutes: aura of sunlight deals Radiant damage to enemies, advantage on saves vs. fiends/undead."),
    ]),
    other="Other subclasses in the Player's Handbook: Oath of Glory, the Ancients, Vengeance.",
),
"ranger": dict(
    tag="A wilderness hunter blending weapon skill with nature magic.",
    role="Ranged damage, scout, tracker", diff="Medium",
    play="Most rangers shoot with a longbow from range, marking their target with Hunter's Mark for extra damage each hit. You're also the party's explorer — tracking, surviving, scouting ahead. Medium armor and some healing/utility spells round you out.",
    build="Dexterity 15, Wisdom 14, Constitution 13. Longbow + shortswords, studded leather. Fighting Style: Archery.",
    feats={
        "Spellcasting": "Half caster using Wisdom. Prepare spells from the Ranger list each long rest.",
        "Favored Enemy": "Always have Hunter's Mark prepared; cast it free a few times per long rest. Hunter's Mark: bonus action, +1d6 Force damage to the marked target on each hit, advantage to track it.",
        "Weapon Mastery": "Use the mastery property of two weapon types.",
        "Deft Explorer": "Expertise in one skill; learn two languages.",
        "Fighting Style": "Gain a Fighting Style feat, or Druidic Warrior (two Druid cantrips).",
        "Ranger Subclass": "Choose your ranger archetype.",
        "Extra Attack": "Attack twice with the Attack action.",
        "Roving": "+10 ft Speed (no heavy armor); climb and swim speed equal to your Speed.",
        "Expertise": "Expertise in two more skills.",
        "Tireless": "Gain temporary HP as a Magic action; short rests reduce Exhaustion.",
        "Relentless Hunter": "Taking damage can't break concentration on Hunter's Mark.",
        "Nature's Veil": "Bonus action: become Invisible until the end of your next turn (Wis mod uses per long rest).",
        "Precise Hunter": "Advantage on attacks against your Hunter's Mark target.",
        "Feral Senses": "Blindsight 30 ft.",
        "Foe Slayer": "Hunter's Mark damage becomes 1d10.",
    },
    sub=("Hunter", "Specialist in bringing down monsters.", [
        (3, "Hunter's Lore", "Know the immunities, resistances and vulnerabilities of your marked target."),
        (3, "Hunter's Prey", "Choose Colossus Slayer (+1d8 to wounded targets once per turn) or Horde Breaker (extra attack against an adjacent enemy)."),
        (7, "Defensive Tactics", "Choose Escape the Horde (opportunity attacks against you have disadvantage) or Multiattack Defense."),
        (11, "Superior Hunter's Prey", "Hunter's Mark extra damage also hits a second creature within 30 ft."),
        (15, "Superior Hunter's Defense", "Reaction: gain resistance to a damage type you just took."),
    ]),
    other="Other subclasses in the Player's Handbook: Beast Master, Fey Wanderer, Gloom Stalker.",
),
"rogue": dict(
    tag="A cunning expert in stealth, skills and precise, deadly strikes.",
    role="Single-target damage, skills, scout", diff="Easy–Medium",
    play="You attack once per turn but make it count: Sneak Attack adds big damage when you have advantage or an ally is next to the target. Cunning Action lets you Dash, Disengage or Hide as a bonus action — hit and vanish. You're the best at locks, traps and sneaking.",
    build="Dexterity 15, Constitution 14, Wisdom 13 (or Intelligence). Rapier or shortbow, leather armor, thieves' tools.",
    feats={
        "Expertise": "Double proficiency on two skills (two more at level 6).",
        "Sneak Attack": "Once per turn, +Sneak Attack dice on a hit with a Finesse or ranged weapon if you have advantage — or an ally is within 5 ft of the target and you don't have disadvantage.",
        "Thieves' Cant": "Secret criminal language plus one other language.",
        "Weapon Mastery": "Use the mastery property of two weapon types.",
        "Cunning Action": "Bonus action: Dash, Disengage or Hide.",
        "Rogue Subclass": "Choose your roguish archetype.",
        "Steady Aim": "Bonus action: advantage on your next attack this turn if you haven't moved (Speed becomes 0).",
        "Ability Score Improvement": "Rogues get an extra ASI/feat at level 10.",
        "Cunning Strike": "Trade Sneak Attack dice for effects: Poison (1d6), Trip (1d6), Withdraw (1d6).",
        "Uncanny Dodge": "Reaction: halve damage from an attack you can see.",
        "Evasion": "Dex save for half damage: take none on a success, half on a failure.",
        "Reliable Talent": "Treat any d20 roll of 9 or lower as a 10 on proficient checks.",
        "Improved Cunning Strike": "Use two Cunning Strike effects at once.",
        "Devious Strikes": "New Cunning Strikes: Daze, Knock Out, Obscure.",
        "Slippery Mind": "Proficiency in Wisdom and Charisma saves.",
        "Elusive": "No attack roll has advantage against you unless you're Incapacitated.",
        "Stroke of Luck": "Turn a failed d20 Test into a 20, once per short rest.",
    },
    sub=("Thief", "Burglar, treasure hunter, item expert.", [
        (3, "Fast Hands", "Cunning Action can also pick locks, disarm traps, pick pockets or use objects."),
        (3, "Second-Story Work", "Climb speed equal to Speed; jump farther using Dexterity."),
        (9, "Supreme Sneak", "New Cunning Strike: Stealth Attack (stay hidden after attacking)."),
        (13, "Use Magic Device", "Attune to four items; may use any spell scroll; magic items' charges may not be spent."),
        (17, "Thief's Reflexes", "Take two turns in the first round of combat."),
    ]),
    other="Other subclasses in the Player's Handbook: Arcane Trickster, Assassin, Soulknife.",
),
"sorcerer": dict(
    tag="A caster whose magic is innate — born of a bloodline, a cosmic event or raw power.",
    role="Blaster, flexible caster", diff="Medium",
    play="You know fewer spells than a wizard but bend them with Metamagic: twin a spell onto two targets, cast quietly, or quicken a spell to a bonus action. Innate Sorcery gives a burst of power. Fragile (d6 HP) — stay back and let the front line protect you.",
    build="Charisma 15, Constitution 14, Dexterity 13. Spells: Fire Bolt, Shocking Grasp, Magic Missile, Shield.",
    feats={
        "Spellcasting": "Full caster using Charisma. Prepared spells grow with level; swap one when you level up.",
        "Innate Sorcery": "Bonus action, 1 minute, twice per long rest: +1 spell save DC and advantage on spell attack rolls.",
        "Font of Magic": "Sorcery Points (= Sorcerer level). Convert points into spell slots and slots into points.",
        "Metamagic": "Learn two (two more at level 10) ways to alter spells with Sorcery Points: Careful, Distant, Empowered, Extended, Heightened, Quickened, Seeking, Subtle, Transmuted, Twinned.",
        "Sorcerer Subclass": "Choose the origin of your power.",
        "Sorcerous Restoration": "Regain Sorcery Points equal to half your level on a short rest (once per long rest).",
        "Sorcery Incarnate": "Spend 2 Sorcery Points to use Innate Sorcery again; use two Metamagic options on one spell while it's active.",
        "Arcane Apotheosis": "During Innate Sorcery, one Metamagic per turn is free.",
    },
    sub=("Draconic Sorcery", "Dragon blood in your veins.", [
        (3, "Draconic Resilience", "+1 HP per Sorcerer level (+3 at 3rd); unarmored AC = 10 + Dex + Cha."),
        (3, "Draconic Spells", "Always-prepared spells: Alter Self, Chromatic Orb, Command, Dragon's Breath, then more at 5, 7, 9."),
        (6, "Elemental Affinity", "Pick acid, cold, fire, lightning or poison: resistance to it, and add Cha mod to that spell damage."),
        (14, "Dragon Wings", "Bonus action: grow wings for a 60-ft fly speed for 1 hour."),
        (18, "Dragon Companion", "Cast Summon Dragon without a component, once free per long rest."),
    ]),
    other="Other subclasses in the Player's Handbook: Aberrant Sorcery, Clockwork Sorcery, Wild Magic Sorcery.",
),
"warlock": dict(
    tag="A seeker of forbidden knowledge who made a pact with a powerful otherworldly patron.",
    role="Ranged damage, utility, face", diff="Medium",
    play="You have very few spell slots — but they're always cast at your highest level and recharge on a short rest. Your bread and butter is the Eldritch Blast cantrip, boosted by invocations like Agonizing Blast. Your patron is a gift for roleplay and story hooks.",
    build="Charisma 15, Constitution 14, Dexterity 13. Leather armor. Eldritch Blast + Agonizing Blast invocation, Hex, Hellish Rebuke.",
    feats={
        "Eldritch Invocations": "Learn magical secrets (more as you level): Agonizing Blast (add Cha to a cantrip's damage), Armor of Shadows, Devil's Sight, Pact of the Blade/Chain/Tome, and many more.",
        "Pact Magic": "Caster using Charisma. Few slots, always at your highest available slot level (up to 5th), and they recharge on a short or long rest.",
        "Magical Cunning": "1-minute rite: regain half your Pact Magic slots, once per long rest.",
        "Warlock Subclass": "Choose your otherworldly patron.",
        "Contact Patron": "Always have Contact Other Plane prepared; cast it free to speak to your patron once per long rest.",
        "Mystic Arcanum": "One free cast each of a 6th (11), 7th (13), 8th (15) and 9th (17) level spell per long rest.",
        "Eldritch Master": "Magical Cunning restores all your Pact Magic slots.",
    },
    sub=("Fiend Patron", "A pact with a devil or demon.", [
        (3, "Dark One's Blessing", "When you (or someone near you) reduce an enemy to 0 HP, gain temporary HP equal to Cha mod + Warlock level."),
        (3, "Fiend Spells", "Always-prepared spells: Burning Hands, Command, Scorching Ray, Suggestion, then more at 5, 7, 9."),
        (6, "Dark One's Own Luck", "Add 1d10 to an ability check or save after seeing the roll (Cha mod times per long rest)."),
        (10, "Fiendish Resilience", "Choose a damage type after each rest: gain resistance to it."),
        (14, "Hurl Through Hell", "Once per long rest on a hit: target makes a Cha save or vanishes through the Lower Planes, taking 8d10 Psychic damage."),
    ]),
    other="Other subclasses in the Player's Handbook: Archfey Patron, Celestial Patron, Great Old One Patron.",
),
"wizard": dict(
    tag="A scholarly mage who masters magic through study, keeping spells in a spellbook.",
    role="Controller, utility, blaster", diff="Hard",
    play="You have the largest spell list in the game and can learn any wizard spell you find written down. You're very fragile (d6 HP, no armor) but can solve almost any problem with the right spell. Prepare a mix: defense (Shield), control (Sleep, Web), damage (Magic Missile, Fireball) and utility.",
    build="Intelligence 15, Constitution 14, Dexterity 13. Spells: Fire Bolt, Mage Hand, Shield, Magic Missile, Sleep, Detect Magic.",
    feats={
        "Spellcasting": "Full caster using Intelligence. Your spellbook holds your spells (6 at level 1, +2 each level); prepare a number of them after each long rest. Copy new spells you find into your book.",
        "Ritual Adept": "Cast any Ritual spell from your spellbook without preparing it (takes 10 minutes longer).",
        "Arcane Recovery": "Once per day on a short rest, recover spell slots totaling up to half your Wizard level (none 6th level or higher).",
        "Scholar": "Expertise in one of Arcana, History, Investigation, Medicine, Nature or Religion.",
        "Wizard Subclass": "Choose your school of magic.",
        "Memorize Spell": "On a short rest, swap one prepared spell for another in your book.",
        "Spell Mastery": "Cast one chosen 1st-level and one 2nd-level spell at will.",
        "Signature Spells": "Two chosen 3rd-level spells are always prepared; cast each once free per short rest.",
    },
    sub=("Evoker", "Master of destructive elemental magic.", [
        (3, "Evocation Savant", "Add two evocation spells to your book free; one more free whenever you gain a new spell level."),
        (3, "Potent Cantrip", "Damaging cantrips deal half damage even on a miss or successful save."),
        (6, "Sculpt Spells", "Allies in your evocation spells' area automatically succeed and take no damage."),
        (10, "Empowered Evocation", "Add Int mod to one damage roll of your evocation spells."),
        (14, "Overchannel", "Deal maximum damage with a 1st–5th level spell; repeated uses hurt you."),
    ]),
    other="Other subclasses in the Player's Handbook: Abjurer, Diviner, Illusionist.",
),
}

# Fix one leftover thinking-out-loud line
INFO["barbarian"]["build"] = "Strength 15, Constitution 14, Dexterity 13. Greataxe plus handaxes to throw. Background: Soldier. Barbarians get no Fighting Style — Rage and Reckless Attack do the work."


def core_traits(d):
    for f in d["features"]:
        if f["feature_type"] == "CORE_TRAITS_TABLE":
            rows = re.findall(r"\|\s*([A-Z][^|]*?)\s*\|\s*([^|]+?)\s*\|", f["desc"])
            fix = lambda s: (s.replace("Ar mor", "Armor").replace("Na ture", "Nature")
                             .replace("Ar rows", "Arrows").replace("Ar cane", "Arcane").replace("In sight", "Insight"))
            fix2 = lambda s: re.sub(r"\bD(\d+)", r"d\1", fix(s))
            return {k.strip(): fix2(v.strip()) for k, v in rows if k.strip() not in ("", "---")}
    return {}


def columns(d):
    cols = []
    for f in d["features"]:
        if f["feature_type"] == "CLASS_TABLE_DATA" and f["data_for_class_table"]:
            t = {x["level"]: re.sub(r"^D(\d)", r"d\1", x["column_value"]) for x in f["data_for_class_table"]}
            cols.append((f["name"], [t.get(l, "—") for l in range(1, 21)]))
    pref = ["Rages", "Rage Damage", "Bardic Die", "Second Wind", "Martial Arts", "Focus Points",
            "Sneak Attack", "Channel Divinity", "Favored Enemy", "Sorcery Points", "Eldritch Invocations",
            "Spell Slots", "Slot Level", "Cantrips", "Prepared Spells", "Weapon Mastery"]
    cols.sort(key=lambda c: pref.index(c[0]) if c[0] in pref else 99)
    return cols


def features_by_level(c, d):
    lv = {l: [] for l in range(1, 21)}
    for f in d["features"]:
        if f["feature_type"] != "CLASS_LEVEL_FEATURE":
            continue
        name = FIX_NAMES.get(f["name"], f["name"])
        if name in SKIP or name in ("Bard Subclass",):
            continue
        levels = sorted({g["level"] for g in f["gained_at"]})
        if name == "Improved Brutal Strike (Enhanced)":
            name = "Improved Brutal Strike"
        for l in levels:
            if 1 <= l <= 20 and name not in lv[l]:
                lv[l].append(name)
    for l, n in EXTRA.get(c, []):
        lv[l].append(n)
    sublabel = INFO[c]["sub"][0]
    for l in SUB_LEVELS[c]:
        if l == 3:
            if not any("Subclass" in x for x in lv[3]):
                lv[3].append(c.capitalize() + " Subclass")
        else:
            lv[l].append("Subclass feature")
    prof = lambda l: "+%d" % (2 + (l - 1) // 4)
    return lv, prof


def render_class(c):
    d = json.load(open(f"{DATA}/{c}.json"))
    info = INFO[c]
    t = core_traits(d)
    cols = columns(d)
    lv, prof = features_by_level(c, d)
    name = d["name"]
    from icons import icon
    nb = " newpage" if c == ORDER[0] else ""
    out = [f'<div class="class-banner{nb}"><div class="ch-num">Class</div><h1 class="classname">{name}</h1>'
           f'<div class="tagline">{info["tag"]}</div><span class="crest">{icon(c, 40, "#c99a3e", 1.4)}</span></div>']
    out.append('<div class="class-head"><div>')
    out.append(f'<p><span class="tag">{info["role"]}</span><span class="tag">Difficulty: {info["diff"]}</span></p>')
    out.append(f'<h3>How to Play</h3><p>{info["play"]}</p>')
    out.append(f'<div class="box"><h4>Quick beginner build</h4><p>{info["build"]}</p></div>')
    out.append('</div><div class="traits">')
    keys = ["Primary Ability", "Hit Point Die", "Saving Throw Proficiencies", "Skill Proficiencies",
            "Weapon Proficiencies", "Tool Proficiencies", "Armor Training", "Starting Equipment"]
    for k in keys:
        if k in t:
            out.append(f'<div><b>{k.replace(" Proficiencies"," ")}</b>{html.escape(t[k])}</div>')
    hd = d["hit_dice"].lower()
    hdn = int(hd[1:])
    out.append(f'<div><b>HP at Level 1</b>{hdn} + Con modifier</div>')
    out.append(f'<div><b>HP per Level After</b>1{hd} (or {hdn//2+1}) + Con modifier</div>')
    out.append('</div></div>')

    # level table
    head = "".join(f'<th class="c">{html.escape(n)}</th>' for n, _ in cols)
    out.append(f'<table class="compact"><caption>{name} Features by Level</caption><thead><tr><th class="c">Lvl</th><th class="c">Prof.</th><th>Features</th>{head}</tr></thead><tbody>')
    for l in range(1, 21):
        feats = ", ".join(lv[l]) or "—"
        cells = "".join(f'<td class="c">{v[l-1]}</td>' for _, v in cols)
        out.append(f'<tr><td class="c">{l}</td><td class="c">{prof(l)}</td><td>{feats}</td>{cells}</tr>')
    out.append('</tbody></table>')

    # features explained
    out.append('<h2>'+icon('book',16)+'Class Features Explained</h2><dl class="feat cols2">')
    seen = set()
    for l in range(1, 21):
        for n in lv[l]:
            if n == "Epic Boon":
                out.append('<div class="avoid"><dt><span class="lv">19</span>Epic Boon</dt><dd>Gain an Epic Boon feat — a near-legendary power.</dd></div>')
                continue
            if n in seen or n == "Subclass feature":
                continue
            seen.add(n)
            desc = info["feats"].get(n)
            if n == "Ability Score Improvement" and not desc:
                desc = "Increase one score by 2 or two by 1, or take a feat (levels 4, 8, 12, 16)."
            elif n == "Ability Score Improvement":
                desc = "Increase one score by 2 or two by 1, or take a feat. " + desc
            if n.endswith("Subclass") and not desc:
                desc = "Choose your subclass."
            if not desc:
                continue
            out.append(f'<div class="avoid"><dt><span class="lv">{l}</span>{n}</dt><dd>{desc}</dd></div>')
    out.append('</dl>')

    sname, sdesc, sfeats = info["sub"]
    out.append(f'<h2>{icon("star",16)}Subclass: {sname}</h2><p><i>{sdesc}</i></p><dl class="feat cols2">')
    for l, n, ds in sfeats:
        out.append(f'<div class="avoid"><dt><span class="lv">{l}</span>{n}</dt><dd>{ds}</dd></div>')
    import orig_render
    out.append(f'</dl><p class="small muted">{info["other"]} <b>Original subclasses in this book (Chapter 24):</b> {", ".join(orig_render.sub_names(c))}.</p>')
    out.append(ideas_block(c))
    import compendium as comp
    out.append(f'<h2>{icon("scroll",16)}{name}: Full Rules Text</h2><p class="small muted">The complete official wording of every {name} feature, for settling rules questions at the table.</p>')
    out.append(f'<div class="cols2 compendium fulltext">{comp.class_full_text(c)}</div>')
    sub = comp.subclass_full_text(c)
    if sub:
        out.append(f'<h2>{icon("star",16)}Subclass Full Rules Text</h2><div class="cols2 compendium fulltext">{sub}</div>')
    return "\n".join(out)


def overview_rows():
    rows = []
    for c in ORDER:
        d = json.load(open(f"{DATA}/{c}.json"))
        t = core_traits(d)
        rows.append((d["name"], INFO[c]["tag"], d["hit_dice"].lower(), t.get("Primary Ability", ""),
                     t.get("Saving Throw Proficiencies", ""), INFO[c]["diff"]))
    return rows


def all_classes():
    return "\n".join(render_class(c) for c in ORDER)


if __name__ == "__main__":
    print(all_classes()[:3000])


def cards():
    out = ['<div class="cards">']
    for c in ORDER:
        d = json.load(open(f"{DATA}/{c}.json"))
        t = core_traits(d)
        from icons import icon
        out.append(f'''<div class="card"><div class="top"><span class="ch-badge">{icon(c, 18, "#f6e2b8", 1.5)}</span>
<div><h3>{d["name"]}</h3><div class="meta">{d["hit_dice"].lower()} HP · {t.get("Primary Ability","")} · {INFO[c]["diff"]}</div></div></div>
<p>{INFO[c]["tag"]}</p><p class="meta" style="margin-top:1mm"><b>Role:</b> {INFO[c]["role"]}</p></div>''')
    out.append('</div>')
    return "\n".join(out)


IDEAS = {
"barbarian": (["A gladiator who won their freedom and never stopped fighting", "Last survivor of a mountain clan, carrying their ancestors' axe", "A gentle giant who rages only to protect children", "A dockworker whose temper got them exiled", "A berserker trying to learn control from a monk", "A tribal champion sent to prove themselves in the cities"],
  ["Rage on your first turn of a fight — it's a bonus action, so you still attack.", "Use Reckless Attack against enemies that hit weakly; skip it against big hitters.", "Stand between enemies and squishy casters. Your job is to be the target."]),
"bard": (["A tavern singer who's secretly a spy", "A disgraced court poet chasing one last great story", "A traveling storyteller collecting legends of a lost hero", "A street performer who talks their way out of everything", "A historian who believes songs are real magic", "A musician bound to a cursed instrument"],
  ["Give Bardic Inspiration before big rolls, not after failures.", "Keep Healing Word ready to pick up downed allies from range.", "Do the talking in social scenes — you have the skills for it."]),
"cleric": (["A temple healer sent out to fight a spreading plague", "A battle chaplain who lost faith and found it again", "An acolyte who received a vision no one believes", "A wandering priest of a forgotten god", "A former thief redeemed by divine grace", "A grave-keeper sworn to put the restless dead to sleep"],
  ["Cast Bless or Spirit Guardians early; prevention beats healing.", "Use Healing Word (bonus action) on unconscious allies, then still act.", "In heavy armor with a shield, you can hold the front line too."]),
"druid": (["A hermit who speaks more with wolves than people", "A city-born druid who finds nature in gardens and rooftops", "A guardian of a sacred grove that was burned", "A herbalist whose remedies hide real magic", "A shapeshifter who isn't sure which form is the real one", "A storm-caller from a coastal village"],
  ["Wild Shape into a spider or cat to scout ahead.", "Entangle and Faerie Fire change whole fights — control first, damage second.", "Your concentration spell is precious; stay out of melee to protect it."]),
"fighter": (["A veteran of a war that ended too soon", "A disgraced knight seeking redemption", "A mercenary who fights for the highest bidder — for now", "A town guard who saw something they shouldn't have", "A duelist chasing the title of greatest blade alive", "A farmer's child who picked up a fallen soldier's sword"],
  ["Save Action Surge for the turn that ends a fight, or saves a friend.", "Use Second Wind whenever you're hurt and have a free bonus action.", "Pick weapon masteries that fit your role: Sap or Push to protect, Graze or Cleave to deal damage."]),
"monk": (["A temple orphan sent into the world to learn", "A former assassin seeking peace through discipline", "A street fighter self-taught from stolen scrolls", "The last student of a destroyed monastery", "A wandering healer who fights only when it's needed", "A pilgrim walking to every shrine in the land"],
  ["Use your speed to reach enemy casters and archers in the back line.", "Stunning Strike the scariest enemy, then let the party pile on.", "Patient Defense when surrounded; Step of the Wind to escape."]),
"paladin": (["A knight sworn to protect a fallen kingdom's heir", "A crusader questioning the order that trained them", "A village defender whose oath came in a dream", "A vengeful warrior hunting the cult that killed their family", "A royal guard who follows the oath over the crown", "A reformed bandit bound to atone for every life taken"],
  ["Save Divine Smite for crits — the extra dice double too.", "Lay On Hands can revive a downed ally with just 1 HP from the pool.", "Stay near allies after level 6: your aura boosts everyone's saves."]),
"ranger": (["A monster hunter paid by frightened villages", "A border scout who knows every forest path", "A tracker searching for a missing sibling", "A poacher turned protector of the wild", "A guide who leads caravans through deadly wastes", "A hermit archer drawn out by a threat to their woods"],
  ["Cast Hunter's Mark on the first big target; move it when that target drops.", "Stay at range, use cover, and make enemies come to you.", "Lead the party when exploring: tracking, navigation, ambush detection."]),
"rogue": (["A pickpocket with a heart of gold", "A noble's spy who knows too many secrets", "A treasure hunter obsessed with ancient ruins", "A con artist running from their last mark", "An assassin who refused one contract", "A guild burglar framed for a theft they didn't do"],
  ["Stay next to an ally's target to get Sneak Attack without advantage.", "Attack, then Cunning Action (Hide or Disengage) to stay safe.", "Scout ahead, check for traps, and pick the locks — that's your spotlight."]),
"sorcerer": (["A noble whose dragon ancestry suddenly awoke", "A survivor of a magical disaster that changed them", "A child of a storm, born during a lightning strike", "A sorcerer hiding powers that terrify their family", "A wild talent who can't always control the magic", "A heir to a bloodline sought by a dark cult"],
  ["Twinned or Quickened spells are your biggest Metamagic power spikes.", "Keep Shield and a defensive option prepared — you're fragile.", "Turn on Innate Sorcery for big turns: higher DC and spell attack advantage."]),
"warlock": (["A scholar who read the wrong book", "A desperate soul who bargained to save someone they love", "A fey-touched wanderer who owes a debt to a faerie queen", "A cultist trying to escape their patron", "A gambler who made a deal they don't fully understand", "A noble's child promised to a devil before birth"],
  ["Eldritch Blast + Agonizing Blast is your reliable every-turn attack.", "Your slots return on short rests — ask the party for them.", "Pick invocations that solve problems: Devil's Sight, Mask of Many Faces."]),
"wizard": (["An academy dropout chasing forbidden research", "A librarian who stumbled on a spellbook", "A court mage exiled for a failed prophecy", "An apprentice whose master vanished", "A scholar of dead languages and older magic", "A tinkerer who treats spells like engineering"],
  ["Always keep Shield prepared; it saves your life constantly.", "Control spells (Sleep, Web, Hypnotic Pattern) often beat damage spells.", "Copy every spell scroll you find into your spellbook."]),
}


def ideas_block(c):
    from icons import icon
    concepts, tips = IDEAS[c]
    rows = "".join(f'<tr><td class="c">{i+1}</td><td>{t}</td></tr>' for i, t in enumerate(concepts))
    tl = "".join(f"<li>{t}</li>" for t in tips)
    return (f'<div class="grid2 keep" style="margin-top:3mm"><div><table class="compact"><caption>{icon("dice",13)} Character Ideas (roll a d6)</caption>'
            f'<tbody>{rows}</tbody></table></div><div class="box" style="margin-top:0"><h4>{icon("tip",14)}Tactics</h4><ul>{tl}</ul></div></div>')
