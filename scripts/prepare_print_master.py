#!/usr/bin/env python3
"""Extract and normalize a complete rectangular calendar print master."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export an edge-to-edge rectangular calendar print master."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--width", type=int, default=1772)
    parser.add_argument("--height", type=int, default=709)
    parser.add_argument("--ppi", type=int, default=300)
    parser.add_argument("--left", type=float, default=0.05)
    parser.add_argument("--top", type=float, default=0.18)
    parser.add_argument("--right", type=float, default=0.95)
    parser.add_argument("--bottom", type=float, default=0.82)
    parser.add_argument("--max-trim", type=float, default=0.03)
    return parser.parse_args()


def crop_to_ratio(
    image: Image.Image, target_ratio: float, max_trim: float
) -> Image.Image:
    width, height = image.size
    current_ratio = width / height
    if abs(current_ratio - target_ratio) < 1e-9:
        return image

    if current_ratio > target_ratio:
        target_width = round(height * target_ratio)
        trim_fraction = (width - target_width) / width
        if trim_fraction > max_trim:
            raise SystemExit(
                f"production rectangle is too wide; would trim {trim_fraction:.1%}"
            )
        left = (width - target_width) // 2
        return image.crop((left, 0, left + target_width, height))

    target_height = round(width / target_ratio)
    trim_fraction = (height - target_height) / height
    if trim_fraction > max_trim:
        raise SystemExit(
            f"production rectangle is too tall; would trim {trim_fraction:.1%}"
        )
    top = (height - target_height) // 2
    return image.crop((0, top, width, top + target_height))


def main() -> None:
    args = parse_args()
    if args.width <= 0 or args.height <= 0 or args.ppi <= 0:
        raise SystemExit("width, height, and ppi must be positive integers")
    if not (0 <= args.left < args.right <= 1 and 0 <= args.top < args.bottom <= 1):
        raise SystemExit("crop bounds must be ordered fractions between 0 and 1")
    if not (0 <= args.max_trim <= 0.25):
        raise SystemExit("max-trim must be between 0 and 0.25")
    if args.output.suffix.lower() != ".png":
        raise SystemExit("output must use the .png extension")

    with Image.open(args.input) as source:
        source = ImageOps.exif_transpose(source).convert("RGB")
        crop_box = (
            round(source.width * args.left),
            round(source.height * args.top),
            round(source.width * args.right),
            round(source.height * args.bottom),
        )
        artwork = source.crop(crop_box)
        artwork = crop_to_ratio(artwork, args.width / args.height, args.max_trim)
        master = artwork.resize(
            (args.width, args.height), resample=Image.Resampling.LANCZOS
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    master.save(
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
        if exported.mode not in {"RGB", "RGBA"}:
            raise SystemExit(f"unexpected export mode: {exported.mode}")

    print(
        f"Wrote rectangular print master {args.output} at "
        f"{args.width}x{args.height}px, {args.ppi} PPI"
    )


if __name__ == "__main__":
    main()
