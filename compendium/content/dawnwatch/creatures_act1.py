"""The new creatures of Act I of The Dawnwatch, Book One (chapters 2 to 5).

The Hush has three tiers: the Snuffer, the Shroud, and the Lightless.
The Long Shadow is the creature at the end of Act I, in chapter 4.
The people of the Hush with names (Mother Sallow and Osk) are in people_act1.py.
"""
from monster_engine import M

R = lambda **k: "; ".join(f"<b>{a}</b> {b}" for a, b in k.items())

HUSH_SIGN = ("Hush Sign", "The Hush speak little. Its members talk to each other with signs of the hand, "
             "and a creature that knows the signs can read them across a dark room.")

MON = [
M("Hush Snuffer", "M", "Humanoid", "Lawful Evil", 0.5, "10 14 12 10 12 11", ac=13, skills="Stealth", lang="Common, Hush Sign",
  traits=[HUSH_SIGN,
          ("Grey Step", "The snuffer has Advantage on Dexterity (Stealth) checks while it is in Dim Light or Darkness.")],
  attacks=[("Hooked Snuffer", "f", "1d6", "Bludgeoning", "plus {1d4} Cold damage if the target is in Dim Light or Darkness")],
  bonus=[("Snuff", "The snuffer puts out one nonmagical flame that it can see within 30 feet of it, such as a candle, a torch, or a lantern.")],
  desc="A member of the Hush in a grey cloak, with a brass snuffer on a long pole. It walks into a lit room, and the room goes dark one candle at a time."),
M("Hush Shroud", "M", "Humanoid", "Lawful Evil", 2, "10 12 14 12 15 13", ac=13, skills="Religion, Stealth", lang="Common, Hush Sign",
  senses="Darkvision 60 ft.",
  traits=[HUSH_SIGN,
          ("Eyes of the Unlit", "Magical Darkness doesn't stop the shroud's Darkvision.")],
  attacks=[("Grey Touch", "s:wis", "2d6", "Cold", "", "60 ft.")], multi=2,
  actions=[("Shush (Recharge 5–6)", "One creature that the shroud can see within 30 feet of it makes a {dc:wis} Wisdom saving throw. "
            "On a failed save, the creature can't speak until the end of its next turn, so it can't cast a spell with a Verbal component."),
           ("Spellcasting", "The shroud casts one of the following spells, using Wisdom as the spellcasting ability ({dc:wis}). "
            "1/Day each: Darkness, Silence.")],
  desc="A priest of the Hush, with a grey veil over a face that never smiles. It prays in silence, and its prayers make the air cold."),
M("Hush Lightless", "M", "Humanoid", "Lawful Evil", 4, "16 12 16 10 12 10", ac=16, saves="Con", skills="Athletics, Perception", lang="Common, Hush Sign",
  senses="Darkvision 120 ft.",
  traits=[HUSH_SIGN,
          ("Eyes of the Unlit", "Magical Darkness doesn't stop the lightless's Darkvision."),
          ("Strength of the Dark", "While the lightless is in Dim Light or Darkness, its weapon attacks deal an extra {1d6} Necrotic damage.")],
  attacks=[("Grey Mace", "m", "1d8", "Bludgeoning")], multi=2,
  bonus=[("Gloom (Recharge 5–6)", "The lightless chooses a point within 60 feet of it. Magical Darkness fills a 10-foot-radius Sphere centered on that point "
          "for 1 minute, or until the lightless dies. Nonmagical light can't light the area.")],
  desc="A warrior of the Hush who drank the black water at the cult's secret rite. Its skin is the color of ash, and its eyes have no white in them."),
M("The Long Shadow", "L", "Undead", "Neutral Evil", 5, "8 16 16 10 14 16", ac=14, speed="40 ft., climb 40 ft.",
  senses="Darkvision 120 ft.", lang="understands Common but speaks only with the voice of the Unlit King",
  res=R(Vulnerabilities="Radiant", Resistances="Cold, Necrotic",
        Immunities="Poison; Charmed, Exhaustion, Frightened, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained"),
  traits=[("Mantle of the Dark", "While the shadow is in Dim Light or Darkness, it has Resistance to Bludgeoning, Piercing, and Slashing damage."),
          ("Hates the Light", "While the shadow is in Bright Light, it has Disadvantage on attack rolls."),
          ("Tied to the Stone", "The shadow can't move more than 120 feet from the black stone that called it. "
           "If that stone is in the light of a piece of the Dawnfire, or if the shadow drops to 0 Hit Points, it fades into the floor and is gone.")],
  attacks=[("Cold Hand", "f", "2d8", "Necrotic")], multi=2,
  actions=[("The King's Voice (Recharge 5–6)", "The shadow speaks with the voice of the Unlit King. Each creature of its choice within 30 feet of it that can hear it "
            "makes a {dc:cha} Wisdom saving throw. On a failed save, a creature takes {3d8} Psychic damage and has the Frightened condition until the end of its next turn. "
            "On a successful save, it takes half as much damage only.")],
  desc="A shadow as tall as a door, in the shape of a knight with a crown of black fire. It is the shadow of something that sleeps far away, and it moves a moment late, like a shadow should."),
]
