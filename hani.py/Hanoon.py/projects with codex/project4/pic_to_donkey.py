from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter


def _add_donkey_features(img: Image.Image) -> Image.Image:
    """Add a playful donkey-style overlay to an image."""
    base = img.convert("RGBA")
    width, height = base.size

    # Warm, earthy tint for a donkey-like tone.
    tint_layer = Image.new("RGBA", base.size, (155, 130, 95, 55))
    base = Image.alpha_composite(base, tint_layer)

    draw = ImageDraw.Draw(base, "RGBA")

    cx = width // 2
    ear_top = int(height * 0.06)
    ear_bottom = int(height * 0.35)
    ear_offset = int(width * 0.22)
    ear_half = max(12, int(width * 0.08))

    # Ears
    left_ear = [(cx - ear_offset, ear_top), (cx - ear_offset - ear_half, ear_bottom), (cx - ear_offset + ear_half, ear_bottom)]
    right_ear = [(cx + ear_offset, ear_top), (cx + ear_offset - ear_half, ear_bottom), (cx + ear_offset + ear_half, ear_bottom)]
    draw.polygon(left_ear, fill=(130, 110, 85, 170), outline=(70, 60, 45, 200))
    draw.polygon(right_ear, fill=(130, 110, 85, 170), outline=(70, 60, 45, 200))

    inner_shrink = max(4, int(ear_half * 0.35))
    left_inner = [(left_ear[0][0], left_ear[0][1] + inner_shrink), (left_ear[1][0] + inner_shrink, left_ear[1][1] - inner_shrink), (left_ear[2][0] - inner_shrink, left_ear[2][1] - inner_shrink)]
    right_inner = [(right_ear[0][0], right_ear[0][1] + inner_shrink), (right_ear[1][0] + inner_shrink, right_ear[1][1] - inner_shrink), (right_ear[2][0] - inner_shrink, right_ear[2][1] - inner_shrink)]
    draw.polygon(left_inner, fill=(188, 153, 132, 160))
    draw.polygon(right_inner, fill=(188, 153, 132, 160))

    # Muzzle
    muzzle_w = int(width * 0.33)
    muzzle_h = int(height * 0.18)
    muzzle_x1 = cx - muzzle_w // 2
    muzzle_y1 = int(height * 0.58)
    muzzle_x2 = cx + muzzle_w // 2
    muzzle_y2 = muzzle_y1 + muzzle_h
    draw.rounded_rectangle((muzzle_x1, muzzle_y1, muzzle_x2, muzzle_y2), radius=max(8, int(muzzle_h * 0.22)), fill=(205, 185, 160, 170), outline=(90, 75, 60, 200), width=max(1, int(width * 0.004)))

    # Nostrils
    nostril_w = int(muzzle_w * 0.14)
    nostril_h = int(muzzle_h * 0.24)
    nostril_y = muzzle_y1 + int(muzzle_h * 0.42)
    left_nostril_x = cx - int(muzzle_w * 0.16)
    right_nostril_x = cx + int(muzzle_w * 0.02)
    draw.ellipse((left_nostril_x, nostril_y, left_nostril_x + nostril_w, nostril_y + nostril_h), fill=(60, 45, 35, 210))
    draw.ellipse((right_nostril_x, nostril_y, right_nostril_x + nostril_w, nostril_y + nostril_h), fill=(60, 45, 35, 210))

    # Cartoon teeth
    tooth_w = int(muzzle_w * 0.18)
    tooth_h = int(muzzle_h * 0.2)
    tooth_y = muzzle_y2 - tooth_h - int(muzzle_h * 0.08)
    draw.rectangle((cx - tooth_w, tooth_y, cx, tooth_y + tooth_h), fill=(245, 240, 220, 220), outline=(120, 110, 95, 180))
    draw.rectangle((cx, tooth_y, cx + tooth_w, tooth_y + tooth_h), fill=(245, 240, 220, 220), outline=(120, 110, 95, 180))

    # Slight sharpen for final result.
    base = ImageEnhance.Sharpness(base).enhance(1.15)
    base = base.filter(ImageFilter.SMOOTH_MORE)

    return base


def convert_to_donkey(input_path: Path, output_path: Path) -> Path:
    with Image.open(input_path) as img:
        donkey = _add_donkey_features(img)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        donkey.convert("RGB").save(output_path)
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert any photo to a donkey-style image.")
    parser.add_argument("input", type=Path, help="Input image path")
    parser.add_argument("-o", "--output", type=Path, default=None, help="Output image path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.input.exists():
        raise SystemExit(f"Input file not found: {args.input}")

    output_path = args.output or args.input.with_name(f"{args.input.stem}_donkey.jpg")
    result = convert_to_donkey(args.input, output_path)
    print(f"Saved donkey image: {result}")


if __name__ == "__main__":
    main()
