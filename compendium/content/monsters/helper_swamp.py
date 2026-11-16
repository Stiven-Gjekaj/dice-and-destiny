"""Original swamp monsters, added by a helper of the bestiary: reed beds, peat bogs, black water, and drowned holy places."""
from monster_engine import M
R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())
UNDEAD = "Charmed, Exhaustion, Frightened, Poisoned"
CONSTRUCT = "Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned"
LEGRES = ("Legendary Resistance ({n}/Day)", "If the creature fails a saving throw, it can choose to succeed instead.")


def legres(n):
    return (LEGRES[0].format(n=n), LEGRES[1])


MON = [
M("Cattail Archer", "S", "Fey", "Neutral", 0.5, "8 16 10 10 14 10", speed="30 ft., swim 30 ft.", senses="Darkvision 60 ft.", lang="Sylvan", skills="Stealth",
  traits=[("Reed Hide", "In reeds or tall marsh grass, the archer can take the Hide action as a Bonus Action.")],
  attacks=[("Reed Bow", "r", "1d6", "Piercing", "", "60/240 ft")],
  desc="A tiny reed-man with a bow of bent cattail. It shoots at anyone who cuts reeds without asking the marsh first."),
M("Quagmire Ooze", "L", "Ooze", "Unaligned", 2, "16 4 18 1 8 1", ac=8, speed="10 ft., swim 10 ft.", senses="Blindsight 60 ft. (blind beyond this radius)",
  res=R(Resistances="Acid, Bludgeoning", Immunities="Blinded, Charmed, Deafened, Exhaustion, Frightened, Prone"),
  traits=[("False Appearance", "While the ooze is motionless, it looks like a patch of mud."), ("Sucking Body", "A creature that starts its turn in the ooze's space has the Restrained condition (escape {dc:str}).")],
  attacks=[("Engulf", "m", "2d8", "Bludgeoning", "and the target is pulled into the ooze's space")],
  desc="A slow, hungry mud that crawls toward warmth. Most bog bodies were found inside one."),
M("Mosquito Matriarch", "M", "Monstrosity", "Unaligned", 3, "8 16 14 2 12 4", speed="10 ft., fly 40 ft. (hover)", senses="Darkvision 60 ft.",
  traits=[("Blood Fever", "A creature that takes damage from the matriarch's Proboscis makes a {dc:con} Constitution saving throw. On a failure, it has the Poisoned condition until it finishes a Long Rest.")],
  attacks=[("Proboscis", "f", "2d8", "Piercing", "and the matriarch regains Hit Points equal to half the damage dealt")], multi=2,
  desc="A mosquito as big as a dog, followed by a cloud of her children. Marsh villages burn smoke all summer to keep her away."),
M("Peat Fire Spirit", "L", "Elemental", "Neutral", 8, "16 14 20 6 12 8", speed="30 ft., burrow 30 ft.", senses="Tremorsense 60 ft.", lang="Ignan",
  res=R(Resistances="Bludgeoning, Piercing, Slashing", Immunities="Fire, Poison; Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious"),
  traits=[("Smolder Underground", "The spirit can burrow through peat and soft earth, leaving the ground hot and smoking. The ground within 10 feet of it is Difficult Terrain."),
          ("Choking Smoke", "Each creature that starts its turn within 10 feet of the spirit takes {2d6} Poison damage unless it can't breathe smoke.")],
  attacks=[("Burning Grasp", "m", "3d8", "Fire", "plus {2d6} Bludgeoning damage")], multi=2,
  desc="A fire that has burned under the peat bog for a hundred years without going out. It rises when someone cuts too deep."),
M("Drowned Abbot", "M", "Undead", "Lawful Evil", 11, "14 12 18 16 20 16", speed="30 ft., swim 30 ft.", senses="Truesight 60 ft.", lang="Common, Celestial",
  res=R(Resistances="Cold; Bludgeoning, Piercing, Slashing", Immunities="Necrotic, Poison; " + UNDEAD), saves="Con, Wis, Cha",
  traits=[legres(1), ("Bells Under the Water", "Undead within 120 feet of the abbot that can hear its bells have Advantage on saving throws against being Turned.")],
  attacks=[("Rotted Censer", "m", "3d10", "Bludgeoning", "plus {3d8} Necrotic damage", "10 ft")], multi=2,
  actions=[("Drowned Hymn (Recharge 5-6)", "Each creature of the abbot's choice within 60 feet of it makes a {dc:wis} Constitution saving throw. On a failure, it takes {8d8} Necrotic damage and can't breathe until the end of its next turn. On a success, it takes half as much damage only.")],
  desc="The head of a monastery that sank into the marsh with all its monks. On still nights, its bells ring under the water, and the monks rise to sing."),
M("Bog Iron Golem", "L", "Construct", "Unaligned", 12, "24 8 22 3 10 1", ac=19, speed="30 ft., swim 20 ft.", senses="Darkvision 120 ft.", lang="understands the languages of its creator but can't speak",
  res=R(Resistances="Bludgeoning, Piercing, Slashing", Immunities="Poison, Psychic; " + CONSTRUCT),
  traits=[("Magic Resistance", "The golem has Advantage on saving throws against spells and other magical effects."), ("Rust Bloom", "A nonmagical metal weapon that hits the golem takes a cumulative -1 penalty to damage rolls.")],
  attacks=[("Slam", "m", "5d10", "Bludgeoning", "", "10 ft")], multi=2,
  actions=[("Red Water (Recharge 5-6)", "The golem breathes rusty bog water in a 30-foot Cone. Each creature in it makes a {dc:con} Constitution saving throw, taking {9d8} Poison damage on a failed save or half as much on a successful one.")],
  desc="A guardian forged from red bog iron by the marsh kings of old. It still walks the causeways their kingdoms built."),
M("Snapping Titan", "G", "Beast", "Unaligned", 13, "26 6 24 2 12 4", ac=20, speed="20 ft., swim 40 ft.", senses="Darkvision 60 ft.",
  traits=[("Hold Breath", "The titan can hold its breath for 2 hours."), ("Shell", "As a Bonus Action, the titan pulls into its shell. Until the start of its next turn, it has a +5 bonus to AC and can't attack.")],
  attacks=[("Beak", "m", "5d10", "Slashing", "and if the target is Large or smaller, it has the Grappled condition (escape {dc:str})", "10 ft")], multi=2,
  desc="A snapping turtle the size of a hill, with moss and young trees on its shell. Some villages are built on one and don't know it."),
M("Blackwater Coil", "H", "Monstrosity", "Neutral Evil", 14, "22 16 20 14 16 18", speed="40 ft., swim 50 ft.", senses="Darkvision 120 ft.", lang="Common, Sylvan",
  res=R(Immunities="Poison; Charmed, Poisoned"), saves="Dex, Con, Wis",
  traits=[legres(2), ("Hypnotic Coils", "When a creature that can see the coil starts its turn within 30 feet of it, the creature makes a {dc:cha} Wisdom saving throw or has the Incapacitated condition until the start of its next turn.")],
  attacks=[("Bite", "m", "3d12", "Piercing", "plus {3d6} Poison damage", "10 ft"), ("Constrict", "m", "3d10", "Bludgeoning", "and the target has the Grappled condition (escape {dc:str})", "15 ft")], multi=2,
  desc="A serpent with a woman's face and black-mirror scales that lies in the darkest pools of the swamp. It trades secrets for warm blood."),
M("Weeping Willow Matriarch", "G", "Plant", "Neutral", 17, "26 8 24 16 22 18", speed="20 ft.", senses="Blindsight 120 ft.", lang="Druidic, Sylvan",
  res=R(Vulnerabilities="Fire", Resistances="Bludgeoning, Piercing", Immunities="Charmed, Frightened"), saves="Con, Wis, Cha",
  traits=[legres(3), ("Sorrow", "Each creature that starts its turn within 60 feet of the matriarch makes a {dc:wis} Wisdom saving throw or has Disadvantage on attack rolls until the start of its next turn, as grief overcomes it.")],
  attacks=[("Lashing Branches", "m", "4d12", "Bludgeoning", "and the target has the Restrained condition (escape {dc:str})", "30 ft")], multi=3,
  actions=[("Drown in Tears (Recharge 5-6)", "Water rises in a 30-foot-radius Sphere around a creature the matriarch can see within 120 feet. Each creature in it makes a {dc:wis} Constitution saving throw, taking {12d10} Bludgeoning damage on a failed save or half as much on a successful one.")],
  leg=[("Lash", "The matriarch makes one Lashing Branches attack."), ("Root Step", "The matriarch moves up to her Speed through the mud without provoking Opportunity Attacks.")],
  desc="The oldest willow of the great marsh, who wept for every child the black water took until her tears became a lake."),
M("Plague-Moon Wyrm", "G", "Dragon", "Chaotic Evil", 21, "28 10 27 16 16 20", ac=21, speed="40 ft., fly 80 ft., swim 40 ft.", senses="Blindsight 60 ft., Darkvision 120 ft.", lang="Common, Draconic",
  res=R(Immunities="Necrotic, Poison; Poisoned"), saves="Dex, Con, Wis, Cha",
  traits=[legres(4), ("Fever Haze", "Each creature that starts its turn within 30 feet of the wyrm makes a {dc:con} Constitution saving throw or gains 1 Exhaustion level. A creature that succeeds is immune for 24 hours.")],
  attacks=[("Bite", "m", "4d12", "Piercing", "plus {4d8} Necrotic damage", "15 ft"), ("Claw", "m", "3d12", "Slashing", "", "10 ft")], multi=2,
  actions=[("Plague Breath (Recharge 5-6)", "The wyrm breathes a green fever cloud in a 90-foot Cone. Each creature in it makes a {dc:con} Constitution saving throw, taking {16d10} Necrotic damage on a failed save or half as much on a successful one.")],
  leg=[("Claw", "The wyrm makes one Claw attack."), ("Fever Wing (Costs 2 Actions)", "Each creature within 20 feet of the wyrm makes a {dc:con} Dexterity saving throw, taking {4d10} Necrotic damage on a failed save or half as much on a successful one.")],
  desc="A sickly green dragon that rises from the swamp only under a blood-colored moon. Plagues follow its shadow for a hundred miles."),
]

# The shared traits say "The creature". Put the name of each monster in its place.
for _m in MON:
    _m.traits = [(n, t.replace("If the creature", "If the " + _m.ref())) for n, t in _m.traits]
