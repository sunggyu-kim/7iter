# 7iter Round 2 Web Visualization Summary — 2026-05-07

## 목표
대표님이 GitHub issue #1~#4에 다시 남긴 comment를 기준으로, 특히 item 1·3·4를 **웹에서 직접 볼 수 있는 형태**로 업그레이드했다. GitHub Pages `/docs` publish root 밖을 가리키던 링크 문제도 수정했다.

## 공통 수정
- GitHub Pages publish root: `/docs`
- 기존 문제: `docs/index.html`에서 `../item-...`처럼 `/docs` 밖 파일을 링크하여 GitHub Pages에서 404 발생
- 수정: `docs/item1/`, `docs/item2/`, `docs/item3/`, `docs/item4/` 하위에 Pages-safe demo page 생성
- 통합 entry: `docs/index.html`

## 대표님 확인 URL
배포 후 아래 URL에서 직접 확인 가능하다.

- Home: `https://sunggyu-kim.github.io/7iter/`
- Item 1: `https://sunggyu-kim.github.io/7iter/item1/`
- Item 2: `https://sunggyu-kim.github.io/7iter/item2/`
- Item 3: `https://sunggyu-kim.github.io/7iter/item3/`
- Item 4: `https://sunggyu-kim.github.io/7iter/item4/`

## Item 1 — Mosaic Year

### 대표님 comment 대응
- `STANDARD.jpg` / `STANDARD.png` / 대소문자 변형 / `.jpeg`까지 다시 검색
- Drive manifest 50 rows 재생성
- 결과: `standard` 계열 파일 미발견
- evidence: `item-1-mosaic-app/logs/standard_search_round2.log` 로컬에 존재

### 산출물
- `docs/item1/index.html`
- `docs/item1/assets/public-placeholder-mosaic.svg`
- `item-1-mosaic-app/TESTING_GUIDE.md`
- `item-1-mosaic-app/COMMENT_RESPONSE_ROUND2.md`
- `item-1-mosaic-app/scripts/download_drive_samples.py` 개선
- `item-1-mosaic-app/scripts/mosaic_poc.py` 개선

### 공개 처리
Drive sample/JPEG 및 Drive 파생 mosaic/contact sheet는 public repo에 업로드하지 않는다. 대신 public-safe placeholder와 실행 방법을 제공한다.

## Item 2 — SG90 Reactive Clicker

### 산출물
- `docs/item2/index.html`
- `item-2-reactive-keyboard-goods/COMMENT_RESPONSE_ROUND2.md`
- `item-2-reactive-keyboard-goods/WIRING_AND_SETUP.md` 보강
- `item-2-reactive-keyboard-goods/firmware/sg90_clicker_mock/sg90_clicker_mock.ino` 보강

### 주요 보강
- 초보자용 10분 quickstart
- Serial command: `DONE`, `CLICK`, `REST`, `PRESS`, `HELP`
- Mac Arduino IDE / PlatformIO 절차
- 배선 및 troubleshooting

## Item 3 — Hip Business Card Customizer

### 대표님 comment 대응
- 직접 볼 수 있는 GitHub Pages page 생성
- local clone/npm 또는 simple http server 확인법 작성
- Vercel-ready static project 구성

### 산출물
- `docs/item3/index.html`
- `item-3-businesscard-storyboard-app/TESTING_GUIDE.md`
- `item-3-businesscard-storyboard-app/COMMENT_RESPONSE_ROUND2.md`
- `item-3-businesscard-storyboard-app/package.json`
- `item-3-businesscard-storyboard-app/vercel.json`

### Vercel
```bash
cd item-3-businesscard-storyboard-app
npx vercel login
npx vercel --prod
```

## Item 4 — Interactive Holo Card

### 대표님 comment 대응
- 직접 볼 수 있는 GitHub Pages page 생성
- Vercel-ready static project 구성
- tier selector, name/role/description/hidden message/photo editing, auto tilt, reduced motion 추가

### 산출물
- `docs/item4/index.html`
- `item-4-hologram-business-card/TESTING_GUIDE.md`
- `item-4-hologram-business-card/PAGES_404_FIX.md`
- `item-4-hologram-business-card/COMMENT_RESPONSE_ROUND2.md`
- `item-4-hologram-business-card/package.json`
- `item-4-hologram-business-card/vercel.json`
- `item-4-hologram-business-card/public/index.html`
- `item-4-hologram-business-card/scripts/build-static.mjs`
- `item-4-hologram-business-card/scripts/validate-static.mjs`

## 검증
- HTML parse: `docs/index.html`, `docs/item1/index.html`, `docs/item2/index.html`, `docs/item3/index.html`, `docs/item4/index.html`
- SVG parse: item1 public placeholder, item2 wiring SVG
- Python compile: item1 downloader/mosaic scripts
- JSON parse: item3/item4 `package.json`, `vercel.json`
- item4 npm validate/build는 subagent에서 통과


## 2026-05-07 Item 2/4 Round 3 Update

- Item 2: 대표님 404 comment 확인. 현재 `https://sunggyu-kim.github.io/7iter/item2/`는 HTTP 200으로 정상 접근됨. 상태 기록: `item-2-reactive-keyboard-goods/PAGES_STATUS_ROUND3.md`.
- Item 4: 최신 comment에 따라 high-detail retro game-card inspired holo demo로 업그레이드. `docs/item4/index.html`에서 직접 확인 가능.
  - Holo styles: Circle foil, Grid, Glitch/static, Prism 3D
  - Game-card mapping: name, HP number, type icon, age/evolution, photo, attack, ability, hidden secrets, card number/rarity
  - KOR/ENG language toggle
  - CSS 3D transform/parallax/layered glare
  - hidden Weakness/Resistance/Retreat Cost reveal
