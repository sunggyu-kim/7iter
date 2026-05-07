# Game Card Mapping Spec — Item 4

## Goal
Turn a person’s business-card data into an IP-safe, retro game-card inspired collectible layout while keeping the card useful as a premium identity object.

## Field Mapping
| Game-card area | Business-card meaning | Demo implementation |
|---|---|---|
| Card name | Person name | Top-left large serif title, editable via `nameInput` |
| HP | HP/contact number | Top-right red HP line, editable via `hpInput` |
| Type | Favorite icon / personal symbol | Circular icon beside HP, editable via `typeInput` |
| Evolution stage | Age or career stage | Small line below name, editable via `ageInput` |
| Illustration area | Personal photo | Central framed portrait; URL/data URL input can replace placeholder |
| Attack | Job-related witty term | Rules panel first row: attack title + explanation |
| Ability | Personality/passive effect | Rules panel second row: passive title + explanation |
| Weakness | Personal secret | Hidden band; blurred until strong tilt angle |
| Resistance | Personal resilience/secret | Hidden band; blurred until strong tilt angle |
| Retreat Cost | Funny personal cost/habit | Hidden band; blurred until strong tilt angle |
| Card number | Identity/set number | Bottom-left footer |
| Rarity | Premium tier/rarity | Bottom-right stars/text |

## Holo Materials
1. **Circle foil** — dimensionalized radial/conic material, replacing the rough single-circle feel.
2. **Grid** — grid shimmer with diagonal reflective passes.
3. **Glitch/static** — scanline and jitter pattern for a zizzling digital foil look.
4. **Prism 3D** — layered prismatic glare and material bands for the most premium 3D feel.

## Interaction Rules
- Pointer/touch position controls `--mx`, `--my`, rotateX, rotateY, glare intensity, and secret reveal strength.
- Hidden secrets are intentionally hard to read at neutral angle.
- Reduce-motion mode keeps the layout accessible while preserving the static look.

## IP Safety
- No brand names, logos, characters, or proprietary card-frame names.
- Use generic wording: “retro game-card inspired”, “collectible card”, “holo material”.
