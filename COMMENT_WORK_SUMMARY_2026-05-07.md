# 7iter Comment Work Summary — 2026-05-07

대표님이 GitHub issue #1~#4에 남긴 최신 comment를 기준으로 item별 전담 agent 4개를 병렬 실행했고, 각 item 폴더에 산출물을 생성했다.

## Item 1 — Mosaic Year

### 대표님 comment 요구
- YouTube mosaic 제작 방식에서 insight 확보
- Google Drive 폴더의 이미지를 샘플로 테스트
- `standard.jpg`를 대표이미지, 나머지를 mosaic tile로 사용
- 기존 이미지를 최대한 변형하지 말 것
- 색 보정이 필요하면 기존 사진을 왜곡하기보다 신규 이미지 생성/보충 방향

### 수행 결과
- Drive public folder 접근 성공
- 50개 JPEG 로컬 다운로드 및 `sample/drive_manifest.tsv` 생성
- `standard.jpg`는 Drive listing에 없어 최종 지정 target 생성은 blocked
- fallback target `IMG_4265.jpeg` 기준 로컬 demo 생성
- 저변형 mosaic PoC 구현
  - EXIF 보정
  - 중앙 크롭
  - 리사이즈
  - tint/hue/opacity 강제 색변형 없음

### 생성 파일
- `item-1-mosaic-app/scripts/mosaic_poc.py`
- `item-1-mosaic-app/README_MOSAIC_POC.md`
- `item-1-mosaic-app/COMMENT_RESPONSE.md`
- `item-1-mosaic-app/PUBLICATION_NOTE.md`
- `item-1-mosaic-app/mockup/decision_mockup.html`
- `item-1-mosaic-app/mockup/low_distortion_pipeline.svg`
- `item-1-mosaic-app/mockup/generated/public_placeholder_mosaic.svg`

### 공개 repo 처리
Repo가 public이므로 원본 Drive JPEG와 실제 Drive 기반 generated mosaic/contact sheet는 업로드 제외. 로컬 검증 결과만 기록.

---

## Item 2 — SG90 Reactive Clicker

### 대표님 comment 요구
- SCAD 초안은 유지
- servo와 ESP32-C3 SuperMini 연결/구동 방법 설명
- Mac 환경에서 설치해야 하는 것 정리

### 수행 결과
- SG90 ↔ ESP32-C3 SuperMini wiring guide 작성
- Mac Arduino IDE / PlatformIO 절차 작성
- mock AI completion firmware 작성
- CAD assembly wiring note 및 wiring SVG 추가

### 생성/수정 파일
- `item-2-reactive-keyboard-goods/WIRING_AND_SETUP.md`
- `item-2-reactive-keyboard-goods/COMMENT_RESPONSE.md`
- `item-2-reactive-keyboard-goods/platformio.ini`
- `item-2-reactive-keyboard-goods/firmware/sg90_clicker_mock/sg90_clicker_mock.ino`
- `item-2-reactive-keyboard-goods/firmware/sg90_clicker_mock/README.md`
- `item-2-reactive-keyboard-goods/cad/ASSEMBLY_WIRING_NOTES.md`
- `item-2-reactive-keyboard-goods/cad/wiring-sg90-esp32c3.svg`

---

## Item 3 — Hip Business Card Customizer

### 대표님 comment 요구
- 20~30대 타깃
- 힙한 디자인 asset 방향
- 무료 한글/영문 글꼴 후보
- 정보입력 전 게임 캐릭터 꾸미듯 명함 꾸미기
- 보안 입력 UX
- Instagram / YouTube / Threads / X 연동
- AirDrop 연락처
- 향후 NFC 실물 카드 / 태깅 정보 수정

### 수행 결과
- self-contained interactive HTML mockup 작성
- Card Dressing Room 커스터마이징 UX 구현
- font pack 후보 정리
- QR/social/NFC/vCard/AirDrop 구조 설계
- 외부 asset 무단 다운로드 없이 placeholder asset 사용

### 생성 파일
- `item-3-businesscard-storyboard-app/mockup/hip-card-customizer.html`
- `item-3-businesscard-storyboard-app/DESIGN_UX_PLAN.md`
- `item-3-businesscard-storyboard-app/FONT_PACK.md`
- `item-3-businesscard-storyboard-app/QR_SOCIAL_NFC_ARCHITECTURE.md`
- `item-3-businesscard-storyboard-app/COMMENT_RESPONSE.md`

---

## Item 4 — Hologram Trading Card

### 대표님 comment 요구
- 유희왕/포켓몬 카드식 holo 개념을 일반화하여 등급화
- 이름/사진/설명 영역을 1개 카드에 구성
- 3D holographic card 방법론 참고
- 실제 제품이 아닌 SW로, 움직이면 빛나는 3D 형식 구현

### 수행 결과
- IP-safe holo tier system 설계
- 단일 카드 layout spec 작성
- mouse/touch 움직임에 반응하는 3D tilt + foil glare + parallax + hidden reveal HTML mockup 작성
- SW 구현 노트 작성

### 생성 파일
- `item-4-hologram-business-card/HOLO_TIER_SYSTEM.md`
- `item-4-hologram-business-card/CARD_LAYOUT_SPEC.md`
- `item-4-hologram-business-card/IMPLEMENTATION_NOTES.md`
- `item-4-hologram-business-card/mockup/holo-trading-card/index.html`
- `item-4-hologram-business-card/COMMENT_RESPONSE.md`

## 통합 업데이트
- `docs/index.html`에 item1 PoC / item2 wiring+firmware / item3 customizer / item4 holo card 링크 추가
- 각 item별 산출물은 item 폴더 내부에 유지
- 다음 단계는 repo push 및 issue comment / Project field 업데이트
