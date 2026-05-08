# 7iter Overall Manager System

## Purpose
One overall manager owns Item 1~4 and every forked item such as Item 1-1 and Item 3-1.

This layer is not a set of LLM-specific documents. It is a repo-native control log so work done by OpenClaw, local Codex, Gemini, Claude, OpenAI, Grok, or any other external/local tool can be checked later through a single audit trail.

## Correct model
- One manager controls all projects/items.
- Items keep their own context/history/status.
- External LLM/local runs are recorded as log entries under `external-llm-logs/`.
- GitHub Issues/Project remain the public tracker.

## Managed items
- Item 1 — Mosaic Year App
- Item 1-1 — Semantic Object Mosaic Lab
- Item 2 — Reactive Keyboard Goods / SOUL modules
- Item 3 — AI Story Business Card
- Item 3-1 — Transparent Jellyfish Business Card
- Item 4 — Hologram Business Card

## Core loop
Representative comment → manager checks item context/history → manager creates/updates job → implementation happens → external/local LLM work is logged if used → item HISTORY/STATUS updated → GitHub issue/project updated.
