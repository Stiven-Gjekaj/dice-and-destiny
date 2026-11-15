#!/usr/bin/env bash
# Rebuild both books and their covers. Requires Google Chrome (or Chromium as google-chrome) and poppler-utils (pdftotext).
set -e
cd "$(dirname "$0")"
python3 build.py player gm
python3 cover.py player gm
mkdir -p dist
cp player.pdf "dist/Player's Compendium - Interior (A4, B&W).pdf"
cp gm.pdf "dist/Game Master's Compendium - Interior (A4, B&W).pdf"
cp player_cover.pdf "dist/Player's Compendium - Cover (color, with bleed).pdf"
cp gm_cover.pdf "dist/Game Master's Compendium - Cover (color, with bleed).pdf"
echo "Done. PDFs are in dist/"
