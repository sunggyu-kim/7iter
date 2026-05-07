# SG90 Clicker Mount CAD v0.1

## Files
- `sg90_clicker_mount_v0_1.scad` — OpenSCAD parametric CAD source
- `sg90_clicker_mount_preview_v0_1.stl` — rough printable/preview mesh generated from the layout
- `sg90-clicker-mount-dimensions.svg` — top/side dimension reference
- `assembly-render.svg` — visual assembly concept

## Purchased parts reflected
- MicroServo 9g SG90
- USB/WiFi ESP32-C3 SuperMini

## Intended mechanism
The SG90 sits in a vertical cradle. A short servo horn/lever presses a target key or plunger. The ESP32-C3 receives the completion signal and drives LED + servo.

## Print notes
- Units: millimeters
- Base: 90 × 70 × 3 mm
- Verify SG90 body/tab/hole dimensions before final print
- Verify exact ESP32-C3 SuperMini board dimensions and USB connector direction before final print
