# 7iter Mockup Review Guide

## 목적
이전 보고서 중심 산출물을 대표가 직접 보고 판단할 수 있는 **사이트 / 이미지 / CAD 도면** 중심 산출물로 정교화했다.

## 직접 볼 파일
- `docs/index.html` — item1~4 통합 목업 사이트
- `docs/assets/item1-mosaic-year.svg`
- `docs/assets/item2-sg90-clicker.svg`
- `docs/assets/item2-cad-dimensions.svg`
- `docs/assets/item3-storycard-flow.svg`
- `docs/assets/item4-hologram-card.svg`

## Item별 판단 포인트
1. **Item 1**: zoom reveal 순간이 충분히 감탄을 주는가
2. **Item 2**: SG90 딸깍 동작이 촬영 가능한 상징성을 주는가
3. **Item 3**: 입력 → 생성 → 결제 CTA 흐름이 빠르게 이해되는가
4. **Item 4**: Black Signature Reveal이 프리미엄 실물 샘플로 충분한가

## GitHub Project 업데이트 원칙
- 각 issue에 이번 변경사항을 comment로 남긴다.
- Project status는 대표 검토가 가능한 상태인 `In review`로 옮긴다.
- Priority는 빠른 검증/사업 임팩트 기준으로 조정한다.


## 2026-05-08 Manager System Update

- Corrected repo-native `manager-system/` to one Overall Manager.
- One Overall Manager owns Item 1~4 and all forked items, including Item 1-1 and Item 3-1.
- External/local LLM work is tracked through date-based log files under `manager-system/external-llm-logs/`, not per-LLM markdown files.
- Added per-item CONTEXT/HISTORY/STATUS/JOBS/GITHUB records for async updates across OpenClaw, local Codex, Gemini, Claude/OpenAI/Grok, and future 3D tools.


## 2026-05-08 Manager System Correction
- Corrected misunderstanding: one Overall Manager controls all items/forks.
- Removed per-LLM docs and per-item manager1~4 directories.
- Added `manager-system/external-llm-logs/` for local Codex/OpenClaw/Gemini/etc update traces.
- Retired GitHub issues #7~#10; use Overall Manager issue #11.
