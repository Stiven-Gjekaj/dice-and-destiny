# The stronghold system (HTML for the GM book)
STRONGHOLDS = """
<p class="chapter-intro">An original system for giving the party a home base that grows with them: a keep, a tavern, a temple or a ship. Use it from level 5 onward, when characters have the gold and reputation to claim land.</p>
<h2>Founding a Stronghold</h2>
<p>A stronghold starts as a <b>Hold</b> (a fortified house, small temple, tavern or ship) costing <b>2,000 GP</b>, or is granted as a story reward. It has three ratings that start at 1:</p>
<table class="compact"><thead><tr><th>Rating</th><th>Measures</th><th>Each level grants</th></tr></thead><tbody>
<tr><td><b>Walls</b></td><td>Defense and safety</td><td>+1 to defense rolls, more guards</td></tr>
<tr><td><b>Coffers</b></td><td>Income and trade</td><td>+50 GP income per month</td></tr>
<tr><td><b>Renown</b></td><td>Reputation and influence</td><td>Followers, favors and rumors</td></tr>
</tbody></table>
<h2>Rooms</h2>
<p>A stronghold has room slots equal to 2 + its total ratings. Each room costs gold and time to build, and gives a benefit:</p>
<table class="compact"><thead><tr><th>Room</th><th>Cost / Time</th><th>Benefit</th></tr></thead><tbody>
<tr><td>Armory</td><td>500 GP / 2 weeks</td><td>Gear the garrison: +1 Walls on defense rolls; craft mundane weapons at half price.</td></tr>
<tr><td>Barracks</td><td>400 GP / 2 weeks</td><td>House 12 guards (Road Wardens). Required for Walls 3+.</td></tr>
<tr><td>Chapel</td><td>600 GP / 3 weeks</td><td>Once per month, a free Revivify or Lesser Restoration; +1 Renown roll.</td></tr>
<tr><td>Forge</td><td>800 GP / 3 weeks</td><td>Craft armor and weapons at half price; craft uncommon magic items in half the time.</td></tr>
<tr><td>Garden</td><td>300 GP / 2 weeks</td><td>Harvest 1d4 Potions of Healing or Healer's Honey per month.</td></tr>
<tr><td>Library</td><td>700 GP / 4 weeks</td><td>Advantage on research checks; copy spells at half cost.</td></tr>
<tr><td>Market Hall</td><td>800 GP / 4 weeks</td><td>+1 Coffers; buy and sell goods at fair price without travel.</td></tr>
<tr><td>Menagerie</td><td>600 GP / 3 weeks</td><td>Raise and train mounts or beasts of CR 2 or lower.</td></tr>
<tr><td>Scriptorium</td><td>500 GP / 3 weeks</td><td>Scribe spell scrolls at half the time and cost.</td></tr>
<tr><td>Spy Network</td><td>1,000 GP / 4 weeks</td><td>Once per month, learn one secret about a person or faction within 50 miles.</td></tr>
<tr><td>Tavern</td><td>400 GP / 2 weeks</td><td>+1 Renown; hear 1d4 rumors per month.</td></tr>
<tr><td>Teleport Circle</td><td>5,000 GP / 8 weeks</td><td>A permanent destination for Teleportation Circle.</td></tr>
<tr><td>Vault</td><td>1,500 GP / 4 weeks</td><td>Treasure stored here can't be stolen except by force; +1 Walls against thieves.</td></tr>
<tr><td>Watchtower</td><td>700 GP / 3 weeks</td><td>See threats coming: never surprised by attacks on the stronghold.</td></tr>
<tr><td>Workshop</td><td>600 GP / 3 weeks</td><td>Craft any tool-based item in half the time.</td></tr>
</tbody></table>
<h2>Upgrading Ratings</h2>
<p>Raising a rating costs <b>1,000 GP × the new level</b> and takes 2 weeks per level. Maximum rating is 5. A stronghold's tier equals its highest rating: <b>Hold</b> (1–2), <b>Keep</b> (3–4), <b>Citadel</b> (5).</p>
<h2>The Monthly Turn</h2>
<p>At the start of each month in the story (or between adventures), the players take a Stronghold Turn:</p>
<ol>
<li><b>Collect income:</b> 50 GP × Coffers, plus room benefits.</li>
<li><b>Pay upkeep:</b> 20 GP × total ratings. If unpaid, lower Renown by 1.</li>
<li><b>Give one order:</b> Build, Recruit (gain a follower), Trade (roll d20 + Coffers; 15+ gains 1d6 × 100 GP), Scout (learn a rumor), or Celebrate (spend 200 GP, +1 to next Renown roll).</li>
<li><b>Roll for an event (d12):</b> see below.</li>
</ol>
<table class="compact"><thead><tr><th class="c">d12</th><th>Stronghold Event</th></tr></thead><tbody>
<tr><td class="c">1</td><td><b>Attack!</b> Bandits or monsters strike. Roll d20 + Walls vs. DC 12 + party level ÷ 2; on a failure lose a room for a month or 1d6 × 100 GP.</td></tr>
<tr><td class="c">2</td><td><b>Fire or flood.</b> Pay 200 GP per room, or one room is out of service for a month.</td></tr>
<tr><td class="c">3</td><td><b>Thief in the walls.</b> Lose 1d4 × 100 GP unless you have a Vault or Spy Network.</td></tr>
<tr><td class="c">4</td><td><b>Petitioner.</b> A local asks for help: an adventure hook.</td></tr>
<tr><td class="c">5–6</td><td><b>Quiet month.</b> Nothing unusual.</td></tr>
<tr><td class="c">7</td><td><b>Traveling merchant.</b> Buy one uncommon magic item at list price.</td></tr>
<tr><td class="c">8</td><td><b>Good harvest.</b> Gain 1d4 × 100 GP.</td></tr>
<tr><td class="c">9</td><td><b>Visiting noble.</b> Roll d20 + Renown; on 15+, gain a favor.</td></tr>
<tr><td class="c">10</td><td><b>New follower.</b> A skilled hireling asks to join.</td></tr>
<tr><td class="c">11</td><td><b>Rival.</b> A rival faction makes a move; a story hook.</td></tr>
<tr><td class="c">12</td><td><b>Fame.</b> +1 Renown (max 5).</td></tr>
</tbody></table>
<h2>Followers</h2>
<p>A stronghold attracts followers equal to its Renown × 2: guards, servants, a steward and specialists. A <b>steward</b> runs the stronghold while the party adventures; without one, skip the order each month.</p>
<div class="box"><h4>Writer's tip</h4><p>The stronghold is a story engine. Name the steward, give the tavern a regular, and let events turn into adventures. A rival burning down the Garden is a better hook than any quest board.</p></div>
"""
