# 7iter GitHub Report

## 2026-05-07 업데이트 요약

이전 산출물은 대표 검토용 문서 중심이었으나, 이번 업데이트에서는 대표가 직접 볼 수 있는 **목업 사이트 / SVG 이미지 / item2 3D CAD** 중심으로 정교화했다.

## GitHub 구조

- Repository: `https://github.com/sunggyu-kim/7iter`
- Project: `https://github.com/users/sunggyu-kim/projects/2`
- Pages mockup URL: `https://sunggyu-kim.github.io/7iter/`

## 바로 볼 산출물

- 통합 목업 사이트: `docs/index.html`
- 목업 리뷰 가이드: `MOCKUP_REVIEW_GUIDE.md`
- 진행 업데이트: `PROJECT_PROGRESS_UPDATE.md`

## Item별 보고/수정 내용

### Item 1 — Mosaic Year App
- Issue: `#1`
- 새 산출물:
  - `docs/assets/item1-mosaic-year.svg`
  - `item-1-mosaic-app/mockup/mosaic-year-hero.svg`
  - `item-1-mosaic-app/MOCKUP_SPEC.md`
- 수정 방향:
  - 보고서형 기획에서 직접 볼 수 있는 `zoom reveal hero mock`으로 전환
  - MVP 기준을 full app이 아니라 **wow demo**로 재정의
- 다음 액션:
  1. 실제 샘플 사진셋 기반 mosaic 생성
  2. 모바일 zoom viewer PoC
  3. export CTA 화면 추가

### Item 2 — Reactive Keyboard Goods / SG90 Clicker
- Issue: `#2`
- 구매 현물 반영:
  - MicroServo 9g SG90
  - USB/WiFi ESP32-C3 SuperMini
- 새 산출물:
  - `docs/assets/item2-sg90-clicker.svg`
  - `docs/assets/item2-cad-dimensions.svg`
  - `item-2-reactive-keyboard-goods/cad/sg90_clicker_mount_v0_1.scad`
  - `item-2-reactive-keyboard-goods/cad/sg90_clicker_mount_preview_v0_1.stl`
  - `item-2-reactive-keyboard-goods/cad/README.md`
  - `item-2-reactive-keyboard-goods/MOCKUP_AND_CAD_SPEC.md`
- 수정 방향:
  - 추상적인 반응형 키보드에서 **SG90 기반 딸깍이 오브젝트**로 구체화
  - 90×70mm base, SG90 cradle, ESP32 shelf, click target 구조 제안
- 다음 액션:
  1. 실측 기반 CAD 치수 보정
  2. 1차 3D print
  3. LED + servo demo firmware 작성

### Item 3 — AI Story Business Card + Storyboard App
- Issue: `#3`
- 새 산출물:
  - `docs/assets/item3-storycard-flow.svg`
  - `item-3-businesscard-storyboard-app/mockup/storycard-flow.svg`
  - `item-3-businesscard-storyboard-app/MOCKUP_SPEC.md`
- 수정 방향:
  - 문서형 앱 기획에서 **입력 → 생성 → 결제 CTA**가 보이는 flow mock으로 전환
  - item4 실물 명함 주문 퍼널과 연결
- 다음 액션:
  1. interactive form prototype
  2. LLM copy generation prompt
  3. SVG/Canvas preview renderer

### Item 4 — Hologram Business Card
- Issue: `#4`
- 새 산출물:
  - `docs/assets/item4-hologram-card.svg`
  - `item-4-hologram-business-card/mockup/black-signature-reveal.svg`
  - `item-4-hologram-business-card/MOCKUP_SPEC.md`
- 수정 방향:
  - 단순 홀로그램 명함에서 **Black Signature Reveal** 대표 샘플 방향으로 구체화
  - 프리미엄 identity object + 주문형 configurator 후보로 정리
- 다음 액션:
  1. 후가공 방식 비교
  2. 샘플 발주용 print spec 작성
  3. configurator preview 화면 제작

## Project 업데이트 계획/결과

- 각 item issue에 이번 변경사항을 comment로 기록
- Project Status를 대표 검토 가능한 `In review`로 변경
- Priority/Size를 실험 우선순위 기준으로 조정

## 현재 추천 우선순위

1. **Item 3** — 가장 빠른 검증/매출 실험
2. **Item 4** — 가장 프리미엄하고 공유성이 강한 실물 전환 후보
3. **Item 1** — 감성형 바이럴/포스터 확장 후보
4. **Item 2** — 상징성과 촬영력은 강하나 하드웨어 실측/출력 리스크 존재


## 2026-05-07 Issue Comment 반영 업데이트

각 issue의 최신 대표님 comment를 기준으로 추가 산출물을 만들었다.

- #1 Item 1: Drive sample 기반 로컬 mosaic PoC, low-distortion pipeline, public-safe decision mockup
- #2 Item 2: SG90/ESP32-C3 wiring, Mac setup, PlatformIO/Arduino firmware
- #3 Item 3: 20~30대 hip card customizer, font pack, social/QR/NFC/vCard architecture
- #4 Item 4: holo tier system, card layout, interactive 3D holo card mockup

통합 사이트: `docs/index.html`
상세 요약: `COMMENT_WORK_SUMMARY_2026-05-07.md`

주의: repo가 public이므로 item1의 원본 Drive 사진과 Drive 기반 mosaic JPEG/contact sheet는 GitHub publish에서 제외했다.


## 2026-05-07 Round 2 Web Visualization Update

최신 issue comment 반영 결과, GitHub Pages에서 바로 확인 가능한 item별 page를 추가했다.

- Item 1: `/item1/` — Mosaic test 방법, STANDARD 재검색 결과, public-safe demo
- Item 2: `/item2/` — SG90/ESP32-C3 quickstart, wiring, firmware test
- Item 3: `/item3/` — Hip business card customizer web demo + Vercel-ready files
- Item 4: `/item4/` — Interactive holo card web demo + Vercel-ready files

기존 404 원인: GitHub Pages source가 `/docs`인데, 링크가 `/docs` 밖의 item folder를 상대경로로 가리켰기 때문. 이번에 `docs/item1~4/index.html`로 수정했다.

상세: `ROUND2_WEB_VISUALIZATION_SUMMARY_2026-05-07.md`


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


## 2026-05-07 Item 2/4 Round 3 Update

- Item 2: 대표님 404 comment 확인. 현재 `https://sunggyu-kim.github.io/7iter/item2/`는 HTTP 200으로 정상 접근됨. 상태 기록: `item-2-reactive-keyboard-goods/PAGES_STATUS_ROUND3.md`.
- Item 4: 최신 comment에 따라 high-detail retro game-card inspired holo demo로 업그레이드. `docs/item4/index.html`에서 직접 확인 가능.
  - Holo styles: Circle foil, Grid, Glitch/static, Prism 3D
  - Game-card mapping: name, HP number, type icon, age/evolution, photo, attack, ability, hidden secrets, card number/rarity
  - KOR/ENG language toggle
  - CSS 3D transform/parallax/layered glare
  - hidden Weakness/Resistance/Retreat Cost reveal


## 2026-05-08 Manager System Update

- Added repo-native `manager-system/` for manager1~4.
- manager1 owns Item 1 and new Item 1-1 Semantic Object Mosaic Lab.
- manager2 owns Item 2 hardware capsule and SOUL modules.
- manager3 owns Item 3 and Item 3-1 jellyfish card.
- manager4 owns Item 4 hologram card.
- Added per-item CONTEXT/HISTORY/STATUS/JOBS/GITHUB records for async updates across OpenClaw, local Codex, Gemini, Claude/OpenAI/Grok, and future 3D tools.
