#!/usr/bin/env python3
"""Generate the plugin badges: Official, Verified and Works with.

Usage: python3 scripts/plugin_badges.py <Geist[wght].ttf> <MartianMono[wdth,wght].ttf>

Writes, under badges/plugins/, a light and a dark (-on-dark) SVG of:
  official-smaltdb.svg        product mark + wordmark + "official plugin"
  verified-smaltdb-api-v1.svg check + "Verified for" + wordmark + "API v1" tag
  works-with-smaltdb.svg      "Works with" + wordmark, grey, dashed, no mark

They share the "Powered by" pill's geometry (scripts/badges.py): 28 px tall, 10 px
padding, 6 px gaps, 16 px mark, Geist 400 11 px labels, Martian Mono 600 12.5 px
wordmark. Text is converted to paths. smaltdb and smaltml have plugin APIs (smaltml:
its kernel contract, smaltml ADR 0035), so theirs are generated; add a product to PRODUCTS
when it gets one.
Requires fonttools.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brand_assets import MARKS, COLOURS, mark_paths  # noqa: E402
from badges import Face, THEMES, H, PAD, GAP, MARK, BORDER, db_mark  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

PRODUCTS = ["db", "ml"]          # products with a plugin API
API_VERSIONS = {"db": [1], "ml": [1]}  # plugin API versions with a Verified badge (smaltml: its kernel contract)

# The check: two 45-degree bars of the Chevron's thickness, drawn on the 64 grid.
CHECK = "M6 33L13 26L25 38L51 12L58 19L25 52Z"

EXTRA = {
    "light": {"tag_bg": "#D6E0F3", "tag_fg": "#001F66", "grey": "#5C6375", "grey_border": "#C9CFDA"},
    "dark": {"tag_bg": "#26324F", "tag_fg": "#D6E0F3", "grey": "#9096A3", "grey_border": "#3A4152"},
}
TAG_H, TAG_PAD, TAG_R = 16, 5, 4


def mark_svg(svg_inner, x):
    return f'<g transform="translate({x} {(H - MARK) / 2}) scale({MARK / 64})">{svg_inner}</g>'


def product_mark(product, c):
    return db_mark(c) if product == "db" else mark_paths(MARKS[product], c, product)


def wordmark(mono, product, c, x, baseline, grey=None):
    segs = ([(grey, "sm"), (grey, "alt"), (grey, product)] if grey else
            [(c["ink"], "sm"), (c["alt"], "alt"), (c["suffix"][product], product)])
    return mono.paths(segs, x, baseline)


def frame(width, t, e, dashed=False):
    if dashed:
        return (f'<rect x="0.5" y="0.5" width="{width - 1}" height="{H - 1}" rx="6.5" fill="none" '
                f'stroke="{e["grey_border"]}" stroke-dasharray="3 2"/>')
    return (f'<rect x="0.5" y="0.5" width="{width - 1}" height="{H - 1}" rx="6.5" '
            f'fill="{t["surface"]}" stroke="{t["border"]}"/>')


def svg(width, label, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{H}" viewBox="0 0 {width} {H}" '
            f'role="img" aria-label="{label}">{body}</svg>\n')


def official(geist, mono, product, theme):
    t, c = THEMES[theme], COLOURS[theme]
    baseline = H / 2 + geist.cap / 2
    word_x = BORDER + PAD + MARK + GAP
    word_svg, x = wordmark(mono, product, c, word_x, baseline)
    label_x = x - mono.track + GAP
    label_svg, x = geist.paths([(t["verb"], "official plugin")], label_x, baseline)
    width = round(x + PAD + BORDER)
    body = frame(width, t, None) + mark_svg(product_mark(product, c), BORDER + PAD) + word_svg + label_svg
    return svg(width, f"smalt{product} official plugin", body)


def verified(geist, mono, tagface, product, theme, api):
    t, c, e = THEMES[theme], COLOURS[theme], EXTRA[theme]
    baseline = H / 2 + geist.cap / 2
    verb_x = BORDER + PAD + MARK + GAP
    verb_svg, x = geist.paths([(t["verb"], "Verified for")], verb_x, baseline)
    word_svg, x = wordmark(mono, product, c, x + GAP, baseline)
    tag_text = f"API v{api}"
    tag_x = x - mono.track + GAP
    tag_w = TAG_PAD * 2 + tagface.width(tag_text)
    tag_svg, _ = tagface.paths([(e["tag_fg"], tag_text)], tag_x + TAG_PAD, H / 2 + tagface.cap / 2)
    width = round(tag_x + tag_w + PAD + BORDER)
    body = (frame(width, t, e) + mark_svg(f'<path d="{CHECK}" fill="{c["body"]}"/>', BORDER + PAD)
            + verb_svg + word_svg
            + f'<rect x="{tag_x:.2f}" y="{(H - TAG_H) / 2}" width="{tag_w:.2f}" height="{TAG_H}" rx="{TAG_R}" fill="{e["tag_bg"]}"/>'
            + tag_svg)
    return svg(width, f"Verified for smalt{product}, plugin API version {api}", body)


def works_with(geist, mono, product, theme):
    t, c, e = THEMES[theme], COLOURS[theme], EXTRA[theme]
    baseline = H / 2 + geist.cap / 2
    verb_svg, x = geist.paths([(e["grey"], "Works with")], BORDER + PAD, baseline)
    word_svg, x = wordmark(mono, product, c, x + GAP, baseline, grey=e["grey"])
    width = round(x - mono.track + PAD + BORDER)
    return svg(width, f"Works with smalt{product}", frame(width, t, e, dashed=True) + verb_svg + word_svg)


if __name__ == "__main__":
    geist = Face(sys.argv[1], {"wght": 400}, 11)
    mono = Face(sys.argv[2], {"wght": 600, "wdth": 112.5}, 12.5, -0.06)
    tagface = Face(sys.argv[2], {"wght": 400, "wdth": 112.5}, 10)
    out = ROOT / "badges" / "plugins"
    out.mkdir(parents=True, exist_ok=True)
    for product in PRODUCTS:
        for theme, suffix in (("light", ""), ("dark", "-on-dark")):
            files = {f"official-smalt{product}{suffix}.svg": official(geist, mono, product, theme),
                     f"works-with-smalt{product}{suffix}.svg": works_with(geist, mono, product, theme)}
            for api in API_VERSIONS[product]:
                files[f"verified-smalt{product}-api-v{api}{suffix}.svg"] = verified(geist, mono, tagface, product, theme, api)
            for name, text in files.items():
                (out / name).write_text(text)
                print((out / name).relative_to(ROOT))
