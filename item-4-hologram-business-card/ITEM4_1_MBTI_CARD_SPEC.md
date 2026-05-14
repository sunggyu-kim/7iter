# Item 4-1 — MBTI 8-question Card Generator

## Scope
GitHub issue #4 latest comment is split into new managed task **Item 4-1**.

## Flow
1. Start screen: answer 8 situation questions.
2. Score pairs: Q1/Q5 = E/I, Q2/Q6 = S/N, Q3/Q7 = T/F, Q4/Q8 = J/P.
3. Loading screen: gacha/card draw animation.
4. Result: MBTI card with type, level, icon, character name, attack, passive trait, weakness, defense mechanism, card number.
5. Image prompt: generate 16 consistent animal-style character images, no text in image, consistent size.

## Data
- Dictionary: `mbti_card_dictionary.json`
- Public mock: `docs/item4-1/index.html`

## Managed as
- GitHub issue: #12 Item 4-1
- Parent context: #4 Item 4 Hologram Business Card

## API Connection Plan
- Orchestration/API map: `ITEM4_1_API_ORCHESTRATION_MAP.md`
- Recommended first implementation: deterministic scoring API + GPT structured JSON card generator + optional async image queue.
