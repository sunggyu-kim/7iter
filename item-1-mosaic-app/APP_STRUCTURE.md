# APP_STRUCTURE

## Purpose
A light implementation structure for building the MVP without overengineering.

## Suggested app modules
### 1. Marketing / landing
- Hero section with zoom-reveal demo
- Simple CTA: upload your year of photos
- Pricing / unlock explanation

### 2. Project creation flow
- Upload source photos
- Select/upload target image
- Choose style preset
- Submit generation job

### 3. Processing layer
- Image normalization
- Tile analysis
- Target-grid matching
- Preview render
- HD render

### 4. Result viewer
- Mosaic preview page
- Zoom/pan interaction
- Watermark on locked preview
- CTA to unlock export

### 5. Admin / ops basics
- Job status view
- Failed job retry
- Storage cleanup policy

## Minimal folder idea
```text
app/
  page.tsx                  # landing
  create/page.tsx           # upload/create flow
  project/[id]/page.tsx     # result viewer
  api/
    projects/
    uploads/
    checkout/

components/
  upload-dropzone.tsx
  target-selector.tsx
  mosaic-viewer.tsx
  pricing-card.tsx

lib/
  mosaic/
    analyze-source.ts
    analyze-target.ts
    match-tiles.ts
    render-preview.ts
    render-export.ts
  storage/
  db/
  jobs/

workers/
  generate-mosaic.ts

public/
  demo-assets/
```

## Prototype-first recommendation
Build in this order:
1. One polished sample demo
2. Working upload flow
3. Async generation job
4. Result viewer with zoom
5. Export/paywall step

This keeps the project sellable early, even before full automation is perfect.
