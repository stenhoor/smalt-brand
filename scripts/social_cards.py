#!/usr/bin/env python3
"""Generate the social preview cards for every smalt product.

Usage: python3 scripts/social_cards.py <Geist[wght].ttf> <MartianMono[wdth,wght].ttf>

Writes social/smalt{db,ui,bi,df,nb,ql,ts}.svg (the source) and .png (1280 x 640, for upload).
Each card is the product's dark lockup, its tagline (Geist 700), its positioning
line (Geist 400) and its address (Martian Mono 400) on the dark Kiln ground, with
a bar in the product colour along the bottom. Text is converted to paths and the
lockup is embedded from logos/<product>/lockup-on-dark.svg, so the SVG needs no
fonts and stays in step with the logos. Run scripts/brand_assets.py first if the
lockups changed.

Requires fonttools and cairosvg (pip install fonttools cairosvg).
"""
import re
import sys
from pathlib import Path

import cairosvg

sys.path.insert(0, str(Path(__file__).resolve().parent))
from badges import Face  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

W, H = 1280, 640
LEFT = 96                       # left margin; content stays inside the 1.91:1 centre crop
INK, INK_2, INK_3 = "#E9EBF0", "#B9BEC9", "#9096A3"   # text, text-2, text-3 (dark)
GROUND = "#14171F"               # bg (dark)
BAR = {"db": "#9DB4F5", "ui": "#5CBDE8", "bi": "#5CBDE8", "nb": "#5CBDE8", "df": "#F57FE6", "ql": "#F57FE6", "ts": "#F57FE6", "works": "#FF8A5C"}  # smalt-200, layer-tool / layer-language (dark), kiln

PRODUCTS = {
    "db": ("Small. Alternative. Fast.",
           "A fast alternative database for the browser, written in TypeScript.",
           "smaltdb.dev"),
    "ui": ("Small. Alternative. Query.",
           "A query workbench for smaltdb that runs entirely in the browser.",
           "github.com/stenhoor/smaltui"),
    "bi": ("Small. Alternative. Insight.",
           "Business intelligence in the browser, powered by smaltdb.",
           "github.com/stenhoor/smaltbi"),
    "df": ("Small. Alternative. Frames.",
           "Dataframes for smaltdb. Small and fast.",
           "github.com/stenhoor/smaltdf"),
    "nb": ("Small. Alternative. Notebooks.",
           "Reactive notebooks for smaltdb.",
           "github.com/stenhoor/smaltnb"),
    "ql": ("Small. Alternative. Familiar.",
           "The SQL you know, for smaltdb.",
           "github.com/stenhoor/smaltql"),
    "ts": ("Small. Alternative. Typed.",
           "smaltdb, straight from TypeScript.",
           "smaltworks.dev/products/smaltts"),
    "works": ("Small. Alternative. Together.",
              "Stay smalty.",
              "smaltworks.dev"),
}

LOCKUP_H = 132                   # rendered height of the lockup's viewBox


def lockup(product, x, y):
    """The dark lockup as a nested <svg>, scaled to LOCKUP_H tall, its artwork's left edge at x."""
    src = (ROOT / "logos" / f"smalt{product}" / "lockup-on-dark.svg").read_text()
    vb = re.search(r'viewBox="([^"]+)"', src).group(1)
    vx, vy, vw, vh = (float(v) for v in vb.split())
    inner = src[src.index(">") + 1: src.rindex("</svg>")]
    scale = LOCKUP_H / vh
    w = vw * scale
    x -= 12 * scale  # the lockup's viewBox has 12 units of padding (0.12em at 100) before the mark
    return (f'<svg x="{x:.2f}" y="{y}" width="{w:.2f}" height="{LOCKUP_H}" viewBox="{vb}">{inner}</svg>', w)


def card(product, tag, body, mono):
    tagline, line, address = PRODUCTS[product]
    logo, _ = lockup(product, LEFT, 96)
    tag_svg, _ = tag.paths([(INK, tagline)], LEFT, 370)
    line_svg, line_end = body.paths([(INK_2, line)], LEFT, 432)
    addr_svg, addr_end = mono.paths([(INK_3, address)], LEFT, 548)
    assert line_end <= W - LEFT, f"smalt{product}: positioning line overruns ({line_end:.0f}px)"
    assert addr_end <= W - LEFT, f"smalt{product}: address overruns ({addr_end:.0f}px)"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
            f'role="img" aria-label="smalt{product}: {tagline} {line}">'
            f'<rect width="{W}" height="{H}" fill="{GROUND}"/>'
            f'{logo}{tag_svg}{line_svg}{addr_svg}'
            f'<rect y="{H - 12}" width="{W}" height="12" fill="{BAR[product]}"/>'
            f"</svg>\n")


if __name__ == "__main__":
    geist, martian = sys.argv[1], sys.argv[2]
    tag = Face(geist, {"wght": 700}, 76, -0.035)
    body = Face(geist, {"wght": 400}, 32)
    mono = Face(martian, {"wght": 400, "wdth": 112.5}, 24, 0.02)
    out = ROOT / "social"
    out.mkdir(exist_ok=True)
    for product in PRODUCTS:
        svg = card(product, tag, body, mono)
        (out / f"smalt{product}.svg").write_text(svg)
        cairosvg.svg2png(bytestring=svg.encode(), write_to=str(out / f"smalt{product}.png"),
                         output_width=W, output_height=H)
        print(f"social/smalt{product}.svg, .png")
    # smaltworks' avatar for GitHub and social profiles: the app icon as a full-bleed square
    # (the sites round or circle-crop it themselves), 512 px.
    icon = (ROOT / "logos" / "smaltworks" / "app-icon.svg").read_text()
    assert 'rx="15"' in icon
    avatar = icon.replace('rx="15"', 'rx="0"', 1).replace("app icon", "avatar")
    (out / "smaltworks-avatar.svg").write_text(avatar)
    cairosvg.svg2png(bytestring=avatar.encode(), write_to=str(out / "smaltworks-avatar.png"), output_width=512, output_height=512)
    print("social/smaltworks-avatar.svg, .png")
