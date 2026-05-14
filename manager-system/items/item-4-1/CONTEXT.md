# Item 4-1 Context — MBTI 8-question Card Generator

## Parent
- Parent issue: #4 Item 4 — Hologram Business Card
- Managed issue: #12 Item 4-1 — MBTI 8-question Card Generator

## Current Product Idea
A user answers 8 lightweight situation questions, receives an MBTI-like result, then sees a gacha/card-opening animation and a generated animal-style holo character card.

## Key Assets
- Public mock: `docs/item4-1/index.html`
- Spec: `item-4-hologram-business-card/ITEM4_1_MBTI_CARD_SPEC.md`
- Dictionary: `item-4-hologram-business-card/mbti_card_dictionary.json`
- API orchestration map: `item-4-hologram-business-card/ITEM4_1_API_ORCHESTRATION_MAP.md`

## Constraints
- Entertainment-only personality framing.
- Avoid protected IP names, characters, logos, and franchise references.
- Keep MBTI scoring deterministic before any GPT call.
- Treat image generation as optional async queue due cost/latency.
