"""Turns compact monster specs into balanced 2024-style stat blocks.
Targets per CR are based on typical published monsters (AC, HP, attack bonus, damage per round, save DC)."""
import re, html

TARGET = {  # cr: (ac, hp, prof)
 0: (12, 4, 2), 0.125: (12, 9, 2), 0.25: (13, 13, 2), 0.5: (13, 22, 2), 1: (13, 30, 2), 2: (13, 45, 2),
 3: (14, 60, 2), 4: (14, 75, 2), 5: (15, 95, 3), 6: (15, 110, 3), 7: (15, 125, 3), 8: (16, 140, 3),
 9: (16, 155, 4), 10: (17, 170, 4), 11: (17, 185, 4), 12: (17, 200, 4), 13: (18, 215, 5), 14: (18, 230, 5),
 15: (18, 245, 5), 16: (18, 260, 5), 17: (19, 290, 6), 18: (19, 310, 6), 19: (19, 330, 6), 20: (19, 360, 6),
 21: (20, 400, 7), 22: (21, 430, 7), 23: (21, 460, 7), 24: (21, 500, 7),
}
XP = {0: 10, 0.125: 25, 0.25: 50, 0.5: 100, 1: 200, 2: 450, 3: 700, 4: 1100, 5: 1800, 6: 2300, 7: 2900, 8: 3900,
      9: 5000, 10: 5900, 11: 7200, 12: 8400, 13: 10000, 14: 11500, 15: 13000, 16: 15000, 17: 18000, 18: 20000,
      19: 22000, 20: 25000, 21: 33000, 22: 41000, 23: 50000, 24: 62000}
DIE = {"T": 4, "S": 6, "M": 8, "L": 10, "H": 12, "G": 20}
SIZE = {"T": "Tiny", "S": "Small", "M": "Medium", "L": "Large", "H": "Huge", "G": "Gargantuan"}
AB = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
AKEY = {"str": 0, "dex": 1, "con": 2, "int": 3, "wis": 4, "cha": 5}


def mod(s): return (s - 10) // 2
def sg(n): return f"+{n}" if n >= 0 else f"−{abs(n)}"
def crs(cr): return {0.125: "1/8", 0.25: "1/4", 0.5: "1/2"}.get(cr, str(int(cr)))


def avg(expr, bonus=0):
    tot, parts = 0, re.findall(r"(\d+)d(\d+)", expr)
    for n, d in parts:
        tot += int(n) * (int(d) + 1) / 2
    # Remove the dice first, so that a bonus such as "+3" after "1d8" is counted.
    flat = sum(int(x.replace(" ", "")) for x in re.findall(r"[+-]\s*\d+", re.sub(r"\d+d\d+", "", expr)))
    return int(tot + flat + bonus)


class M:
    def __init__(self, name, size, typ, align, cr, abil, ac=None, speed="30 ft.", senses="", lang="–", res="",
                 skills="", saves="", traits=(), attacks=(), multi=1, actions=(), bonus=(), react=(), leg=(),
                 hp=1.0, desc=""):
        self.__dict__.update(locals()); del self.__dict__["self"]
        self.sc = [int(x) for x in abil.split()]

    def ref(self):
        """Give the name in lower case for use after "the". Remove a first "The " so that it does not show two times."""
        name = self.name.lower()
        return name[4:] if name.startswith("the ") else name

    def stats(self):
        tac, thp, pb = TARGET[self.cr]
        ac = self.ac or tac
        die, con = DIE[self.size], mod(self.sc[2])
        target = thp * self.hp
        n = max(1, round(target / (die / 2 + 0.5 + con)))
        hp = max(1, int(n * (die / 2 + 0.5) + n * con))
        hpd = f"{n}d{die}" + (f" {'+' if con >= 0 else '−'} {abs(n * con)}" if con else "")
        return ac, hp, hpd, pb

    def fmt(self, text):
        _, _, _, pb = self.stats()
        text = re.sub(r"\{dc:(\w+)\}", lambda m: f"DC {8 + pb + mod(self.sc[AKEY[m.group(1)]])}", text)
        text = re.sub(r"\{atk:(\w+)\}", lambda m: sg(pb + mod(self.sc[AKEY[m.group(1)]])), text)
        text = re.sub(r"\{(\d+d\d+(?:\s*[+-]\s*\d+)?)\}", lambda m: f"{avg(m.group(1).replace(' ', ''))} ({m.group(1)})", text)
        return html.escape(text).replace("&lt;i&gt;", "<i>").replace("&lt;/i&gt;", "</i>")

    def attack_line(self, a):
        name, kind, dice, dtype = a[:4]
        extra = a[4] if len(a) > 4 else ""
        reach = a[5] if len(a) > 5 else None
        _, _, _, pb = self.stats()
        s, d = mod(self.sc[0]), mod(self.sc[1])
        reach = (reach or "").rstrip(".")
        if kind == "m": m, lab, rng = s, "Melee Attack Roll", f"reach {reach or '5 ft'}"
        elif kind == "f": m, lab, rng = max(s, d), "Melee Attack Roll", f"reach {reach or '5 ft'}"
        elif kind == "r": m, lab, rng = d, "Ranged Attack Roll", f"range {reach or '80/320 ft'}"
        else:  # spell attack by casting ability e.g. "s:cha"
            m, lab, rng = mod(self.sc[AKEY[kind.split(':')[1]]]), "Ranged Attack Roll", f"range {reach or '120 ft'}"
        dmg_bonus = 0 if kind.startswith("s") else m
        dm = f"{avg(dice, dmg_bonus)} ({dice}{' ' + ('+' if dmg_bonus >= 0 else '−') + ' ' + str(abs(dmg_bonus)) if dmg_bonus else ''})"
        txt = f"<i>{lab}:</i> {sg(pb + m)}, {rng}. <i>Hit:</i> {dm} {dtype} damage"
        if extra:
            txt += (" " if extra[0].islower() else ". ") + self.fmt(extra)
        if not txt.endswith("."):
            txt += "."
        if not txt.endswith("."):
            txt += "."
        return f"<p><b><i>{html.escape(name)}.</i></b> {txt}</p>"

    def html(self):
        ac, hp, hpd, pb = self.stats()
        init = mod(self.sc[1])
        rows = ""
        save_profs = [x.strip().lower() for x in self.saves.split(",") if x.strip()]
        for i, a in enumerate(AB):
            sv = mod(self.sc[i]) + (pb if a.lower() in save_profs else 0)
            rows += f"<td><b>{a}</b></td><td>{self.sc[i]}</td><td>{sg(mod(self.sc[i]))}</td><td>{sg(sv)}</td>"
        cut = rows.index("<td><b>Int")
        ab = ('<table class="mon-ab"><thead><tr>' + "<th></th><th></th><th>Mod</th><th>Save</th>" * 3
              + f"</tr></thead><tbody><tr>{rows[:cut]}</tr><tr>{rows[cut:]}</tr></tbody></table>")
        pp = 10 + mod(self.sc[4]) + (pb if "Perception" in self.skills else 0) + (pb if "Perception+" in self.skills else 0)
        lines = []
        if self.skills:
            sk = []
            for x in self.skills.replace("+", "").split(","):
                x = x.strip(); expert = x.endswith("*"); x = x.rstrip("*")
                abil = {"Athletics": 0, "Acrobatics": 1, "Stealth": 1, "Sleight of Hand": 1, "Arcana": 3, "History": 3,
                        "Investigation": 3, "Nature": 3, "Religion": 3, "Perception": 4, "Insight": 4, "Survival": 4,
                        "Medicine": 4, "Animal Handling": 4, "Deception": 5, "Intimidation": 5, "Persuasion": 5, "Performance": 5}[x]
                sk.append(f"{x} {sg(mod(self.sc[abil]) + pb * (2 if expert else 1))}")
            lines.append("<b>Skills</b> " + ", ".join(sk))
        if self.res: lines.append(self.res)
        lines.append("<b>Senses</b> " + (self.senses + ", " if self.senses else "") + f"Passive Perception {pp}")
        lines.append("<b>Languages</b> " + html.escape(self.lang))
        lines.append(f"<b>CR</b> {crs(self.cr)} (XP {XP[self.cr]:,}; PB {sg(pb)})")
        body = ""
        if self.traits:
            body += '<div class="mon-sec">Traits</div>' + "".join(f"<p><b><i>{html.escape(n)}.</i></b> {self.fmt(t)}</p>" for n, t in self.traits)
        body += '<div class="mon-sec">Actions</div>'
        if self.multi > 1:
            names = sorted({a[0] for a in self.attacks})
            body += f"<p><b><i>Multiattack.</i></b> The {html.escape(self.ref())} makes {['', 'one', 'two', 'three', 'four', 'five'][self.multi]} attacks{', using ' + ' or '.join(names) + ' in any combination' if len(names) > 1 else ''}.</p>"
        body += "".join(self.attack_line(a) for a in self.attacks)
        body += "".join(f"<p><b><i>{html.escape(n)}.</i></b> {self.fmt(t)}</p>" for n, t in self.actions)
        if self.bonus:
            body += '<div class="mon-sec">Bonus Actions</div>' + "".join(f"<p><b><i>{html.escape(n)}.</i></b> {self.fmt(t)}</p>" for n, t in self.bonus)
        if self.react:
            body += '<div class="mon-sec">Reactions</div>' + "".join(f"<p><b><i>{html.escape(n)}.</i></b> {self.fmt(t)}</p>" for n, t in self.react)
        if self.leg:
            body += ('<div class="mon-sec">Legendary Actions</div>'
                     f"<p class='small'><i>Legendary Action Uses: 3. Immediately after another creature's turn, the {html.escape(self.ref())} can expend a use to take one of the following actions. It regains all expended uses at the start of each of its turns.</i></p>"
                     + "".join(f"<p><b><i>{html.escape(n)}.</i></b> {self.fmt(t)}</p>" for n, t in self.leg))
        desc = f'<p class="mon-desc"><i>{html.escape(self.desc)}</i></p>' if self.desc else ""
        return (f'<div class="monster"><h4 class="mon-name">{html.escape(self.name)}</h4>'
                f'<div class="mon-type"><i>{SIZE[self.size]} {self.typ}, {self.align}</i></div>{desc}'
                f'<div class="mon-top"><b>AC</b> {ac} &nbsp; <b>Initiative</b> {sg(init)} ({10 + init})<br><b>HP</b> {hp} ({hpd})<br><b>Speed</b> {self.speed}</div>'
                f'{ab}<div class="mon-lines">{"<br>".join(lines)}</div>{body}</div>')
