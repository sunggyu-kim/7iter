# Mosaic Year testing guide

## 1) GitHub Pages web review

After the repository is published with GitHub Pages source set to `/docs`, open:

```text
https://sunggyu-kim.github.io/7iter/item1/
```

Expected:

- Page title: `Item 1 — Mosaic Year Safe Web Demo`
- A large public-safe placeholder mosaic appears.
- The page states `PUBLIC SAFE PAGE · no raw Drive photos`.
- No raw Drive JPEGs are loaded by the browser.
- The old GitHub 404 should be gone because the docs index now links to `item1/`, not `../item-1-mosaic-app/...`.

## 2) Local docs web server test

```bash
cd /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter
python3 -m http.server 8000 --directory docs
```

Open:

```text
http://localhost:8000/
http://localhost:8000/item1/
```

Expected:

- `/` shows the integrated 7iter mockup page.
- The Item1 buttons open `/item1/`.
- `/item1/` loads `assets/public-placeholder-mosaic.svg` successfully.
- Browser devtools Network should show no requests to `item-1-mosaic-app/sample/`.

## 3) Recheck Drive for STANDARD

```bash
cd /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter/item-1-mosaic-app
./scripts/download_drive_samples.py --refresh-manifest --find-standard --skip-download
```

Expected when STANDARD is still missing:

```text
REFRESHED_MANIFEST	sample/drive_manifest.tsv	50 rows
STANDARD_MATCH	NONE	checked=50	candidates=[]
```

Expected when STANDARD exists in Drive as `STANDARD.jpg`, `STANDARD.jpeg`, `STANDARD.png`, or lower/mixed case:

```text
STANDARD_MATCH	STANDARD.jpg	<drive-file-id>	image/jpeg
```

## 4) Download STANDARD and generate real mosaic

Run only after command #3 shows a `STANDARD_MATCH`:

```bash
./scripts/download_drive_samples.py --download-standard
./scripts/mosaic_poc.py --tiles sample --cols 42 --cell 28
```

Expected:

- `STANDARD_DOWNLOAD` line is true.
- `mockup/generated/mosaic_demo.jpg` is generated using `sample/STANDARD.<ext>` as target.
- `mockup/generated/mosaic_report.json` has `fallback_note: null`.

## 5) Script / image validation

```bash
cd /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter/item-1-mosaic-app
python3 -m py_compile scripts/download_drive_samples.py scripts/mosaic_poc.py
python3 - <<'PY'
from pathlib import Path
from PIL import Image
import json
for p in ['mockup/generated/mosaic_demo.jpg','mockup/generated/tile_contact_sheet.jpg']:
    im = Image.open(p); im.verify(); print('IMAGE_VERIFY', p, 'ok')
report = json.loads(Path('mockup/generated/mosaic_report.json').read_text())
print('REPORT_TARGET', report['target'])
print('REPORT_FALLBACK', report['fallback_note'])
PY
```

Expected:

- Python compile exits with code 0.
- Both JPEGs verify with PIL.
- If STANDARD is absent, fallback note explains the substituted demo target.
- If STANDARD is present, fallback note is `None`/`null`.

## 6) Public safety check before any push

Do not include these in public GitHub Pages or public commits unless explicitly approved:

```text
item-1-mosaic-app/sample/*
item-1-mosaic-app/mockup/generated/mosaic_demo.jpg
item-1-mosaic-app/mockup/generated/tile_contact_sheet.jpg
any STANDARD original image
any real mosaic generated from private Drive photos
```

Safe public web artifacts:

```text
docs/item1/index.html
docs/item1/assets/public-placeholder-mosaic.svg
docs/index.html
```
