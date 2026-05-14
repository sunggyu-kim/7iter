# Item 4-1 — API Orchestration Map

## Goal
Connect the current static **MBTI 8-question Card Generator** mock to a real API-driven service.

Representative requirement:
- Explain every app stage.
- Describe the backend/API connection separately.
- Use an n8n-like orchestration map so the flow can be understood as nodes, triggers, branches, and outputs.

## Recommended MVP Architecture

```text
[Web/App]
  ↓ POST /api/item4-1/sessions
[Session API]
  ↓
[Question Engine]
  ↓ POST /api/item4-1/answers
[MBTI Scoring Node]
  ↓
[Card Trait Generator: GPT]
  ↓
[Image Prompt Generator: GPT]
  ↓ optional
[Image Generation Queue]
  ↓
[Card Renderer]
  ↓
[Share / Save / Payment]
```

### Why this structure
- The 8-question MBTI scoring is deterministic and cheap. Do **not** send raw answers to GPT until scoring is complete.
- GPT should generate only card text/trait flavor after MBTI is known.
- Image generation should be queued separately because it is slower, more expensive, and may fail independently.
- Card rendering can happen on the client first, then later be rendered server-side for high-resolution export/payment fulfillment.

## n8n-style Node Map

| Node | Type | Input | Output | Notes |
|---|---|---|---|---|
| 01. Start Trigger | Webhook | user opens `/item4-1/` | `session_id` | Creates anonymous session. |
| 02. Consent Gate | UI/API | privacy notice accepted | `consent=true` | Required if photo/name/birthday are added later. |
| 03. Question Screen | Frontend | 8 fixed questions | answer array | No AI call. |
| 04. Validate Answers | API Function | answer array | normalized answers | Reject incomplete/invalid payload. |
| 05. MBTI Scoring | API Function | normalized answers | `mbti` + score details | Deterministic E/I, S/N, T/F, J/P pair scoring. |
| 06. Dictionary Lookup | API Function | `mbti` | base type/icon/tone | Uses `mbti_card_dictionary.json`. |
| 07. GPT Trait Draft | OpenAI/GPT node | mbti + dictionary + optional nickname | attack, ability, weakness, defense | Use structured JSON mode. |
| 08. Prompt Draft | OpenAI/GPT node | mbti + type + tone | character image prompt | Text-free animal-style prompt. |
| 09. Safety/Policy Filter | Function | generated JSON/prompt | safe JSON | Blocks trademark names, celebrity likeness, medical/fortune claims. |
| 10. Gacha Loading Event | Frontend | status stream | progress states | UI-only animation while nodes 07~09 complete. |
| 11. Card JSON Persist | DB | safe card JSON | `card_id` | Store result for share/reopen. |
| 12. Optional Image Queue | Queue worker | image prompt | image job id/result URL | Async because image generation is expensive. |
| 13. Card Renderer | Frontend or server | card JSON + image | rendered card | Client for MVP, server for export/payment. |
| 14. Share/Payment Branch | Payment/API | selected product | order id | Later revenue path. |
| 15. Analytics Event | Analytics | stage events | funnel metrics | Needed for conversion testing. |

## App Stage-by-Stage Explanation

### Stage 0 — Landing / Start
**User sees:** short explanation, `Start` button.  
**API action:** create session.

```http
POST /api/item4-1/sessions
```

Response:

```json
{
  "session_id": "i41_20260514_abcd",
  "status": "created",
  "next": "questions"
}
```

### Stage 1 — 8 Situation Questions
**User sees:** 8 binary choices.  
**API action:** none until submit, or incremental autosave if desired.

Submit payload:

```http
POST /api/item4-1/answers
```

```json
{
  "session_id": "i41_20260514_abcd",
  "answers": [
    {"question_id": 1, "selected_axis": "E"},
    {"question_id": 2, "selected_axis": "N"},
    {"question_id": 3, "selected_axis": "F"},
    {"question_id": 4, "selected_axis": "P"},
    {"question_id": 5, "selected_axis": "I"},
    {"question_id": 6, "selected_axis": "N"},
    {"question_id": 7, "selected_axis": "T"},
    {"question_id": 8, "selected_axis": "P"}
  ]
}
```

### Stage 2 — Deterministic MBTI Scoring
**User sees:** loading begins.  
**API action:** calculate MBTI without GPT.

Scoring rule:

```text
Q1,Q5 → E/I
Q2,Q6 → S/N
Q3,Q7 → T/F
Q4,Q8 → J/P
Tie rule: choose the axis selected in the later paired question, or ask a tie-break question in v2.
```

Response:

```json
{
  "session_id": "i41_20260514_abcd",
  "mbti": "ENFP",
  "scores": {"E": 1, "I": 1, "S": 0, "N": 2, "T": 1, "F": 1, "J": 0, "P": 2},
  "base_profile": {
    "type": "Fire",
    "emoji": "🔥",
    "tone": "분위기 점화"
  },
  "next": "generate_card"
}
```

### Stage 3 — GPT Card Trait Generation
**User sees:** gacha animation / card pack opening.  
**API action:** call GPT with strict JSON schema.

```http
POST /api/item4-1/cards/generate
```

Minimum request:

```json
{
  "session_id": "i41_20260514_abcd",
  "mbti": "ENFP",
  "language": "ko",
  "style": {
    "holo_style": "prism",
    "background": "gold",
    "title_holo": true
  },
  "optional_user_inputs": {
    "nickname": "대표님",
    "photo_url": null
  }
}
```

Expected response:

```json
{
  "card_id": "card_i41_enfp_001",
  "mbti": "ENFP",
  "card": {
    "character_name": "Spark Fox",
    "level": 37,
    "type": "Fire",
    "preferred_icon": "🔥",
    "holo_style": "prism",
    "background": "gold",
    "rarity": "Ultra Rare + Signature",
    "attack": {
      "name": "분위기 점화",
      "power": 90,
      "description": "어색한 흐름을 빠르게 밝히고 팀의 행동 에너지를 끌어올린다."
    },
    "ability": {
      "name": "아이디어 점프",
      "description": "막힌 문제를 전혀 다른 각도에서 다시 열어본다."
    },
    "summary": "밝은 반응성과 상상력으로 주변의 가능성을 확장하는 Fire type 카드.",
    "weakness": "반복적인 루틴에는 집중력이 빠르게 떨어질 수 있음.",
    "defense_mechanism": "농담과 즉흥 제안으로 긴장감을 흩뜨림.",
    "card_number": "4-1-ENFP-037"
  },
  "image_prompt": "consistent animal-style collectible card character, energetic fire fox mascot, premium illustration, no text in image, same series style, square composition",
  "next": "render"
}
```

### Stage 4 — Character Image Generation
**User sees:** optional `캐릭터 이미지 생성 중`.  
**API action:** queue image generation.

```http
POST /api/item4-1/images/jobs
```

```json
{
  "card_id": "card_i41_enfp_001",
  "prompt": "consistent animal-style collectible card character...",
  "size": "1024x1024",
  "transparent_background": false
}
```

Response:

```json
{
  "image_job_id": "imgjob_123",
  "status": "queued",
  "poll_url": "/api/item4-1/images/jobs/imgjob_123"
}
```

### Stage 5 — Card Render
**User sees:** generated card.  
**API action:** return card JSON; frontend renders immediately. Later server-side rendering can export PNG/PDF.

```http
GET /api/item4-1/cards/card_i41_enfp_001
```

Response includes:
- card attributes
- rarity level
- image URL if ready
- share URL
- export options

### Stage 6 — Share / Payment / Fulfillment
**User sees:** save/share/order CTA.  
**API action:** create checkout or order.

MVP revenue branch:

```text
Free: low-res share card + watermark
Paid A: high-res image export
Paid B: animated holo short video
Paid C: physical holo card print order
Paid D: 16-type collectible pack / group event pack
```

## GPT Prompt Drafts

### System Prompt

```text
You generate fictional, entertainment-only collectible identity card traits.
Never mention any protected monster/card-game franchise, character, logo, or brand.
Do not produce medical, psychological diagnosis, fate claims, or deterministic personality judgments.
Return only valid JSON matching the schema.
Tone: playful, premium, card-game inspired, Korean-first.
```

### User Prompt Template

```text
Generate one MBTI-inspired animal character card.

Inputs:
- MBTI: {{mbti}}
- Type: {{type}}
- Emoji/Icon: {{emoji}}
- Tone: {{tone}}
- Language: {{language}}
- Optional nickname: {{nickname}}
- Rarity rule: {{rarity_rule}}

Required fields:
character_name, level, type, preferred_icon, attack.name, attack.power, attack.description,
ability.name, ability.description, summary, weakness, defense_mechanism, card_number, image_prompt.

Constraints:
- image_prompt must describe an original animal-like character.
- no text, logo, trademark, known character, celebrity, or franchise reference in image_prompt.
- weakness and defense_mechanism should be light, relatable, not insulting.
- card_number format: 4-1-{{mbti}}-NNN.
```

## Minimal Backend API List

| Method | Path | Purpose | Needed for MVP? |
|---|---|---:|---:|
| POST | `/api/item4-1/sessions` | create session | Yes |
| POST | `/api/item4-1/answers` | submit answers + score MBTI | Yes |
| POST | `/api/item4-1/cards/generate` | GPT card text + image prompt | Yes |
| GET | `/api/item4-1/cards/:card_id` | reload/share result | Yes |
| POST | `/api/item4-1/images/jobs` | optional image generation | v1.1 |
| GET | `/api/item4-1/images/jobs/:id` | poll image job | v1.1 |
| POST | `/api/item4-1/exports` | PNG/PDF/video render | v1.2 |
| POST | `/api/item4-1/checkout` | paid flow | v1.2 |

## Data Storage

### Tables / Collections

```text
item41_sessions
- session_id
- created_at
- consent_version
- locale
- source

item41_answers
- session_id
- answers_json
- mbti
- scores_json
- created_at

item41_cards
- card_id
- session_id
- mbti
- card_json
- image_prompt
- image_url
- rarity
- created_at

item41_orders
- order_id
- card_id
- product_type
- payment_status
- fulfillment_status
```

## Cost Control

- Cache generated card JSON by `mbti + language + style + nickname hash`.
- Run GPT only after all 8 answers are submitted.
- Use cheaper model for text traits; reserve expensive models for image prompt refinement only if needed.
- Do not generate all 16 images per user by default. Generate only the final MBTI card first.
- Add daily spend cap and per-IP/session rate limit.

## Safety / Privacy

- MBTI result is entertainment only, not a psychological diagnosis.
- If photo upload is enabled later, delete originals after card rendering unless user explicitly saves.
- Birthday/saju scenario should be framed as entertainment, not factual fate prediction.
- Block trademark names and franchise references in prompts and outputs.
- Avoid using real-person likeness unless the user uploads their own photo and consents.

## Implementation Options

### Option A — Fastest MVP: Vercel + Serverless + OpenAI
- Frontend: current static `docs/item4-1/index.html` migrated to Next.js or Vite.
- API: Vercel serverless routes.
- DB: Supabase or Vercel Postgres.
- Queue: simple DB status polling first.
- Best for: quick public test.

### Option B — n8n-first Prototype
- Frontend posts to n8n webhook.
- n8n nodes handle scoring, GPT call, safety filtering, and DB insert.
- Best for: visual orchestration demo and fast iteration.
- Risk: less polished for production, harder to version-control complex workflows.

### Option C — Production Service
- Frontend: Next.js.
- Backend: FastAPI or NestJS.
- Queue: Redis/BullMQ or Cloud Tasks.
- Storage: S3/R2 for images/exports.
- Best for: paid export and print fulfillment.

## Recommended Next Build Order

1. Keep current static mock as the review UI.
2. Add a local mock API returning deterministic fake GPT JSON.
3. Replace fake generator with GPT structured JSON.
4. Add card persistence and share URL.
5. Add optional image queue.
6. Add export/payment only after conversion signal exists.

## Test Checklist

- [ ] 16 MBTI outcomes can be reached from answer combinations.
- [ ] Tie cases are deterministic and explained.
- [ ] GPT response always validates against schema.
- [ ] Banned IP tokens are filtered.
- [ ] Korean output uses: 공격, 특성, 약점, 방어기제.
- [ ] Card can render without generated image.
- [ ] Image job failure does not lose card text.
- [ ] Cost estimate per generated card is logged.
- [ ] Share URL works without exposing private raw answers.
