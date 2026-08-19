# Design Specification

Use this reference when composing or reviewing the calendar card.

## Canvas And Ticket

- Use a standard landscape raster canvas around 16:9. An aspect ratio from 1.8:1 to 2:1 is acceptable.
- Do not default to a 3:1 full canvas. That creates an overly long banner and removes the intended breathing room.
- Center one connected ticket on a warm ivory, lightly fibrous paper field.
- The ticket should occupy about 88%-92% of the canvas width and 60%-68% of its height, leaving obvious outer margin above and below.
- Keep the inner ticket itself around 2.2:1 to 2.5:1 so it feels long without making the whole image ultra-wide.
- Three adjacent panels with stable proportions:
  - Left photo: 30%.
  - Center calendar: 45%.
  - Right doodle: 25%.
- Small semicircular notches where panels meet.
- Softly scalloped outer vertical edges.
- Flat printed colors with subtle paper grain; no drop-shadow-heavy card UI.

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

Always provide the image model with an explicit date grid. Do not merely say "an accurate calendar".

## Right Doodle Panel

- Use a lighter related background color and preserve its paper texture.
- Draw one compact vignette centered slightly above the visual middle.
- Target 55%-65% panel occupancy and at least 15% clear margin on every side.
- Prefer a bust, waist-up, seated, or otherwise compact pose when a full body would fill the panel.
- Keep the key gesture and identifying details, but remove background clutter.

### Line And Fill

- Rough black crayon, charcoal, or wax-pencil outline.
- Slightly wobbly contours, occasional double strokes, and imperfect joins.
- Sparse internal lines; avoid realistic crosshatching across the entire figure.
- Flat, scribbled fills with small uncolored gaps.
- Two to four accent colors sampled from the photo.
- Optional small blush circles for a human face.

### Cuteness Level

- Friendly and softly stylized rather than childish.
- Head may be modestly enlarged, but the body and limbs remain plausible.
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
