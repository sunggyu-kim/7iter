# Item 3 Mockup Spec — AI Story Business Card

## 이번 정교화
- `docs/index.html`에 직접 볼 수 있는 form → card → storyboard 흐름 추가
- `mockup/storycard-flow.svg` 및 `docs/assets/item3-storycard-flow.svg` 생성

## 대표 검토 장면
1. 사용자가 5개 정보를 입력한다.
2. AI가 digital business card 1장과 3컷 storyboard를 생성한다.
3. watermark 제거 / PNG/PDF export / item4 실물 카드 주문으로 전환한다.

## 다음 개발 단위
- 실제 HTML form prototype
- LLM copy generation prompt
- SVG/Canvas 기반 preview renderer
- export CTA 화면
