# MVP_SPEC

## 1. MVP goal
Build a demoable web app that lets a user upload a personal photo set, generate a large mosaic image from those photos, explore it with zoom, and unlock/download a higher-quality export.

## 2. Core v1 features
### Must-have
1. **Photo upload**
   - Drag-and-drop or mobile picker
   - Batch upload of 100-1000 images
   - Basic validation (file type, count, total size)

2. **Target image selection**
   - Upload one target image
   - Or choose from a few built-in templates for demo reliability

3. **Mosaic generation pipeline**
   - Resize and normalize uploaded photos
   - Compute color signature per tile
   - Match tiles to target image regions
   - Render final mosaic image

4. **Interactive viewer**
   - Zoom and pan on web/mobile
   - Inspect individual tiles at closer zoom levels

5. **Preview/export split**
   - Low-res/watermarked preview for free
   - High-res export behind a paywall or gated button stub for demo

6. **Simple project persistence**
   - Temporary job/session save so generation is resumable

### Nice-to-have if easy
- Style presets (classic / vibrant / clean)
- Auto date-range label (“Your 2025 Mosaic”)
- Short auto-generated zoom video

## 3. Out of scope for v1
- Full social network/community features
- Multi-user collaboration
- Native mobile apps
- Face clustering, smart curation, or semantic search
- Complex subscriptions
- Advanced print fulfillment integration
- Heavy account/profile systems

## 4. Recommended architecture
### Frontend
- Landing page + upload/generation flow
- Viewer page for preview and export unlock

### Backend
- Upload endpoint
- Job queue for mosaic processing
- Storage for originals, processed tiles, preview, and final export
- Payment hook or placeholder checkout step

### Processing pipeline
1. Receive uploads
2. Generate thumbnails / normalized tiles
3. Analyze target image grid
4. Match tile candidates by average color / simple similarity metric
5. Compose preview image
6. Compose higher-resolution export asset
7. Publish result to viewer

## 5. Recommended stack
### Best practical MVP stack
- **Frontend:** Next.js
- **UI:** Tailwind CSS
- **Backend/API:** Next.js server routes or lightweight Node service
- **Image processing:** Sharp + custom mosaic generator logic
- **Storage:** S3-compatible object storage
- **DB:** Postgres or Supabase
- **Queue/background jobs:** BullMQ + Redis, or hosted async job alternative
- **Payments:** Stripe Checkout (or mock checkout in demo phase)
- **Viewer:** OpenSeadragon or similar zoomable image viewer

### Why this stack
- Fast to prototype
- Good Node image tooling
- Easy deploy path
- Clean handoff from MVP to production

## 6. Data model (minimal)
- **Project**
  - id
  - created_at
  - status
  - target_image_url
  - preview_url
  - export_url
  - style_preset
- **SourcePhoto**
  - id
  - project_id
  - original_url
  - thumb_url
  - capture_date (optional)
  - dominant_color
- **Payment/Unlock**
  - id
  - project_id
  - unlock_type
  - status

## 7. Main technical risks
1. **Performance / processing time**
   - Large batches can be slow
   - Mitigation: thumbnail-first pipeline, async jobs, preview-first rendering

2. **Upload friction**
   - Users may abandon if upload is slow or fragile
   - Mitigation: chunked uploads, progress UI, clear recommended limits

3. **Output quality inconsistency**
   - Some target images work poorly with limited photo sets
   - Mitigation: built-in templates, minimum photo guidance, automatic quality score

4. **Mobile UX**
   - Large zoomable assets can feel heavy on phones
   - Mitigation: tiled viewer, progressive loading

5. **Storage cost**
   - Original photos are heavy
   - Mitigation: retention policy, auto-delete raw uploads after export window

## 8. MVP success bar
A successful v1 should prove:
- people understand the concept quickly
- upload + generation is reliable enough for demos
- output is visually impressive on first use
- zoom exploration creates delight
- users understand why they would pay for the clean export

## 9. Suggested build sequence
1. Hardcoded demo with sample assets
2. Upload + target image flow
3. Background generation pipeline
4. Zoomable viewer
5. Export asset generation
6. Payment/unlock layer
