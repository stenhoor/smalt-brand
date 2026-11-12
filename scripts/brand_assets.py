#!/usr/bin/env python3
"""Generate the smalt family's logo files.

Usage: python3 scripts/brand_assets.py <MartianMono[wdth,wght].ttf>

For every product (smaltdb, smaltui, smaltbi, smaltdf, smaltnb, smaltfl, smaltql, smaltts, smaltty, and the parent, smaltworks) writes, under logos/<product>/:
  wordmark.svg, wordmark-on-dark.svg, lockup.svg, lockup-on-dark.svg
For smaltui, smaltbi, smaltdf, smaltnb, smaltfl, smaltql, smaltts, smaltty and smaltworks it also writes the mark, app icon and favicons:
  <mark>-mark.svg, <mark>-mark-on-dark.svg, app-icon.svg, favicon-32.svg, favicon-16.svg
(smaltdb's mark, app icon and favicons were drawn by hand and are left untouched.)

The wordmark is Martian Mono 600 at width 112.5, tracking -0.06em, converted to
paths: "alt" in smalt, the product suffix in the product's text colour.
Requires fonttools (pip install fonttools).
"""
import math
import sys
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = Path(__file__).resolve().parent.parent


def rr(x, y, w, h, r):
    """Rounded rectangle as path data."""
    def n(v):
        return f"{v:g}"
    return (f"M{n(x + r)} {n(y)}h{n(w - 2 * r)}a{n(r)} {n(r)} 0 0 1 {n(r)} {n(r)}v{n(h - 2 * r)}"
            f"a{n(r)} {n(r)} 0 0 1 -{n(r)} {n(r)}h-{n(w - 2 * r)}a{n(r)} {n(r)} 0 0 1 -{n(r)} -{n(r)}"
            f"v-{n(h - 2 * r)}a{n(r)} {n(r)} 0 0 1 {n(r)} -{n(r)}z")


def _poly(points):
    return "M" + "L".join(f"{round(x, 2):g} {round(y, 2):g}" for x, y in points) + "Z"


def _folds(pts):
    """True if any two non-adjacent edges of the closed polygon intersect."""
    def o(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    n = len(pts)
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        for j in range(i + 2, n):
            if i == 0 and j == n - 1:
                continue
            c, d = pts[j], pts[(j + 1) % n]
            if o(a, b, c) * o(a, b, d) < 0 and o(c, d, a) * o(c, d, b) < 0:
                return True
    return False


def band(centre, t):
    """A solid band of thickness t around a dense centreline, its ends cut square. Refuses an outline that folds."""
    left, right = [], []
    for i, (x, y) in enumerate(centre):
        a, b = centre[max(i - 1, 0)], centre[min(i + 1, len(centre) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        d = math.hypot(dx, dy)
        nx, ny = -dy / d, dx / d
        left.append((x + nx * t / 2, y + ny * t / 2))
        right.append((x - nx * t / 2, y - ny * t / 2))
    pts = left + right[::-1]
    if _folds(pts):
        raise ValueError("band folds over itself: lower the amplitude or the thickness")
    return _poly(pts)


def sine(x0, x1, cy, amp, wavelength, n=72):
    """Centreline of a sine wave, in phase with every other wave of the same wavelength that starts at x0."""
    return [(x0 + (x1 - x0) * i / n, cy - amp * math.sin(2 * math.pi * ((x1 - x0) * i / n) / wavelength))
            for i in range(n + 1)]


GRAIN = "M14 18h18v10h14v24a6 6 0 0 1-6 6H14a6 6 0 0 1-6-6V24a6 6 0 0 1 6-6z"

# Marks on a 64-unit grid: (path, role). Roles map to colours per theme below.
MARKS = {
    "db": [(GRAIN, "body"), (rr(38, 8, 16, 16, 3), "chip")],
    "ui": [("M8 17L15 10L37 32L15 54L8 47L23 32Z", "body"), (rr(38, 46, 20, 8, 3), "accent")],
    "bi": [(rr(8, 44, 10, 10, 3), "chip"), (rr(22, 42, 7, 7, 2), "chip"), (rr(24, 28, 12, 12, 3), "body"),
           (rr(40, 30, 7, 7, 2), "chip"), (rr(46, 8, 12, 12, 3), "accent")],
    "df": [("M8 8H56V17H17V56H8Z", "body"), (rr(27, 27, 14, 14, 3), "accent")],
    # smaltnb's pencil: a 45-degree body and cap, and a right-angled point set apart by a gap.
    "nb": [("M12 52 L19.78 52 L12 44.22Z", "accent"), ("M21.55 50.23 L47 24.78 L39.22 17 L13.77 42.45Z", "body"),
           ("M49.12 22.66 L54.07 17.71 L46.29 9.93 L41.34 14.88Z", "body")],
    # smaltfl's Twin: two waves in step, the old sign for water, and the chip where they arrive (smaltfl's round 3, M13).
    # Curved: an exception to the 0/45/90-degree rule, as smaltql's Star is one.
    "fl": [(band(sine(8, 44, 24, 5, 36), 7), "body"), (band(sine(8, 44, 40, 5, 36), 7), "body"),
           (rr(49, 27, 7, 10, 3), "accent")],
    # smaltql's star: the * of SELECT *, six separate arms 60 degrees apart around the chip.
    # The family's one exception to the 0/45/90-degree rule: a * needs evenly spaced arms.
    "ql": [("M27.5 21.5L27.5 5L36.5 5L36.5 21.5Z", "body"), ("M38.84 22.85L53.13 14.6L57.63 22.4L43.34 30.65Z", "body"),
           ("M43.34 33.35L57.63 41.6L53.13 49.4L38.84 41.15Z", "body"), ("M36.5 42.5L36.5 59L27.5 59L27.5 42.5Z", "body"),
           ("M25.16 41.15L10.87 49.4L6.37 41.6L20.66 33.35Z", "body"), ("M20.66 30.65L6.37 22.4L10.87 14.6L25.16 22.85Z", "body"),
           (rr(25.5, 25.5, 13, 13, 3), "accent")],
    # smaltts' Generic: the <T> of a TypeScript generic, two 45-degree angles with the type as the chip.
    "ts": [("M4 32L18 18L25 25L18 32L25 39L18 46Z", "body"), ("M60 32L46 18L39 25L46 32L39 39L46 46Z", "body"),
           (rr(28, 25, 8, 14, 3), "accent")],
    # smaltty's Tree: the syntax tree it builds, TypeScript's node for node. Two branches from one stem, and the root,
    # where the parse starts, as the chip. Bars 9 units thick, 0 and 90 degrees only. A first version (2026-11-12),
    # drawn to the mark rules without an options round: for the owner's review.
    # smaltty's Grain, turned: smaltdb's Grain rotated half a turn, the notch and the chip at the bottom left, the chip
    # in kiln (owner, 2026-11-12).
    "ty": [("M50 46h-18v-10h-14v-24a6 6 0 0 1 6-6h26a6 6 0 0 1 6 6v28a6 6 0 0 1-6 6z", "body"), (rr(10, 40, 16, 16, 3), "accent")],
    # smaltworks' Together: two L-shaped pieces that lock into one frame.
    "works": [("M8 8H44V18H18V44H8Z", "body"), ("M56 56H20V46H46V20H56Z", "accent")],
}
# smaltbi's 16 px mark: three larger grains, because the full scatter breaks into specks.
MARK_16 = {"bi": [(rr(6, 40, 16, 16, 4), "chip"), (rr(22, 22, 20, 20, 5), "body"), (rr(44, 4, 16, 16, 4), "accent")]}
# Horizontal extent of each mark's artwork on the 64 grid, used to space the lockup.
ART_X = {"db": (8, 54), "ui": (8, 58), "bi": (8, 58), "df": (8, 56), "nb": (10, 54), "fl": (5.7, 56), "ql": (6.37, 57.63), "ts": (4, 60), "ty": (10, 56), "works": (8, 56)}
MARK_NAME = {"ui": "chevron", "bi": "scatter", "df": "axes", "nb": "pencil", "fl": "twin", "ql": "star", "ts": "generic", "ty": "grain", "works": "together"}

# Colour by layer: each layer of the stack has one colour, and a product takes its layer's colour.
# (fill, text, dark) per layer. The engine layer (smaltdb) uses smalt itself: the pale chip and an ink suffix.
LAYER_COLOURS = {
    "language": ("#B0249F", "#981C89", "#F57FE6"),   # magenta: smaltql, smaltdf, smaltts
    "kit": ("#0A7C76", "#086A65", "#10C2B9"),        # jade: smaltml
    # smaltty is in no layer: TypeScript is the language of everything smalt, so it takes the family's kiln
    # (owner, 2026-11-12): kiln-500 as the fill, the accent token as text.
    "family": ("#E5622F", "#A33A12", "#FF8A5C"),     # kiln: smaltty
    "tool": ("#0E7FAE", "#0B6A91", "#5CBDE8"),       # cerulean: smaltui, smaltbi, smaltnb, smaltfl
    "ai": ("#6E4BC2", "#6141AE", "#B8A1F2"),         # violet: smaltai, alongside the layers
}
LAYER = {"ql": "language", "df": "language", "ts": "language", "ty": "family", "ui": "tool", "bi": "tool", "nb": "tool", "fl": "tool"}
# smaltworks is not a layer: it keeps kiln orange.
WORKS = ("#E5622F", "#151922", "#FF8A5C")


def _layer(product, i):
    return (WORKS if product == "works" else LAYER_COLOURS[LAYER[product]])[i]


COLOURED = [*LAYER, "works"]
COLOURS = {
    "light": {"ink": "#151922", "alt": "#003399", "body": "#003399", "chip": "#7B97D4",
              "accent": {p: _layer(p, 0) for p in COLOURED},
              "suffix": {"db": "#151922", **{p: _layer(p, 1) for p in LAYER}, "works": "#151922"}},
    "dark": {"ink": "#E9EBF0", "alt": "#9DB4F5", "body": "#9DB4F5", "chip": "#D6E0F3",
             "accent": {p: _layer(p, 2) for p in COLOURED},
             "suffix": {"db": "#E9EBF0", **{p: _layer(p, 2) for p in LAYER}, "works": "#E9EBF0"}},
    # App icon: the mark knocked out of a smalt tile.
    "tile": {"body": "#F5F6F8", "chip": "#9DB4F5", "accent": {p: _layer(p, 2) for p in COLOURED}},
}


def fill(role, palette, product):
    v = palette[role]
    return v[product] if isinstance(v, dict) else v


def mark_paths(shapes, palette, product):
    return "".join(f'<path d="{d}" fill="{fill(role, palette, product)}"/>' for d, role in shapes)


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    print(path.relative_to(ROOT))


def build_marks(product):
    out = ROOT / "logos" / f"smalt{product}"
    name = MARK_NAME[product]
    label = f"smalt{product}"
    for theme, suffix in (("light", ""), ("dark", "-on-dark")):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="{label}">'
               + mark_paths(MARKS[product], COLOURS[theme], product) + "</svg>\n")
        write(out / f"{name}-mark{suffix}.svg", svg)
    tile = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="{label} app icon">'
            '<rect width="64" height="64" rx="15" fill="#003399"/><g transform="translate(10.9 10.9) scale(0.66)">'
            + mark_paths(MARKS[product], COLOURS["tile"], product) + "</g></svg>\n")
    write(out / "app-icon.svg", tile)
    for size, shapes in ((32, MARKS[product]), (16, MARK_16.get(product, MARKS[product]))):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="{size}" height="{size}">'
               + mark_paths(shapes, COLOURS["light"], product) + "</svg>\n")
        write(out / f"favicon-{size}.svg", svg)


def build_wordmarks(font_path, product):
    f = instantiateVariableFont(TTFont(font_path), {"wght": 600, "wdth": 112.5})
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    upm = f["head"].unitsPerEm
    cap = f["OS/2"].sCapHeight
    size = 100.0
    s = size / upm
    track = -0.06 * size
    base = 200.0
    cap_h = cap * s

    def word(x0):
        parts, x, bp = [], x0, BoundsPen(gs)
        for seg, text in (("ink", "sm"), ("alt", "alt"), ("suffix", product)):
            sp = SVGPathPen(gs)
            for ch in text:
                g = cmap[ord(ch)]
                t = (s, 0, 0, -s, x, base)
                gs[g].draw(TransformPen(sp, t))
                gs[g].draw(TransformPen(bp, t))
                x += gs[g].width * s + track
            parts.append((seg, sp.getCommands()))
        return parts, bp.bounds

    out = ROOT / "logos" / f"smalt{product}"
    left_art, right_art = ART_X[product]
    for lockup in (False, True):
        mark_h = 1.6 * cap_h if lockup else 0
        mark_w = mark_h
        _, (bx, _, _, _) = word(0)
        art_r = right_art / 64 * mark_w
        art_w = (right_art - left_art) / 64 * mark_w
        x0 = art_r + (art_w / 2 if lockup else 0) - bx
        parts, (xmin, ymin, xmax, ymax) = word(x0)
        my = base - cap_h + cap_h / 2 - mark_h / 2
        top, bot = min(ymin, my), max(ymax, my + mark_h)
        left = left_art / 64 * mark_w if lockup else xmin
        pad = 0.12 * size
        vx, vy, vw, vh = left - pad, top - pad, (xmax - left) + 2 * pad, (bot - top) + 2 * pad
        for theme, suffix in (("light", ""), ("dark", "-on-dark")):
            c = COLOURS[theme]
            seg_colour = {"ink": c["ink"], "alt": c["alt"], "suffix": c["suffix"][product]}
            svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx:.2f} {vy:.2f} {vw:.2f} {vh:.2f}" '
                   f'width="{vw * 1.6:.0f}" height="{vh * 1.6:.0f}" role="img" aria-label="smalt{product}">']
            if lockup:
                if product == "db":  # keep smaltdb's original Grain markup, so its files stay byte-identical
                    inner = (f'<path d="{GRAIN}" fill="{c["body"]}"/>'
                             f'<rect x="38" y="8" width="16" height="16" rx="3" fill="{c["chip"]}"/>')
                else:
                    inner = mark_paths(MARKS[product], c, product)
                svg.append(f'<g transform="translate(0 {my:.2f}) scale({mark_h / 64:.4f})">' + inner + "</g>")
            for seg, d in parts:
                svg.append(f'<path fill="{seg_colour[seg]}" d="{d}"/>')
            svg.append("</svg>")
            write(out / f"{'lockup' if lockup else 'wordmark'}{suffix}.svg", "".join(svg))


if __name__ == "__main__":
    font = sys.argv[1]
    for p in ("ui", "bi", "df", "nb", "fl", "ql", "ts", "ty", "works"):
        build_marks(p)
    for p in ("db", "ui", "bi", "df", "nb", "fl", "ql", "ts", "ty", "works"):
        build_wordmarks(font, p)
