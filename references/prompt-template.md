# Image Generation Prompt Scaffold

Use this reference when building the final image-generation request. Replace bracketed values and remove irrelevant lines.

```text
Use case: stylized-concept
Asset type: landscape monthly calendar card with a centered horizontal ticket
Input images: Image 1 is the source photo and subject reference. [Image 2 is a style reference only.]

Primary request: Create a [YEAR] [MONTH] three-panel ticket calendar from Image 1.

Ticket print specification: the inner three-panel ticket, not the surrounding preview canvas, will be printed at exactly 25 x 10 cm, 2953 x 1181 px, 300 PPI. Keep the ticket exactly 2.5:1 and use the same specification for every image in the series.

Left panel: Use Image 1 edge to edge with a proportional crop. Keep [SUBJECT], [POSE], and [KEY DETAILS] recognizable. Crop away any platform watermark or account overlay when possible without harming the subject.

Middle panel: Show an elegant and accurate [MONTH] [YEAR] calendar. Use large '[MM]' and '[MON.]' at upper-left and small '[YEAR]' at upper-right. Week headers exactly '[WEEKDAY ORDER]'. Use this exact date grid: [WRITE EVERY ROW, INCLUDING LEADING AND TRAILING BLANKS].

Right panel: Redraw the main subject as a compact, charming handmade doodle. Use chunky uneven black crayon/colored-pencil outlines, slight double lines, simplified friendly facial features, restrained blush where appropriate, and loose incomplete color fills that leave paper visible. Preserve [IDENTITY CUES]. [For a full-body adult: keep the complete standing pose and adult anatomy at roughly 1:6 to 1:7.5 head-to-body height; head 13%-17% of total figure height; legs 45%-52%; preserve the natural waistline and long-leg silhouette. Do not use a five-five or chibi proportion.] Keep the illustration centered and occupying only 55%-65% of the panel, with at least 15% empty background on every side. No part may touch the ticket edge or perforation notch.

Composition: Use a standard 16:9 landscape preview canvas, never a 3:1 full-canvas banner unless explicitly requested. The preview is not the print region. Place the printable inner ticket at stable bounds: left 5%, top 18%, right 95%, bottom 82%. The ticket must be exactly 2.5:1, leaving clearly visible warm-ivory preview margins. Within it, use a left photo panel about 30%, center calendar about 45%, and right doodle panel about 25%. Keep all three panels connected and aligned. Use semicircular separator notches, softly scalloped outer edges, and warm ivory fibrous paper. Do not stretch any panel.

Color palette: Center panel [DARK SOURCE-DERIVED COLOR] with warm cream serif text. Right panel [LIGHT RELATED OR COMPLEMENTARY COLOR]. Doodle accents [2-4 SOURCE COLORS]. Avoid an orange-dominant or monochrome result unless requested.

Constraints: The calendar must be correct and legible. The year must appear at the center panel's upper-right. No date may be circled, highlighted, underlined, boxed, bolded, recolored, marked, or decorated. No text, logo, or watermark in the doodle panel.

Avoid: ultra-wide full-canvas banner, realistic pencil portrait, dense hatching, polished vector art, excessive cuteness, extreme chibi, huge doll eyes, oversized head, five-five head-to-body silhouette, short compressed legs, low childlike waist, baby face, distorted anatomy, malformed hands, extra fingers, duplicate held objects, full-panel doodle, artwork touching edges, decorative handwriting, date markers.
```

## Targeted Retry Prompts

### Canvas Is Too Wide

```text
Reframe the preview onto a standard 16:9 landscape canvas. Keep the existing three-panel ticket exactly 2.5:1 at stable bounds: left 5%, top 18%, right 95%, bottom 82%. Restore visible warm-ivory preview margin above and below. Preserve the panel proportions and content; do not stretch any panel. The ticket will be extracted separately for printing at 25 x 10 cm.
```

### Doodle Is Too Large

```text
Change only the right-panel illustration. Scale it down to occupy 55%-60% of the panel, use a compact waist-up vignette, and leave at least 15%-20% uninterrupted background on all four sides. Preserve every other panel exactly.
```

### Doodle Is Too Realistic

```text
Change only the right-panel rendering style. Replace realistic shading and dense hatching with chunky uneven crayon outlines, simplified features, restrained blush, sparse internal lines, and incomplete scribbled fills. Preserve the pose and identifying details.
```

### Calendar Is Wrong

```text
Change only the center calendar panel. Preserve its color, typography, heading positions, ticket geometry, photo, and doodle. Replace the date grid with this exact layout: [GRID]. Do not mark any date.
```

### Cuteness Is Too Strong

```text
Change only the doodle proportions. Keep the friendly handmade style, but reduce head enlargement and eye size, restore adult age cues and natural limbs, and preserve the source pose and outfit.
```

### Full-Body Proportions Are Wrong

```text
Change only the right-panel full-body doodle anatomy. Keep the same rough crayon style, expression, pose, outfit, colors, and panel placement. Restore an adult 1:6 to 1:7.5 head-to-body ratio: head about 13%-17% of total height, natural waist placement, and legs about 45%-52% of total height. The figure must read as a graceful adult, not a five-five, big-head, short-leg, or chibi character. Preserve clear empty space above the head and below the feet.
```
