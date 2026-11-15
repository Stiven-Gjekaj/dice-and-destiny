from monster_engine import M
R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())
CON = R(Immunities="Poison, Psychic; Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned")

def dragon(kind, color, elem, cond, age, cr, size, ab, ac, extra_trait=None, leg=False):
    breath_shape = "60-foot Cone" if size in ("H", "G") else ("30-foot Cone" if size == "L" else "15-foot Cone")
    dice = {"Wyrmling": "4d10", "Young": "10d8", "Adult": "14d10", "Ancient": "18d10"}[age]
    traits = [("Elemental Body", f"The dragon has Immunity to {elem} damage.")]
    if extra_trait: traits.append(extra_trait)
    if age in ("Adult", "Ancient"):
        traits.insert(0, ("Legendary Resistance (3/Day)", "If the dragon fails a saving throw, it can choose to succeed instead."))
    multi = {"Wyrmling": 2, "Young": 3, "Adult": 3, "Ancient": 3}[age]
    bite = {"Wyrmling": "1d10", "Young": "2d10", "Adult": "2d10", "Ancient": "2d12"}[age]
    edice = {"Wyrmling": "1d6", "Young": "2d6", "Adult": "3d6", "Ancient": "4d6"}[age]
    reach = "10 ft." if size in ("L", "H", "G") else "5 ft."
    lg = []
    if age in ("Adult", "Ancient"):
        lg = [("Strike", "The dragon makes one Rend attack."), ("Wing Gust", "Each creature within 15 feet makes a {dc:str} Strength save or is pushed 15 feet and knocked Prone."),
              (f"{kind} Pulse (Costs 2)", f"Each creature of the dragon's choice within 30 feet takes {{{edice}}} {elem} damage.")]
    return M(f"{age} {kind} Dragon", size, "Dragon", "Neutral" if kind != "Ash" else "Chaotic Evil", cr, ab, ac=ac,
             speed="40 ft., fly 80 ft." if age != "Wyrmling" else "30 ft., fly 60 ft.", senses="Blindsight 30 ft., Darkvision 120 ft.", skills="Perception, Stealth",
             saves="Dex, Wis", res=R(Immunities=elem), lang="Common, Draconic" if age != "Wyrmling" else "Draconic",
             traits=traits, attacks=[("Rend", "m", bite, "Slashing", f"plus {{{edice}}} {elem} damage", reach)], multi=multi,
             actions=[(f"{kind} Breath (Recharge 5–6)", f"Each creature in a {breath_shape} makes a {{dc:con}} Constitution save, taking {{{dice}}} {elem} damage on a failure, or half on a success. {cond}")],
             leg=lg, desc=color if age == "Young" else "")

MON = [
# ================= DRAGONS: two original families =================
dragon("Ash", "Ash dragons nest in volcanic calderas and burn whole forests to make room for their hoards. Their breath is a choking cloud of cinders.", "Fire",
       "A creature that fails is also Blinded until the end of its next turn.", "Wyrmling", 2, "M", "17 12 15 10 11 13", 16),
dragon("Ash", "Ash dragons nest in volcanic calderas and burn whole forests to make room for their hoards. Their breath is a choking cloud of cinders.", "Fire",
       "A creature that fails is also Blinded until the end of its next turn.", "Young", 9, "L", "21 10 19 13 12 16", 18,
       ("Smoldering Scales", "A creature that hits the dragon with a melee attack within 5 feet takes {2d6} Fire damage.")),
dragon("Ash", "", "Fire", "A creature that fails is also Blinded until the end of its next turn.", "Adult", 16, "H", "25 10 23 15 13 19", 19,
       ("Smoldering Scales", "A creature that hits the dragon with a melee attack within 5 feet takes {3d6} Fire damage.")),
dragon("Ash", "", "Fire", "A creature that fails is also Blinded until the end of its next turn.", "Ancient", 23, "G", "29 10 27 17 15 22", 21,
       ("Smoldering Scales", "A creature that hits the dragon with a melee attack within 5 feet takes {4d6} Fire damage.")),
dragon("Storm", "Storm dragons ride thunderheads above the sea. They are proud, curious and fiercely territorial about the skies.", "Lightning",
       "A creature that fails also can't take Reactions until the start of its next turn.", "Wyrmling", 2, "M", "15 14 13 12 12 14", 16),
dragon("Storm", "Storm dragons ride thunderheads above the sea. They are proud, curious and fiercely territorial about the skies.", "Lightning",
       "A creature that fails also can't take Reactions until the start of its next turn.", "Young", 9, "L", "19 14 17 14 13 17", 18,
       ("Charged Air", "Creatures wearing metal armor within 10 feet of the dragon have Disadvantage on attack rolls against it.")),
dragon("Storm", "", "Lightning", "A creature that fails also can't take Reactions until the start of its next turn.", "Adult", 16, "H", "23 14 21 16 15 20", 19,
       ("Charged Air", "Creatures wearing metal armor within 15 feet of the dragon have Disadvantage on attack rolls against it.")),
dragon("Storm", "", "Lightning", "A creature that fails also can't take Reactions until the start of its next turn.", "Ancient", 22, "G", "27 14 25 18 17 23", 21,
       ("Charged Air", "Creatures wearing metal armor within 30 feet of the dragon have Disadvantage on attack rolls against it.")),
M("Cinder Drake", "L", "Dragon", "Unaligned", 4, "18 13 16 4 11 7", ac=15, speed="30 ft., fly 60 ft.", senses="Darkvision 60 ft.", res=R(Immunities="Fire"),
  attacks=[("Bite", "m", "2d8", "Piercing", "plus {1d6} Fire damage", "10 ft.")], multi=2,
  actions=[("Spit Cinders (Recharge 5–6)", "A 30-foot line: each creature makes a {dc:con} Dexterity save, taking {5d6} Fire damage on a failure, half on a success.")],
  desc="Wingless-minded cousins of true dragons, bred as war mounts."),
M("Sky Serpent", "H", "Dragon", "Unaligned", 7, "19 18 16 4 12 8", ac=15, speed="10 ft., fly 90 ft.", senses="Blindsight 60 ft.", res=R(Immunities="Lightning"),
  attacks=[("Bite", "m", "3d8", "Piercing", "", "10 ft."), ("Tail Coil", "m", "2d8", "Bludgeoning", "and the target is Grappled (escape {dc:str})", "15 ft.")], multi=2),

# ================= ABERRATIONS =================
M("Eye of the Hollow Moon", "L", "Aberration", "Lawful Evil", 10, "10 14 18 19 15 17", ac=17, speed="0 ft., fly 20 ft. (hover)", senses="Darkvision 120 ft.", skills="Perception*", saves="Int, Wis", res=R(Immunities="Prone"), lang="Deep Speech, telepathy 120 ft.",
  attacks=[("Gaze Ray", "s:int", "4d10", "Psychic", "", "120 ft.")], multi=2,
  actions=[("Pale Stare (Recharge 5–6)", "Each creature in a 60-foot Cone makes a {dc:int} Wisdom save or has the Paralyzed condition for 1 minute (save ends at end of each turn).")],
  traits=[("Silent Mind", "The eye can't be targeted by divination magic.")],
  desc="A floating eye the size of a carriage, ringed by drifting moon-white motes."),
M("Tunnel Mouth", "H", "Aberration", "Neutral Evil", 8, "22 6 20 3 10 3", ac=15, speed="10 ft., burrow 40 ft.", senses="Tremorsense 120 ft.", res=R(Immunities="Blinded, Deafened"),
  attacks=[("Maw", "m", "4d10", "Piercing", "and a Large or smaller target is swallowed on a hit: it is Blinded and Restrained and takes {4d8} Acid damage at the start of each of the mouth's turns", "10 ft.")],
  traits=[("False Appearance", "While motionless, the mouth looks like a cave entrance.")]),
M("Whispering Brain", "S", "Aberration", "Chaotic Evil", 3, "4 12 12 18 14 15", ac=12, speed="10 ft., fly 30 ft. (hover)", senses="Blindsight 60 ft.", res=R(Immunities="Psychic"), lang="telepathy 120 ft.",
  attacks=[("Mind Lash", "s:int", "3d6", "Psychic", "", "60 ft.")],
  actions=[("Implant Thought", "A creature within 120 feet makes a {dc:int} Wisdom save or has the Charmed condition for 1 hour, believing a single false idea the brain chooses.")]),
M("Star Spawn Drifter", "M", "Aberration", "Chaotic Evil", 5, "14 16 15 14 12 10", ac=15, speed="30 ft., fly 30 ft. (hover)", senses="Darkvision 120 ft.", res=R(Resistances="Cold, Psychic"), lang="Deep Speech",
  attacks=[("Starlit Claw", "f", "2d8", "Slashing", "plus {2d6} Cold damage")], multi=2,
  traits=[("Wrong Geometry", "Opportunity Attacks against the drifter have Disadvantage.")]),
M("Flesh Weaver", "L", "Aberration", "Neutral Evil", 12, "16 14 20 20 16 18", ac=17, saves="Con, Int, Wis", senses="Truesight 60 ft.", res=R(Resistances="Psychic, Necrotic"), lang="Deep Speech, Common, telepathy 120 ft.",
  attacks=[("Tendril", "m", "3d8", "Bludgeoning", "and the target makes a {dc:con} Constitution save or its Hit Point maximum is reduced by {2d8}", "15 ft.")], multi=3,
  actions=[("Reshape (Recharge 5–6)", "One creature within 60 feet makes a {dc:int} Constitution save or is Petrified into living clay until the end of its next turn and takes {6d10} Psychic damage.")]),
M("Abyssal Lamprey", "L", "Aberration", "Unaligned", 2, "16 14 15 2 10 4", ac=13, speed="0 ft., swim 50 ft.", senses="Blindsight 60 ft.",
  attacks=[("Sucker Bite", "m", "2d6", "Piercing", "and the lamprey attaches; while attached it drains {2d6} Hit Points at the start of each of its turns")]),

# ================= CONSTRUCTS =================
M("Clockwork Sentry", "M", "Construct", "Lawful Neutral", 2, "15 12 15 3 12 1", ac=17, senses="Darkvision 60 ft.", res=CON, lang="understands Common",
  attacks=[("Halberd", "m", "1d10", "Slashing", "", "10 ft.")], multi=2,
  traits=[("Alarm Bell", "When the sentry sees an intruder, it rings a bell audible for 300 feet.")]),
M("Brass Hound", "M", "Construct", "Unaligned", 1, "14 14 14 3 12 1", ac=15, speed="40 ft.", senses="Darkvision 60 ft.", skills="Perception", res=CON,
  attacks=[("Bite", "m", "1d8", "Piercing", "plus {1d6} Fire damage")]),
M("Stone Warden", "L", "Construct", "Unaligned", 6, "20 8 20 3 11 1", ac=17, speed="25 ft.", senses="Darkvision 60 ft.", res=R(Resistances="Bludgeoning, Piercing, Slashing from nonmagical attacks") + "; " + CON,
  attacks=[("Stone Fist", "m", "2d10", "Bludgeoning", "", "10 ft.")], multi=2,
  traits=[("Immutable Form", "The warden is immune to effects that would alter its form."), ("Guardian's Bond", "The warden knows the location of its creator's chosen ward and always moves to protect it.")]),
M("Iron Colossus", "G", "Construct", "Unaligned", 20, "28 6 26 3 12 1", ac=22, speed="40 ft.", senses="Darkvision 120 ft.", res=R(Immunities="Fire, Poison, Psychic; Bludgeoning, Piercing, Slashing from nonmagical attacks; Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned"),
  attacks=[("Fist", "m", "4d12", "Bludgeoning", "", "20 ft.")], multi=3,
  traits=[("Siege Monster", "The colossus deals double damage to objects and structures."), ("Magic Resistance", "The colossus has Advantage on saves against spells.")],
  actions=[("Furnace Breath (Recharge 5–6)", "A 90-foot Cone: each creature makes a {dc:con} Dexterity save, taking {16d10} Fire damage on a failure, half on a success.")]),
M("Paper Golem", "M", "Construct", "Unaligned", 1, "10 16 10 3 10 1", ac=13, speed="30 ft., fly 30 ft.", res=R(Vulnerabilities="Fire") + "; " + CON,
  attacks=[("Paper Cut", "f", "1d8", "Slashing")], multi=2,
  traits=[("Flatten", "The golem can slip through any gap at least 1/8 inch wide.")]),
M("Clockwork Spider", "S", "Construct", "Unaligned", 0.5, "8 16 12 3 10 1", ac=14, speed="30 ft., climb 30 ft.", senses="Darkvision 60 ft.", res=CON,
  attacks=[("Needle", "f", "1d6", "Piercing", "plus {1d6} Poison damage")]),
M("Forge Titan", "H", "Construct", "Lawful Neutral", 14, "25 8 22 10 14 8", ac=20, speed="30 ft.", senses="Darkvision 120 ft.", res=R(Immunities="Fire, Poison, Psychic; Charmed, Exhaustion, Frightened, Paralyzed, Poisoned"), lang="understands Dwarvish",
  attacks=[("Hammer Arm", "m", "4d10", "Bludgeoning", "plus {2d10} Fire damage", "15 ft.")], multi=2,
  actions=[("Slag Pour (Recharge 5–6)", "A 20-foot-radius area within 60 feet: each creature makes a {dc:con} Dexterity save, taking {12d10} Fire damage and having its Speed halved for 1 minute on a failure, half damage only on a success.")]),

# ================= GIANTS =================
M("Hill Ogre Brute", "L", "Giant", "Chaotic Evil", 3, "20 8 18 5 8 6", ac=12, speed="40 ft.", lang="Giant",
  attacks=[("Tree Club", "m", "3d8", "Bludgeoning", "", "10 ft.")]),
M("Fog Giant", "H", "Giant", "Neutral", 8, "22 12 20 12 15 10", ac=15, senses="Blindsight 30 ft.", skills="Stealth", lang="Giant, Common",
  attacks=[("Mist Spear", "m", "3d8", "Piercing", "", "15 ft.")], multi=2,
  traits=[("Fog Shroud", "The giant is always surrounded by fog in a 20-foot radius that Heavily Obscures the area for creatures other than it.")]),
M("Bridge Troll", "L", "Giant", "Chaotic Evil", 5, "19 13 20 7 9 7", ac=15, senses="Darkvision 60 ft.", lang="Giant",
  attacks=[("Claw", "m", "2d6", "Slashing"), ("Bite", "m", "1d10", "Piercing")], multi=3,
  traits=[("Regeneration", "The troll regains 10 Hit Points at the start of each of its turns unless it took Acid or Fire damage since its last turn. It dies only if it starts its turn with 0 Hit Points and doesn't regenerate."),
          ("Toll Keeper", "The troll knows if anyone crosses its bridge without paying.")]),
M("Mountain King", "H", "Giant", "Lawful Neutral", 16, "27 10 24 14 18 18", ac=20, saves="Str, Con, Wis", skills="Athletics, Perception", lang="Giant, Common, Terran",
  traits=[("Legendary Resistance (2/Day)", "If the king fails a saving throw, it can choose to succeed instead.")],
  attacks=[("Granite Maul", "m", "4d12", "Bludgeoning", "and the target makes a {dc:str} Strength save or has the Prone condition", "15 ft."), ("Hurl Boulder", "r", "6d10", "Bludgeoning", "", "120/480 ft.")], multi=2,
  actions=[("Earthquake Stomp (Recharge 5–6)", "Each creature within 30 feet makes a {dc:str} Dexterity save, taking {8d10} Bludgeoning damage and falling Prone on a failure, half damage only on a success.")],
  leg=[("Maul", "The king makes one Granite Maul attack."), ("Shake the Ground", "Each creature within 10 feet falls Prone unless it succeeds on a {dc:str} Dexterity save.")]),
M("Ice Ogre", "L", "Giant", "Chaotic Evil", 4, "19 8 18 6 9 7", ac=14, res=R(Immunities="Cold"), lang="Giant",
  attacks=[("Frozen Club", "m", "2d10", "Bludgeoning", "plus {1d8} Cold damage", "10 ft.")], multi=2),

# ================= MONSTROSITIES =================
M("Lantern Crab", "H", "Monstrosity", "Unaligned", 5, "20 10 18 2 12 4", ac=17, speed="30 ft., swim 30 ft.", senses="Darkvision 60 ft.",
  attacks=[("Claw", "m", "2d10", "Bludgeoning", "and the target is Grappled (escape {dc:str})", "10 ft.")], multi=2,
  traits=[("Lure Light", "A glowing stalk sheds Dim Light 30 feet; creatures that see it make a {dc:wis} Wisdom save or are Charmed and must move toward it.")]),
M("Hookhorror Moth", "L", "Monstrosity", "Unaligned", 3, "14 16 13 3 12 6", ac=14, speed="10 ft., fly 60 ft.", senses="Darkvision 60 ft.",
  attacks=[("Hooked Legs", "f", "2d6", "Piercing")], multi=2,
  actions=[("Hypnotic Wings (Recharge 5–6)", "Each creature within 30 feet that can see the moth makes a {dc:con} Wisdom save or has the Incapacitated condition until the end of its next turn.")]),
M("Chimera of the Three Winds", "L", "Monstrosity", "Chaotic Evil", 7, "19 13 18 4 14 9", ac=15, speed="30 ft., fly 60 ft.", senses="Darkvision 60 ft.", skills="Perception",
  attacks=[("Lion Bite", "m", "2d8", "Piercing"), ("Ram Horns", "m", "1d12", "Bludgeoning"), ("Serpent Fangs", "m", "1d8", "Piercing", "plus {2d6} Poison damage")], multi=3,
  actions=[("Three Winds (Recharge 5–6)", "A 30-foot Cone of hot, cold and stormy wind: each creature makes a {dc:con} Dexterity save, taking {2d8} Fire, {2d8} Cold and {2d8} Lightning damage on a failure, half on a success.")]),
M("Glass Basilisk", "M", "Monstrosity", "Unaligned", 4, "16 8 15 2 8 7", ac=15, speed="20 ft.", senses="Darkvision 60 ft.",
  attacks=[("Bite", "m", "2d8", "Piercing", "plus {2d6} Slashing damage from glass shards")],
  traits=[("Crystallizing Gaze", "A creature that starts its turn within 30 feet and can see the basilisk makes a {dc:con} Constitution save. On a failure it is Restrained as its skin turns to glass; on a second failure it is Petrified for 24 hours.")]),
M("Rust Stalker", "M", "Monstrosity", "Unaligned", 2, "13 14 13 2 13 6", ac=14, speed="40 ft.", senses="Darkvision 60 ft.",
  attacks=[("Bite", "m", "1d8", "Piercing")],
  traits=[("Iron Scent", "The stalker can smell ferrous metal within 30 feet.")],
  actions=[("Corroding Antennae", "One nonmagical metal weapon or armor within 5 feet takes a permanent −1 penalty (armor to AC, weapons to damage). Items reduced to −5 are destroyed.")]),
M("Bog Hydra", "H", "Monstrosity", "Unaligned", 9, "20 12 20 2 10 7", ac=15, speed="30 ft., swim 30 ft.", senses="Darkvision 60 ft.",
  attacks=[("Bite", "m", "1d10", "Piercing", "plus {1d10} Poison damage", "10 ft.")], multi=5,
  traits=[("Many Heads", "When the hydra takes 25 damage on one turn, a head dies; at the end of its turn it grows two heads for each head that died unless it took Fire damage. Each head grants one Bite in its Multiattack (start: 5).")]),
M("Sandshark", "L", "Monstrosity", "Unaligned", 5, "19 13 17 2 12 4", ac=14, speed="10 ft., burrow 50 ft.", senses="Tremorsense 60 ft.",
  attacks=[("Bite", "m", "3d8", "Piercing")], multi=2,
  traits=[("Sand Dive", "The sandshark can move through sand as if swimming; if it emerges and hits on the same turn, the target is knocked Prone.")]),
M("Thornback Manticore", "L", "Monstrosity", "Lawful Evil", 4, "17 15 16 8 12 9", ac=14, speed="30 ft., fly 50 ft.", senses="Darkvision 60 ft.", lang="Common",
  attacks=[("Claw", "m", "1d8", "Slashing"), ("Tail Thorn", "r", "1d10", "Piercing", "", "100/200 ft.")], multi=3),
M("Gloom Stalker Cat", "L", "Monstrosity", "Unaligned", 3, "16 17 14 3 13 6", ac=14, speed="40 ft., climb 30 ft.", senses="Darkvision 120 ft.", skills="Stealth*",
  attacks=[("Claw", "m", "1d10", "Slashing")], multi=2,
  traits=[("Shadow Blend", "While in Dim Light or darkness, the cat has the Invisible condition until it attacks.")]),
M("Abyssal Kraken Spawn", "H", "Monstrosity", "Chaotic Evil", 11, "22 10 20 12 14 10", ac=16, speed="10 ft., swim 60 ft.", senses="Darkvision 120 ft.", lang="understands Abyssal",
  attacks=[("Tentacle", "m", "3d8", "Bludgeoning", "and the target is Grappled (escape {dc:str})", "20 ft.")], multi=3,
  actions=[("Ink Cloud (Recharge 5–6)", "A 30-foot sphere of ink around the spawn is Heavily Obscured; creatures in it take {6d6} Poison damage ({dc:con} Constitution save for half).")]),
M("Roc of the Ember Peaks", "G", "Monstrosity", "Unaligned", 12, "27 10 22 3 12 9", ac=16, speed="20 ft., fly 120 ft.", skills="Perception",
  attacks=[("Beak", "m", "4d8", "Piercing", "", "10 ft."), ("Talons", "m", "4d6", "Slashing", "and the target is Grappled (escape {dc:str})")], multi=2,
  res=R(Resistances="Fire")),
M("Wyvern of the Salt Coast", "L", "Monstrosity", "Unaligned", 6, "19 10 16 5 12 6", ac=13, speed="20 ft., fly 80 ft.", senses="Darkvision 60 ft.",
  attacks=[("Bite", "m", "2d6", "Piercing", "", "10 ft."), ("Stinger", "m", "2d6", "Piercing", "plus {5d6} Poison damage ({dc:con} Constitution save for half)", "10 ft.")], multi=2),
M("Owlbear Matriarch", "L", "Monstrosity", "Unaligned", 5, "21 12 19 3 13 7", ac=14, speed="40 ft.", senses="Darkvision 60 ft.", skills="Perception",
  attacks=[("Rend", "m", "2d8", "Slashing")], multi=3,
  traits=[("Protective Fury", "While a young owlbear is within 30 feet, the matriarch has Advantage on attack rolls.")]),
]
