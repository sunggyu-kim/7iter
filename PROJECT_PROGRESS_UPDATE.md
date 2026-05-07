# Project Progress Update — 2026-05-07

## 이번 변경 목표
대표가 직접 볼 수 없는 보고서형 산출물을, **직접 열어볼 수 있는 mockup / SVG / CAD** 중심 산출물로 정교화.

## 진행한 부분
- 통합 mockup site 작성: `docs/index.html`
- item1 Mosaic Year visual mock 작성
- item2 SG90/ESP32-C3 clicker visual mock + CAD v0.1 작성
- item3 Story Business Card flow mock 작성
- item4 Black Signature Reveal hologram card mock 작성
- GitHub Project issue별 진행 내용 업데이트 예정

## 수정한 부분
- 기존 item별 문서에 mockup spec 추가
- item2는 구매 현물 기준으로 CAD 구조 재정의
- README/GITHUB_REPORT는 mockup site와 CAD 파일을 참조하도록 업데이트 필요

## 아직 남은 부분
- item1 실제 사진 기반 mosaic generator PoC
- item2 실측 기반 CAD 치수 보정 및 출력 테스트
- item3 실제 interactive form prototype
- item4 인쇄소 샘플 제작 사양 확정


## 2026-05-07 Comment-driven heavy work update

대표님이 issue #1~#4에 추가한 comment를 기준으로 item별 전담 agent 4개를 병렬 실행했다.

- Item 1: Drive 샘플 50개 로컬 테스트, 저변형 mosaic PoC script 작성. `standard.jpg` 부재로 최종 지정 target은 blocked. Public repo에는 원본 사진/Drive 기반 output 제외.
- Item 2: SG90 + ESP32-C3 SuperMini wiring/setup, Mac 설치 절차, Arduino/PlatformIO firmware mock 작성.
- Item 3: 20~30대 타깃 hip card customizer interactive HTML, font pack, social/QR/NFC/vCard architecture 작성.
- Item 4: IP-safe holo tier system, card layout spec, pointer-responsive 3D holo trading card mockup 작성.

통합 목업 사이트 `docs/index.html`에 신규 산출물 링크를 추가했다.

상세: `COMMENT_WORK_SUMMARY_2026-05-07.md`


## 2026-05-07 Round 2 — Web에서 직접 볼 수 있게 수정

- 최신 issue comment 재수집 후 item1~4 전담 agent 재실행.
- item1·3·4는 GitHub Pages에서 직접 볼 수 있는 `docs/itemN/index.html` 구조로 변경.
- item2도 테스트/설치 가이드를 `docs/item2/index.html`로 추가.
- Vercel-ready 파일은 item3/item4에 추가.
- 404 원인은 `/docs` publish root 밖을 링크한 상대경로 문제로 확인 및 수정.

검증 후 GitHub push 및 issue comment 업데이트 예정.


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
