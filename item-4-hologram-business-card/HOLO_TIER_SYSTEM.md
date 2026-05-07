# Holo Card Tier System — Digital Identity Card

## Design intent
A single digital business card should feel collectible without using any third-party card-game IP. The tier system borrows the general idea of trading-card rarity, foil zones, and reveal intensity, but uses original naming, patterns, and interaction rules.

## Tier ladder

| Tier | Short label | Surface language | Motion / light behavior | Best use |
|---|---|---|---|---|
| Common | `COMMON` | Premium matte base, one small satin accent | Soft edge sheen on card border only | Conservative executives, first MVP default |
| Rare | `RARE` | Gradient foil band + subtle micro-dots | Cursor/touch sweep reveals one diagonal prism band | Personal brand, creators, sales intros |
| Super | `SUPER` | Multi-zone foil: name, portrait rim, keyword chips | Stronger tilt parallax; background grid moves slower than highlight | Event networking, landing page hero preview |
| Secret | `SECRET` | Hidden glyph field + serial/tier stamp + star/prism scatter | Hidden message appears only at high tilt; chromatic glow blooms around portrait | Premium upsell, limited-run campaign, VIP gift |
| Signature | `SIGNATURE` | Monochrome luxury card with name-only holo signature | Very restrained light sweep; no loud background | Founder/CEO version, black-card aesthetic |

## Original pattern vocabulary
Use generic, non-infringing pattern families:

- **Prism Grid**: repeating diamond/triangle interference lines.
- **Aura Wave**: flowing contour lines around the portrait.
- **Spectral Dust**: low-opacity star/noise particles, not character art.
- **Hidden Glyphs**: abstract initials, role icons, or brand-safe symbols.
- **Serial Foil**: small edition code such as `ID-004 / SECRET`.

## Tier rules for implementation

1. **Common** keeps the card readable even with effects disabled.
2. **Rare** introduces one active highlight layer.
3. **Super** adds depth: background, portrait, and text foil move at different rates.
4. **Secret** adds a hidden reveal zone and stronger chromatic color split.
5. **Signature** is a separate premium restraint track, not necessarily louder than Secret.

## IP safety guardrails

- Do not use third-party character silhouettes, card backs, logos, elemental symbols, set icons, or trade dress.
- Avoid exact frame compositions associated with named franchises.
- Keep names generic: `Common`, `Rare`, `Super`, `Secret`, `Signature` are product rarity descriptors only.
- Generate all patterns procedurally or from customer-owned brand assets.
