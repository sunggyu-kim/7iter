# History Context — Item 1-1

## Source item
- Original folder: `item-1-mosaic-app/`
- Public page: `docs/item1/index.html`
- Source issue: GitHub issue #1

## Timeline
1. Original annual image mosaic concept.
2. Drive sample PoC:
   - Drive-derived outputs are not public-safe.
3. GitHub Pages fix:
   - Pages root is `/docs`.
   - Anything outside `/docs` is not directly served.
4. Imagenette public dataset mosaic:
   - public ImageNet-derived fallback.
   - target: `n03028079 · church`.
5. Round 4:
   - object readability issue identified.
   - object/background separation proposed.
6. Round 5 correction:
   - every cell must be an image tile.
   - NULL/background cannot be blank white/color.
   - production should use MS COCO segmentation/object labels.
7. Round 6 fork:
   - Item 1-1 created as separate semantic object mosaic project.

## Critical constraints
- Do not publish private Drive photos.
- Do not use blank cells as final mosaic cells.
- Do not solve color mismatch by heavily tinting user images.
