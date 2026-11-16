"""Original NPCs of the temples and the cults."""
from monster_engine import M
R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())
P, CU = "Priests and the Faithful", "Cultists"
HUM = "Humanoid"

NPCS = [
# ================= PRIESTS AND THE FAITHFUL =================
(P, M("Temple Novice", "M", HUM, "Lawful Good", 0.125, "10 10 12 11 14 11", skills="Religion", lang="Common",
  attacks=[("Mace", "m", "1d6", "Bludgeoning")],
  actions=[("Spellcasting", "The novice casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). At will: Light, Thaumaturgy. 1/Day: Bless.")],
  desc="A young member of a temple who sweeps the floors, rings the bells, and dreams of miracles.")),
(P, M("Wandering Friar", "M", HUM, "Neutral Good", 1, "12 10 14 11 15 13", skills="Insight, Medicine, Persuasion", lang="Common, and one other language",
  attacks=[("Quarterstaff", "m", "1d8", "Bludgeoning", "plus {1d6} Radiant damage")],
  actions=[("Spellcasting", "The friar casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). At will: Guidance, Spare the Dying. 1/Day each: Cure Wounds, Sanctuary.")],
  desc="A traveling priest with a staff, a bowl, and a story for every village. The roads are safer where friars walk.")),
(P, M("Plague Doctor", "M", HUM, "Lawful Neutral", 3, "10 12 14 16 16 10", ac=13, skills="Medicine*, Nature", lang="Common, and two other languages",
  res=R(Resistances="Necrotic, Poison", Immunities="Poisoned"),
  traits=[("Beaked Mask", "The doctor has Advantage on saving throws against disease and against inhaled poisons and gases.")],
  attacks=[("Cane Blade", "f", "1d8", "Piercing", "plus {2d6} Poison damage")], multi=2,
  actions=[("Cleansing Smoke (Recharge 5–6)", "The doctor burns herbs. Each ally in a 15-foot Emanation originating from it ends the Poisoned condition on itself and regains {2d8} Hit Points. Each enemy in the area makes a {dc:int} Constitution saving throw or has the Poisoned condition until the end of its next turn.")],
  desc="A healer in a waxed coat and a bird mask who walks into the sick quarter when everyone else walks out.")),
(P, M("Battle Abbess", "M", HUM, "Lawful Good", 6, "16 10 16 12 18 14", ac=18, saves="Con, Wis", skills="Insight, Medicine, Religion", lang="Common, and one other language",
  traits=[("Aura of Faith", "Allies within 10 feet of the abbess have Advantage on saving throws against being Charmed and Frightened.")],
  attacks=[("Flail", "m", "1d10", "Bludgeoning", "plus {2d8} Radiant damage")], multi=2,
  actions=[("Spellcasting", "The abbess casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). At will: Sacred Flame. 1/Day each: Mass Healing Word, Spirit Guardians.")],
  bonus=[("Field Prayer", "One ally within 30 feet that the abbess can see regains {2d8} Hit Points. (3/Day)")],
  desc="The head of a fighting abbey, who swings a flail in one hand and blesses the wounded with the other.")),
(P, M("High Inquisitor", "M", HUM, "Lawful Neutral", 12, "16 12 18 16 20 18", ac=19, saves="Con, Wis, Cha", skills="Insight*, Intimidation, Investigation, Religion", lang="Common, and three other languages",
  res=R(Immunities="Charmed, Frightened"),
  traits=[("Truthseeker", "The inquisitor always knows when a creature within 30 feet of it says something that the creature knows is false."),
          ("Indomitable (2/Day)", "If the inquisitor fails a saving throw, it can reroll the save and must use the new roll.")],
  attacks=[("Branding Mace", "m", "2d8", "Bludgeoning", "plus {4d8} Radiant damage")], multi=2,
  actions=[("Judgment (Recharge 5–6)", "Each creature of the inquisitor's choice within 30 feet makes a {dc:wis} Wisdom saving throw. On a failed save, a creature takes {8d10} Radiant damage and has the Incapacitated condition until the end of its next turn. On a successful save, it takes half as much damage only."),
           ("Spellcasting", "The inquisitor casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). 1/Day each: Dispel Magic, Hold Monster, Zone of Truth.")],
  desc="The temple's hunter of heretics and fiends. Even the innocent sweat when it enters the room.")),

# ================= CULTISTS =================
(CU, M("Cult Initiate", "M", HUM, "Chaotic Evil", 0.25, "11 12 12 10 10 13", lang="Common",
  traits=[("Fanatic Hope", "The initiate has Advantage on saving throws against being Frightened.")],
  attacks=[("Sickle", "f", "1d4", "Slashing", "plus {1d4} Necrotic damage")],
  desc="A desperate person who joined the cult for a promise. The promise was a lie, but the initiate doesn't know it yet.")),
(CU, M("Blood Chanter", "M", HUM, "Chaotic Evil", 4, "10 14 14 12 13 17", ac=13, skills="Deception, Religion", lang="Common, Abyssal",
  traits=[("Blood Price", "When an ally of the chanter dies within 30 feet of it, the chanter regains {1d10} Hit Points.")],
  attacks=[("Bleeding Dagger", "f", "1d4", "Piercing", "plus {2d6} Necrotic damage")], multi=2,
  actions=[("Chant of Ruin (Recharge 5–6)", "Each creature of the chanter's choice within 30 feet that can hear it makes a {dc:cha} Constitution saving throw. On a failed save, a creature takes {4d8} Necrotic damage and can't regain Hit Points until the end of its next turn. On a successful save, it takes half as much damage only."),
           ("Spellcasting", "The chanter casts one of the following spells, using Charisma as the spellcasting ability ({dc:cha}). 1/Day each: Bane, Hold Person.")],
  desc="The voice of the cult's rites, who leads the chanting until the candles drip red.")),
(CU, M("Herald of the Hidden God", "M", HUM, "Chaotic Evil", 9, "12 14 16 16 16 20", ac=16, saves="Con, Wis, Cha", skills="Deception, Insight, Persuasion, Religion", lang="Common, Abyssal, Infernal",
  res=R(Resistances="Necrotic, Psychic"),
  traits=[("Faithful Shield", "While a cultist ally is within 5 feet of the herald, attack rolls against the herald have Disadvantage.")],
  attacks=[("Sacrificial Knife", "f", "1d6", "Piercing", "plus {4d8} Necrotic damage"), ("Word of the God", "s:cha", "4d10", "Psychic", "", "120 ft.")], multi=2,
  actions=[("Unveil the God (Recharge 5–6)", "Each creature of the herald's choice within 60 feet that can see it makes a {dc:cha} Wisdom saving throw. On a failed save, a creature takes {6d10} Psychic damage and has the Frightened condition for 1 minute. It repeats the save at the end of each of its turns, ending the Frightened condition on itself on a success. On a successful save, it takes half as much damage only."),
           ("Spellcasting", "The herald casts one of the following spells, using Charisma as the spellcasting ability ({dc:cha}). 1/Day each: Dimension Door, Dominate Person.")],
  desc="The high priest of a god that the world forgot on purpose. Its sermons are beautiful, and they end in blood.")),
]
