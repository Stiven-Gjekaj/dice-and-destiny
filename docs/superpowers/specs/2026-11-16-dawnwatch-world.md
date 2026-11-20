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
| About -60 | The rival ports Corrin and Tey send one fleet west together, to find land beyond the Western Sea. A wall of storms traps the fleet at Farholm. No ship comes back. Beyond the Western Sea. |
| About -45 | Sir Garrath, the first knight of the sun, founds the Dawnwatch and writes its oath. |
| About -40 | Sir Garrath, the first knight of the sun, sees that the sun is weaker each winter. |
| About -20 | Garrath goes north and tries to take the fire of the sun into himself, to save it. He becomes the Unlit King. The five sleepers swear the oath after he goes. They never meet him. |
| -20 to 0 | The war of the Unlit King. Ostrey cannot kill him. |
| 0 | Steward Haskel Orme puts Garrath to sleep in crystal under Kingsholm. Then he puts the five Dawnwatch to sleep under Dawnwatch Keep, to wait. Orme writes the official history: Ostrey "pushed the king back into the dark". He makes Wick on the last night. |
| 0 to 100 | Ostrey splits the Dawnfire into pieces and keeps them in shrines. The pieces keep Garrath asleep. |
| About 100 | The Grey Winter: three years with almost no summer. The last king of Ostrey dies with no heir. Civil war. A flood covers Fennick. Ostrey falls. |
| About 140 | Pilgrims tell stories of the five sleepers. The Church of the Five Sleepers starts at the shrine of Saint Ivo. |
| About 150 | The Gauntry family holds the south with an army. The March of Gauntry becomes the state of Gaunt. The grandmother of the grandmother of Marshal Ide Gauntry carries the red banner of the house (chapter 5). |
| About 151 | The *Hopewell* year on Farholm. The Corrin men light the Corrin Light in the storm season, and the *Hopewell* sails into the path through the storms. The Tey folk put out the light. The path closes, and the storms throw the ship back onto the island. The sea drowns the low part of Hythe. Beyond the Western Sea. |
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
| Wenlow | 148 | 200 | A small village of the Church on the old road, three days south of the keep. The Hush burned its chapel. Chapter 9. |
| Wendle | 144 | 256 | A village of farms on the border, in Gaunt by a mile, on the good road south. Chapters 5 and 9. |
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
- The old roads of Ostrey lead to Kingsholm. One goes south-east to the
  ford of the Brann, and then south to the shrine of Saint Ivo. Today only
  the part from Brannock's Ford to Saint Ivo's is left, broken in places.
  One goes south-west along the Dunn to Corrin. One goes south to the shrine
  at Kell. The roads of today to Stannard and Corrantey are not on the old
  map.
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
| Brannock's Ford | Wenlow | 2 | The old road of Ostrey |
| Wenlow | Saint Ivo's | 1 | The old road of Ostrey |
| Dawnwatch Keep | Saint Ivo's | 4 | The sheep track, then the old road through Brannock's Ford |
| Dawnwatch Keep | Wenlow | 3 | The sheep track, then the old road |
| Saint Ivo's | The shrine at Kell | 3 | Off the road |
| Saint Ivo's | Stannard | 3 | A good road, made by Gaunt |
| Saint Ivo's | Wendle and the border of Gaunt | 2 | A good road, made by Gaunt |
| Saint Ivo's | Ashby Field | 2 | A good road, made by Gaunt |
| Wenlow | Ashby Field | 3 | The old road to Saint Ivo's, then the road of Gaunt |
| Dawnwatch Keep | Ashby Field | 6 | By Wenlow and Saint Ivo's |
| Saint Ivo's | Corrantey | 5 | The pilgrim road west |
| Saint Ivo's | Fennick | 4 | Off the road, through the Low Fen |
| Dawnwatch Keep | Kingsholm | 3 | Off the road: north-west over the Wolds to the Dunn, then up its bank |
| Kingsholm | Saint Ivo's | 7 | By Dawnwatch Keep |

The roads do not go in straight lines. The old road from Brannock's Ford
to Saint Ivo's is about 72 miles long (49 miles in a straight line). Wenlow
is on it, about 20 miles north of Saint Ivo's. The shrine at Kell is about
43 miles from Saint Ivo's, all off the road. Ashby Field is on the road of
Gaunt, about 32 miles south of Saint Ivo's, on day 2 of the road to
Stannard, as the border and Wendle are.

### Farholm, beyond the map

Beyond the Western Sea uses these facts. The land map does not show
Farholm. It is off the west edge of the map.

- **Where:** Farholm is an island in the Western Sea, about 300 miles west
  of Corrantey. It is on no chart of the land.
- **The size:** about 20 miles from west to east and 12 miles from north
  to south. Its map has its own coordinates, in miles from the north-west
  corner of the island map: x goes east, y goes south. The list in
  `compendium/content/western_sea/places.py` holds these places.
- **The truth:** the island is the back of a giant sea creature that
  sleeps. Its heart is deep under the island. The colonists call it the
  Grandam. The island moves very slowly. This is why no chart shows it.
- **The wall of storms:** a ring of storms around the island, about 20
  miles out. It is the breath of the Grandam. A ship that comes near the
  wall goes in with the wind and wrecks on the island. No ship has gone out
  through it.
- **The storm season:** each storm season, the Grandam stirs, and the
  storms come in over the island. The Corrin Light can open a path through
  the wall, but only while she stirs.
- **The fleet:** in about year -60, eleven ships of Corrin and Tey sailed
  west with about 700 people, to find land and to settle it. The flagship
  was the *Morning Star*, of Corrin. The wall of storms trapped the fleet.
  The ships wrecked on Farholm, and the people lived.
- **The colony today:** about 400 people, in the town of Hythe. They keep
  the customs of old Ostrey (see "Old Ostrey"): the greeting "Light to
  you", the Morning Flame, and the count in suns, stars, and bits. They
  left before the war of the Unlit King, so they do not know of it.
- **The two sides:** the Corrin men want to go home, and they guard the
  ruins of the Corrin Light. The Tey folk worship the Grandam. They believe
  that to leave, or to light the lighthouse, wakes her and sinks everyone.
- **The saint:** the church of the colony tells of a saint who lit a fire
  on the back of the Grandam, and the island moved.
- **In year 300:** the *Good Intent*, a merchant ship of Corrantey, wrecks
  on Farholm. It is the first ship from the land in 360 years.
- Farholm has no link to the story of Book One. The Hush, Malgrath, the
  black stones, and the Dawnfire are not on the island.

### Farholm: the history of the colony

The gazetteer of Beyond the Western Sea tells these facts. Each writer of
the book uses them.

- **The count of years:** the colonists count the years from the Landing.
  The Landing is their year 0, our year -60. Year 300 is "the year 360 of
  the Landing".
- **The ships of the fleet:** six ships of Corrin and five of Tey. The
  ships of Corrin are the *Morning Star*, the *Speedwell*, the *Hopewell*,
  the *Swallow*, the *Increase*, and the *Desire*. The ships of Tey are the
  *Patience*, the *Dove*, the *Blessing*, the *Content*, and the *Unity*.
- **The leaders of the fleet:** Captain Humphrey Gale of Corrin, master of
  the *Morning Star*, leads the fleet. Magnus Isbister of Tey is master of
  the *Patience* and leads the ships of Tey.
- **The Landing:** in the summer of year -60, a wind takes the fleet
  through the wall of storms. The sea "stands up". The ships wreck on the
  south and north coasts. The sea puts the *Morning Star* high on the
  Ribs. About 700 people come ashore. About 500 live through the first
  winter.
- **The saint:** Father Mawes is a priest of the Morning Flame on the
  *Patience*. In the first winter, he lights the dawn fire on bare ground
  in the west of the island. The ground shakes and the island moves. He
  puts out the fire and prays until the ground is still. He dies in the
  year 3 of the Landing. The colony calls him Saint Mawes. The place of
  his fire is the Saint's Hearth.
- **The Corrin Light:** in the first ten years, Captain Gale builds a
  tower of stone on the east point, toward home. It holds the great lamp
  of the *Morning Star*: a lamp of brass, with a mirror behind it and a
  lens of glass in front of it. Gale dies in the year 19 of the Landing.
- **The Grandam:** after the saint, the Tey folk believe that the island
  is alive. They call it the Grandam and pray to it at the Grandam's
  Well. The first Well Keeper is Agnes Flett, in about the year 60 of the
  Landing.
- **The *Hopewell* year:** in the year 211 of the Landing (year 151), the
  Corrin men build a new ship from the wrecks. They give it the name of an
  old ship, the *Hopewell*. John Pascoe is its master. They light the
  Corrin Light in the storm season, and a path opens through the wall to
  the east. The *Hopewell* sails. Sander Linklater leads the Tey folk into
  the tower, and they put out the lamp and break its lens. The path
  closes, and the storms throw the *Hopewell* back onto the north coast.
  Nobody on it lives. In the same season, the sea comes up the Fleet and
  drowns the low part of Hythe, on the Tey bank. Forty people die. The
  colonists call this the Drowning.
- **After the Drowning:** the Moot of Hythe forbids anyone to light the
  Corrin Light. The Corrin men keep a watch at the ruin. The Tey folk
  carry the pieces of the lamp away. Some pieces go down the Grandam's
  Well as gifts. Some families keep a piece. The Corrin men keep the brass
  frame of the lamp.
- **What each side believes about the *Hopewell*:** the Corrin men believe
  that it reached home, and that Corrin will send ships one day. The Tey
  folk believe that the Grandam threw it back. The truth: the path closed
  when the light went out. The name board of the *Hopewell* lies in the
  Boneyard.

### Farholm: Hythe and the customs

- **Hythe:** the only town. About 400 people. About 180 live on the east
  bank of the Fleet (the Corrin bank) and about 220 on the west bank (the
  Tey bank). One bridge of ballast stone crosses the Fleet. The colonists
  call it the Bridge. The market is on the Bridge.
- **The houses:** timber from the wrecks, walls of turf, and roofs of turf.
  Some houses are old hulls, upside down.
- **The halls:** the Moot House is the great cabin of the *Patience*, on
  the Tey bank near the Bridge. The Corrin men meet in the Lamp Room, on
  the Corrin bank. A lamp burns in its east window each night. The Tey
  folk meet in the Net Loft.
- **The Moot:** six headmen of each bank meet at the Moot House. The
  priest of the church keeps the peace at the Moot. The Captain of the
  Light leads the Corrin men. The Well Keeper leads the Tey folk.
- **The church:** the church of the Morning Flame on Founders' Hill. Both
  sides pray there, on two sides of the aisle. The priest wears red and
  gold, as in old Ostrey.
- **The speech:** the speech of old Ostrey, slow and formal, with many sea
  words. "Light to you." "And dawn to you." "Dark take it." The colonists
  think that the speech of today is fast and rough.
- **Their words:** the Wall is the wall of storms. The Turning is the
  storm season. The Landing is the arrival of the fleet. "Over the Wall"
  means the land of Ostrey, and also means "never".
- **The coins:** a few suns, stars, and bits of the fleet, with the head
  of King Edwy, the king of Ostrey in year -60. The colonists also cut
  bits from the copper nails of the wrecks. Most trade is in salt, fish,
  and work.
- **The colors:** Corrin is a white ship on blue. Tey is a silver fish on
  green. Each side wears a ribbon of its color on a holy day.
- **The hearth stones:** no fire burns on the bare ground of Farholm. Each
  hearth in Hythe stands on ballast stones from the ships. The Tey folk
  keep this custom strictly. The Corrin men keep it too, from habit.
- **The Morning Flame on Farholm:** a priest lights the dawn fire on a
  ballast stone in the church, never on the ground. The holy days are
  Landing Day at midsummer, Saint Mawes's Day in midwinter, and the
  Longest Night.
- **The food:** fish, seal, sea birds and their eggs from Gull Rock,
  limpets, laver bread from seaweed, barley, small sheep, and ale. No
  wine, no spice, and little iron.
- **The names:** the Corrin men have the old surnames of Corrin, for
  example Pascoe, Hocking, Nance, Gale, and Rundle. The Tey folk have the
  old surnames of Tey, for example Flett, Linklater, Halcrow, Isbister,
  Spence, and Tulloch.
- **Marriage across the Bridge** is rare. It is not forbidden, but each
  side treats the couple coldly.

### Farholm: the truth of the Grandam

- **What she is:** a creature of the deep sea, older than Ostrey, as big
  as the island. The island is the crust of her back: stone, sand, turf,
  and shell. The Ribs are the ridges of her back. The Kettles are near the
  place where she breathes. The Grandam's Well goes down to her heart.
- **What she is not:** she is not a god. She does not know the colonists.
  She does not punish anyone. Fire on her bare back hurts her and makes
  her stir, as the saint found.
- **The breath:** her breath goes out under the sea and makes the wall of
  storms. When she stirs, she breathes harder and the storms come in.
- **The light:** she rises toward a great light, as a fish rises to a
  lantern. While she rises, she holds her breath, and the wall on the side
  of the light goes quiet. This is the path. A light on a still night does
  nothing, because she does not see it in her sleep.
- **The long sleep:** each storm season she stirs. Once in about 360 years
  she almost wakes. The last time was the Landing. Year 300 is the next
  time. The Tey folk call this the Long Count.
- **If she wakes:** within days she dives. The island goes under the sea,
  and the wall of storms breaks up. A person on the island drowns.
- **If she sleeps again:** the wall stays for another long sleep. The path
  closes. The Light can open it again only in a later storm season.
- **How to make her sleep:** do what the saint did. Put out each fire on
  her back and go down to her heart in the dark, quietly. The Tey folk
  keep the old dawn hymn of the saint. They sing it at the Well, and they
  do not know why it matters. The last chapter gives the rules.
- **Who is right:** neither side. The Corrin men are right that the Light
  opens a path. They are wrong that it works at any time, and wrong about
  the *Hopewell* and about home: Corrin and Tey are one city now, and
  nobody there remembers the fleet as more than a story. The Tey folk are
  right that the Grandam is alive and that fire wakes her. They are wrong
  that she loves them, wrong that leaving wakes her, and wrong that the
  Light caused the Drowning. The storm season caused the Drowning.

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
  It started with the apprentices of Haskel Orme. Orme made the First Lamp
  in the first winter of the war. The piece of the Dawnfire went into it
  after the war, from the fire in the chapel of the keep. It keeps the First Lamp,
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

- **The greeting today:** "Wake well." The answer is "And see the
  morning." It comes from the Sleepers. The small curse is "Darkit."
- **The coins today:** gold, silver, and copper pieces. Corrantey stamps a
  lamp on its coins. Gaunt stamps the iron gauntlet of the Gauntry family. A collector pays 5 GP or
  more for a gold sun of Ostrey.
- **The Church art:** the Five are tall, golden, and human. The faces are
  wrong. Nobody knows that the Spark is an elf.
- **The holy days:** the Longest Night is now the Vigil of the Five. The
  great feast is the Feast of the Five Sleepers in Saint Ivo's.
- **The Church books** say that the Five sleep "under a hill somewhere in
  the north". The Church does not know about Dawnwatch Keep.
- **The priests of the Church** wear grey and blue. The Morning Flame is
  half forgotten. The Church keeps a saint's day for it.
- **The Lampwrights** keep a book of the times of sunrise and sunset. They
  know that the days become shorter.
- **The sky at noon:** on the day of the Waking, the sky over the Grey
  Teeth went black for a moment. All the land saw it.
- **Kingsholm** burned in the civil war of the Grey Winter. A forest grows
  around it now.
- **The statue in Kingsholm:** a knight in the armor of the Dawnwatch in
  the old square, with the face and the name cut away. It was Garrath.
  Orme had them cut. Chapter 10.
- **The door of the vault under Kingsholm** opens only for the Dawnwatch.
  The badge of the order opens it, and so does the black stone. The Hush
  cannot open it. This is why the Hush needs the party and the stone in
  Kingsholm (chapter 10). Mother Sallow drank the dark that seeps out under
  the shut door.
- **The mark of Haskel Orme:** a small sun inside a square. The
  Lampwrights put it on every lamp. It is on Wick.
- **The council of Corrantey:** twelve guild masters, one seat each, at a
  round table in the Council House.
- **The Book of the Vigil:** the holy book of the Church, with the stories
  of the Five. Most of the stories are wrong.
- **The strength of the powers:** Gaunt has about three thousand soldiers
  and twenty war mages. The Church has a guard of about four hundred. The
  city watch of Corrantey is about five hundred. The Hush has a few
  hundred members.
- **The sizes of the towns:** Brannock's Ford about two hundred people,
  Saint Ivo's about four thousand, Stannard about six thousand, Corrantey
  about fifteen thousand.
- **Small places in the gazetteer:** in Corrantey, Lantern Street, the
  Hall of the Lampwrights, and the Council House on the bridge between the
  two halves. In Stannard, the Marshal's Hall, the College of War, and the
  Gate of the Five. In Saint Ivo's, the Church of the Five with five
  towers, and the sealed old chapel of Saint Ivo under it.
- **The goliath name for the Unlit King:** "the one who ate the fire". A
  hint for chapter 10.
- **Kell** had its own piece of the Dawnfire after the war. It went out in
  the Broken Years. The Hush uses its dead bowl for the rite that puts out
  a living piece (chapter 4).
- **The song:** "The Five at the Gate" is sung on the pilgrim road. In it,
  seven heroes hold the gate at Ashby Field, and they sleep under Saint
  Ivo's. Almost every fact is wrong (chapter 2 handout).
- **Brannock's Ford:** a village of about two hundred people. Brannock, a
  ferryman, built the first house about 150 years ago, after the bridge of
  Ostrey fell. The ferry is older: after the Grey Winter, an ancestor of
  Tamsin married the ferryman at the ford, and her family ran the ferry
  before Brannock built the first house (year 150). The inn is the Ferry Bell. The old barrow of the road
  wardens of Ostrey is on Ferry Hill, a mile north.
- **Saint Ivo's:** a town of about four thousand people inside a wall of
  yellow stone. The Church of the Five stands over the old shrine. The
  Ember lives on its high altar. The Feast of the Sleepers lasts three
  days, and ends with the Waking Service, when the Abbess carries the
  Ember out to the people. Pell's Players perform in the Players' Yard of
  the inn called the Lamb and Lantern.
- **Under Saint Ivo's:** around the old shrine lies an old crypt of
  Ostrey. In the Grey Winter, people hid in it, and some became ghouls.
  The Church found the crypt later, made its upper galleries an ossuary,
  and sealed the deep part. The Ember burned in the bowl of the old chapel
  until about year 150. Then the Church moved it up to the high altar and
  sealed the chapel. Nobody opened the chapel again until chapter 3.
- **The Ember glows:** for two hundred years, the Ember was a dull red
  coal. On the night that the Dawnwatch woke, it started to burn gold
  (chapter 3).
- **Wendle:** a village of farms on the border, in Gaunt by a mile. Its
  people pray at Saint Ivo's. A press gang of Gaunt takes its sons in
  chapter 5. If the party does not stop it, the boys are soldiers at Ashby
  Field in chapter 9.
- **Sergeant Maud Kettle** was a sergeant of the last garrison of the king
  in Fennick, in the Grey Winter. She drowned in the flood of year 100.
- **The keep after the sleep:** later stewards held it until the Grey
  Winter. Then the last steward left for the war of the lords. The last
  watchman, an ancestor of Tamsin six generations back, left with him.
  Neither came back. The watchman's family stayed and kept the watch: his
  wife kept the door shut for three years, then went down to the ford.

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
- **The guest master of the shrine** in the year of the sleep was Brother
  Alys. He had one leg and kept bees. The guest book of the shrine has the
  names of the Dawnwatch from their last visit (chapter 3).
- **The shrine at Kell:** a ring of standing stones with a small chapel
  inside it.
- **Fennick:** a market town on a small rise in the farmland by the
  Brann, with dikes and a church with a square tower.
- **Corrin and Tey:** two rival port towns, about a mile apart.
- **The lost fleet:** in about year -60, Corrin and Tey sent one fleet west
  together. It did not come back. Each town said that the other town lost
  it. In year 0, old sailors still tell the story.
- **The March of Gauntry:** the south border. The Gauntry family held it
  for the king from a fortress on a rock above the south road. Stannard
  grew around that fortress later.
- **The homes of the pregens:** the Shield is a human soldier of Ostrey.
  The Light came from the dwarf holds under the Grey Teeth. The Spark is
  an elf scholar. The Shadow was a thief in Kingsholm. The Storm was a
  goliath guide in the passes of the Grey Teeth.

## The people of Book One

Each writer uses these names. Add a new person here before a chapter uses
the person in more than one scene.

| Name | Role | Chapters | Statblock |
|---|---|---|---|
| Haskel Orme | The steward of Dawnwatch Keep, 300 years ago. Dead. He made Wick and wrote the lie. | 1, 6, 7, 10 (letters) | No |
| Wenna Orme | The sister of Haskel Orme, in Kingsholm, 300 years ago. Dead. His letters in chapter 7 are to her. | 7 (letters) | No |
| Wick | The talking lantern. He is "he" in every book. The tutorial has no statblock for him, only notes on his personality (`statblocks.md`). Book Two secret: his flame is the last true piece of the Dawnfire. In Book One, only hint at it: his flame reacts to the Dawnfire. He knows of only one hall of sleepers, the hall under Dawnwatch Keep. The second group of Book Two is hidden from him. | All | No |
| Tamsin | The old ferry woman at Brannock's Ford. Kind, and she asks too many questions. | 2 | No |
| Dace | A pedlar who sells "bones of the Five Sleepers" to pilgrims. | 2, 3 | No |
| Abbess Merrow | The head of the Church in Saint Ivo's. She wants the party as living saints. | 3, 9, 10 | No |
| Brother Cade | A priest who thinks that the party are impostors. Later an ally. | 3, 4, 9, 10 | Yes |
| Corvin Lisle | An antiquary from Corrantey who buys old things of Ostrey. He offers a lot of money for the thing that the Shadow stole. | 2, 3 | No |
| Garret Pell | The leader of a troupe of actors who play the Dawnwatch. | 3 | No |
| Captain Joss Marrick | The captain of the honor guard of Gaunt at the feast of Saint Ivo's. He reports to the Marshal and makes the party her offer. | 3, 5 | No |
| Tilly Ashe | An actress of Pell's Players. She plays the Shadow. | 3 | No |
| Mother Sallow | The leader of the Hush. She watches the Waking Service at the end of chapter 3, with no candle. Chapter 10 uses a stronger statblock, "Mother Sallow, Unbound" (`people_act2.py`). | 3, 4, 7, 10 | Yes |
| Osk | The enforcer of Mother Sallow. Big, and he does not speak. | 4, 7 | Yes |
| Marshal Ide Gauntry | The ruler of Gaunt. She signs as "Marshal of Gaunt, Warden of the March". Her statblock is in `people_act1.py`: CR 8, about 52 damage each round (three longsword attacks). | 5, 9, 10 | Yes |
| Captain Ilse Varro | The spymaster of Gaunt in Corrantey. She works for Marshal Gauntry. | 6, 9, 10 | Yes |
| Tobin Gauntry | Her son. He does not want a war. | 5, 9, 10 | No |
| Magister Aud Brennet | The first war mage of Gaunt. She teaches a "Dawnwatch spell" that is wrong. | 5 | No |
| Perrin Hale | The master of the Lampwrights in Corrantey. | 6, 7, 10 | No |
| Edric Pole | An old shepherd of the Wolds. The Hush burned his farm. He can keep the gate of the keep. | 7 | No |
| Hesper Wren | A young Lampwright, sent by Perrin Hale. If the party sided with Gaunt in chapter 6, she comes on her own. She becomes the steward of Dawnwatch Keep when the party takes it back. | 7, 10 | No |
| Ada Ferrow | An old eel catcher of the Low Fen. She takes the party to Fennick by boat. Her brother Tam died there. | 8 | No |
| Lieutenant Roe | The aide of Marshal Gauntry. A secret agent of the Hush. He is the helpful aide of the party in Stannard (chapter 5). | 5, 9 | Yes (Hush Dusk Priest) |
| Brother Ansel | The secretary of Abbess Merrow. A secret agent of the Hush. If the Church keeps the Ember, he steals it from the high altar in chapter 9. | 5 (the false letter), 9, 10 | Yes (Hush Dusk Priest) |
| Corporal Lenna | A young soldier of the levy of Saint Ivo's. Her family name is the family of the person of the Shield's promise. | 9 | Yes (Line Pikeman) |
| Sergeant Maud Kettle | The ghost of a soldier of Ostrey in Fennick. She teaches the old fighting ways. | 8 | Yes |
| Sir Garrath (Malgrath) | The first Dawnwatch. He founded the order a generation before the five sleepers, and they never met him. "Brothers. Sisters." is the kinship of the order. The Unlit King. Only his voice in Book One. | 1, 4, 6 (a dream), 7, 10 | No (Book Two) |

## The creatures of Book One

Each new creature of the content files has a row here. The file column
tells which lane owns the creature.

| Name | What it is | Chapters | File |
|---|---|---|---|
| Hush Snuffer | The first tier of the Hush. A cultist with a brass snuffer on a pole. CR 1/2. | 3, 4 | `creatures_act1.py` |
| Hush Shroud | The second tier of the Hush. A priest in a grey veil who prays in silence. CR 2. | 3, 4, 5 | `creatures_act1.py` |
| Hush Lightless | The third tier of the Hush. A warrior who drank the black water at the rite of the cult. CR 4. | 4, 5 | `creatures_act1.py` |
| The Long Shadow | The shadow of the Unlit King. Mother Sallow calls it through the black stone at Kell. The creature at the end of Act I. CR 5. | 4 | `creatures_act1.py` |
| Hush Night Warden | A soldier of the Hush in grey mail. CR 4. | 7, 8, 9, 10 | `creatures_act2.py` |
| Hush Grey Choir | A crowd of Hush singers that acts as one swarm. CR 6. | 7, 9, 10 | `creatures_act2.py` |
| Hush Dusk Priest | A priest of the Hush who puts out lights. CR 7. | 7, 8, 9, 10 | `creatures_act2.py` |
| Brass Lamp Warden | A brass guardian of the hall of the Lampwrights, with the maker's mark of Haskel Orme. Orme made the six guards (handout of chapter 6). CR 5. | 6 | `creatures_act2.py` |
| Fennick Drowned | A drowned townsperson of Fennick. CR 2. | 8 | `creatures_act2.py` |
| Grief of Fennick | The sorrow of the drowned town, in the old church. CR 8. | 8 | `creatures_act2.py` |
| Sergeant Maud Kettle | See the people. CR 5. | 8 | `creatures_act2.py` |
| The Unlit Knight | The empty armor that guards the crystal under Kingsholm. The creature of the end of Act II. CR 12. | 10 | `creatures_act2.py` |

## The things of Book One

| Thing | What it is | Chapters |
|---|---|---|
| The black stone | A piece of the crystal of Garrath. It points at Garrath: at Kingsholm on the road (the dark that he left in the vault), and to the far north after the vault (chapter 10). It hums near the Hush and when Malgrath speaks. Chapter 4 gives it rules with the Marks system: the open Taint of the Black Stone (a Taint, not a Curse: it grows when the bearer uses its power). Artifact. | 1, 4, 10 |
| The Ember of Saint Ivo | A piece of the Dawnfire. A small coal that never goes cold, in a cage of old gold. Artifact. | 3 to 10 |
| Compass of the Old Road | A brass compass of Ostrey that points along the old roads. The unique item of chapter 2. Uncommon. | 2 |
| Mask of the Fifth Sleeper | A painted mask from the play of the troupe of Garret Pell. The unique item of chapter 3. Uncommon. | 3 |
| Kell Warden's Shield | A shield of oak and bronze from the shrine at Kell. The unique item of chapter 4. Uncommon. | 4 |
| Gauntry War Banner | The red banner with the iron gauntlet of the house of Gauntry. The unique item of chapter 5. Rare. | 5 |
| The First Lamp | A piece of the Dawnfire. A lamp with a flame that needs no oil. Very Rare (`treasures_act2.py`). | 6 |
| The Fennick Candle (the piece in Fennick) | A piece of the Dawnfire, under the water, in the old church of Fennick. A candle that burns under water. Very Rare (`treasures_act2.py`). | 8 |
| Storm Lantern of Corrantey | The unique item of chapter 6. The Lampwrights make it from the materials of the party. Rare. | 6 |
| The Dawn Banner | The unique item of chapter 7. The last war banner of the Dawnwatch, in the keep. Rare. | 7, 9 |
| Maud Kettle's Whistle | The unique item of chapter 8. The drill whistle of Sergeant Maud Kettle. Uncommon. | 8 |
| The Bonesetter's Needle | The unique item of chapter 9. A healer's needle from the field of Ashby. Uncommon. | 9 |
| The Badge of Sir Garrath | The unique item of chapter 10. The badge of the first Dawnwatch, on the empty crystal. Rare. | 10 |
| The grey ledger | The book of prayers of Mother Sallow. Its last page lists the pieces of the Dawnfire that the Hush hunts: the keep, Kell, the Ember, the lamp in Corrantey, and the church in Fennick. A handout. | 4 |
| The letters of Haskel Orme | Handouts. They show the lie, step by step. | 7, 10 |

## The people of Beyond the Western Sea

Each writer of Beyond the Western Sea uses these names. The people with a
statblock are in `compendium/content/western_sea/people.py`.

| Name | Side | Role | Statblock |
|---|---|---|---|
| Absalom Pascoe | Corrin men | The Captain of the Light, the leader of the Corrin men. About 60. Stubborn and honest. A descendant of John Pascoe of the *Hopewell*. | Yes |
| Kit Hocking | Corrin men | A young Corrin man, the leader of the young men who want to light the Light now. | Yes |
| Nathaniel Gale | Corrin men | The schoolmaster and the keeper of the Landing Book, the records of the colony. The last of the family of Captain Humphrey Gale. He knows how the lamp works. | No |
| Margery Nance | Corrin men | The shipwright of the Corrin bank. She builds a boat in secret, in a shed on the Corrin bank. | No |
| Elspeth Flett | Tey folk | The Well Keeper, the leader of the Tey folk. About 70. She keeps the dawn hymn of the saint. | No |
| Erlend Linklater | Tey folk | The leader of the Well Watch, the Tey men who keep people away from the Light. A descendant of Sander Linklater. | Yes |
| Inga Halcrow | Tey folk | A girl of 14 who dreams the dreams of the Grandam. The Tey folk think that she is holy. | No |
| Thomas Spence | Tey folk | A fisherman of the Tey bank, the best guide on the island. The husband of Hester Spence. | Yes |
| Hester Spence | Both | The daughter of Absalom Pascoe. She married Thomas Spence and lives on the Tey bank. Neither side fully trusts her. | No |
| Father Gilbert Rundle | The church | The priest of the Morning Flame on Founders' Hill. Born on the Corrin bank. He keeps the peace at the Moot. | No |
| Amos Tulloch | Neither | An old salt boiler at the Saltpans. He lives apart from both sides. The first colonist that the party meets. | No |
| Elias Trewin | The *Good Intent* | The master of the *Good Intent*, of Corrantey. About 50. He stays at the helm when she strikes the reef, and the sea takes him. Chapter 1. | No |
| Hannah Rowse | The *Good Intent* | The mate. About 35. She breaks a leg in the wreck and leads the survivors after it. Chapter 1. | No |
| Jory Kitto | The *Good Intent* | The bosun. About 45. He saves the ship's boat in the wreck. Chapter 1. | No |
| Simeon Tregear | The *Good Intent* | The cook, and the surgeon in an emergency. About 60. Chapter 1. | No |
| Nell Jago | The *Good Intent* | The ship's girl. 12 years old. The sea puts her ashore alone at the west end of Wreckers' Bay. Chapter 1. | No |

People of the past (no statblock):

| Name | What the people know of the person |
|---|---|
| Captain Humphrey Gale | The leader of the fleet and the master of the *Morning Star*, of Corrin. He built the Corrin Light. Died in the year 19 of the Landing. |
| Magnus Isbister | The master of the *Patience*, of Tey, and the leader of the ships of Tey. |
| Saint Mawes | Father Mawes, a priest of the Morning Flame on the *Patience*. He lit the dawn fire on the bare ground, and the island moved. |
| Agnes Flett | The first Well Keeper of the Tey folk, in about the year 60 of the Landing. |
| John Pascoe | The master of the *Hopewell* in the year 211 of the Landing. Lost with the ship. |
| Sander Linklater | The Tey man who led the Tey folk into the Corrin Light in the *Hopewell* year and put out the lamp. |
| King Edwy | The king of Ostrey in year -60. His head is on the old coins of the colony. |

Minor people of the island (chapter 2). The people with a role line are in
`compendium/content/western_sea/people_island.py`. None has a statblock.

| Name | Side | Role |
|---|---|---|
| Loveday Penrose | Neither | A salt boiler at the Saltpans. A widow of the Corrin bank. |
| Ola Drever | Neither | A boy of 12 of the Tey bank. He boils salt at the Saltpans and wants to be a sailor. |
| Digory Rowe | Corrin men | An old man of the watch at the Corrin Light. He keeps the log of the watch. |
| Thorfinn Harcus | Tey folk | The oldest egg climber of Gull Rock. |
| Jory Treloar | Corrin men | A man who takes wood and iron from the Boneyard. |
| Wenna Kitto | The church | The sexton of the church on Founders' Hill. |
| Sam Hocking | Corrin men | The brother of Kit Hocking. 17. |
| Jacky Hocking | Corrin men | A cousin of Kit Hocking. 8. |

People of the past in chapter 2 (no statblock, except the ghost of John
Pascoe in `creatures_island.py`):

| Name | What the people know of the person |
|---|---|
| Jenefer Tulloch | The wife of Amos Tulloch, of the Corrin bank. She died about 10 years ago. She cut the marks of the dry tides on the door post of the hut. |
| Mary Pascoe | The wife of John Pascoe. Their son is the ancestor of Absalom Pascoe. |
| Barbara Rendall | A colonist of the *Dove*. She died in the year 2 of the Landing. Her grave is on Founders' Hill. |
| William Nance | A colonist of the *Swallow*. He died in the year 0 of the Landing. His grave is on Founders' Hill. |

People of the last chapter (chapter 3). They meet the party in Corrantey,
in the epilogue. They are in `compendium/content/western_sea/people_finale.py`.
None has a statblock.

| Name | Side | Role |
|---|---|---|
| Ruth Polglase | Corrantey | The harbor master of Corrantey. She has watched the western sea for thirty years. |
| Walter Isbister | Corrantey | A merchant of the Tey half and the chief owner of the *Good Intent*. A relative of Magnus Isbister. Three families of the Tey bank of Hythe have the same name. |
