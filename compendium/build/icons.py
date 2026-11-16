"""Hand-drawn inline SVG icons (stroke style, 24x24 viewBox)."""

P = {
 # ---- general ----
 "d20": '<path d="M12 2 21 7v10l-9 5-9-5V7z"/><path d="M12 7 6.5 15.5h11z"/><path d="M12 2v5M3 7l9 0M12 7l9 0M3 7l3.5 8.5M21 7l-3.5 8.5M3 17l3.5-1.5M21 17l-3.5-1.5M6.5 15.5 12 22l5.5-6.5"/>',
 "crown": '<path d="M3 18h18l-1.5-10-4.5 4-3-6-3 6-4.5-4z"/><path d="M4 21h16"/>',
 "quill": '<path d="M20 3c-7 1-12 6-14 14l-2 4"/><path d="M20 3c0 6-4 11-11 12"/><path d="M9 15l-3-3"/>',
 "dice": '<rect x="3" y="3" width="11" height="11" rx="2"/><circle cx="6.5" cy="6.5" r="1"/><circle cx="10.5" cy="10.5" r="1"/><path d="M14 9h5a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-8a2 2 0 0 1-2-2v-5"/><circle cx="17" cy="17" r="1"/>',
 "scales": '<path d="M12 3v18M7 21h10M4 7h16"/><path d="M4 7l-2.5 6a3 3 0 0 0 5 0z"/><path d="M20 7l-2.5 6a3 3 0 0 0 5 0z"/>',
 "swords": '<path d="M3 3h3l10 10-3 3L3 6z"/><path d="M12.3 16.7l4.4-4.4"/><path d="M16.5 16.5l3 3"/><circle cx="20.3" cy="20.3" r="1"/><path d="M21 3h-3L8 13l3 3L21 6z"/><path d="M7.3 12.3l4.4 4.4"/><path d="M7.5 16.5l-3 3"/><circle cx="3.7" cy="20.3" r="1"/>',
 "heart": '<path d="M12 21s-8-5.2-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 5.8-8 11-8 11z"/><path d="M7 11h3l1.5-2.5 2 5 1.5-2.5h2"/>',
 "skull": '<path d="M12 3a8 8 0 0 0-5 14.2V20h10v-2.8A8 8 0 0 0 12 3z"/><circle cx="9" cy="12" r="1.6"/><circle cx="15" cy="12" r="1.6"/><path d="M10 20v-2M14 20v-2M12 15l-1 1.5h2z"/>',
 "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
 "dragon": '<path d="M5 3c2.5 6 2.5 12-.5 18M11 3c2.5 6 2.5 12-.5 18M17 3c2.5 6 2.5 12-.5 18"/>',
 "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5 13.5 13.5 8.5 15.5 10.5 10.5z"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2"/>',
 "chest": '<path d="M3 10a5 5 0 0 1 5-5h8a5 5 0 0 1 5 5v9H3z"/><path d="M3 11h18"/><rect x="10" y="9.5" width="4" height="4" rx="1"/><path d="M7 5v14M17 5v14"/>',
 "scroll": '<path d="M6 4h12v14a3 3 0 0 1-3 3H5a2 2 0 0 1-2-2v-2h3"/><path d="M6 4a2 2 0 0 0-2 2v1h2"/><path d="M18 4a2 2 0 0 1 2 2v1h-2"/><path d="M9 9h6M9 12h6M9 15h4"/>',
 "sheet": '<rect x="4" y="3" width="16" height="18" rx="2"/><circle cx="9" cy="9" r="2.5"/><path d="M14 8h3M14 11h3M7 15h10M7 18h7"/>',
 "eye": '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "hourglass": '<path d="M6 3h12M6 21h12M7 3c0 5 10 5 10 9s-10 4-10 9M17 3c0 5-10 5-10 9s10 4 10 9"/>',
 "spark": '<path d="M12 2v6M12 16v6M2 12h6M16 12h6M5 5l4 4M15 15l4 4M19 5l-4 4M9 15l-4 4"/>',
 "book": '<path d="M4 4h6a3 3 0 0 1 2 1 3 3 0 0 1 2-1h6v15h-6a2 2 0 0 0-2 1 2 2 0 0 0-2-1H4z"/><path d="M12 5v15"/>',
 "up": '<path d="M12 21V5M6 11l6-6 6 6"/><path d="M5 3h14"/>',
 "people": '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.4"/><path d="M3 20c0-3.5 2.7-6 6-6s6 2.5 6 6M15 14c3 0 6 2 6 5"/>',
 "flag": '<path d="M5 21V4M5 4h12l-2 4 2 4H5"/>',
 "tip": '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
 "shield": '<path d="M12 3c3 2 6 2 8 2 0 8-3 13-8 16-5-3-8-8-8-16 2 0 5 0 8-2z"/><path d="M12 6.5v12"/><path d="M5.3 9.5h13.4"/>',
 "warn": '<path d="M12 3 2 20h20z"/><path d="M12 9v5M12 17v.5"/>',
 # ---- classes ----
 "barbarian": '<path d="M12 3v19"/><path d="M12 5.5c-3-2.2-6.3-2-8.5 0 0 3.2 1.2 6 3.3 8 1.3-2 3-3 5.2-3.2z"/><path d="M12 5.5c3-2.2 6.3-2 8.5 0 0 3.2-1.2 6-3.3 8-1.3-2-3-3-5.2-3.2z"/>',
 "bard": '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/><path d="M9 9l12-2"/>',
 "cleric": '<circle cx="12" cy="12" r="3.5"/><path d="M12 2v5M12 17v5M2 12h5M17 12h5M5 5l3 3M16 16l3 3M19 5l-3 3M8 16l-3 3"/>',
 "druid": '<path d="M5 19C5 10 11 4 20 4c0 9-6 15-15 15z"/><path d="M5 19 14 10M10 14h-3M13 11V8"/>',
 "fighter": '<path d="M12 2l2.2 2.8V15h-4.4V4.8z"/><path d="M6.5 15h11"/><path d="M12 15v4.5"/><circle cx="12" cy="21" r="1.3"/>',
 "monk": '<circle cx="12" cy="12" r="9"/><path d="M12 3a4.5 4.5 0 0 0 0 9 4.5 4.5 0 0 1 0 9"/><circle cx="12" cy="7.5" r="1"/><circle cx="12" cy="16.5" r="1"/>',
 "paladin": '<path d="M12 3c3 2 6 2 8 2 0 8-3 13-8 16-5-3-8-8-8-16 2 0 5 0 8-2z"/><path d="M12 7v10M8.5 10.5h7"/>',
 "ranger": '<path d="M7 3c5 3 7.5 6 7.5 9S12 18 7 21"/><path d="M7 3v18"/><path d="M3 12h17.5M17.5 9l3 3-3 3"/><path d="M5 12 3.5 10M5 12l-1.5 2"/>',
 "rogue": '<path d="M2 9.5c3-2.3 7-2.3 10 0 3-2.3 7-2.3 10 0 0 4-2 7-5 7-2 0-3.5-1.2-5-3-1.5 1.8-3 3-5 3-3 0-5-3-5-7z"/><ellipse cx="7.2" cy="11.5" rx="2" ry="1.3"/><ellipse cx="16.8" cy="11.5" rx="2" ry="1.3"/>',
 "sorcerer": '<path d="M12 22c-4 0-7-3-7-7 0-4 3-6 4-10 2 2 2 4 2 6 1-1 2-3 2-5 3 3 6 6 6 9 0 4-3 7-7 7z"/><path d="M12 22c-2 0-3-1.5-3-3.5 0-2 2-3 3-5 1 2 3 3 3 5S14 22 12 22z"/>',
 "warlock": '<path d="M12 2 22 12 12 22 2 12z"/><path d="M5 12s3-4 7-4 7 4 7 4-3 4-7 4-7-4-7-4z"/><circle cx="12" cy="12" r="1.8"/>',
 "wizard": '<ellipse cx="12" cy="19" rx="9.5" ry="2.3"/><path d="M6.8 18.3 10.6 5c.5-1.8 2.4-2.5 3.6-1.3l-1.5 1.2 4.5 13.4"/><path d="M12 10.5l.6 1.3 1.4.2-1 1 .2 1.4-1.2-.7-1.2.7.2-1.4-1-1 1.4-.2z"/>',
}


def icon(name, size=18, color="currentColor", sw=1.6):
    return (f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">'
            f'{P[name]}</svg>')


def big_d20(size=260, stroke="#d6aa55", flat=False):
    """flat=True: no glow, no shadow, and no transparency (for the black and white interior)."""
    """Large shaded d20 for covers: correct icosahedron silhouette, light from top-left."""
    T, UL, UR, LL, LR, B = (50, 3), (91, 26.5), (91, 73.5), (9, 73.5), (9, 26.5), (50, 97)
    UL, UR, LL, LR = (9, 26.5), (91, 26.5), (9, 73.5), (91, 73.5)
    ct, cl, cr = (50, 27), (22, 70), (78, 70)   # central "20" face
    faces = [
        ((T, UL, ct), "#d9564a"), ((T, UR, ct), "#b23a2f"),
        ((UL, ct, cl), "#c4473b"), ((UR, ct, cr), "#8f251c"),
        ((UL, LL, cl), "#a3362b"), ((UR, LR, cr), "#6e1912"),
        ((LL, B, cl), "#7f2017"), ((LR, B, cr), "#5a120c"),
        ((cl, cr, B), "#741c14"), ((ct, cl, cr), "url(#face)"),
    ]
    poly = lambda pts: " ".join(f"{x},{y}" for x, y in pts)
    body = "".join(f'<polygon points="{poly(p)}" fill="{c}" stroke="{stroke}" stroke-width="0.9" stroke-linejoin="round"/>' for p, c in faces)
    if flat:
        # Solid colors only. Lulu warns about transparency in an interior.
        return f'''<svg width="{size}" height="{size}" viewBox="-6 -6 112 116" xmlns="http://www.w3.org/2000/svg">
<defs>
 <linearGradient id="face" x1="0.2" y1="0" x2="0.8" y2="1"><stop offset="0" stop-color="#e2604f"/><stop offset="1" stop-color="#9c2a1f"/></linearGradient>
</defs>{body}
<text x="50" y="59" text-anchor="middle" font-family="Caladea, serif" font-weight="bold" font-size="19" fill="#f8e6c0" stroke="#5a120c" stroke-width=".4">20</text>
<text x="31" y="23" text-anchor="middle" font-family="Caladea, serif" font-weight="bold" font-size="7" fill="#f8e6c0" transform="rotate(-30 31 23)">8</text>
<text x="69" y="23" text-anchor="middle" font-family="Caladea, serif" font-weight="bold" font-size="7" fill="#f8e6c0" transform="rotate(30 69 23)">14</text>
<text x="50" y="84" text-anchor="middle" font-family="Caladea, serif" font-weight="bold" font-size="7" fill="#f8e6c0" transform="rotate(180 50 82)">2</text>
</svg>'''
    return f'''<svg width="{size}" height="{size}" viewBox="-6 -6 112 116" xmlns="http://www.w3.org/2000/svg">
<defs>
 <linearGradient id="face" x1="0.2" y1="0" x2="0.8" y2="1"><stop offset="0" stop-color="#e2604f"/><stop offset="1" stop-color="#9c2a1f"/></linearGradient>
 <radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#d6aa55" stop-opacity=".28"/><stop offset="1" stop-color="#d6aa55" stop-opacity="0"/></radialGradient>
 <filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#000" flood-opacity=".55"/></filter>
</defs>
<circle cx="50" cy="52" r="58" fill="url(#glow)"/>
<polygon points="{poly([(T[0],T[1]+4),(UR[0]+1,UR[1]+4),(LR[0]+1,LR[1]+4),(B[0],B[1]+4),(LL[0]-1,LL[1]+4),(UL[0]-1,UL[1]+4)])}" fill="#000" opacity=".35"/>{body}
<polygon points="{poly((T, UL, ct))}" fill="#fff" opacity=".10"/>

<text x="50" y="59" text-anchor="middle" font-family="Caladea, serif" font-weight="bold" font-size="19" fill="#f8e6c0" stroke="#5a120c" stroke-width=".4">20</text>
<text x="31" y="23" text-anchor="middle" font-family="Caladea, serif" font-weight="bold" font-size="7" fill="#f8e6c0" opacity=".85" transform="rotate(-30 31 23)">8</text>
<text x="69" y="23" text-anchor="middle" font-family="Caladea, serif" font-weight="bold" font-size="7" fill="#f8e6c0" opacity=".7" transform="rotate(30 69 23)">14</text>
<text x="50" y="84" text-anchor="middle" font-family="Caladea, serif" font-weight="bold" font-size="7" fill="#f8e6c0" opacity=".6" transform="rotate(180 50 82)">2</text>
</svg>'''


def divider():
    return ('<svg class="divider" viewBox="0 0 200 12" preserveAspectRatio="none" height="10">'
            '<path d="M0 6h85M115 6h85" stroke="#b8892d" stroke-width="0.8"/>'
            '<path d="M100 1l5 5-5 5-5-5z" fill="#8c1c13" stroke="#b8892d" stroke-width="0.6"/>'
            '<circle cx="89" cy="6" r="1.2" fill="#b8892d"/><circle cx="111" cy="6" r="1.2" fill="#b8892d"/></svg>')
