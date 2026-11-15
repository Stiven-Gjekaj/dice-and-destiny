"""Make sure that each PDF uses only the expected fonts.

A different font changes the page breaks of the books, but the build does
not stop. This check stops the build when a PDF has a font that is not in
the list.

Usage: python3 check_fonts.py FILE.pdf [FILE.pdf ...]
"""
import re
import subprocess
import sys

# Caladea, Inter, and Liberation Serif set the text of the books.
# DejaVu Sans gives some symbols on the covers, for example the diamond on the spine.
ALLOWED = {"Caladea", "Inter", "LiberationSerif", "DejaVuSans"}


def families(pdf):
    out = subprocess.run(["pdffonts", pdf], capture_output=True, text=True, check=True).stdout
    names = [line.split()[0] for line in out.splitlines()[2:] if line.strip()]
    # Remove the subset prefix (for example "AAAAAA+") and the style (for example "-Bold").
    return {re.sub(r"^[A-Z]{6}\+", "", n).split("-")[0] for n in names}


def main(pdfs):
    bad = 0
    for pdf in pdfs:
        found = families(pdf)
        other = sorted(found - ALLOWED)
        if other:
            bad += 1
            print(f"FONT ERROR: {pdf} uses {', '.join(other)}")
        else:
            print(f"fonts OK: {pdf} ({', '.join(sorted(found))})")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
