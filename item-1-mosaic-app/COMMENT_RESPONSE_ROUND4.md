# 2026-05-08 Round 4 — Object-first mosaic improvement

최신 comment 기준으로 target과 mosaic이 닮지 않는 원인을 해결하기 위한 대안을 반영했습니다.

## 원인
기존 church target은 하늘/벽/그림자 등 배경 면적이 커서 전체 프레임 색상 매칭은 되지만 object silhouette가 약했습니다.

## 반영
- target background를 NULL/transparent 개념으로 분리
- object 영역만 semantic target으로 유지
- 배경 cell은 white/black/저채도 cell로만 채우는 정책 추가
- animal/person처럼 중앙 object가 큰 target으로 바꾸는 대안 mockup 추가
- 후처리 target 색상 histogram을 먼저 체크한 뒤 tile 후보군을 선별하는 정책 명시

## Web 확인
- `https://sunggyu-kim.github.io/7iter/item1/`
- `assets/semantic-object-mask.svg`
- `assets/semantic-object-cat-mosaic.svg`
- `assets/semantic-object-mosaic-report.json`
