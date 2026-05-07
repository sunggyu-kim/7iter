# Item 1 Publication Note

Drive sample images were downloaded and tested locally as requested, but this repository is public.

Therefore the following are intentionally excluded from GitHub publication unless 대표님 explicitly approves publishing them:

- `sample/*.jpeg` raw Drive images
- `logs/drive_folder_page.html` / related Drive scraping logs
- `mockup/generated/mosaic_demo.jpg` generated from Drive images
- `mockup/generated/tile_contact_sheet.jpg` generated from Drive images

Public-safe files retained for GitHub:

- `scripts/mosaic_poc.py`
- `README_MOSAIC_POC.md`
- `COMMENT_RESPONSE.md`
- `mockup/decision_mockup.html` using `public_placeholder_mosaic.svg`
- `mockup/low_distortion_pipeline.svg`

Local reproduction command when `standard.jpg` is available:

```bash
./scripts/mosaic_poc.py --target sample/standard.jpg --tiles sample --cols 42 --cell 28
```
