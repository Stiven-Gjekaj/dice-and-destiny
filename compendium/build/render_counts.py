"""Write the counts of the original content into the part pages of the books.

The part pages of both books name how many original entries each book has.
The counts come from the content, so they are correct after each batch.
"""


def gm_counts(monsters, npcs, items):
    """The counts for Part IV of the GM's book."""
    return (f"{len(monsters)} new monsters and {len(npcs)} people with full stat blocks, "
            f"{len(items)} new magic items, and a stronghold system")


def player_counts(classes, subs):
    """The counts for the Expanded Options part of the Player's book. `subs` is a dict of lists, as SUBS is."""
    n_subs = sum(len(v) for v in subs.values())
    return f"{len(classes)} new classes, {n_subs} new subclasses"


def all_gm_counts():
    from content.items import ITEMS
    from content.monsters import MON
    from content.npcs import NPCS
    return gm_counts(MON, NPCS, ITEMS)


def all_player_counts():
    from content.classes import CLASSES
    from content.subclasses import SUBS
    return player_counts(CLASSES, SUBS)


def origin_counts(backgrounds, species):
    """The counts for the intro of the backgrounds and species chapter."""
    return f"{len(backgrounds)} new backgrounds and {len(species)} new species"


def spell_counts(spells):
    """The count for the intro of the spells chapter."""
    return f"{len(spells)} new spells"


def all_origin_counts():
    from content.backgrounds import BACKGROUNDS
    from content.species import SPECIES
    return origin_counts(BACKGROUNDS, SPECIES)


def all_spell_counts():
    from content.spells import SPELLS
    return spell_counts(SPELLS)
