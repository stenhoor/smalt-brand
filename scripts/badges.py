#!/usr/bin/env python3
"""Generate the "Powered by" badges (style P1 pill) for every smalt product.

Usage: python3 scripts/badges.py <Geist[wght].ttf> <MartianMono[wdth,wght].ttf>

Writes badges/powered-by-smalt{db,ui,bi,df,nb,ql,ts}.svg and -on-dark.svg: 172 x 28 px,
padding 0 10, gap 6, radius 7, 1 px border, 16 px mark, "Powered by" in Geist 400
11 px, wordmark in Martian Mono 600 12.5 px tracking -0.06em. All text is
converted to paths, so the files need no fonts. Requires fonttools.
"""
import sys
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brand_assets import MARKS, MARK_16, COLOURS, mark_paths, GRAIN  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

THEMES = {
    "light": {"surface": "#FFFFFF", "border": "#D6DBE4", "verb": "#3F4656"},
    "dark": {"surface": "#1B1F29", "border": "#2C3240", "verb": "#B9BEC9"},
}
H, PAD, GAP, MARK, BORDER = 28, 10, 6, 16, 1


class Face:
    def __init__(self, path, axes, size, track_em=0.0):
        f = instantiateVariableFont(TTFont(path), axes)
        self.gs, self.cmap = f.getGlyphSet(), f.getBestCmap()
        self.s = size / f["head"].unitsPerEm
        self.cap = f["OS/2"].sCapHeight * self.s
        self.track = track_em * size

    def width(self, text):
        return sum(self.gs[self.cmap[ord(c)]].width * self.s for c in text) + self.track * (len(text) - 1)

    def paths(self, segments, x, baseline):
        out = []
        for colour, text in segments:
            pen = SVGPathPen(self.gs)
            for ch in text:
                g = self.cmap[ord(ch)]
                self.gs[g].draw(TransformPen(pen, (self.s, 0, 0, -self.s, x, baseline)))
                x += self.gs[g].width * self.s + self.track
            out.append(f'<path fill="{colour}" d="{pen.getCommands()}"/>')
        return "".join(out), x


def db_mark(c):
    return (f'<path d="{GRAIN}" fill="{c["body"]}"/>'
            f'<rect x="38" y="8" width="16" height="16" rx="3" fill="{c["chip"]}"/>')


def badge(geist, mono, product, theme):
    t, c = THEMES[theme], COLOURS[theme]
    verb, word = "Powered by", "smalt" + product
    verb_x = BORDER + PAD + MARK + GAP
    word_x = verb_x + geist.width(verb) + GAP
    width = round(word_x + mono.width(word) + PAD + BORDER)
    baseline = H / 2 + geist.cap / 2
    shapes = MARK_16.get(product, MARKS[product])
    mark = db_mark(c) if product == "db" else mark_paths(shapes, c, product)
    verb_svg, _ = geist.paths([(t["verb"], verb)], verb_x, baseline)
    word_svg, _ = mono.paths([(c["ink"], "sm"), (c["alt"], "alt"), (c["suffix"][product], product)], word_x, baseline)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{H}" viewBox="0 0 {width} {H}" '
            f'role="img" aria-label="Powered by smalt{product}">'
            f'<rect x="0.5" y="0.5" width="{width - 1}" height="{H - 1}" rx="6.5" fill="{t["surface"]}" stroke="{t["border"]}"/>'
            f'<g transform="translate({BORDER + PAD} {(H - MARK) / 2}) scale({MARK / 64})">{mark}</g>'
            f"{verb_svg}{word_svg}</svg>\n")


def endorsement(geist, mono, theme):
    """'A smaltworks project': the Together mark, "A", the wordmark, "project"."""
    t, c = THEMES[theme], COLOURS[theme]
    baseline = H / 2 + geist.cap / 2
    a_svg, x = geist.paths([(t["verb"], "A")], BORDER + PAD + MARK + GAP, baseline)
    word_svg, x = mono.paths([(c["ink"], "sm"), (c["alt"], "alt"), (c["suffix"]["works"], "works")], x + GAP * 0.6, baseline)
    p_svg, x = geist.paths([(t["verb"], "project")], x - mono.track + GAP * 0.6, baseline)
    width = round(x + PAD + BORDER)
    mark = mark_paths(MARKS["works"], c, "works")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{H}" viewBox="0 0 {width} {H}" '
            f'role="img" aria-label="A smaltworks project">'
            f'<rect x="0.5" y="0.5" width="{width - 1}" height="{H - 1}" rx="6.5" fill="{t["surface"]}" stroke="{t["border"]}"/>'
            f'<g transform="translate({BORDER + PAD} {(H - MARK) / 2}) scale({MARK / 64})">{mark}</g>'
            f"{a_svg}{word_svg}{p_svg}</svg>\n")


if __name__ == "__main__":
    geist = Face(sys.argv[1], {"wght": 400}, 11)
    mono = Face(sys.argv[2], {"wght": 600, "wdth": 112.5}, 12.5, -0.06)
    out = ROOT / "badges"
    out.mkdir(exist_ok=True)
    for product in ("db", "ui", "bi", "df", "nb", "ql", "ts"):
        for theme, suffix in (("light", ""), ("dark", "-on-dark")):
            path = out / f"powered-by-smalt{product}{suffix}.svg"
            path.write_text(badge(geist, mono, product, theme))
            print(path.relative_to(ROOT))
    for theme, suffix in (("light", ""), ("dark", "-on-dark")):
        path = out / f"a-smaltworks-project{suffix}.svg"
        path.write_text(endorsement(geist, mono, theme))
        print(path.relative_to(ROOT))
