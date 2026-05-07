# Item 1 — issue #1 round 2 response

## Summary

- Rechecked the public Drive folder `item1-mosaic_photo` directly from the folder page.
- Updated downloader and mosaic scripts to recognize `standard`, `STANDARD`, `.jpg`, `.jpeg`, `.png` case-insensitively.
- Result: **STANDARD representative image was not visible in the public Drive folder listing from this environment**.
- Because STANDARD was not found, the real representative mosaic was **not** generated. The fallback demo mosaic was regenerated only for pipeline validation.
- Created a public-safe web page at `docs/item1/index.html` for GitHub Pages review without raw/private photos.

## Evidence for STANDARD search

Command run:

```bash
cd /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter/item-1-mosaic-app
./scripts/download_drive_samples.py --refresh-manifest --find-standard --skip-download | tee logs/standard_search_round2.log
```

Observed output:

```text
REFRESHED_MANIFEST	sample/drive_manifest.tsv	50 rows
STANDARD_MATCH	NONE	checked=50	candidates=[]
```

Matching rule now used by the script:

- basename: `standard` or `STANDARD` or any case variation
- extension: `.jpg`, `.jpeg`, `.png` or any case variation

## Mosaic regeneration result

Because no STANDARD file was found, the real target mosaic is blocked. I regenerated the existing fallback demo to prove the pipeline still works:

```bash
./scripts/mosaic_poc.py --allow-fallback-target --cols 36 --cell 24 | tee logs/mosaic_poc_round2.log
```

Observed summary:

```text
wrote mockup/generated/mosaic_demo.jpg
wrote mockup/generated/tile_contact_sheet.jpg
wrote mockup/generated/mosaic_report.json
avg_distance=108.64 hard_ratio=0.5237
NOTE: standard/STANDARD jpg/jpeg/png was missing; demo target substituted with IMG_4265.jpeg
```

Important: `mockup/generated/mosaic_demo.jpg` and `tile_contact_sheet.jpg` are Drive-photo-derived local outputs. Do **not** publish them to public GitHub Pages.

## GitHub Pages / 404 finding

Likely 404 cause: the shared docs site is published from `/docs`. Links like:

```html
../item-1-mosaic-app/mockup/decision_mockup.html
```

point outside the `/docs` publish root, so GitHub Pages cannot serve them and returns GitHub 404.

Fix applied:

- `docs/index.html` now links Item 1 PoC/review to `item1/`.
- `docs/item1/index.html` contains a public-safe demo and testing instructions.

Expected public URL after Pages publishes from `/docs`:

```text
https://sunggyu-kim.github.io/7iter/item1/
```

## Public / private publishing rule

Safe to publish:

- `docs/item1/index.html`
- `docs/item1/assets/public-placeholder-mosaic.svg`
- `docs/index.html` link fix
- scripts and Markdown docs

Do not publish to public GitHub:

- `item-1-mosaic-app/sample/*`
- `item-1-mosaic-app/mockup/generated/mosaic_demo.jpg`
- `item-1-mosaic-app/mockup/generated/tile_contact_sheet.jpg`
- any real STANDARD image from Drive
- any real mosaic generated from private Drive photos unless explicitly approved for public use

## Next step when STANDARD is added

```bash
cd /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter/item-1-mosaic-app
./scripts/download_drive_samples.py --refresh-manifest --find-standard --skip-download
./scripts/download_drive_samples.py --download-standard
./scripts/mosaic_poc.py --tiles sample --cols 42 --cell 28
```

If the first command prints `STANDARD_MATCH`, the second downloads it to `sample/STANDARD.<ext>`, and the third uses it automatically as the target.
