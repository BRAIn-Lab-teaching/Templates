"""Flag slides whose content runs off the frame.

Beamer never warns when a tcolorbox inside a column overflows the bottom of a
frame — the content is simply cut by the page edge, the log stays clean and
latexmk exits 0. Detect it by rasterising each page, stripping the theme's own
chrome (full-width bands such as a frametitle bar or a progress bar) and
measuring how much clear space is left under the content.

Works on any background colour: the page background is read from the corners,
not assumed white.

Run:  .venv/bin/python check_overflow.py [file.pdf]
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pymupdf
from PIL import Image

DPI = 150
BAND_FRAC = 0.85       # a row this full of ink is theme chrome, not content
INK_TOL = 26           # channel distance from the background that counts as ink
CUT_PT = 2.0           # content this close to the body edge is being cut
TIGHT_PT = 6.0         # content this close is uncomfortably tight


def _ink_mask(arr: np.ndarray) -> np.ndarray:
    """Pixels that differ from the page background colour."""
    corners = np.stack([arr[0, 0], arr[0, -1], arr[-1, 0], arr[-1, -1]])
    bg = np.median(corners, axis=0)
    return np.abs(arr - bg).max(axis=2) > INK_TOL


def page_report(page: pymupdf.Page) -> tuple[float, str]:
    """Return (clear space under the content in pt, flag)."""
    pix = page.get_pixmap(dpi=DPI)
    arr = np.asarray(Image.frombytes("RGB", (pix.width, pix.height), pix.samples)).astype(int)
    arr = arr[2:-2, 2:-2]          # the canvas edge itself is not content
    ink = _ink_mask(arr)
    row_frac = ink.mean(axis=1)
    h = arr.shape[0]
    sy = page.rect.height / pix.height
    sx = page.rect.width / pix.width

    band = row_frac > BAND_FRAC          # frametitle bar, progress bar, rules
    content = ink.copy()
    content[band] = False                 # chrome must not count as content

    # the frame body ends where the last trailing chrome band starts
    bottom = h - 1
    while bottom > 0 and band[bottom]:
        bottom -= 1

    rows = np.where(content[:bottom + 1].any(axis=1))[0]
    if rows.size == 0:
        return page.rect.height, ""
    gap = (bottom - rows[-1]) * sy

    cols = np.where(content.any(axis=0))[0]
    side = min(cols[0] * sx, (arr.shape[1] - 1 - cols[-1]) * sx)
    side_flag = f"; WIDE (side gap {side:.1f}pt)" if side < CUT_PT else ""

    if gap < CUT_PT:
        return gap, "CUT" + side_flag
    if gap < TIGHT_PT:
        return gap, "tight" + side_flag
    return gap, side_flag.lstrip("; ")


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "ouroboros-talk.pdf")
    doc = pymupdf.open(path)
    bad = []
    for i, page in enumerate(doc, start=1):
        gap, flag = page_report(page)
        if flag:
            bad.append((i, flag, gap))
        print(f"p{i:02d}  clear below content: {gap:6.1f}pt   {flag}")
    print()
    if bad:
        print("PROBLEM PAGES: " + ", ".join(f"p{i} {f} ({g:.1f}pt)" for i, f, g in bad))
        return 1
    print("all pages fit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
