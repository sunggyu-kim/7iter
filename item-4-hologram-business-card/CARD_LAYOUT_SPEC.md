# Holographic Digital Business Card — Layout Spec

## Assumption
One card contains: name, photo, description, QR, social/contact links, and rarity/tier metadata. The prototype is digital-first, but dimensions and zones are chosen so it can later inform a physical print mock.

## Canvas

- Default ratio: **2.5:3.5 trading-card portrait** for collectibility.
- Prototype size: `420 x 588 px`, scalable via CSS.
- Safe margin: `24 px`.
- Corner radius: `26 px`.
- Accessibility: all essential identity text remains visible without holo effects.

## Front layout

| Zone | Position | Content | Holo treatment |
|---|---|---|---|
| Tier rail | Top-left, vertical/compact | Tier label + edition code | Metallic stamp with small sweep |
| Identity header | Top 10–22% | Name, role/title | Name receives foil gradient for Rare+ |
| Portrait window | Center 26–60% | Photo/avatar | Depth rim, aura wave, tilt parallax |
| Description panel | Lower 61–78% | 1–2 sentence intro or positioning line | Glass panel; Secret tier reveals hidden line on tilt |
| Keyword chips | Lower 78–87% | 3 social/professional keywords | Tiny foil chips for Super+ |
| Contact strip | Bottom 87–96% | QR, handle, website/social | QR remains high-contrast; only frame shines |

## Back / expanded digital state

For a web profile or tap-expanded state:

- Larger QR and CTA: `Scan / Save Contact / Portfolio`.
- Social links: website, LinkedIn, Instagram/X, email.
- Optional “proof of edition” metadata: tier, generated date, edition number.
- Optional animated background preview matching the front.

## Content guidelines

- **Name**: maximum 24 characters for large type, then auto-fit.
- **Photo**: square or portrait crop; face/object centered.
- **Description**: 90–130 Korean characters or 70–100 English words max for readability.
- **QR**: minimum 72 px on prototype; physical version should follow print QR minimums.
- **Social**: show one primary handle on front; place extras in expanded/back state.

## Tier-specific layout deltas

- `COMMON`: flat portrait window, satin border, no hidden copy.
- `RARE`: one diagonal holo sweep across name and frame.
- `SUPER`: portrait, name, and background each receive different parallax speeds.
- `SECRET`: hidden message panel appears at tilt threshold; edition stamp is prominent.
- `SIGNATURE`: removes decorative chips; emphasizes large name signature and QR frame.
