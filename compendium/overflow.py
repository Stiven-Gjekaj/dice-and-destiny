import sys
from playwright.sync_api import sync_playwright
f = sys.argv[1]
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 650, "height": 1000})
    pg.goto(f"file://{__import__("os").path.abspath(f)}")
    pg.emulate_media(media="print")
    res = pg.evaluate("""() => {
      const out = [];
      document.querySelectorAll('td, th, .stat, .traits, .traits div, .box, .card, .example, .tag, caption, .abil-card, .class-banner').forEach(el => {
        if (el.scrollWidth > el.clientWidth + 1 || (getComputedStyle(el).height !== 'auto' && el.scrollHeight > el.clientHeight + 2 && el.classList.contains('stat')))
          out.push([el.tagName, el.className, el.scrollWidth, el.clientWidth, el.textContent.trim().slice(0, 60)]);
      });
      // any element whose box sticks out of its parent's box
      document.querySelectorAll('.stat *, .ab *, .ab, .traits *, td *, th *, .card *, .tag, .ch-badge, .crest, .lv').forEach(el => {
        const r = el.getBoundingClientRect(), pr = el.parentElement.getBoundingClientRect();
        if (r.width && (r.left < pr.left - 0.5 || r.right > pr.right + 0.5))
          out.push(['CHILD', el.className || el.tagName, Math.round(r.right - pr.right), Math.round(pr.width), el.textContent.trim().slice(0, 40)]);
        if (el.scrollWidth > el.clientWidth + 1 && el.clientWidth)
          out.push(['SCROLL', el.className || el.tagName, el.scrollWidth, el.clientWidth, el.textContent.trim().slice(0, 40)]);
      });
      // tables wider than their container
      document.querySelectorAll('table').forEach(t => {
        const pw = t.parentElement.clientWidth;
        if (t.offsetWidth > pw + 1) out.push(['TABLE', 'wider-than-parent', t.offsetWidth, pw, t.textContent.trim().slice(0, 60)]);
      });
      return out;
    }""")
    for r in res: print(r)
    print("issues:", len(res))
    b.close()
