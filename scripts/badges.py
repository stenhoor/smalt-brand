#!/usr/bin/env python3
"""Generate the "Powered by" badges (style P1 pill) for every smalt product.

Usage: python3 scripts/badges.py <Geist[wght].ttf> <MartianMono[wdth,wght].ttf>

Writes badges/powered-by-smalt{db,ui,bi,df,nb,fl,ql,ts,ty}.svg and -on-dark.svg: 172 x 28 px,
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


# The two-line badges, twice the height of the others. Before 1.0, the preview badge: "Work in
# progress" above "Come build with us", led by a pull-request sign (the contributor's branch in kiln
# orange, arrowing into the smalt main line). From 1.0, the release badge: "Release 1.x" above "Come
# build with us", led by a release-commit sign (a release node on the smalt main line, which runs on,
# with the same pull request still coming in). Signs are signage, not product marks, so they use
# strokes and rings.
SIGN_COLOURS = {"light": ("#003399", "#E5622F"), "dark": ("#9DB4F5", "#FF8A5C")}
SIGN_W, SIGN_R = 6, 7


def _ring(x, y, c):
    return f'<circle cx="{x}" cy="{y}" r="{SIGN_R}" fill="none" stroke="{c}" stroke-width="{SIGN_W - 1}"/>'


def _line(d, c):
    return (f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{SIGN_W}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def _incoming(k):
    """The contributor's branch, in kiln, with the arrow asking to bring it in."""
    return _line("M48 47V26C48 20 44 16 38 16H28", k) + _line("M34 10L28 16L34 22", k) + _ring(48, 54, k)


def pull_request(theme):
    s, k = SIGN_COLOURS[theme]
    return _line("M16 17V47", s) + _ring(16, 10, s) + _ring(16, 54, s) + _incoming(k)


def release_commit(theme):
    """The main line runs on past a release node (a ring round a dot); the pull request still comes in."""
    s, k = SIGN_COLOURS[theme]
    return (_line("M16 6V26", s) + _line("M16 54V58", s)
            + f'<circle cx="16" cy="40" r="9" fill="none" stroke="{s}" stroke-width="4"/>'
            + f'<circle cx="16" cy="40" r="4" fill="{s}"/>' + _incoming(k))


PREVIEW_H, PREVIEW_PAD, PREVIEW_SIGN = 56, 12, 32
TWO_LINE = {
    "work-in-progress": ("Work in progress", pull_request, "Work in progress. Come build with us."),
    "release-1x": ("Release 1.x", release_commit, "Release 1.x. Come build with us."),
}


def two_line_badge(strong, regular, theme, kind):
    """A two-line badge, twice the height of the others."""
    top, sign_fn, label = TWO_LINE[kind]
    t = THEMES[theme]
    ink = "#151922" if theme == "light" else "#E9EBF0"
    x0 = BORDER + PREVIEW_PAD + PREVIEW_SIGN + 10
    top_svg, x1 = strong.paths([(ink, top)], x0, PREVIEW_H / 2 - 4)
    bottom_svg, x2 = regular.paths([(t["verb"], "Come build with us")], x0, PREVIEW_H / 2 + 4 + regular.cap)
    width = round(max(x1 - strong.track, x2 - regular.track) + PREVIEW_PAD + BORDER)
    sign = (f'<g transform="translate({BORDER + PREVIEW_PAD} {(PREVIEW_H - PREVIEW_SIGN) / 2}) '
            f'scale({PREVIEW_SIGN / 64})">{sign_fn(theme)}</g>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{PREVIEW_H}" '
            f'viewBox="0 0 {width} {PREVIEW_H}" role="img" aria-label="{label}">'
            f'<rect x="0.5" y="0.5" width="{width - 1}" height="{PREVIEW_H - 1}" rx="9.5" fill="{t["surface"]}" stroke="{t["border"]}"/>'
            f"{sign}{top_svg}{bottom_svg}</svg>\n")


def sign_icon(sign_fn, label, theme):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" role="img" '
            f'aria-label="{label}">{sign_fn(theme)}</svg>\n')


if __name__ == "__main__":
    geist = Face(sys.argv[1], {"wght": 400}, 11)
    mono = Face(sys.argv[2], {"wght": 600, "wdth": 112.5}, 12.5, -0.06)
    out = ROOT / "badges"
    out.mkdir(exist_ok=True)
    for product in ("db", "ui", "bi", "df", "nb", "fl", "ql", "ts", "ty"):
        for theme, suffix in (("light", ""), ("dark", "-on-dark")):
            path = out / f"powered-by-smalt{product}{suffix}.svg"
            path.write_text(badge(geist, mono, product, theme))
            print(path.relative_to(ROOT))
    for theme, suffix in (("light", ""), ("dark", "-on-dark")):
        path = out / f"a-smaltworks-project{suffix}.svg"
        path.write_text(endorsement(geist, mono, theme))
        print(path.relative_to(ROOT))
    strong = Face(sys.argv[1], {"wght": 600}, 13)
    regular = Face(sys.argv[1], {"wght": 400}, 13)
    (out / "signs").mkdir(exist_ok=True)
    for theme, suffix in (("light", ""), ("dark", "-on-dark")):
        for path, text in (
                (out / f"work-in-progress{suffix}.svg", two_line_badge(strong, regular, theme, "work-in-progress")),
                (out / f"release-1x{suffix}.svg", two_line_badge(strong, regular, theme, "release-1x")),
                (out / "signs" / f"pull-request{suffix}.svg", sign_icon(pull_request, "Come build with us", theme)),
                (out / "signs" / f"release-commit{suffix}.svg", sign_icon(release_commit, "Release", theme))):
            path.write_text(text)
            print(path.relative_to(ROOT))
