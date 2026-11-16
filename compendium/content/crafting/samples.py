"""The first materials and recipes of the crafting system."""

MATERIALS = [
    dict(name="Moonpetal", source="Biome", origin="Forest", rarity="Common", check="Intelligence (Nature)",
         text="A pale flower that opens only under the full moon. Its sap makes a potion cling and climb."),
    dict(name="Spinner's Gland", source="Monster", origin="Giant Spider", rarity="Common", check="Wisdom (Survival)",
         text="The silk gland of a giant spider, still sticky. Alchemists use it in anything that has to grip."),
    dict(name="Frost Salt", source="Biome", origin="Arctic", rarity="Uncommon", check="Intelligence (Nature)",
         text="Blue crystals that form where the ice never melts. They keep their cold for a year in a sealed jar."),
    dict(name="Kelp Heart", source="Biome", origin="Coast or Underwater", rarity="Uncommon", check="Wisdom (Survival)",
         text="The thick root bulb of a giant kelp, full of air. It must be cut from a living plant in deep water."),
    dict(name="Winter Wolf Pelt", source="Monster", origin="Winter Wolf", rarity="Uncommon", check="Wisdom (Survival)",
         text="A white pelt that is always cold to the touch. A cobbler who knows the trade can sew its chill into boots."),
    dict(name="Young Dragon Scale", source="Monster", origin="any Dragon of CR 7 to 12", rarity="Rare", check="Wisdom (Survival)",
         text="A scale the size of a hand, from a young dragon. It keeps the dragon's resistance to its own breath."),
]

RECIPES = [
    dict(item="Potion of Climbing", rarity="Common", consumable=True, tool="Alchemist's Supplies",
         materials=["Moonpetal", "Spinner's Gland"], gold=5, days=3, note=""),
    dict(item="Potion of Resistance", rarity="Uncommon", consumable=True, tool="Alchemist's Supplies",
         materials=["Frost Salt"], gold=50, days=5,
         note="With Frost Salt, the potion gives Resistance to Cold damage. Another Uncommon material of an element gives that element instead."),
    dict(item="Potion of Water Breathing", rarity="Uncommon", consumable=True, tool="Alchemist's Supplies",
         materials=["Kelp Heart"], gold=50, days=5, note=""),
    dict(item="Boots of the Winterlands", rarity="Uncommon", consumable=False, tool="Leatherworker's Tools",
         materials=["Winter Wolf Pelt"], gold=150, days=10, note=""),
    dict(item="Armor of Resistance", rarity="Rare", consumable=False, tool="Smith's Tools or Leatherworker's Tools",
         materials=["Young Dragon Scale"], gold=1500, days=50,
         note="The crafter also needs the base armor. The armor resists the damage type of the dragon's breath."),
]
