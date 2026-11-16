# World bible: The Dawnwatch

Date: 2026-11-16.
Status: the source of truth for each writer of The Dawnwatch. If a chapter
needs a fact that is not here, add the fact here first, in the same
commit.

Parent design: [The Dawnwatch](2026-11-16-the-dawnwatch-design.md).
Book One outline: [Waking](2026-11-16-dawnwatch-waking-outline.md).

## The timeline

Years count from the long sleep. "Today" is year 300.

| Year | Event |
|---|---|
| About -40 | Sir Garrath, the first knight of the sun, sees that the sun is weaker each winter. |
| About -20 | Garrath tries to take the fire of the sun into himself, to save it. He becomes the Unlit King. |
| -20 to 0 | The war of the Unlit King. Ostrey cannot kill him. |
| 0 | Steward Haskel Orme puts Garrath to sleep in crystal under Kingsholm. Then he puts the five Dawnwatch to sleep under Dawnwatch Keep, to wait. Orme writes the official history: Ostrey "pushed the king back into the dark". He makes Wick on the last night. |
| 0 to 100 | Ostrey splits the Dawnfire into pieces and keeps them in shrines. The pieces keep Garrath asleep. |
| About 100 | The Grey Winter: three years with almost no summer. The last king of Ostrey dies with no heir. Civil war. A flood covers Fennick. Ostrey falls. |
| About 140 | Pilgrims tell stories of the five sleepers. The Church of the Five Sleepers starts at the shrine of Saint Ivo. |
| About 150 | The Gauntry family holds the south with an army. The March of Gauntry becomes the state of Gaunt. |
| About 210 | The towns of Corrin and Tey grow into one city, Corrantey. |
| About 270 | The days start to become shorter. Few people see it. The Hush starts, in secret. |
| 300 | The Hush puts out the Dawnfire in the chapel of the keep. The crystal cracks. The tutorial starts. |

## The truth and the lie

- **The lie (the player's guide, and what people know):** Malgrath, a
  demon king, came from the dark and tried to put out the sun. Ostrey
  pushed him back. The Dawnwatch sleep to wait for his return.
- **The truth (Book One, chapter 10):** Malgrath was Sir Garrath, the first
  of the Dawnwatch. People called him "Mal Garrath", the bad Garrath. Over
  300 years the name wore down to "Malgrath". He was not defeated. He was
  put to sleep, with the same crystal spell as the Dawnwatch.
- **Why Garrath wants to put out the sun (Book Two):** the sun is dying. He
  thinks that a sun that goes out and burns again can last.

## The map

The map is about 240 miles from west to east and 320 miles from north to
south. The coordinates are in miles from the north-west corner: x goes
east, y goes south. The maps lane uses these numbers.

| Place | x | y | What it is |
|---|---|---|---|
| Coldharrow | 120 | 20 | The fortress of Malgrath, behind the Grey Teeth mountains. Book Two. |
| The Grey Teeth | 60 to 200 | 40 to 60 | A wall of mountains across the north. |
| Kingsholm | 125 | 120 | The old capital of Ostrey, now ruins, on the River Dunn. Chapter 10. |
| Dawnwatch Keep | 165 | 150 | The keep of the tutorial, in the Wolds. Chapters 1 and 7. |
| The Wolds | 145 to 190 | 135 to 165 | Low hills with sheep and old stones. |
| Brannock's Ford | 160 | 172 | A village at a ford of the River Brann. Chapter 2. |
| Saint Ivo's | 150 | 220 | The town of the Church. Chapter 3. |
| The shrine at Kell | 110 | 205 | An old shrine of Ostrey on a hill. Chapter 4. |
| Ashby Field | 140 | 250 | Open land on the border of Gaunt and Saint Ivo's. Chapter 9. |
| Stannard | 130 | 285 | The seat of the Gauntry family. Chapter 5. |
| Corrantey | 35 | 200 | The city on the west coast, at the mouths of the Corrin and the Tey. Chapter 6. |
| Fennick | 205 | 245 | A drowned town in the Low Fen. Chapter 8. |
| The Low Fen | 185 to 235 | 225 to 275 | Marsh and black water in the south-east. |
| The Western Sea | 0 to 20 | all | The sea on the west coast. |

### The map 300 years ago

The map of Ostrey in the player's guide uses these places. The list in
`compendium/content/dawnwatch/places.py` holds all the places of both
maps.

| Place then | x | y | Place today |
|---|---|---|---|
| Ostrey | 20 to 240 | 60 to 320 | The land. People still say "old Ostrey". |
| Kingsholm, a whole city | 125 | 120 | Kingsholm, in ruins |
| Caer Dunholm | 120 | 20 | Coldharrow |
| The shrine of Saint Ivo | 150 | 220 | Saint Ivo's |
| The March of Gauntry | 70 to 190 | 255 to 320 | Gaunt |
| Corrin, a sea town | 33 | 193 | Corrantey |
| Tey, a sea town | 35 | 207 | Corrantey |
| Fennick, a town in farmland | 205 | 245 | Fennick, drowned in the Low Fen |

- Before the flood of the Grey Winter, the Low Fen was the farmland of
  Fennick. The flood made the marsh.
- Brannock's Ford, Stannard, and Ashby Field are not on the old map.
- Gaunt has the same land as the March of Gauntry: x 70 to 190, y 255 to
  320. Ashby Field is on its north border.

### Rivers

- **The River Dunn** comes down from the Grey Teeth, passes Kingsholm, and
  goes south-west to the sea north of Corrantey.
- **The River Brann** comes from the Wolds, passes Brannock's Ford, and
  goes south into the Low Fen.
- **The Corrin** and **the Tey** are two short rivers. They reach the sea
  at Corrantey.

### Travel

Use these days for the Journeys system. A day is about 24 miles on a
road and about 16 miles off the road.

| From | To | Days | Road |
|---|---|---|---|
| Dawnwatch Keep | Brannock's Ford | 1 | A sheep track |
| Brannock's Ford | Saint Ivo's | 3 | The old road of Ostrey, broken in places |
| Saint Ivo's | The shrine at Kell | 2 | Off the road |
| Saint Ivo's | Stannard | 3 | A good road, made by Gaunt |
| Saint Ivo's | Corrantey | 5 | The pilgrim road west |
| Saint Ivo's | Fennick | 4 | Off the road, through the Low Fen |
| Dawnwatch Keep | Kingsholm | 3 | Off the road, along the Dunn |

## The powers of today

### Gaunt

- A state of soldiers in the south. The Gauntry family rules from
  Stannard.
- It says that it is the true heir of Ostrey. It wants the Dawnwatch as
  living banners for its army.
- Its war mages keep "the spells of Ostrey", but most of the spells are
  wrong.

### The Church of the Five Sleepers

- It started at the shrine of Saint Ivo. The town of Saint Ivo's grew
  around it.
- It prays for the return of the five sleepers. It keeps the Ember of
  Saint Ivo, a piece of the Dawnfire, as a holy relic. It does not know
  what the relic does.
- Its art shows the five sleepers, but the faces are wrong.

### Corrantey and the guild of lantern makers

- A city of free merchants. A council of guilds rules it.
- The **Lampwrights**, the guild of lantern makers, is the oldest guild.
  It started with the apprentices of Haskel Orme. It keeps the First Lamp,
  a piece of the Dawnfire, in its hall.

### The Hush

- The cult of the Unlit King. It started about 30 years ago, when the days
  started to become shorter.
- Its members think that the sun is dying and that only the Unlit King can
  save the world. They are partly correct.
- They speak little and wear grey. They put out lights.
- They look for the pieces of the Dawnfire, to put them out and wake their
  king. They put out the piece in the chapel of the keep.

## Small facts of today

The gazetteer sets these facts. Each writer uses them.

- **The greeting today:** "Lightye." The answer is "Dawn." The small curse
  is "Darkit."
- **The coins today:** gold, silver, and copper pieces. Corrantey stamps a
  lamp on its coins. Gaunt stamps a mailed fist. A collector pays 5 GP or
  more for a gold sun of Ostrey.
- **The Church art:** the Five are tall, golden, and human. The faces are
  wrong. Nobody knows that the Spark is an elf.
- **The holy days:** the Longest Night is now the Vigil of the Five. The
  great feast is the Feast of the Five Sleepers in Saint Ivo's.
- **The Church books** say that the Five sleep "under a hill in the east".
  The Church does not know about Dawnwatch Keep.
- **The Lampwrights** keep a book of the times of sunrise and sunset. They
  know that the days become shorter.
- **The sky at noon:** on the day of the Waking, the sky over the Grey
  Teeth went black for a moment. All the land saw it.
- **Kingsholm** burned in the civil war of the Grey Winter. A forest grows
  around it now.

## Old Ostrey

The player's guide tells these facts. They are the world of year 0, as
the Dawnwatch know it. Each writer uses them.

- **The king at the time of the sleep:** King Aldwin. He was young when
  the war started. He is not in Book One.
- **The faith:** the Morning Flame, the god of the dawn. The priests wear
  red and gold and pray at dawn. The symbol is a sun disk.
- **The greeting:** "Light to you." The answer is "And dawn to you." The
  small curse is "Dark take it."
- **The coins:** a gold **sun**, a silver **star**, and a copper **bit**.
  Ten bits make a star. Ten stars make a sun. The coins of the tutorial
  are suns.
- **The Longest Night:** the winter vigil. Each house keeps one candle
  until dawn.
- **The badge of the Dawnwatch:** a rising sun, a half circle of gold on a
  straight line, with seven rays.
- **The oath of the Dawnwatch** ends with "I swear to wake the dawn." The
  player's guide has the full text.
- **The motto:** before the sleep, "We watch so that the dawn can wake."
  On the last night, the steward carved "We sleep so that the dawn can
  wake."
- **The order:** forty knights at the start of the war. Five at the end.
  The Dawnwatch marched at night and arrived at dawn.
- **The Dawnfire in the war:** it went in front of the army in a bronze
  bowl on a wagon. After the war, it burned in the chapel of the keep.
- **The Field of the Five:** the old name of Ashby Field. The army of the
  king stopped the hounds of the Unlit King there, in the snow, at dawn.
  The song "The Five at the Gate" tells of it. The old map does not show
  it.
- **Saint Ivo:** a healer of the Morning Flame. He stayed with the sick in
  a hard winter and did not catch the sickness. His shrine was a chapel,
  a well, and a guesthouse.
- **The shrine at Kell:** a ring of standing stones with a small chapel
  inside it.
- **Fennick:** a market town on a small rise in the farmland by the
  Brann, with dikes and a church with a square tower.
- **Corrin and Tey:** two rival port towns, about a mile apart.
- **The March of Gauntry:** the south border. The Gauntry family held it
  for the king from a fortress on a rock above the south road. Stannard
  grew around that fortress later.
- **The homes of the pregens:** the Shield is a human soldier of Ostrey.
  The Light came from the dwarf holds under the Grey Teeth. The Spark is
  an elf scholar. The Shadow was a thief in Kingsholm. The Storm was a
  goliath guide in the passes of the Grey Teeth.

## The creatures of Book One

The statblocks are in `compendium/content/dawnwatch/creatures_*.py`.

| Name | What it is | CR | Chapters |
|---|---|---|---|
| Hush Snuffer | The first tier of the Hush. A cultist with a brass snuffer on a pole. | 1/2 | 3, 4 |
| Hush Shroud | The second tier of the Hush. A priest in a grey veil who prays in silence. | 2 | 4, 5 |
| Hush Lightless | The third tier of the Hush. A warrior who drank the black water at the rite of the cult. | 4 | 4, 5 |
| The Long Shadow | The shadow of the Unlit King. Mother Sallow calls it through the black stone at Kell. The creature at the end of Act I. | 5 | 4 |

## The people of Book One

Each writer uses these names. Add a new person here before a chapter uses
the person in more than one scene.

| Name | Role | Chapters | Statblock |
|---|---|---|---|
| Haskel Orme | The steward of Dawnwatch Keep, 300 years ago. Dead. He made Wick and wrote the lie. | 1, 7, 10 (letters) | No |
| Wick | The talking lantern. The tutorial has his statblock. | All | Yes (tutorial) |
| Tamsin | The old ferry woman at Brannock's Ford. Kind, and she asks too many questions. | 2 | No |
| Dace | A pedlar who sells "bones of the Five Sleepers" to pilgrims. | 2, 3 | No |
| Abbess Merrow | The head of the Church in Saint Ivo's. She wants the party as living saints. | 3, 9 | No |
| Brother Cade | A priest who thinks that the party are impostors. Later an ally. | 3, 4, 9 | Yes |
| Corvin Lisle | An antiquary from Corrantey who buys old things of Ostrey. He offers a lot of money for the thing that the Shadow stole. | 2, 3 | No |
| Garret Pell | The leader of a troupe of actors who play the Dawnwatch. | 3 | No |
| Mother Sallow | The leader of the Hush. | 4, 7, 10 | Yes |
| Osk | The enforcer of Mother Sallow. Big, and he does not speak. | 4, 7 | Yes |
| Marshal Ide Gauntry | The ruler of Gaunt. | 5, 9 | Yes |
| Tobin Gauntry | Her son. He does not want a war. | 5, 9 | No |
| Magister Aud Brennet | The first war mage of Gaunt. She teaches a "Dawnwatch spell" that is wrong. | 5 | No |
| Perrin Hale | The master of the Lampwrights in Corrantey. | 6, 7 | No |
| Sergeant Maud Kettle | The ghost of a soldier of Ostrey in Fennick. She teaches the old fighting ways. | 8 | Yes |
| Sir Garrath (Malgrath) | The first Dawnwatch. The Unlit King. Only his voice in Book One. | 1, 4, 10 | No (Book Two) |

## The things of Book One

| Thing | What it is | Chapters |
|---|---|---|
| The black stone | A piece of the crystal of Garrath. It hums near the Hush and when Malgrath speaks. Chapter 4 gives it rules with the Marks system: the open Curse of the Black Stone. Artifact. | 1, 4, 10 |
| The Ember of Saint Ivo | A piece of the Dawnfire. A small coal that never goes cold, in a cage of old gold. Artifact. | 3, 4 |
| Compass of the Old Road | A brass compass of Ostrey that points along the old roads. The unique item of chapter 2. Uncommon. | 2 |
| Mask of the Fifth Sleeper | A painted mask from the play of the troupe of Garret Pell. The unique item of chapter 3. Uncommon. | 3 |
| Kell Warden's Shield | A shield of oak and bronze from the shrine at Kell. The unique item of chapter 4. Uncommon. | 4 |
| Gauntry War Banner | The red banner with the iron gauntlet of the house of Gauntry. The unique item of chapter 5. Rare. | 5 |
| The First Lamp | A piece of the Dawnfire. A lamp with a flame that needs no oil. | 6 |
| The piece in Fennick | A piece of the Dawnfire, under the water, in the old church of Fennick. | 8 |
| The letters of Haskel Orme | Handouts. They show the lie, step by step. | 7, 10 |
