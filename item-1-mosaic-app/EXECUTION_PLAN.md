# EXECUTION PLAN — Mosaic Year

## 목표
대표님이 빠르게 판단할 수 있도록, **"보는 순간 이해되는 데모"**를 우선 만든다.
핵심은 완전한 자동화보다 **강한 결과물 + 자연스러운 줌 경험 + 유료 전환 그림**이다.

## 1. What we should ship first
### Phase 1 — Sellable demo
기간 기준: 가장 먼저 착수해야 할 1차 목표

산출물:
1. 샘플 사진셋 기반 완성 모자이크 2종
2. 모바일 친화 줌 뷰어 1개
3. 랜딩 1장 + 결과 페이지 1장
4. HD 다운로드 / 포스터 CTA가 붙은 구매 유도 흐름

이 단계에서 증명할 것:
- 사람들이 개념을 5초 안에 이해하는가
- 결과물이 공유 욕구를 만들 정도로 예쁜가
- 무료 미리보기 → 유료 잠금 해제가 자연스러운가

## 2. Recommended build order
### Step 1. Hardcoded wow demo
- 샘플 원본 사진 200~500장 확보
- 타깃 hero 이미지 2~3개 제작/선정
- 오프라인 스크립트로 모자이크 결과물 먼저 생성
- 결과 이미지를 viewer에 연결

**목적:** 기술 리스크보다 먼저 상품 매력을 검증

### Step 2. Interactive viewer polish
- OpenSeadragon 등으로 확대/이동 최적화
- 모바일 pinch zoom UX 확인
- CTA overlay와 워터마크 처리

**목적:** 이 제품의 핵심 훅인 줌 리빌을 완성

### Step 3. Guided creation flow
- 사진 업로드
- 타깃 이미지 선택
- 스타일 프리셋 선택
- 생성 대기 화면

**목적:** 실제 사용 상상을 가능하게 만들기

### Step 4. Async generation pipeline
- 업로드 정규화
- 타일 분석
- 타깃 매칭
- preview/export 분리 렌더링

**목적:** 하드코딩 데모를 실제 생성형 제품으로 전환

### Step 5. Monetization layer
- 무료 미리보기 잠금
- HD export 버튼
- print-ready / reveal video 업셀링

**목적:** 체험형 아이디어를 상품으로 닫기

## 3. Concrete 2-week sprint suggestion
### Sprint A — 대표님 검토용 데모 스프린트
**Day 1-2**
- 샘플셋 선정
- hero image 2종 확정
- 레퍼런스 무드보드 정리

**Day 3-4**
- 모자이크 생성 스크립트로 정적 결과물 제작
- 품질 튜닝(타일 크기, 색감, 대비)

**Day 5-6**
- 결과 뷰어 구현
- 모바일 줌 동작 확인

**Day 7**
- 랜딩/결과 페이지 연결
- CTA 문구, 가격 가정 반영

**Day 8-9**
- 화면 녹화용 데모 동선 정리
- 포스터 mockup 추가

**Day 10**
- 대표님 리뷰 패키지 정리
  - 라이브 데모
  - 30초 화면 녹화
  - 결과 이미지 2장
  - 상품 구조 1장

## 4. Deliverables for decision-making
대표님 판단용 최소 패키지:
- `Demo URL` 또는 로컬 실행 가능한 데모
- `Best result image x2`
- `Zoom reveal recording x1`
- `상품 구조 요약 x1` (무료/유료/출력 옵션)
- `다음 개발 로드맵 x1`

## 5. Main risks and how to handle them
### Risk 1. 첫 결과물이 기대보다 안 예쁠 수 있음
대응:
- 사용자 업로드 이전에 **잘 나온 샘플 결과물**을 먼저 만든다
- hero image를 초상/숫자/심볼 중심으로 제한한다

### Risk 2. 업로드/생성이 느리게 느껴질 수 있음
대응:
- MVP는 preview-first로 간다
- 고해상도 export는 비동기 후처리

### Risk 3. 모바일 줌이 답답할 수 있음
대응:
- tiled viewer 사용
- 초기 확대 포인트를 미리 설계
- 결과 화면 UI를 최소화

## 6. Suggested team posture
이 아이템은 기능을 넓히는 팀보다 **미감을 집요하게 다듬는 팀**이 유리합니다.
우선순위는 아래 순서가 맞습니다.

1. 결과물이 예쁜가
2. 줌 리빌이 재밌는가
3. 구매 CTA가 자연스러운가
4. 자동화가 완전한가

## 7. Go / No-go checkpoint
다음 3개가 충족되면 계속 밀 가치가 큽니다.
- 데모를 본 사람이 바로 "이거 내 사진으로 해보고 싶다"고 말함
- 줌 리빌 영상만으로도 제품 차별점이 전달됨
- 포스터/HD 저장 CTA가 어색하지 않음

## 8. Final recommendation
**이 아이템은 “기술 완성”보다 “첫 감탄”을 먼저 만들어야 합니다.**
따라서 바로 해야 할 일은 풀스택 완성보다,

> 샘플 기반 최고 품질 데모를 만들고, 그 데모를 실제 구매 가능한 제품처럼 보이게 정리하는 것

입니다.