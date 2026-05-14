# 7iter Overall Roadmap

## 2026-05-08 ~ 2026-05-10 — Item 2 SW signal capture
- Goal: define and test start/done inference signal capture via host/port webhook.
- Scope: OpenClaw Linux local test first; Codex/Mac environment requires separate validation.
- Output: `item-2-reactive-keyboard-goods/software/` signal server/client and test guide.

## 2026-05-12 ~ 2026-05-14 — Item 2 HW second revision
- HW v0.2 capsule is marked first-pass complete.
- Next revision should use real dimensional references and replace concept-only STL placeholders with proper OpenSCAD-exported models.

## 2026-05-08 ~ 2026-05-12 — Item 4 service/revenue design
- Item 4 design draft is treated as roughly complete.
- Work stream A: photo + MBTI → GPT-derived attack/ability/weakness/defense mechanism.
- Work stream B: name + birthday → 사주 prompt + character activation + card traits.
- Output: service pipeline, prompts, platform/revenue report.

## 2026-05-14 ~ 2026-05-16 — Item 4-1 API orchestration and mock backend
- Goal: connect the MBTI 8-question static mock to a real API/GPT-ready architecture.
- Work stream A: stage-by-stage app/API map in n8n-style nodes.
- Work stream B: local mock API for answer submit → MBTI score → card JSON.
- Work stream C: GPT structured JSON prompt and safety filter validation.
- Output: `ITEM4_1_API_ORCHESTRATION_MAP.md`, then mock API prototype.
