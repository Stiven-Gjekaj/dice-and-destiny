"""Original underdark monsters of CR 11 to 16, added by a helper of the bestiary: deep caves, fungus forests, and the lightless seas."""
from monster_engine import M
R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())
UNDEAD = "Charmed, Exhaustion, Frightened, Poisoned"
CONSTRUCT = "Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned"
LEGRES = ("Legendary Resistance ({n}/Day)", "If the creature fails a saving throw, it can choose to succeed instead.")


def legres(n):
    return (LEGRES[0].format(n=n), LEGRES[1])


MON = [
# ================= CR 5 TO 10 =================
M("Glimmerworm", "L", "Monstrosity", "Unaligned", 5, "18 10 18 2 12 4", speed="20 ft., climb 20 ft.", senses="Blindsight 60 ft. (blind beyond this radius)",
  traits=[("Lure Lights", "The worm's back is covered in small lights like a starry sky. A creature that sees them for the first time on a turn makes a {dc:con} Wisdom saving throw or has the Charmed condition until the end of its next turn and must move toward the worm.")],
  attacks=[("Bite", "m", "2d8", "Piercing", "plus {1d8} Acid damage")], multi=2,
  desc="A pale worm that hangs from cave ceilings and glows like the night sky. Lost miners walk toward the stars, and up into its mouth."),
M("Stalagmite Ambusher", "L", "Monstrosity", "Unaligned", 8, "22 10 20 4 14 4", ac=17, speed="10 ft., climb 10 ft.", senses="Tremorsense 60 ft.", skills="Stealth",
  traits=[("False Appearance", "While the ambusher is motionless, it looks like a stalagmite."), ("Sudden Strike", "In the first round of a combat, the ambusher has Advantage on attack rolls against a creature that hasn't taken a turn yet.")],
  attacks=[("Stone Spike", "m", "3d10", "Piercing", "", "10 ft")], multi=2,
  desc="A cave hunter shaped like a cone of wet stone. A forest of stalagmites in a quiet cave is never only stone."),
# ================= CR 11 TO 16 =================
M("Crystal Basilisk Queen", "H", "Monstrosity", "Unaligned", 11, "22 10 22 4 14 8", ac=19, speed="30 ft., burrow 20 ft.", senses="Darkvision 120 ft.",
  traits=[legres(1), ("Prism Hide", "When a spell attack misses the queen, she can reflect it at another creature within 60 feet. Use the same attack roll against the new target.")],
  attacks=[("Bite", "m", "3d12", "Piercing", "plus {2d6} Force damage", "10 ft")], multi=2,
  actions=[("Petrifying Prism (Recharge 5-6)", "Each creature in a 60-foot Cone that can see the queen makes a {dc:con} Constitution saving throw. On a failure, it takes {8d8} Force damage and has the Restrained condition as it starts to turn to crystal. It repeats the save at the end of its next turn; on a failure, it has the Petrified condition until a Greater Restoration spell ends it. On a success, it takes half as much damage only.")],
  desc="A many-legged lizard of living crystal who lays her eggs in geodes. Her gaze turns flesh into glittering stone."),
M("Gloomweaver Matron", "H", "Monstrosity", "Neutral Evil", 12, "22 16 20 12 16 10", speed="40 ft., climb 40 ft.", senses="Blindsight 60 ft., Darkvision 120 ft.", lang="understands Undercommon but can't speak", skills="Stealth",
  res=R(Immunities="Poison; Poisoned"), saves="Dex, Con, Wis",
  traits=[legres(1), ("Web Walker", "The matron ignores movement restrictions caused by webs, and she knows the location of any creature that touches her webs within 300 feet.")],
  attacks=[("Bite", "m", "3d12", "Piercing", "plus {3d6} Poison damage", "10 ft")], multi=2,
  actions=[("Web Storm (Recharge 5-6)", "The matron sprays webbing in a 30-foot Cube within 60 feet. Each creature in the area makes a {dc:con} Dexterity saving throw. On a failure, it takes {8d8} Poison damage from the barbs and has the Restrained condition (escape {dc:str}). On a success, it takes half as much damage only.")],
  desc="A spider the size of a house with a pale mark like a face on her back. Her webs span whole chasms, and the cave folk pay her a toll to cross."),
M("Lightless Sea Kraken", "G", "Monstrosity", "Neutral Evil", 13, "24 12 22 14 14 12", speed="10 ft., swim 60 ft.", senses="Blindsight 120 ft.", lang="understands Undercommon but can't speak",
  res=R(Resistances="Cold"), saves="Str, Con, Wis",
  traits=[legres(2), ("Amphibious", "The kraken can breathe air and water.")],
  attacks=[("Tentacle", "m", "3d10", "Bludgeoning", "and the target has the Grappled condition (escape {dc:str})", "30 ft")], multi=3,
  actions=[("Ink of Nothing (Recharge 5-6)", "The kraken releases black ink in a 40-foot-radius Sphere around it. The area is Heavily Obscured for 1 minute. Each creature in it makes a {dc:con} Constitution saving throw, taking {8d10} Necrotic damage on a failed save or half as much on a successful one.")],
  desc="A pale, eyeless squid of the sunless seas under the earth. The cave fishers make offerings of light to keep it away."),
M("Echo Wyrm", "H", "Dragon", "Chaotic Evil", 14, "22 14 22 14 14 14", speed="40 ft., climb 40 ft., fly 60 ft.", senses="Blindsight 120 ft.", lang="Draconic, Undercommon",
  res=R(Immunities="Thunder; Deafened"), saves="Dex, Con, Wis",
  traits=[legres(2), ("Echo Sight", "The wyrm can't be surprised, and it knows the location of each creature within 120 feet that makes a sound.")],
  attacks=[("Bite", "m", "3d12", "Piercing", "plus {2d8} Thunder damage", "10 ft"), ("Claw", "m", "3d8", "Slashing")], multi=2,
  actions=[("Shriek (Recharge 5-6)", "The wyrm shrieks in a 60-foot Cone. Each creature in it makes a {dc:con} Constitution saving throw. On a failure, it takes {10d8} Thunder damage and has the Deafened and Stunned conditions until the end of its next turn. On a success, it takes half as much damage only.")],
  desc="A blind black dragon of the great caverns that sees with sound. The caves ring for days after it passes."),
M("Hollow King's Golem", "H", "Construct", "Unaligned", 15, "26 8 24 3 10 1", ac=20, speed="30 ft.", senses="Darkvision 120 ft.", lang="understands the languages of its creator but can't speak",
  res=R(Resistances="Bludgeoning, Piercing, Slashing", Immunities="Fire, Poison, Psychic; " + CONSTRUCT), saves="Str, Con",
  traits=[("Magic Resistance", "The golem has Advantage on saving throws against spells and other magical effects."), ("Forge Heart", "When the golem takes Fire damage, it regains Hit Points equal to the damage instead.")],
  attacks=[("Slam", "m", "4d12", "Bludgeoning", "plus {2d8} Fire damage", "10 ft")], multi=2,
  actions=[("Molten Breath (Recharge 5-6)", "The golem breathes molten metal in a 30-foot Cone. Each creature in it makes a {dc:con} Dexterity saving throw, taking {10d10} Fire damage on a failed save or half as much on a successful one.")],
  desc="A guardian of black iron and lava, forged in the deepest hall of a dwarf king whose kingdom fell long ago. It still guards the door."),
M("Deep Mother", "G", "Aberration", "Neutral Evil", 16, "20 10 24 20 18 20", speed="10 ft., burrow 20 ft., swim 30 ft.", senses="Truesight 120 ft.", lang="Deep Speech, telepathy 1 mile",
  res=R(Resistances="Acid, Cold; Bludgeoning, Piercing, Slashing", Immunities="Psychic; Charmed, Frightened, Prone"), saves="Con, Int, Wis",
  traits=[legres(3), ("Brood", "At the start of each of the Deep Mother's turns, a Medium Aberration hatchling (use the Grick) appears in an unoccupied space within 30 feet of her. No more than four hatchlings exist at a time.")],
  attacks=[("Tendril", "m", "4d10", "Bludgeoning", "plus {2d8} Psychic damage", "20 ft")], multi=2,
  actions=[("Mind Flood (Recharge 5-6)", "Each creature within 120 feet that the Deep Mother can sense makes a {dc:int} Intelligence saving throw. On a failure, it takes {9d10} Psychic damage and has the Incapacitated condition until the end of its next turn. On a success, it takes half as much damage only.")],
  leg=[("Spawn", "A new hatchling appears, if there are fewer than four."), ("Tendril", "The Deep Mother makes one Tendril attack.")],
  desc="A vast, soft thing that fills a cavern the size of a city square. Everything that crawls in the deep tunnels came from her once."),
# ================= CR 17 TO 24 =================
M("Queen Below the Roots", "M", "Fey", "Neutral Evil", 17, "14 20 18 20 20 24", speed="40 ft.", senses="Truesight 120 ft.", lang="Common, Elvish, Sylvan, Undercommon", skills="Deception, Insight, Persuasion",
  res=R(Resistances="Cold, Necrotic", Immunities="Charmed, Frightened"), saves="Dex, Wis, Cha",
  traits=[legres(3), ("Court of Shadows", "Fey and Undead within 120 feet of the queen have Advantage on saving throws."), ("Magic Resistance", "The queen has Advantage on saving throws against spells and other magical effects.")],
  attacks=[("Thorn Blade", "f", "5d10", "Slashing", "plus {2d8} Necrotic damage")], multi=2,
  actions=[("Bargain of Shadows (Recharge 5-6)", "Each creature of the queen's choice within 60 feet of her makes a {dc:cha} Charisma saving throw. On a failure, it takes {10d10} Psychic damage and has the Charmed condition until the end of its next turn. On a success, it takes half as much damage only."),
           ("Spellcasting", "The queen casts one of the following spells, using Charisma as the spellcasting ability ({dc:cha}). 1/Day each: Dominate Person, Plane Shift, Teleport.")],
  leg=[("Shadow Step", "The queen teleports up to 30 feet to a space in Dim Light or Darkness."), ("Thorn Blade", "The queen makes one Thorn Blade attack.")],
  desc="A fey queen who left the courts of the moon and took a kingdom under the earth, where no sun can judge her."),
M("Mountain-Eater Worm", "G", "Monstrosity", "Unaligned", 19, "28 6 26 2 12 4", ac=20, speed="40 ft., burrow 40 ft.", senses="Tremorsense 300 ft.",
  res=R(Resistances="Bludgeoning, Piercing, Slashing"), saves="Str, Con",
  traits=[legres(3), ("Tunneler", "The worm can burrow through solid rock at half its Burrow Speed and leaves a tunnel 30 feet wide."), ("Siege Monster", "The worm deals double damage to objects and structures.")],
  attacks=[("Bite", "m", "5d12", "Piercing", "and if the target is Huge or smaller, it is swallowed on a roll of 18 or more. A swallowed creature has the Blinded and Restrained conditions and takes {8d6} Acid damage at the start of each of the worm's turns", "15 ft"), ("Tail Sting", "m", "4d10", "Piercing", "plus {6d6} Poison damage", "15 ft")], multi=2,
  actions=[("Cave-In (Recharge 5-6)", "The worm thrashes against the walls. Each creature within 60 feet of it makes a {dc:con} Dexterity saving throw. On a failure, it takes {12d10} Bludgeoning damage and has the Restrained condition under rubble (escape DC 15). On a success, it takes half as much damage only.")],
  leg=[("Burrow", "The worm moves up to half its Burrow Speed."), ("Tail Sting", "The worm makes one Tail Sting attack.")],
  desc="A worm so old and so long that the great cave roads of the deep are its old tunnels. The deep folk mark each tremor it makes."),
]
