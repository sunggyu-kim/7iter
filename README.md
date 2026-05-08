# 7iter

`7iter`는 바이브코딩을 마케팅/제품화 요소로 쓰기 위한 4개 아이템 실험 프로젝트입니다.

## 바로 볼 것

- **통합 목업 사이트**: `docs/index.html`
- **목업 리뷰 가이드**: `MOCKUP_REVIEW_GUIDE.md`
- **진행 업데이트**: `PROJECT_PROGRESS_UPDATE.md`
- **GitHub 보고 요약**: `GITHUB_REPORT.md`

GitHub Pages가 활성화되면 아래 주소에서 직접 볼 수 있습니다.

- https://sunggyu-kim.github.io/7iter/

## 아이템 구성

### Item 1 — Mosaic Year App
- 폴더: `item-1-mosaic-app/`
- 성격: 연간 사진을 하나의 zoom-reveal mosaic artwork로 만드는 감성형 디지털 상품
- 직접 볼 파일:
  - `docs/assets/item1-mosaic-year.svg`
  - `item-1-mosaic-app/mockup/mosaic-year-hero.svg`
  - `item-1-mosaic-app/MOCKUP_SPEC.md`

### Item 2 — Reactive Keyboard Goods / SG90 Clicker
- 폴더: `item-2-reactive-keyboard-goods/`
- 성격: AI 추론 완료 순간을 LED + SG90 딸깍 동작으로 보여주는 책상 위 오브젝트
- 구매 현물 반영:
  - MicroServo 9g SG90
  - USB/WiFi ESP32-C3 SuperMini
- 직접 볼 파일:
  - `docs/assets/item2-sg90-clicker.svg`
  - `docs/assets/item2-cad-dimensions.svg`
  - `item-2-reactive-keyboard-goods/cad/sg90_clicker_mount_v0_1.scad`
  - `item-2-reactive-keyboard-goods/cad/sg90_clicker_mount_preview_v0_1.stl`
  - `item-2-reactive-keyboard-goods/MOCKUP_AND_CAD_SPEC.md`

### Item 3 — AI Story Business Card + Storyboard App
- 폴더: `item-3-businesscard-storyboard-app/`
- 성격: 입력 1분 → 명함 + 3컷 스토리보드 → 유료 export로 이어지는 빠른 검증형 앱
- 직접 볼 파일:
  - `docs/assets/item3-storycard-flow.svg`
  - `item-3-businesscard-storyboard-app/mockup/storycard-flow.svg`
  - `item-3-businesscard-storyboard-app/MOCKUP_SPEC.md`

### Item 4 — Hologram Business Card
- 폴더: `item-4-hologram-business-card/`
- 성격: Black Signature Reveal 방향의 프리미엄 AI-personalized identity object
- 직접 볼 파일:
  - `docs/assets/item4-hologram-card.svg`
  - `item-4-hologram-business-card/mockup/black-signature-reveal.svg`
  - `item-4-hologram-business-card/MOCKUP_SPEC.md`

## GitHub Project 운영 방식

- Repository: 문서, 목업, CAD, 시각 자료 저장
- Issues: item1~4 실행 단위 분리
- Project: Status / Priority / Size로 현재 진행상태 추적

현재 issue 구성:

- #1 Item 1 — Mosaic Year App
- #2 Item 2 — Reactive Keyboard Goods
- #3 Item 3 — AI Story Business Card + Storyboard App
- #4 Item 4 — Hologram Business Card

## 현재 판단

- 빠른 매출 검증: **Item 3**
- 프리미엄 실물 대표샘플: **Item 4**
- 감성형 바이럴/출력 상품: **Item 1**
- 가장 상징적인 하드웨어 데모: **Item 2**


## Round 2 직접 확인 링크

GitHub Pages `/docs` 기준으로 각 item별 직접 확인 page를 추가했습니다.

- Home: https://sunggyu-kim.github.io/7iter/
- Item 1: https://sunggyu-kim.github.io/7iter/item1/
- Item 2: https://sunggyu-kim.github.io/7iter/item2/
- Item 3: https://sunggyu-kim.github.io/7iter/item3/
- Item 4: https://sunggyu-kim.github.io/7iter/item4/

상세 요약: `ROUND2_WEB_VISUALIZATION_SUMMARY_2026-05-07.md`


## 2026-05-07 Item 1 ImageNet-derived Mosaic Update

Issue #1 최신 comment에 따라 Drive 이미지가 아니라 라벨링된 공공 ImageNet-derived dataset으로 mosaic 결과를 생성했습니다.

- Dataset: Imagenette 2 160px, fast.ai public ImageNet-derived subset
- Target label: `n03028079 · church`
- Tile labels: target 제외 9개 Imagenette label × 12장 = 108장
- Web result: `docs/item1/index.html`
- Output image: `docs/item1/assets/imagenette-mosaic-output.jpg`
- Target image: `docs/item1/assets/imagenette-target-church.jpg`
- Contact sheet: `docs/item1/assets/imagenette-tile-contact-sheet.jpg`
- Repro docs: `item-1-mosaic-app/IMAGENET_DATASET_MOSAIC.md`


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
