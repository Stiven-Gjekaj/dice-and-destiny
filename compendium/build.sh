#!/usr/bin/env bash
# Rebuild both books in three forms. Requires Google Chrome (or Chromium as google-chrome) and poppler-utils (pdftotext).
#   Screen:      color, with links and bookmarks, for reading on a device.
#   Home print:  black and white, with a black and white front page, for a home printer and a binder.
#   Print shop:  the black and white interior, the Lulu A4 casewrap hardcover cover, and an A4 paperback cover.
set -e
cd "$(dirname "$0")"
export PYTHONPATH="$PWD:$PWD/build${PYTHONPATH:+:$PYTHONPATH}"
python3 -m pytest -q
python3 build/check_content.py content
python3 build/build.py player gm
python3 build/check_content.py pages player.pdf gm.pdf
python3 build/build.py --screen player gm
python3 build/cover.py player gm
python3 build/editions.py player gm
rm -rf dist
mkdir -p dist
for book in "player:Player's Compendium" "gm:Game Master's Compendium"; do
  n="${book%%:*}"; title="Dice & Destiny - ${book#*:}"
  cp "${n}_screen_edition.pdf" "dist/${title} - Screen (color).pdf"
  cp "${n}_home_print.pdf" "dist/${title} - Home Print (A4, B&W).pdf"
  cp "${n}.pdf" "dist/${title} - Lulu Interior (A4, B&W).pdf"
  cp "${n}_cover_hardcover.pdf" "dist/${title} - Lulu Hardcover Cover.pdf"
  cp "${n}_cover.pdf" "dist/${title} - Paperback Cover (color, 3 mm bleed).pdf"
done

python3 build/check_fonts.py dist/*.pdf
echo "Done. PDFs are in dist/"
