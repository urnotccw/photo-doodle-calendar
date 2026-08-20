# Calendar Panel Layout

Use this deterministic layout for the center panel of the default `1772 x 709 px` print master.

## Panel Geometry

- Center panel bounds in the print master: `x=532..1329`, width `797 px`, height `709 px`.
- Physical center-panel size: `67.5 x 60 mm`.
- Local coordinate origin: the center panel's upper-left corner.
- Safe margins: left and right `64 px`; top and bottom `43 px`.

## Heading

| Element | Local anchor | Size | Alignment |
|---|---:|---:|---|
| Two-digit month `MM` | `(64, 43)` | `106 px` | left/top |
| Abbreviated month `Mon.` | `(67, 150)` | `38 px` | left/top |
| Four-digit year `YYYY` | `(733, 55)` | `26 px` | right/top |

Use a classic regular-weight serif such as Cormorant Garamond, Libre Baskerville, or Georgia. Use warm cream `#f5e8c8` unless contrast requires another near-white.

## Calendar Grid

- Default weekday order: `Sun Mon Tue Wed Thu Fri Sat`.
- Column centers: `80, 186, 292, 399, 505, 611, 717 px`.
- Weekday baseline: `y=258 px`; weekday size: `24 px`.
- Reserve six stable date rows at `y=321, 381, 441, 501, 562, 621 px`.
- Date size: `30 px`; center every label in its cell.
- Keep unused leading, trailing, or sixth-row cells empty.
- Draw no grid lines, borders, selected states, circles, underlines, boxes, or date decorations.

## Date Placement

Number weekdays from Sunday:

```text
Sun=0, Mon=1, Tue=2, Wed=3, Thu=4, Fri=5, Sat=6
offset = weekday index of the month's first day
column = (offset + day - 1) mod 7
row = floor((offset + day - 1) / 7)
```

Always calculate the grid outside the image model. Prefer programmatic text placement for a final print file; otherwise provide the complete seven-column grid explicitly in the image-generation prompt.
