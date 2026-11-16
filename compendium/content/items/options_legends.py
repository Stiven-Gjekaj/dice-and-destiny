# Original magic items for the Legend paths (optional rules). Anyone can use them.
# A character who walks the named path gets a small extra benefit.
# Format: (name, category, rarity, attunement, text)
A = "Requires Attunement"
ITEMS = [
# ---------- Dragonslayer
("Scale-Tooth Charm", "Wondrous Item", "Uncommon", None,
 "This charm is made from a dragon's tooth. While you carry it, you have Advantage on saving throws against the Frightened condition caused by Dragons. A creature on the Dragonslayer path also knows when a Dragon is within 1 mile of it."),
("Wyrmbane Spear", "Weapon (Spear)", "Rare", A,
 "You have a +2 bonus to attack and damage rolls made with this magic weapon. When you hit a Dragon with it, the Dragon takes an extra 2d10 damage of the weapon's type. A creature on the Dragonslayer path can throw the spear at a flying Dragon up to 120 feet away, and the spear returns to its hand after the attack."),
# ---------- Saint
("Pilgrim's Candle", "Wondrous Item", "Common", None,
 "This white candle burns for 1 hour each night for a year without shrinking. Undead can't willingly come within 5 feet of its flame. A creature on the Saint path who prays by its light regains one expended Hit Point Die."),
("Halo of the Humble", "Wondrous Item", "Rare", A,
 "This thin gold circlet glows faintly. Once per Long Rest, as a Bonus Action, you can restore Hit Points equal to 2d8 plus your Wisdom modifier to a creature you touch. A creature on the Saint path can use this property twice per Long Rest."),
# ---------- Tyrant
("Iron Crown of Obedience", "Wondrous Item", "Rare", A,
 "While you wear this heavy crown, you have Advantage on Charisma (Intimidation) checks, and once per Long Rest, you can cast Command from it (save DC 15). A creature on the Tyrant path can cast it at its highest normal level, targeting up to three creatures. The crown is cold and uncomfortable, and it whispers that others should kneel."),
("Chain of Fealty", "Wondrous Item", "Very Rare", A,
 "When a creature kneels before you and swears loyalty while you hold this golden chain, you know the creature's direction and distance for 30 days, and it has Disadvantage on saving throws against your Charmed and Frightened effects. You can have up to three such vassals at a time. A creature that is forced to swear the oath can make a Wisdom saving throw (DC 15) to resist. Talk with your table before you use this item."),
# ---------- Wanderer
("Road-Worn Boots", "Wondrous Item", "Uncommon", None,
 "While you wear these boots, you can travel for 10 hours a day without risking Exhaustion from a forced march, and rough roads don't slow your travel pace. A creature on the Wanderer path also never gets blisters, and its feet are always dry."),
("Map of Every Road", "Wondrous Item", "Very Rare", None,
 "This map is blank until you speak the name of a place you want to reach on the same plane. Then it draws the safest route there from where you stand, and it updates the route each dawn. Once per 7 days, a creature on the Wanderer path can step onto the map and cast Teleport from it, arriving at the place the map shows."),
# ---------- Spellbreaker
("Nullstone Amulet", "Wondrous Item", "Uncommon", A,
 "While you wear this gray amulet, you have Advantage on saving throws against spells of level 2 or lower. A creature on the Spellbreaker path can also see the faint aura of any spell that is active on a creature within 30 feet of it."),
("Gauntlet of Unweaving", "Wondrous Item", "Very Rare", A,
 "While you wear this iron gauntlet, you can take a Reaction when a creature you can see within 60 feet of you casts a spell, to cast Counterspell from the gauntlet (using Constitution as your spellcasting ability). Once used, this property can't be used again until the next dawn. A creature on the Spellbreaker path has Advantage on the ability check that Counterspell needs."),
# ---------- Liberator
("Broken Shackle", "Wondrous Item", "Uncommon", None,
 "This broken iron shackle is worn on a cord. While you carry it, you have Advantage on checks to escape a grapple or bonds. As a Magic action, you can touch a lock, a chain, or a manacle and cast Knock on it from the shackle. Once used this way, it can't be used again until the next dawn. A creature on the Liberator path can use it this way twice per day."),
("Banner of the Free", "Wondrous Item", "Very Rare", A,
 "As a Bonus Action, you can unfurl this banner. For 1 minute, you and each ally within 30 feet of you can't be Charmed or Frightened, and each such ally that is Grappled or Restrained can end the condition on itself at the start of its turn. Once used, the banner can't be used again until the next dawn. A creature on the Liberator path can unfurl it for 10 minutes instead."),
# ---------- Lorekeeper
("Quill of Remembering", "Wondrous Item", "Common", None,
 "This quill writes down anything you say aloud while you hold it, in your own hand, on any surface you touch with it. A creature on the Lorekeeper path can also recall anything it wrote with the quill, word for word."),
("Atlas of Forgotten Kingdoms", "Wondrous Item", "Rare", None,
 "When you open this heavy book and name a ruin, a lost city, or a fallen kingdom, the book shows its old maps and tells its history in a few pages, as far as anyone ever wrote it down. Once per Long Rest, a creature on the Lorekeeper path can cast Legend Lore from it without material components."),
# ---------- Warden of the Wild
("Acorn of the Old Grove", "Wondrous Item", "Common", None,
 "While you carry this acorn, Beasts that aren't hungry or magically compelled don't attack you unless you attack them first. A creature on the Warden of the Wild path can plant the acorn to grow a small oak in one night; the acorn returns to its pocket at dawn."),
("Antler Crown of the Warden", "Wondrous Item", "Very Rare", A,
 "While you wear this crown of antlers, you can cast Speak with Animals and Speak with Plants at will. Once per Long Rest, you can cast Commune with Nature from it. A creature on the Warden of the Wild path can also cast Tree Stride from it once per Long Rest."),
# ---------- Shadow
("Smoke Pellets of the Quiet Way", "Wondrous Item", "Uncommon", None,
 "This pouch holds 5 pellets. As a Bonus Action, you can throw one at a point within 30 feet, where it bursts into a 10-foot-radius Sphere of thick smoke that is Heavily Obscured for 1 minute. The pouch regains 1d4 pellets at dawn. A creature on the Shadow path can take the Hide action as part of the same Bonus Action."),
("Mask Without a Face", "Wondrous Item", "Rare", A,
 "While you wear this smooth black mask, creatures can't remember your face once they stop seeing you, and divination magic that would show your face shows only darkness. A creature on the Shadow path can also cast Pass without Trace from the mask once per Long Rest."),
# ---------- Peacemaker
("White Ribbon of Parley", "Wondrous Item", "Common", None,
 "When you raise this white ribbon, any creature that sees it and understands what it means knows that you want to talk, not fight. A creature on the Peacemaker path also has Advantage on the first Charisma check it makes to start a parley."),
("Olive Staff of Calm", "Staff", "Rare", A,
 "This staff has 5 charges and regains 1d4 + 1 charges at dawn. While you hold it, you can expend 1 charge to cast Calm Emotions or 2 charges to cast Sanctuary at its highest normal level (save DC 15). A creature on the Peacemaker path can cast Calm Emotions from it without expending a charge once per Long Rest."),
# ---------- Deathless
("Sand of the Last Breath", "Wondrous Item", "Rare", A,
 "This small glass vial of gray sand has 1 charge and regains it at dawn. When you fail a Death Saving Throw, you can expend the charge to succeed instead. A creature on the Deathless path can scatter a pinch of the sand to stop its own aging for one day."),
("Phylactery of the Unbowed", "Wondrous Item", "Legendary", A,
 "While you wear this sealed silver locket, you have Resistance to Necrotic damage, and your Hit Point maximum can't be reduced. Once per 7 days, when you die, the locket breaks open and you return to life at the next dawn with 1 Hit Point, in the place where you died; the locket then mends. It doesn't work in the same turn as a Deathless benefit or any other effect that stops a death: each death can be stopped only once. A creature on the Deathless path returns at the next sunset instead."),
# ---------- Founder
("Cornerstone of the First Hall", "Wondrous Item", "Rare", None,
 "When you lay this carved stone in the foundation of a building, the building is finished in half the normal time, and its walls can't be damaged by nonmagical weather. A creature on the Founder path also knows when anyone enters the building, wherever it is on the same plane."),
("Charter of the Free Town", "Wondrous Item", "Very Rare", A,
 "This sealed parchment grants a settlement to the one who holds it. While you are attuned to it and you are in a settlement that you founded or that you lead, you and your allies have Advantage on Charisma checks with its people, and once per Long Rest you can cast Guards and Wards from it on one building there. A creature on the Founder path can name up to six loyal folk of the settlement as its stewards; they know at once when the town is in danger."),
]
