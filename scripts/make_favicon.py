#!/usr/bin/env python3
"""Draw the site's tab icon (favicon) from the self-hosted Inter font.

Usage (from the repo root):
    pip install fonttools brotli pillow
    python3 scripts/make_favicon.py              # writes the icon files listed below
    python3 scripts/make_favicon.py --preview out.png   # also writes a sheet of the options

The icon is the letters in TEXT, set in Inter at weight WEIGHT, white on a rounded square of BG.
Outputs:
    favicon.ico                    16, 32 and 48 px; browsers request /favicon.ico by default
    assets/favicon.ico             same file; the old theme pages link to this path
    assets/academic/favicon.svg    sharp at any size; letters are outlines, so no font is needed
    apple-touch-icon.png           180 px, for home-screen bookmarks
"""
import argparse
import io
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "assets/academic/fonts/inter-latin-wght-normal.woff2"

TEXT = "AK"
WEIGHT = 600
BG = "#1d5fd3"      # the site's link colour (light theme); reads on light and dark tab bars
FG = "#ffffff"
RADIUS = 0.22       # corner radius as a fraction of the side
LETTER_H = 0.40     # cap height as a fraction of the side
TRACKING = -0.02    # extra space between letters, in em


def static_font(weight):
    """Instance the variable Inter at one weight and return it as a TTFont."""
    vf = TTFont(FONT)
    inst = instantiateVariableFont(vf, {"wght": weight})
    inst.flavor = None
    buf = io.BytesIO()
    inst.save(buf)
    buf.seek(0)
    return TTFont(buf), buf.getvalue()


def text_outline(font, text, tracking):
    """SVG path data for `text` in font units, baseline at y=0 (y up), plus its advance width."""
    cmap, gs = font.getBestCmap(), font.getGlyphSet()
    upm = font["head"].unitsPerEm
    pen = SVGPathPen(gs)
    x = 0
    for i, ch in enumerate(text):
        name = cmap[ord(ch)]
        gs[name].draw(TransformPen(pen, (1, 0, 0, 1, x, 0)))
        x += gs[name].width + (tracking * upm if i < len(text) - 1 else 0)
    return pen.getCommands(), x


def ink_box(font, text, tracking):
    """Bounding box of the drawn letters (font units): xmin, ymin, xmax, ymax."""
    from fontTools.pens.boundsPen import BoundsPen
    cmap, gs = font.getBestCmap(), font.getGlyphSet()
    upm = font["head"].unitsPerEm
    pen = BoundsPen(gs)
    x = 0
    for i, ch in enumerate(text):
        name = cmap[ord(ch)]
        gs[name].draw(TransformPen(pen, (1, 0, 0, 1, x, 0)))
        x += gs[name].width + (tracking * upm if i < len(text) - 1 else 0)
    return pen.bounds


def svg_icon(font, text=TEXT, bg=BG, fg=FG, radius=RADIUS, letter_h=LETTER_H, tracking=TRACKING):
    """A 64x64 SVG: rounded square plus the letters as outlines, centred on their ink box."""
    d, _ = text_outline(font, text, tracking)
    xmin, ymin, xmax, ymax = ink_box(font, text, tracking)
    cap = font["OS/2"].sCapHeight
    s = 64 * letter_h / cap
    w, h = (xmax - xmin) * s, (ymax - ymin) * s
    tx, ty = (64 - w) / 2 - xmin * s, (64 + h) / 2 + ymin * s
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        f'<rect width="64" height="64" rx="{64 * radius:.2f}" fill="{bg}"/>'
        f'<path fill="{fg}" transform="translate({tx:.3f} {ty:.3f}) scale({s:.5f} {-s:.5f})" d="{d}"/>'
        "</svg>\n"
    )


def png_icon(ttf_bytes, font, size, text=TEXT, bg=BG, fg=FG, radius=RADIUS, letter_h=LETTER_H,
             tracking=TRACKING, ss=8):
    """Raster icon at `size` px, drawn at ss times the size and downsampled for smooth edges."""
    big = size * ss
    im = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, big - 1, big - 1), radius=big * radius, fill=bg)
    upm, cap = font["head"].unitsPerEm, font["OS/2"].sCapHeight
    px = big * letter_h * upm / cap                       # font size in px giving that cap height
    f = ImageFont.truetype(io.BytesIO(ttf_bytes), size=round(px))
    xmin, ymin, xmax, ymax = ink_box(font, text, tracking)
    k = round(px) / upm
    # draw letter by letter so tracking matches the SVG
    cmap, gs = font.getBestCmap(), font.getGlyphSet()
    x0 = (big - (xmax - xmin) * k) / 2 - xmin * k
    base = (big + (ymax - ymin) * k) / 2 + ymin * k        # baseline y in image coordinates
    x = 0
    for i, ch in enumerate(text):
        dr.text((x0 + x * k, base), ch, font=f, fill=fg, anchor="ls")
        x += gs[cmap[ord(ch)]].width + (tracking * upm if i < len(text) - 1 else 0)
    return im.resize((size, size), Image.LANCZOS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", help="also write a PNG sheet comparing icon options")
    args = ap.parse_args()

    font, ttf = static_font(WEIGHT)
    icons = {s: png_icon(ttf, font, s) for s in (16, 32, 48, 180)}
    for out in (ROOT / "favicon.ico", ROOT / "assets/favicon.ico"):
        icons[48].save(out, sizes=[(16, 16), (32, 32), (48, 48)],
                       append_images=[icons[16], icons[32]])
    icons[180].convert("RGB").save(ROOT / "apple-touch-icon.png", optimize=True)
    (ROOT / "assets/academic/favicon.svg").write_text(svg_icon(font))
    print("wrote favicon.ico, assets/favicon.ico, assets/academic/favicon.svg, apple-touch-icon.png")

    if args.preview:
        preview(ttf, font, args.preview)


def preview(ttf, font, path):
    """Sheet of options at tab sizes, on a light and a dark tab bar."""
    photo = Image.open(ROOT / "assets/academic/ayush.jpg").convert("RGB")
    w, h = photo.size
    side = min(w, h)
    photo = photo.crop(((w - side) // 2, 0, (w + side) // 2, side))

    def photo_icon(size):
        big = photo.resize((size * 8, size * 8), Image.LANCZOS).convert("RGBA")
        mask = Image.new("L", big.size, 0)
        ImageDraw.Draw(mask).ellipse((0, 0, big.width - 1, big.height - 1), fill=255)
        big.putalpha(mask)
        return big.resize((size, size), Image.LANCZOS)

    options = [
        ("1  AK, ink", lambda s: png_icon(ttf, font, s, bg="#1d1d1f")),
        ("2  AK, link blue (default)", lambda s: png_icon(ttf, font, s)),
        ("3  A, ink", lambda s: png_icon(ttf, font, s, text="A", bg="#1d1d1f", letter_h=0.46)),
        ("4  photo", photo_icon),
    ]
    sizes = (16, 32, 64)
    row_h, label_w = 90, 170
    sheet = Image.new("RGB", (label_w + 2 * (sum(sizes) + 40 * len(sizes)) + 40, row_h * len(options) + 50), "white")
    dr = ImageDraw.Draw(sheet)
    lf = ImageFont.truetype(io.BytesIO(ttf), 15)
    dr.text((label_w, 12), "light tab bar", font=lf, fill="#333")
    dr.text((label_w + sum(sizes) + 40 * len(sizes) + 20, 12), "dark tab bar", font=lf, fill="#333")
    for r, (name, make) in enumerate(options):
        y = 50 + r * row_h
        dr.text((10, y + 25), name, font=lf, fill="#111")
        for b, bar in enumerate(("#e8eaed", "#202124")):
            x = label_w + b * (sum(sizes) + 40 * len(sizes) + 20)
            dr.rectangle((x - 10, y - 5, x + sum(sizes) + 40 * len(sizes) - 20, y + 75), fill=bar)
            for s in sizes:
                ic = make(s)
                sheet.paste(ic, (x, y + (64 - s) // 2 + 3), ic)
                x += s + 40
    sheet.save(path)
    print("wrote", path)


if __name__ == "__main__":
    main()
