# Design Specification

Use this reference when composing or reviewing the calendar card.

## Two Required Outputs

Create both files from one shared artwork:

1. **Print master:** an opaque rectangular `150 x 60 mm` image at `1772 x 709 px`, `300 PPI`, PNG. The three panels fill the complete canvas. There is no surrounding background, padding, transparency, hole, notch, scallop, rounded corner, or shadow.
2. **Presentation preview:** a separate 16:9 image derived from the verified print master. It adds the warm paper field and ticket-shaped mask for presentation only.

Never regenerate the preview independently. Deriving it from the print master guarantees identical dates, photo crop, doodle, and colors.

## Canvas And Ticket

- Use a standard 16:9 landscape preview canvas. The preview canvas is not the printable object and does not determine physical print size.
- The complete three-panel rectangle is the print region. Keep it exactly 2.5:1 with straight outer edges.
- Default print master: exactly `150 x 60 mm`, `1772 x 709 px`, `300 PPI`, PNG.
- In the presentation preview, place the masked ticket at stable normalized bounds: left `5%`, top `18%`, right `95%`, bottom `82%`.
- A user-specified ticket size may replace the default, but convert it to one exact pixel width and height and keep that specification unchanged across the whole series.
- Extract the full straight-edged rectangle while excluding the temporary production field. Normalize it edge to edge with no padding. If the extracted ratio differs materially from 2.5:1, correct the generation instead of cropping important panel content.
- Do not default to a 3:1 full canvas. That creates an overly long banner and removes the intended breathing room.
- Center one connected ticket on a warm ivory, lightly fibrous paper field.
- The ticket should occupy about 88%-92% of the canvas width and 60%-68% of its height, leaving obvious outer margin above and below.
- Keep the inner ticket itself around 2.2:1 to 2.5:1 so it feels long without making the whole image ultra-wide.
- Three adjacent panels with stable proportions:
  - Left photo: 30%, `45 mm`, `532 px`.
  - Center calendar: 45%, `67.5 mm`, `797 px`.
  - Right doodle: 25%, `37.5 mm`, `443 px`.
- Integer print-master boundaries: photo `x=0..532`, calendar `x=532..1329`, doodle `x=1329..1772`.
- The print master has no notches or scallops.
- The preview mask uses semicircular notches where panels meet and softly scalloped outer vertical edges.
- Flat printed colors with subtle paper grain; no drop-shadow-heavy card UI.

### Print Export

- Export the rectangular print master as PNG to avoid repeated lossy compression. Generate the presentation preview from that PNG.
- Set the file's PPI metadata to `300` by default. PPI metadata does not replace the required pixel dimensions; both must be checked.
- Keep important content inside the rectangle. Add bleed only when the user or print shop supplies an exact bleed requirement.
- Reopen the exported master and confirm exactly `1772 x 709 px`, opaque RGB, and filled at all four corners. A visually correct image with the wrong dimensions or decorative holes is not a finished print deliverable.

### Preview Edge Geometry

Apply these values only to the presentation preview, scaling them from the ticket height:

- Outer corner cutout radius: `2%` of ticket height (`14 px` at print-master scale).
- Separator notch radius: `2%` of ticket height (`14 px` at print-master scale).
- Separator centers: at `30%` and `75%` of ticket width, on both the top and bottom edges.
- Left and right scalloped edges: `16` cycles per vertical edge.
- Scallop inward depth: `1.5%` of ticket height (`11 px` at print-master scale).
- Top and bottom edges remain straight except for the separator notches.
- Preview field: warm ivory `#f3eedf`, lightly fibrous, with only a faint contact shadow.

## Left Photo Panel

- Use a proportional cover crop; never stretch the image.
- Favor the face or primary subject plus one or two identifying objects or gestures.
- Keep useful context when it explains the pose, but remove empty or distracting background first.
- Crop away platform watermarks and account text when possible without harming the subject.
- Do not synthesize a replacement photo or alter the subject's identity unless requested.

## Center Calendar Panel

- Large `MM` at upper-left, with `Mon.` directly below.
- Four-digit year at upper-right.
- Seven weekday columns below the heading.
- Four to six stable date rows depending on the month.
- Classic serif typography, warm cream color, generous spacing.
- The calendar area should feel calm and editorial, not like an app widget.
- No selected-day treatment by default.

For the default `797 x 709 px` center panel, use the deterministic layout in [calendar-layout.md](calendar-layout.md). Prefer programmatic text placement when exact printing matters.

Always provide the image model with an explicit date grid. Do not merely say "an accurate calendar".

## Right Doodle Panel

- Use a lighter related background color and preserve its paper texture.
- Draw one compact vignette centered slightly above the visual middle.
- Target 55%-65% panel occupancy and at least 15% clear margin on every side.
- Prefer a compact crop for portrait sources. For a full-body source whose stance or outfit is important, keep the complete figure and scale it down instead of changing it to a bust or waist-up pose.
- Keep the key gesture and identifying details, but remove background clutter.
- For an adult full-body source, use roughly 1:6 to 1:7.5 head-to-body height: head about 13%-17% of the complete figure and legs about 45%-52%.
- Preserve the source waistline, limb length, stance, and outfit silhouette. Do not enlarge the head or compress the legs to make the drawing cute.
- Let line softness, small facial marks, restrained blush, and loose color fill carry the charm.

### Line And Fill

- Rough black crayon, charcoal, or wax-pencil outline.
- Slightly wobbly contours, occasional double strokes, and imperfect joins.
- Sparse internal lines; avoid realistic crosshatching across the entire figure.
- Flat, scribbled fills with small uncolored gaps.
- Two to four accent colors sampled from the photo.
- Optional small blush circles for a human face.

### Cuteness Level

- Friendly and softly stylized rather than childish.
- For portraits or half-body figures, the head may be modestly enlarged while the body and limbs remain plausible. For adult full-body figures, do not enlarge the head beyond roughly one-sixth of total figure height.
- Eyes may be simplified and slightly rounder, but not oversized anime-doll eyes unless present in the source.
- Preserve age cues, hairstyle, pose, outfit, and accessories.

## Palette Selection

Build a small palette from the source:

1. Pick a dominant dark or medium hue for the center panel.
2. Pick a lighter adjacent or complementary hue for the right panel.
3. Use warm cream for calendar text.
4. Reserve source-specific colors for doodle accents.

Examples of varied pairings:

- Deep teal center + butter-yellow doodle panel.
- Aubergine center + pale blue-gray doodle panel.
- Forest green center + light celadon doodle panel.
- Indigo center + powder-blue doodle panel.
- Muted red center + blush-pink doodle panel.

Do not force orange when the source suggests a better palette.
