#!/usr/bin/env python3
"""Compose a ticket-style presentation preview from a rectangular print master."""

from __future__ import annotations

import argparse
import math
import random
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw, ImageFilter, ImageOps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply paper, notches, and scallops to a print-master preview copy."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--master-width", type=int, default=1772)
    parser.add_argument("--master-height", type=int, default=709)
    parser.add_argument("--width", type=int, default=3200)
    parser.add_argument("--height", type=int, default=1800)
    parser.add_argument("--left", type=float, default=0.05)
    parser.add_argument("--top", type=float, default=0.18)
    parser.add_argument("--right", type=float, default=0.95)
    parser.add_argument("--bottom", type=float, default=0.82)
    parser.add_argument("--background", default="#f3eedf")
    return parser.parse_args()


def paper_field(size: tuple[int, int], color: str) -> Image.Image:
    base_rgb = ImageColor.getrgb(color)
    base = Image.new("RGB", size, base_rgb)
    small = (max(1, size[0] // 4), max(1, size[1] // 4))
    rng = random.Random(20260820)
    noise = Image.new("L", small)
    noise.putdata(
        [rng.randint(108, 148) for _ in range(small[0] * small[1])]
    )
    noise = noise.resize(size, Image.Resampling.BICUBIC).filter(
        ImageFilter.GaussianBlur(0.6)
    )
    dark = tuple(max(0, channel - 8) for channel in base_rgb)
    light = tuple(min(255, channel + 8) for channel in base_rgb)
    texture = ImageOps.colorize(noise, dark, light)
    return Image.blend(base, texture, 0.22)


def ticket_mask(width: int, height: int) -> Image.Image:
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    depth = max(1, round(height * 0.015))
    cycles = 16

    left = []
    right = []
    for y in range(height + 1):
        phase = 2 * math.pi * cycles * y / height
        inset = depth * 0.5 * (1 - math.cos(phase))
        left.append((round(inset), y))
        right.append((width - 1 - round(inset), y))
    draw.polygon(left + list(reversed(right)), fill=255)

    radius = max(1, round(height * 0.02))
    cutouts = [
        (0, 0),
        (width - 1, 0),
        (0, height - 1),
        (width - 1, height - 1),
    ]
    for x_fraction in (0.30, 0.75):
        x = round(width * x_fraction)
        cutouts.extend(((x, 0), (x, height - 1)))
    for x, y in cutouts:
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=0)

    return mask


def main() -> None:
    args = parse_args()
    if args.output.suffix.lower() != ".png":
        raise SystemExit("output must use the .png extension")
    if args.width <= 0 or args.height <= 0:
        raise SystemExit("preview dimensions must be positive")
    if abs(args.width / args.height - 16 / 9) > 0.001:
        raise SystemExit("preview canvas must use a 16:9 aspect ratio")
    if not (0 <= args.left < args.right <= 1 and 0 <= args.top < args.bottom <= 1):
        raise SystemExit("ticket bounds must be ordered fractions between 0 and 1")

    with Image.open(args.input) as source:
        source = ImageOps.exif_transpose(source).convert("RGB")
        if source.size != (args.master_width, args.master_height):
            raise SystemExit(
                "print master must be prepared first: expected "
                f"{args.master_width}x{args.master_height}, got "
                f"{source.width}x{source.height}"
            )

        x0 = round(args.width * args.left)
        y0 = round(args.height * args.top)
        x1 = round(args.width * args.right)
        y1 = round(args.height * args.bottom)
        ticket_width = x1 - x0
        ticket_height = y1 - y0
        artwork = ImageOps.fit(
            source,
            (ticket_width, ticket_height),
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        ).convert("RGBA")

    mask = ticket_mask(ticket_width, ticket_height)
    artwork.putalpha(mask)
    preview = paper_field((args.width, args.height), args.background).convert("RGBA")

    shadow_alpha = mask.filter(ImageFilter.GaussianBlur(12)).point(
        lambda value: round(value * 0.10)
    )
    shadow = Image.new("RGBA", (ticket_width, ticket_height), (107, 90, 72, 0))
    shadow.putalpha(shadow_alpha)
    preview.alpha_composite(shadow, (x0, y0 + 4))
    preview.alpha_composite(artwork, (x0, y0))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    preview.convert("RGB").save(args.output, format="PNG", optimize=True)

    with Image.open(args.output) as exported:
        if exported.size != (args.width, args.height):
            raise SystemExit("preview export dimension verification failed")

    print(
        f"Wrote presentation preview {args.output} at "
        f"{args.width}x{args.height}px"
    )


if __name__ == "__main__":
    main()
