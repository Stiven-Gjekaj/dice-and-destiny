# Review request: player options, spells batch 2

Backgrounds batch 2 is on main (37b223c, docs 11a75eb). Backgrounds: 40 of
40. Species: 20 of 20.

## The batch

- Files: `compendium/content/spells/class_gaps_2.py` (11 spells) and
  `compendium/content/spells/class_gaps_3.py` (25 spells). Not committed.
- Entries: 36 spells (fewer than 40, so it is one batch). Spells: 58 to 94
  of 220.
- Build: `compendium/build.sh` passes. 81 tests pass, the checks are OK.
  Player 244 pages, GM 237. I read pages 227 to 229. There is no overflow.
- I searched every content file for each new name. No name is in use.

## The gap table after this batch (SRD + original)

| Class | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bard | 10+3 | 23+5 | 23+3 | 17+3 | 10+2 | 17+1 | 8+2 | 11+2 | 6+3 | 5+2 |
| Cleric | 7+2 | 15+4 | 17+5 | 19+3 | 9+3 | 13+4 | 11+2 | 8+3 | 5+3 | 5+3 |
| Druid | 11+3 | 18+4 | 21+5 | 13+3 | 18+5 | 15+3 | 10+2 | 6+3 | 8+3 | 4+3 |
| Paladin | 0+1 | 13+5 | 11+4 | 6+4 | 4+5 | 4+4 | - | - | - | - |
| Ranger | 0+2 | 13+6 | 15+3 | 12+3 | 5+4 | 3+4 | - | - | - | - |
| Sorcerer | 16+3 | 21+5 | 27+3 | 21+3 | 13+2 | 12+2 | 11+2 | 8+2 | 6+3 | 5+3 |
| Warlock | 7+3 | 12+4 | 10+4 | 11+3 | 5+4 | 7+3 | 4+4 | 4+3 | 5+2 | 7+3 |
| Wizard | 15+5 | 30+7 | 36+8 | 29+7 | 26+6 | 24+2 | 19+6 | 15+3 | 12+4 | 12+2 |

Original spells now: 94.

## The spells, with the SRD spell that each is equal to

| Level | Spell | Classes | Equal to |
|---|---|---|---|
| 1 | Warding Word | B, C, P | Shield (+3, for an ally) |
| 1 | Splinter Volley | R, S, W | Magic Missile (3 attacks of 1d6) |
| 1 | Salt Ward | C, P, W | Protection from Evil and Good (ritual) |
| 1 | Predator's Leap | R, D | Jump plus a single Advantage |
| 2 | Anthem of Iron | B, P | Aid (temp HP, not max HP) |
| 2 | Interposing Step | P, C | Warding Bond (one hit, with Resistance) |
| 2 | Gnawing Doubt | B, K, W | Ray of Enfeeblement |
| 2 | Spectral Shackles | K, P, W | Hold Person (Restrained, any creature) |
| 2 | Cleansing Rain | C, D | Lesser Restoration (Poisoned only, in an area) |
| 2 | Bloodscent | R, D | Locate Creature (only wounded creatures, 60 ft) |
| 3 | Shattering Chord | B, S, W | Thunderwave scaled up (5d8, Cone) |
| 3 | Sundering Smite | P | Blinding Smite (3d8, AC -2) |
| 3 | Bramble Cloak | R, D | Fire Shield (smaller) |
| 3 | Pry the Secret | B, K, W | Zone of Truth (one question, one creature) |
| 4 | Masquerade | B, K, W | Seeming (fewer creatures, 1 hour) |
| 4 | Wolfpack Hunt | R, D | Faerie Fire (Advantage) plus Longstrider, for 5 creatures |
| 4 | Mantle of the Martyr | C, P | Warding Bond for the party |
| 4 | Hungering Rift | K, W | Black Tentacles (area control, 4d10, pull) |
| 4 | Falcon's Sight | R, D | Swift Quiver (range, not attacks) |
| 5 | Grand Finale | B, S | Flame Strike (7d8, with temp HP for allies) |
| 5 | Ambush Veil | R, D | Pass without Trace plus Greater Invisibility (only when still) |
| 5 | Soulfire | K, C | Blight scaled up (8d8, no healing for 1 turn) |
| 5 | Dawn Bulwark | P, C | Spirit Guardians (only Fiends and Undead) |
| 6 | Stampede of Spirits | D | Sunbeam (8d10 Line, Prone) |
| 6 | Prism Lance | S, W | Sunbeam / Chain Lightning (10d8 Line) |
| 6 | Mirror Throng | B, K, W | Mirror Image for 6 creatures |
| 6 | Withering Pact | K, W | Circle of Death (9d8, 30 ft) |
| 7 | Swallowing Earth | D, C, S | Finger of Death (10d10, Restrained) |
| 7 | Fracture the Mind | B, K, W | Finger of Death (10d10 Psychic, no spells 1 turn) |
| 7 | Great Renewal | C, D | Mass Cure Wounds scaled up (7d8, 8 creatures) |
| 8 | Storm of Glass | S, D, W | Incendiary Cloud (8d6) |
| 8 | Peace Unbroken | B, C | Antipathy / Mass Suggestion |
| 8 | Stormborne Form | S, D | Fly plus Call Lightning (self buff, 4d10 Bonus Action) |
| 9 | Absolute Zero | S, K, W | Meteor Swarm (20d6, one Sphere) |
| 9 | Entombing Root | D, C | Imprisonment |
| 9 | Unwritten Fate | B, S, K | Foresight / Wish-lite (3 reversals in 1 hour) |

## Things that I am not sure of

1. Wolfpack Hunt (level 4): Advantage for up to 5 creatures when an ally
   is next to the target. Faerie Fire gives Advantage at level 1, but on a
   save. I think that level 4 is correct.
2. Unwritten Fate (level 9) is the strongest. It reverses 3 rolls in 1
   hour, after you see them. Foresight gives Advantage on everything for 8
   hours to one creature. I can lower it to 2 uses.
3. Mantle of the Martyr: you take half of the damage of your allies. The
   damage can't be reduced, so the caster can't stack Resistance on it.
4. Interposing Step gives Resistance to the hit you take. Without it, the
   spell only moves damage.

## A question about shared text (not in this batch)

Three texts in shared files have counts that are now wrong:

- `compendium/books/player.src.html` line 827: "Twelve new backgrounds and
  two new species." (now 40 and 20)
- `compendium/books/player.src.html` line 836: "Forty-seven new spells"
  (now 94, and it grows)
- `compendium/build/cover.py` line 58: "47 new spells"

I propose to remove the numbers, so that the text stays correct, for
example "New backgrounds and species. Backgrounds follow the 2024 format:
..." and "New spells, from cantrips to 9th level." I can do this in one
commit, or you can do it, because these files are shared.
