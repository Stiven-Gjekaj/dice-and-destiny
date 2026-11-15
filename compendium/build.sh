#!/usr/bin/env bash
# Rebuild both books and their covers. Requires Google Chrome (or Chromium as google-chrome) and poppler-utils (pdftotext).
set -e
cd "$(dirname "$0")"
export PYTHONPATH="$PWD:$PWD/build${PYTHONPATH:+:$PYTHONPATH}"
python3 build/check_content.py content
python3 build/build.py player gm
python3 build/check_content.py pages player.pdf gm.pdf
python3 build/cover.py player gm
mkdir -p dist
cp player.pdf "dist/Dice & Destiny - Player's Compendium - Interior (A4, B&W).pdf"
cp gm.pdf "dist/Dice & Destiny - Game Master's Compendium - Interior (A4, B&W).pdf"
cp player_cover.pdf "dist/Dice & Destiny - Player's Compendium - Cover (color, with bleed).pdf"
cp gm_cover.pdf "dist/Dice & Destiny - Game Master's Compendium - Cover (color, with bleed).pdf"
echo "Done. PDFs are in dist/"
