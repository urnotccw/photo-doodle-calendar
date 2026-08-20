#!/usr/bin/env python3
"""Extract a calendar ticket and normalize it to an exact physical print size."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageColor, ImageOps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crop the inner ticket and export a fixed-size print master."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--width", type=int, default=2953)
    parser.add_argument("--height", type=int, default=1181)
    parser.add_argument("--ppi", type=int, default=300)
    parser.add_argument("--left", type=float, default=0.05)
    parser.add_argument("--top", type=float, default=0.18)
    parser.add_argument("--right", type=float, default=0.95)
    parser.add_argument("--bottom", type=float, default=0.82)
    parser.add_argument("--background", default="#f3eedf")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.width <= 0 or args.height <= 0 or args.ppi <= 0:
        raise SystemExit("width, height, and ppi must be positive integers")
    if not (0 <= args.left < args.right <= 1 and 0 <= args.top < args.bottom <= 1):
        raise SystemExit("crop bounds must be ordered fractions between 0 and 1")
    if args.output.suffix.lower() != ".png":
        raise SystemExit("output must use the .png extension")

    with Image.open(args.input) as source:
        source = ImageOps.exif_transpose(source).convert("RGBA")
        crop_box = (
            round(source.width * args.left),
            round(source.height * args.top),
            round(source.width * args.right),
            round(source.height * args.bottom),
        )
        ticket = source.crop(crop_box)
        fitted = ImageOps.contain(
            ticket,
            (args.width, args.height),
            method=Image.Resampling.LANCZOS,
        )

    background = ImageColor.getrgb(args.background)
    canvas = Image.new("RGBA", (args.width, args.height), (*background, 255))
    x = (args.width - fitted.width) // 2
    y = (args.height - fitted.height) // 2
    canvas.alpha_composite(fitted, (x, y))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(
        args.output,
        format="PNG",
        dpi=(args.ppi, args.ppi),
        optimize=True,
    )

    with Image.open(args.output) as exported:
        if exported.size != (args.width, args.height):
            raise SystemExit(
                f"export verification failed: expected {args.width}x{args.height}, "
                f"got {exported.width}x{exported.height}"
            )

    print(
        f"Wrote ticket {args.output} at {args.width}x{args.height}px, "
        f"{args.ppi} PPI"
    )


if __name__ == "__main__":
    main()
