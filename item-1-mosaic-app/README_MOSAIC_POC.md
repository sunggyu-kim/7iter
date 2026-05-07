# Mosaic Year — low-distortion mosaic PoC

## What changed after the latest comment

- Referenced the YouTube video `How I rendered 17,731 Donuts` (`jv3GijkzIdk`) as a production insight: build a mosaic from many repeated, individually recognizable units, then let distance/scale create the representative image. The useful product takeaway is **quantity + placement + zoomable inspection**, not recoloring each unit until it stops feeling like a memory.
- Pulled the public Drive folder listing and downloaded the available shared images into `sample/`.
- The folder listing did **not** include `standard.jpg`; therefore the generated demo uses `IMG_4265.jpeg` as a clearly marked fallback target and excludes it from the tile pool.

## Current sample status

- Drive folder title: `item1-mosaic_photo`
- Public image files found: 50 JPEGs
- Download result: 50/50 JPEGs saved to `sample/`
- Required representative file: `sample/standard.jpg` ❌ missing in public folder listing
- Manifest: `sample/drive_manifest.tsv`

## Mosaic strategy: preserve existing photos

The PoC intentionally avoids strong transformations:

1. EXIF-rotate each source image correctly.
2. Center-crop to the square tile cell.
3. Resize only.
4. Match tiles to target cells by average RGB color.
5. Apply a reuse penalty so the same tile is not overused too early.
6. Report color gaps; fill those gaps with newly generated/acquired images instead of hue-shifting old memories.

No tint, hue rotation, opacity overlay, or per-tile color wash is applied.

## Demo outputs

- Mosaic preview: `mockup/generated/mosaic_demo.jpg`
- Source tile contact sheet: `mockup/generated/tile_contact_sheet.jpg`
- Quality report: `mockup/generated/mosaic_report.json`
- Representative HTML: `mockup/decision_mockup.html`
- Flow SVG: `mockup/low_distortion_pipeline.svg`

## Run commands

```bash
cd /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter/item-1-mosaic-app

# Re-download public Drive files from the parsed manifest
./scripts/download_drive_samples.py

# Preferred final run once standard.jpg is supplied
./scripts/mosaic_poc.py --target sample/standard.jpg --tiles sample --cols 42 --cell 28

# Current demo run because standard.jpg is missing
./scripts/mosaic_poc.py --allow-fallback-target --cols 36 --cell 24
```

## Decision needed

Please add/rename the representative image as `standard.jpg` in the Drive folder or place it at `sample/standard.jpg`. After that, the same script will generate the real representative mosaic without fallback.
