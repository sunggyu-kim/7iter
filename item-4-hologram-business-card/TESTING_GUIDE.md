# Item 4 Hologram Card — Testing Guide

## 1. 대표님이 바로 보는 방법

GitHub Pages에서 `docs/`가 publish root라면 아래 URL이 최종 확인 주소입니다.

```text
https://sunggyu-kim.github.io/7iter/item4/
```

통합 목업 홈:

```text
https://sunggyu-kim.github.io/7iter/
```

## 2. 로컬 clone 후 바로 보기

Repository root 기준:

```bash
git clone https://github.com/sunggyu-kim/7iter.git
cd 7iter
python3 -m http.server 4174 --directory docs
```

브라우저:

```text
http://localhost:4174/item4/
```

## 3. item4 폴더에서 npm 방식

```bash
cd item-4-hologram-business-card
npm run serve
```

브라우저:

```text
http://localhost:4174/
```

## 4. Vercel-ready static build

Vercel Project Root를 `item-4-hologram-business-card`로 잡는 경우:

```bash
npm install
npm run build
```

- Build Command: `npm run build`
- Output Directory: `dist`
- `vercel.json` included

`npm run build`는 shared `../docs/item4/index.html`이 있으면 이를 우선 사용하고, Vercel subdirectory 환경에서는 `public/index.html` snapshot을 `dist/index.html`로 복사합니다. 그래서 GitHub Pages와 Vercel preview가 같은 데모를 보게 됩니다.

## 5. 조작 검수 체크리스트

- Tier selector: Common/Rare/Super/Secret/Signature 클릭 시 색/foil 강도 변경
- Name/role/description 입력 즉시 카드 반영
- Photo URL 입력 시 portrait 영역이 이미지로 변경
- Mouse/touch move 시 3D tilt, glare, hidden reveal 작동
- `자동 틸트 보기` 버튼으로 움직임을 비개발자도 확인 가능
- 외부 카드게임 IP/상표/캐릭터/로고 없음
