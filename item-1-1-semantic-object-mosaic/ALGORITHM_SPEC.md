# Algorithm Spec

## Target preprocessing
- EXIF transpose.
- Resize target.
- Optional segmentation mask.
- Grid target into cells.

## Cell classification
- object cell if mask coverage >= threshold.
- background cell otherwise.

## Tile analysis
For each tile:
- average RGB/Lab color
- brightness
- saturation
- edge density
- white/background ratio
- optional class label

## Matching
Object cells:
- prioritize semantic class / contrast / target color distance.

Background cells:
- use real tiles with high white/sky/background ratio.
- never use blank solid blocks.

## Report fields
- target source
- mask source
- grid size
- object cell count
- background cell count
- tile counts by pool
- hard match ratio
- unmatched color families
- warnings
