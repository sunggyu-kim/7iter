# Item 1 — ImageNet-derived public dataset mosaic

## Summary

Latest issue comment requested replacing Drive photos with a labeled public dataset and showing a real mosaic where a representative image is formed from mosaic tile images selected by label.

This round uses **Imagenette 2 160px**, a public fast.ai subset derived from ImageNet classes. Direct ImageNet original access is gated/heavy, so Imagenette is the practical reproducible fallback while still preserving ImageNet class labels (`n########` WordNet IDs).

- Dataset source: <https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-160.tgz>
- Dataset page/background: <https://github.com/fastai/imagenette>
- Split used: `val/`
- Drive image usage: **none**

## Label-based selection

### Representative target

- `n03028079` — `church`
- Reason: a church image has a recognizable building silhouette plus sky/dark/bright regions, making it suitable for checking whether the target image is readable from the sum of tiles.
- Prepared target: `public_data/imagenette_mosaic/target/n03028079_church_target.jpg`
- Published target preview: `../docs/item1/assets/imagenette-target-church.jpg`

### Mosaic tile pool

The target label is excluded from tiles. The tile pool uses a balanced deterministic set: 12 validation images per remaining Imagenette label.

| WNID | Label | Count |
|---|---:|---:|
| `n01440764` | tench | 12 |
| `n02102040` | English springer | 12 |
| `n02979186` | cassette player | 12 |
| `n03000684` | chain saw | 12 |
| `n03394916` | French horn | 12 |
| `n03417042` | garbage truck | 12 |
| `n03425413` | gas pump | 12 |
| `n03445777` | golf ball | 12 |
| `n03888257` | parachute | 12 |

Total tile images: **108**.

Selection manifest and summary:

- `public_data/imagenette_mosaic/selection_manifest.csv`
- `public_data/imagenette_mosaic/selection_summary.json`

## Generated outputs

Published under `docs/item1/assets/` because they are public dataset derivatives, not private Drive photo derivatives.

- Actual mosaic: `docs/item1/assets/imagenette-mosaic-output.jpg` — 864×576
- Target image: `docs/item1/assets/imagenette-target-church.jpg` — 240×160
- Tile contact sheet: `docs/item1/assets/imagenette-tile-contact-sheet.jpg` — 1388×2168
- JSON report: `docs/item1/assets/imagenette-mosaic-report.json`

The updated web page is `docs/item1/index.html`.

## Reproduction commands

```bash
cd /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter/item-1-mosaic-app

mkdir -p public_data
curl -L -o public_data/imagenette2-160.tgz \
  https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-160.tgz
tar -xzf public_data/imagenette2-160.tgz -C public_data

./scripts/prepare_imagenette_mosaic.py \
  --dataset-root public_data/imagenette2-160 \
  --out public_data/imagenette_mosaic \
  --target-wnid n03028079 \
  --tiles-per-label 12

./scripts/mosaic_poc.py \
  --dataset-name 'Imagenette 2 160px (fast.ai ImageNet-derived subset)' \
  --target public_data/imagenette_mosaic/target/n03028079_church_target.jpg \
  --tiles public_data/imagenette_mosaic/tiles \
  --out ../docs/item1/assets/imagenette-mosaic-output.jpg \
  --report ../docs/item1/assets/imagenette-mosaic-report.json \
  --cols 48 \
  --cell 18

cp ../docs/item1/assets/tile_contact_sheet.jpg \
  ../docs/item1/assets/imagenette-tile-contact-sheet.jpg
rm -f ../docs/item1/assets/tile_contact_sheet.jpg
```

## Script changes

- `scripts/prepare_imagenette_mosaic.py` added to prepare target/tile images from labeled Imagenette folders.
- `scripts/mosaic_poc.py` reused and improved:
  - keeps the original low-distortion mosaic process,
  - accepts `--dataset-name`,
  - infers ImageNet/Imagenette label metadata from WNID in file paths/names,
  - writes `target_label`, `tile_label_counts`, and `tile_wnid_counts` to the JSON report.

## Test / validation

Run from repository root:

```bash
cd /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter
python3 -m py_compile item-1-mosaic-app/scripts/mosaic_poc.py item-1-mosaic-app/scripts/prepare_imagenette_mosaic.py
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
HTMLParser().feed(Path('docs/item1/index.html').read_text(encoding='utf-8'))
print('html parse ok')
PY
python3 - <<'PY'
from PIL import Image
for p in [
  'docs/item1/assets/imagenette-target-church.jpg',
  'docs/item1/assets/imagenette-mosaic-output.jpg',
  'docs/item1/assets/imagenette-tile-contact-sheet.jpg',
]:
  img = Image.open(p); img.verify(); print(p, 'ok')
PY
python3 -m http.server 8000 --directory docs
# then GET http://127.0.0.1:8000/item1/
```

## Limitations

- Imagenette 160px is intentionally small and only has 10 classes; color coverage is limited.
- The current report shows a high `hard_match_cell_ratio` because many target cells require dark/sky/white color buckets that the small tile pool does not fully cover.
- For production-quality output, use a larger ImageNet-derived/public labeled set or increase selected labels/images, while preserving the same label-based selection and no-recolor tile rule.
