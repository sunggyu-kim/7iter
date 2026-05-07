# Item 2 Pages Status — Round 3

## 대표님 comment
> html이 404 error로 열리지 않음 확인할 것

## 확인 결과
2026-05-07 현재 GitHub Pages에서 Item 2 페이지는 정상 접근된다.

- URL: `https://sunggyu-kim.github.io/7iter/item2/`
- GitHub Pages source: `main` branch `/docs`
- 확인 결과: HTTP 200

## 이전 404 가능 원인
이전 구조에서는 `docs/index.html`이 `/docs` 밖의 item 폴더를 상대경로로 가리켰다.
GitHub Pages는 `/docs`를 publish root로 사용하므로, `/docs` 밖 파일은 Pages에서 직접 접근할 수 없어 404가 발생할 수 있다.

## 수정된 구조
- Pages-safe file: `docs/item2/index.html`
- 통합 index link: `docs/index.html` → `item2/`
- 관련 docs:
  - `item-2-reactive-keyboard-goods/WIRING_AND_SETUP.md`
  - `item-2-reactive-keyboard-goods/COMMENT_RESPONSE_ROUND2.md`

## 로컬 확인 방법
```bash
git clone https://github.com/sunggyu-kim/7iter.git
cd 7iter
python3 -m http.server 4172 --directory docs
# open http://127.0.0.1:4172/item2/
```
