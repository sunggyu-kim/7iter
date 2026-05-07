# 7iter GitHub Report

이 문서는 `7iter` GitHub repository / project 보고용 요약본입니다.

## 현재 보고 구조
- Repository: 전략/문서/아이템별 산출물의 기준 저장소
- GitHub Project: 실행 단위 추적 보드
- Project item 단위: item 1 ~ item 4 각각 개별 관리

## Item 요약

### Item 1 — Mosaic Year App
- 성격: 감성형 공유 중심 소프트웨어
- 현재 상태: 1차 SW 기획 완료
- 핵심 문서:
  - `item-1-mosaic-app/REPRESENTATIVE_DECISION_PROPOSAL.md`
  - `item-1-mosaic-app/PRODUCT_PLAN.md`
  - `item-1-mosaic-app/MVP_SPEC.md`
- 다음 액션:
  1. 샘플 자산 기반 demo
  2. mosaic pipeline PoC
  3. mobile zoom UX 검증

### Item 2 — Reactive Keyboard Goods
- 성격: AI 완료 순간을 물성 반응으로 보여주는 하드웨어형 굿즈
- 현재 상태: 채택 제안/실행안 정리 완료
- 핵심 문서:
  - `item-2-reactive-keyboard-goods/REP_REVIEW_PROPOSAL_DOHYEON.md`
  - `item-2-reactive-keyboard-goods/EXECUTION_PLAN.md`
- 다음 액션:
  1. 외형 스케치 2안
  2. 3~6키 LED macro pad MVP
  3. hero shot / demo video 설계

### Item 3 — AI Story Business Card + Storyboard App
- 성격: 가장 빠른 검증형 매출 소프트웨어
- 현재 상태: 1차 SW 기획 완료
- 핵심 문서:
  - `item-3-businesscard-storyboard-app/REPRESENTATIVE_DECISION_PROPOSAL.md`
  - `item-3-businesscard-storyboard-app/PRODUCT_PLAN.md`
  - `item-3-businesscard-storyboard-app/MVP_SPEC.md`
- 다음 액션:
  1. 입력 폼 + LLM copy generation 연결
  2. preview renderer 구현
  3. PNG/PDF export 및 결제 CTA 검증

### Item 4 — Hologram Business Card
- 성격: 프리미엄 실물 아이덴티티 오브젝트
- 현재 상태: 채택 제안/실행안 정리 완료
- 핵심 문서:
  - `item-4-hologram-business-card/REPRESENTATIVE_ADOPTION_PROPOSAL.md`
  - `item-4-hologram-business-card/EXECUTION_PLAN.md`
- 다음 액션:
  1. 후가공 shortlist 및 샘플 방향 확정
  2. Black Signature Reveal 샘플 검토
  3. 주문형 configurator MVP 정의

## 업로드/관리 원칙
1. **Repository에는 문서와 산출물**을 올린다.
2. **Project에는 item별 이슈/진행상태**를 나눠 넣는다.
3. 한 저장소 안에서 4개 item을 나눠 관리하는 것은 가능하며, 현재 단계에서는 오히려 그 편이 적절하다.
4. 이후 실제 개발이 깊어지면 각 item을 separate repo로 독립시킬 수 있다.

## 현재 추천 우선순위
1. Item 3 — 가장 빠른 검증/매출 실험
2. Item 4 — 가장 프리미엄하고 공유성이 강한 실물 전환 후보
3. Item 1 — 감성형 바이럴/포스터 확장 후보
4. Item 2 — 상징성과 촬영력은 강하나 하드웨어 리스크 존재
