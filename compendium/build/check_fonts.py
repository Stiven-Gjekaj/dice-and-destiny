"""Make sure that each PDF uses only the expected fonts, and no Type 3 fonts.

A different font changes the page breaks of the books, but the build does
not stop. A Type 3 font makes printers such as Lulu give a warning. This
check stops the build in both cases.

Usage: python3 check_fonts.py FILE.pdf [FILE.pdf ...]
"""
import re
import subprocess
import sys

# Caladea, Inter, and Liberation Serif set the text of the books.
# DejaVu Sans gives some symbols on the covers, for example the diamond on the spine.
ALLOWED = {"Caladea", "Inter", "LiberationSerif", "DejaVuSans"}


def fonts(pdffonts_text):
    """Return (family, type) for each font in the output of pdffonts."""
    out = []
    for line in pdffonts_text.splitlines()[2:]:
        if not line.strip():
            continue
        name = line.split()[0]
        kind = line[37:54].strip()
        # Remove the subset prefix (for example "AAAAAA+") and the style (for example "-Bold").
        out.append((re.sub(r"^[A-Z]{6}\+", "", name).split("-")[0], kind))
    return out


def problems(pdffonts_text):
    errors = []
    for family, kind in fonts(pdffonts_text):
        if family not in ALLOWED:
            errors.append(f"uses {family}")
        elif kind == "Type 3":
            errors.append(f"has {family} as a Type 3 font")
    return sorted(set(errors))


def main(pdfs):
    bad = 0
    for pdf in pdfs:
        text = subprocess.run(["pdffonts", pdf], capture_output=True, text=True, check=True).stdout
        errs = problems(text)
        if errs:
            bad += 1
            print(f"FONT ERROR: {pdf} {'; '.join(errs)}")
        else:
            print(f"fonts OK: {pdf} ({', '.join(sorted({f for f, _ in fonts(text)}))})")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
