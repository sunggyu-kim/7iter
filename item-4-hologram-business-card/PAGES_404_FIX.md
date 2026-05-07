# GitHub Pages 404 / Relative Path Fix Notes

## Problem observed

기존 item4 mockup은 아래처럼 repository source folder를 기준으로 연결되어 있었습니다.

```text
../item-4-hologram-business-card/mockup/holo-trading-card/
```

로컬 파일 탐색에서는 열릴 수 있지만, GitHub Pages가 `docs/`를 publish root로 쓰면 `item-4-hologram-business-card/`는 public site에 포함되지 않습니다. 따라서 대표님이 웹 URL로 눌렀을 때 404가 날 수 있습니다.

## Root cause

- GitHub Pages publish root: `docs/`
- 기존 mockup 위치: `item-4-hologram-business-card/mockup/...`
- Pages 배포 대상 밖의 상대경로를 링크함
- 디렉터리 URL은 `index.html`이 publish root 안에 있어야 안정적으로 동작함

## Fix applied

1. interactive demo를 publish root 내부로 이관/업그레이드:

```text
docs/item4/index.html
```

2. 통합 docs index 링크를 Pages-safe URL로 변경:

```text
item4/
```

3. item4 folder의 Vercel build는 같은 `docs/item4` 소스를 `dist/`로 복사하도록 구성:

```text
item-4-hologram-business-card/package.json
item-4-hologram-business-card/vercel.json
item-4-hologram-business-card/scripts/build-static.mjs
```

## Correct URLs

GitHub Pages:

```text
https://sunggyu-kim.github.io/7iter/item4/
```

Local docs root server:

```text
python3 -m http.server 4174 --directory docs
http://localhost:4174/item4/
```

Item folder npm server:

```text
cd item-4-hologram-business-card
npm run serve
http://localhost:4174/
```
