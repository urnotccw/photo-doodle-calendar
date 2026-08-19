# Image Generation Prompt Scaffold

Use this reference when building the final image-generation request. Replace bracketed values and remove irrelevant lines.

```text
Use case: stylized-concept
Asset type: wide horizontal monthly calendar ticket
Input images: Image 1 is the source photo and subject reference. [Image 2 is a style reference only.]

Primary request: Create a [YEAR] [MONTH] three-panel ticket calendar from Image 1.

Left panel: Use Image 1 edge to edge with a proportional crop. Keep [SUBJECT], [POSE], and [KEY DETAILS] recognizable. Crop away any platform watermark or account overlay when possible without harming the subject.

Middle panel: Show an elegant and accurate [MONTH] [YEAR] calendar. Use large '[MM]' and '[MON.]' at upper-left and small '[YEAR]' at upper-right. Week headers exactly '[WEEKDAY ORDER]'. Use this exact date grid: [WRITE EVERY ROW, INCLUDING LEADING AND TRAILING BLANKS].

Right panel: Redraw the main subject as a compact, charming handmade doodle. Use chunky uneven black crayon/colored-pencil outlines, slight double lines, simplified friendly facial features, restrained blush where appropriate, and loose incomplete color fills that leave paper visible. Preserve [IDENTITY CUES]. Keep the illustration centered and occupying only 55%-65% of the panel, with at least 15% empty background on every side. No part may touch the ticket edge or perforation notch.

Composition: Landscape ticket close to 3:1. Left photo about 30%, center calendar about 45%, right doodle about 25%. Use semicircular separator notches, softly scalloped outer edges, and warm ivory fibrous paper.

Color palette: Center panel [DARK SOURCE-DERIVED COLOR] with warm cream serif text. Right panel [LIGHT RELATED OR COMPLEMENTARY COLOR]. Doodle accents [2-4 SOURCE COLORS]. Avoid an orange-dominant or monochrome result unless requested.

Constraints: The calendar must be correct and legible. The year must appear at the center panel's upper-right. No date may be circled, highlighted, underlined, boxed, bolded, recolored, marked, or decorated. No text, logo, or watermark in the doodle panel.

Avoid: realistic pencil portrait, dense hatching, polished vector art, excessive cuteness, extreme chibi, huge doll eyes, baby face, distorted anatomy, malformed hands, extra fingers, duplicate held objects, full-panel doodle, artwork touching edges, decorative handwriting, date markers.
```

## Targeted Retry Prompts

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
