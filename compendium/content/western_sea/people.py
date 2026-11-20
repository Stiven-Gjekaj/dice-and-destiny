"""The people of Beyond the Western Sea.

A person who fights is a pair (role, M(...)). A person with no statblock is a pair (role, "Name").
The role is one free line of text.
Keep the armor class at 16 or less and each save DC at 15 or less.
The world bible has a row for each person, in the section "The people of Beyond the Western Sea".
"""
from monster_engine import M

NPCS = [
# ================= THE PEOPLE WITH STATBLOCKS =================
("The Captain of the Light, the leader of the Corrin men. He wants to light the Corrin Light and sail home.",
 M("Absalom Pascoe", "M", "Humanoid", "Lawful Neutral", 2, "15 12 14 11 13 14", ac=14, saves="Str, Con",
   skills="Athletics, Intimidation, Perception", lang="Common",
   traits=[("Keeper of the Light", "Each Corrin man within 30 feet of Absalom that can see him has Advantage on saving throws against the Frightened condition.")],
   attacks=[("Cutlass", "m", "1d8", "Slashing"), ("Boarding Axe", "t", "1d6", "Slashing")], multi=2,
   react=[("Parry", "Absalom adds 2 to his AC against one melee attack roll that would hit him. He must see the attacker and hold a weapon.")],
   desc="A square, grey man of sixty in a blue coat that was his grandfather's. He carries the old Pascoe cutlass, "
        "and he means every word he says. He has never seen home, and he has never doubted it.")),
("A young Corrin man, the leader of the young men who want to light the Corrin Light now, with or without the Moot.",
 M("Kit Hocking", "M", "Humanoid", "Chaotic Neutral", 1, "14 14 12 10 10 13", ac=13, skills="Athletics, Persuasion", lang="Common",
   traits=[("Hot Blood", "On the first round of a fight, Kit has Advantage on attack rolls, and attack rolls against him have Advantage.")],
   attacks=[("Boat Hook", "m", "1d8", "Piercing", "", "10 ft"), ("Lit Torch", "t", "1d6", "Fire")], multi=2,
   bonus=[("Rally", "Kit shouts. Each ally within 30 feet of him that can hear him can move up to 10 feet without provoking Opportunity Attacks.")],
   desc="A tall, loud young man of twenty with salt in his red hair and a torch never far from his hand. He has heard about home all his life, "
        "and he is tired of waiting for old men to go there.")),
("The leader of the Well Watch, the Tey men who keep people away from the Corrin Light. He will kill to keep the Light dark.",
 M("Erlend Linklater", "M", "Humanoid", "Lawful Neutral", 2, "16 12 15 10 13 11", ac=13, saves="Str, Wis",
   skills="Perception, Stealth, Survival", lang="Common",
   traits=[("No Light at Night", "The Well Watch carries no fire after dark. Erlend has Advantage on Wisdom (Perception) checks and Dexterity (Stealth) checks in Dim Light.")],
   attacks=[("Seal Spear", "m", "1d8", "Piercing"),
            ("Harpoon", "t", "1d10", "Piercing", "and the target makes a {dc:str} Strength saving throw. On a failed save, Erlend pulls the target up to 10 feet toward him.")],
   multi=2,
   bonus=[("Smother", "Erlend puts out one nonmagical flame within 5 feet of him with his cloak or his hand.")],
   desc="A dark, quiet man of forty in sealskin, with a scar where his ear was. His family has kept the Watch since the Drowning. "
        "He does not hate the Corrin men. He thinks that they will drown his children, and he is ready to stop them.")),
("A fisherman of the Tey bank, the best guide on Farholm, and the husband of Hester Spence.",
 M("Thomas Spence", "M", "Humanoid", "Neutral Good", 0.5, "12 14 12 10 14 11", ac=13, skills="Nature, Perception, Survival", lang="Common",
   traits=[("Islander", "Thomas ignores the Difficult Terrain of Farholm, and he has Advantage on Wisdom (Survival) checks to find his way on the island.")],
   attacks=[("Gutting Knife", "f", "1d4", "Slashing"), ("Sling", "r", "1d4", "Bludgeoning", "", "30/120 ft")],
   desc="A slow, kind man with big hands and few words. He knows each path, pool, and gull cliff of the island, and he will take the party anywhere "
        "that is not the Corrin Light.")),

# ================= THE PEOPLE WITH NO STATBLOCK =================
("The schoolmaster of Hythe and the keeper of the Landing Book, the records of the colony. The last of the Gales. He knows how the lamp of the Light works.",
 "Nathaniel Gale"),
("The shipwright of the Corrin bank. She builds a boat in secret, for the day when the Light burns again.", "Margery Nance"),
("The Well Keeper, the leader of the Tey folk. She keeps the dawn hymn of Saint Mawes and fears that the Grandam will wake.", "Elspeth Flett"),
("A girl of fourteen on the Tey bank who dreams the dreams of the Grandam. The Tey folk think that she is holy.", "Inga Halcrow"),
("The daughter of Absalom Pascoe, married across the Bridge to Thomas Spence. Neither side fully trusts her.", "Hester Spence"),
("The priest of the Morning Flame on Founders' Hill. He keeps the peace at the Moot of Hythe and the legend of the saint.", "Father Gilbert Rundle"),
("An old salt boiler at the Saltpans who lives apart from both sides. The first colonist that the party meets.", "Amos Tulloch"),
]
