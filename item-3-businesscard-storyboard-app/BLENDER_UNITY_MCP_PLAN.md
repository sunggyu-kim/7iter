# Blender / Unity / MCP Plan for Item 3-1

## Current tool availability from this Linux host
- blender: `not found`
- unity/unityhub: `not found`

## Current decision
No Blender/Unity MCP execution was available in this OpenClaw run. Therefore the immediate deliverable is a web-safe HTML/SVG 3D-like asset plus saved reference sources.

## Recommended 3D workflow
1. Collect jellyfish references and define silhouette/volume target.
2. Blender:
   - model bell shell as translucent mesh,
   - add bevelled rim,
   - create curve tentacles with bevel depth,
   - add emissive cyan/violet material,
   - export GLB.
3. Web:
   - use model-viewer or three.js for GLB preview if file size is acceptable,
   - keep static SVG fallback for GitHub Pages.
4. Unity:
   - only needed if later interactive mobile/app rendering is selected.

## Acceptance
A viewer should read the object as a transparent volumetric jellyfish, not an emoji or flat icon.
