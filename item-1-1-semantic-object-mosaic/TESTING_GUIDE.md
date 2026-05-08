# Testing Guide

## Local validation
```bash
python3 -m py_compile item-1-1-semantic-object-mosaic/scripts/*.py
python3 -m http.server 8000 --directory docs
# open http://127.0.0.1:8000/item1-1/
```

## Acceptance checks
- Target object recognizable from distance.
- All cells are image tiles.
- Background cells are not blank.
- Public page does not reference private assets.
