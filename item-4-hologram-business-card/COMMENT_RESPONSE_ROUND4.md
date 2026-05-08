# 2026-05-08 Round 4 — Holo rarity/background level system

대표님 최신 comment 기준으로 최고 레벨만 남아 보이던 구조를 rarity design system으로 확장했습니다.

## 반영
- 기존 4종 holo 유지: Circle foil / Grid / Glitch-static / Prism 3D
- background 선택 추가: Gold / Silver / Normal
- Normal background RGB palette 추가: R/G/B/W 계열 preset + color picker
- holo 없는 Normal mode 추가
- title holo ON/OFF 추가
- title holo는 배경 holo와 다른 방향/촘촘함/색감으로 적용
- 조합별 rarity 자동 산출
  - holo + gold = Ultra Rare
  - holo + silver = High Rare
  - holo + normal = Rare
  - no holo + gold = Super
  - no holo + silver = High
  - normal bg + no holo = Normal
  - title holo 추가 = + Signature
- 우측 상단 rarity badge와 하단 rarity text 동시 표기

## Web 확인
- `https://sunggyu-kim.github.io/7iter/item4/`
