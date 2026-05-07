# Software Interpretation of 3D Holographic Card Methodology

## Reference status
The requested PledgeBox article URL (`https://www.pledgebox.com/post/3-d-holographic-cards`) returned HTTP 403 from this environment, so the prototype uses the general 3D/holographic card methodology implied by the request: layered depth, parallax, lenticular-like view changes, and angle-reactive specular highlights.

## Physical-method concept → software equivalent

| Physical 3D/holo idea | Software equivalent in this prototype |
|---|---|
| Lenticular depth layers | Separate CSS layers for background grid, portrait window, name foil, glare, and hidden message |
| Card tilt changes reflected light | Mouse/touch position maps to CSS variables `--mx`, `--my`, `--rx`, `--ry` |
| Holographic foil film | Animated conic/linear gradients blended with `screen`, `overlay`, and masks |
| Secret/high-rarity reveal | Opacity threshold and transform change when tilt distance exceeds a set value |
| Printed edition stamp | Tier badge and serial metadata embedded in the card face |
| 3D object feel | `perspective`, `rotateX`, `rotateY`, `translateZ`, and shadow displacement |

## Prototype implementation

File: `mockup/holo-trading-card/index.html`

- Pure HTML/CSS/JS; no build step.
- Pointer and touch movement update light source and tilt.
- Tier buttons switch CSS state (`common`, `rare`, `super`, `secret`, `signature`).
- Portrait is represented by an original abstract avatar placeholder, not a third-party image.
- QR is represented by a safe mock pattern. Replace with a generated real QR later.

## Interaction model

1. User moves cursor or finger over the card.
2. JS normalizes the pointer to `0..1` x/y coordinates.
3. CSS variables drive:
   - glare position,
   - holo gradient angle,
   - 3D rotation,
   - portrait/background parallax,
   - secret reveal opacity.
4. On pointer leave, the card eases back to a neutral collectible-card pose.

## Next production steps

- Replace placeholder avatar and QR with user-provided assets.
- Add export states: static PNG thumbnail, animated MP4/GIF, embeddable web card.
- Add device orientation support for mobile (`DeviceOrientationEvent`) after permission handling.
- Add configurator controls for tier, color palette, keyword chips, and hidden copy.
- Define print-safe mapping if this later becomes a physical sample: matte base, spot UV, foil zone, laminate choice.
