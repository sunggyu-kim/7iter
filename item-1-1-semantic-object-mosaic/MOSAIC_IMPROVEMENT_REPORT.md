# Item 1-1 Mosaic Improvement Report

## What changed now
- Replaced the hand-drawn/synthetic cat-like standard image with a real transparent cat image from Wikimedia Commons.
- Regenerated the public static demo mosaic using real image tiles for both object and NULL/background cells.
- Kept the rule: no blank color cells.

## Why the mosaic still looks imperfect
The current public demo uses a small existing tile pool. Even if every cell is a real image, object readability is limited when the tile pool lacks enough color, texture, and edge diversity.

## Improvement methods

### 1. Larger tile pool
Use COCO/OpenImages or a larger user photo pool. A larger pool improves color/texture coverage without heavy recoloring.

### 2. Segmentation with SAM / Mask R-CNN / COCO masks
Separate object/background precisely. Object cells should use object-like tiles; background cells should use sky/white/background-like tiles.

### 3. CLIP/DINO semantic matching
Match object cells using semantic embeddings, not only RGB distance. This helps eyes/ears/fur/body cells use visually compatible tiles.

### 4. LAB color + edge density matching
Use CIE Lab color distance, local contrast, and edge orientation. This preserves silhouette better than average RGB.

### 5. Multi-scale / hierarchical mosaic
Render a coarse mosaic first, then split hard regions into smaller cells. This reduces blockiness around ears, eyes, and body contours.

### 6. Saliency-weighted matching
Give high weight to eyes, face outline, and ears. Less important body/background regions can tolerate weaker matches.

### 7. Learned optimization
A learned tile selector or differentiable mosaic optimization could optimize object recognizability directly. This is the strongest path but requires more compute/training.

### 8. Curated filler tile generation
If the memory/photo tile pool lacks bright background tiles, generate or source additional public filler image tiles rather than painting blank white cells.

## Practical next step
For the next build, run a COCO cat/person target with segmentation mask and a larger public tile pool, then compare:
- RGB-only matcher
- LAB+edge matcher
- CLIP/DINO semantic matcher
- multi-scale matcher
