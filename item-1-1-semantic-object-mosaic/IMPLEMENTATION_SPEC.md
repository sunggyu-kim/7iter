# Implementation Spec

## Pipeline
1. Load target image.
2. Run segmentation or use provided mask.
3. Split target grid into object cells and background/NULL cells.
4. Analyze tile pool:
   - dominant color
   - brightness
   - saturation
   - semantic label if available
   - white/background area ratio
5. Select candidate pools:
   - object pool
   - background/null pool
6. Match each cell to a real image tile.
7. Render mosaic.
8. Export mosaic image, contact sheet, JSON report, public-safe web demo assets.

## Non-goals
- Full upload SaaS.
- Payment.
- private Drive publishing.
