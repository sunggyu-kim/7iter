# 2026-05-08 Round 5 — Image-filled NULL/object mosaic correction

대표님 지적대로 Round 4의 의도가 잘못 반영된 부분을 수정했습니다.

## 핵심 수정
- 모든 cell은 단순 색상 block이 아니라 이미지 tile로 채움
- NULL/background 영역도 빈 값이나 흰색 사각형이 아니라 흰색 영역이 많은 이미지 tile로 채움
- object 영역은 segmentation/mask 후처리 target 기준으로 별도 tile 후보군을 재선별
- 데이터셋은 production에서는 MS COCO segmentation/object labels 사용을 권장하도록 명시

## 추가 산출물
- `docs/item1/assets/coco-style-animal-semantic-target.jpg`
- `docs/item1/assets/real-image-null-background-animal-mosaic.jpg`
- `docs/item1/assets/real-image-null-background-mosaic-report.json`

## 확인
- `https://sunggyu-kim.github.io/7iter/item1/`
