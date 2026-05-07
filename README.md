# marketing : seven iter

iteration 7 프로젝트의 하위 아이템 진행 현황, 관련 세션, 산출물 위치를 한 번에 보는 인덱스 문서입니다.

## 1. 프로젝트 개요
- 원본 브리프: `PROJECT_BRIEF.md`
- 목적: 바이브코딩 기반 제품 아이디어를 격주~1달 간격으로 공개 가능한 형태로 정리/실행
- 현재 관리 단위: item 1 ~ item 4

## 2. 관련 세션 요약

### 2.1 대표 세션
- **Telegram direct**: `agent:main:telegram:direct:7119839326`
  - 역할: 프로젝트 브리프 저장, item 1·3 SW화 지시, item 4 아이디어 추가, GitHub 분리 관리 지시 수신
  - 핵심 로그:
    - `2026-05-06 19:50` 전후: `PROJECT_BRIEF.md` 저장
    - `2026-05-06 19:51~19:53` : item 1, 3을 각 세션으로 분리하여 1차 SW화 지시
    - `2026-05-06 19:56` : item 4 홀로그램 명함 아이디어 추가 저장
    - `2026-05-07 14:28` : 4번 별도 아이템화, 1/2/3/4 각각 GitHub 분리 관리 지시 수신
  - 참고: 이 세션의 메시지 스냅샷에는 `무료로 3d 프린팅할만한곳이 있을까 연희동근처` 문의가 포함되어 있어, 물성형/제작형 아이템 검토 맥락이 이어진 상태로 해석 가능

### 2.2 하위 작업 세션
- **item 1 subagent**: `agent:main:subagent:4e13d684-3a19-4f08-a299-51dc6d45acc6`
  - 결과: done
  - 역할: `item-1-mosaic-app` 1차 SW화
- **item 3 subagent**: `agent:main:subagent:c873583d-cc05-4079-a6e8-43b4f4172bf1`
  - 결과: done
  - 역할: `item-3-businesscard-storyboard-app` 1차 SW화

## 3. 아이템별 진행 현황

### Item 1. Mosaic Year / 연간 이미지 모자이크 생성 앱
- 폴더: `item-1-mosaic-app/`
- 상태: **1차 SW화 완료**
- 관련 세션:
  - parent: `agent:main:telegram:direct:7119839326`
  - subagent: `agent:main:subagent:4e13d684-3a19-4f08-a299-51dc6d45acc6`
- 생성 문서:
  - `BRIEF.md`
  - `PRODUCT_PLAN.md`
  - `MVP_SPEC.md`
  - `APP_STRUCTURE.md`
- 현재까지 확정된 방향:
  - 12개월 사진을 하나의 hero mosaic로 재구성
  - zoom reveal 자체를 인스타그래머블 훅으로 사용
  - Freemium + 유료 export/print 전환 구조
  - Next.js + Sharp + 비동기 job 구조 중심의 MVP 제안
- 이번 단계 산출 의미:
  - 아이디어 수준을 넘어 제품 컨셉, 유저 여정, 수익화, MVP 범위, 구조까지 1차 명세 확보
- 다음 필요 작업:
  1. 샘플 자산 기반 hardcoded demo
  2. 실제 mosaic generation pipeline PoC
  3. zoom viewer 선택(OpenSeadragon 등) 및 모바일 UX 검증

### Item 2. 추론 완료 반응형 키보드 / 굿즈
- 폴더: `item-2-reactive-keyboard-goods/`
- 상태: **아이디어 정리만 존재 / SW화 미착수**
- 관련 세션:
  - 명시적 전용 subagent 세션은 아직 확인되지 않음
  - 상위 기획은 `agent:main:telegram:direct:7119839326` 및 `PROJECT_BRIEF.md`에 반영됨
- 현재 정의:
  - 추론 완료 시 색이 변하거나, 팝업/가동 반응이 발생하는 키보드/굿즈
  - 사용 흐름 자체가 시각 콘텐츠가 되는 물성형 아이템
  - 3D printing 프로토타입 제작 트랙과 연동 가능성이 큼
- 현재 문서 상태:
  - `BRIEF.md` 생성
- 판단:
  - 제품 콘셉트는 강하지만, 하드웨어 인터랙션 정의/프로토타입 범위/제조 방식이 아직 비어 있음
- 다음 필요 작업:
  1. 반응 방식 정의(LED / 기계식 팝업 / 커버 오브젝트 등)
  2. 3D printing 가능 부품과 시제품 난이도 분해
  3. 데모 우선형 MVP(가짜 inference signal 기반) 설계

### Item 3. AI 스토리 명함 + 스토리보드 앱
- 폴더: `item-3-businesscard-storyboard-app/`
- 상태: **1차 SW화 완료**
- 관련 세션:
  - parent: `agent:main:telegram:direct:7119839326`
  - subagent: `agent:main:subagent:c873583d-cc05-4079-a6e8-43b4f4172bf1`
- 생성 문서:
  - `BRIEF.md`
  - `PRODUCT_PLAN.md`
  - `MVP_SPEC.md`
  - `APP_STRUCTURE.md`
- 현재까지 확정된 방향:
  - 단순 명함 생성기가 아니라 **AI 스토리 비즈니스카드**로 포지셔닝
  - 입력 1분 → 결과 30초 내 생성 흐름
  - 디지털 명함 1안 + 3~6컷 스토리보드 동시 생성
  - 무료 미리보기 → 유료 다운로드/실물 명함 전환 구조
- 이번 단계 산출 의미:
  - 메시지/랜딩/수익화/MVP 구조까지 실험 가능한 수준의 1차 제품 명세 확보
- 다음 필요 작업:
  1. preset 2~3개 기준 렌더링 프로토타입
  2. 입력 폼 → LLM copy generation → preview 렌더링 연결
  3. PNG/PDF export와 결제 CTA 검증

### Item 4. 홀로그램 명함 제작
- 폴더: `item-4-hologram-business-card/`
- 상태: **아이디어 분리 완료 / SW화 전 단계**
- 관련 세션:
  - `agent:main:telegram:direct:7119839326`
- 현재 정의:
  - 포켓몬 카드처럼 각도에 따라 빛나는 홀로그램 명함
  - 실물 수령 순간과 촬영 결과 모두 강한 공유 포인트
  - 문구/패턴/광택을 개인별 커스터마이즈 가능
- 현재 문서 상태:
  - `BRIEF.md` 생성
- 판단:
  - 4번은 대표님 지시대로 **별도 아이템으로 분리 관리해야 하는 우선 대상**
  - 디지털 앱보다 물성/제작 프로세스 설계가 핵심이며, 제조 파트너/시제품 샘플링 전략이 중요
- 다음 필요 작업:
  1. 홀로그램 가공 방식 조사(foil, laminate, lenticular 대체 포함)
  2. 소량 제작 단가/리드타임 조사
  3. 주문 전환형 configurator MVP 가능성 검토

## 4. 폴더 구조
```text
marketing-seven-iter/
├─ PROJECT_BRIEF.md
├─ README.md  # 이 문서
├─ item-1-mosaic-app/
│  ├─ BRIEF.md
│  ├─ PRODUCT_PLAN.md
│  ├─ MVP_SPEC.md
│  └─ APP_STRUCTURE.md
├─ item-2-reactive-keyboard-goods/
│  └─ BRIEF.md
├─ item-3-businesscard-storyboard-app/
│  ├─ BRIEF.md
│  ├─ PRODUCT_PLAN.md
│  ├─ MVP_SPEC.md
│  └─ APP_STRUCTURE.md
└─ item-4-hologram-business-card/
   └─ BRIEF.md
```

## 5. 현재 판단
- **실제로 1차 SW화가 끝난 것은 item 1, item 3**
- **item 2, item 4는 아이디어는 살아 있으나 제품 명세/구조 문서는 아직 최소 수준**
- **item 4는 separate repo 후보로 우선도 높음**
- **item 2는 3D printing/인터랙션 프로토타입 관점에서 별도 실험 세션을 붙일 가치가 있음**

## 6. GitHub 연동 상태
- 현재 이 workspace 루트 Git에는 remote가 연결되어 있지 않음
- 따라서 이번 작업에서는:
  1. iteration 7 인덱스 문서 작성
  2. item 2 / item 4 폴더 및 brief 정리
  3. 프로젝트 단위 로컬 git 커밋 준비
- 실제 GitHub push는 remote 또는 repo 생성 정보가 필요함

## 7. 다음 권장 순서
1. item 4를 별도 repo 1순위로 분리
2. item 2를 3D printing prototype repo로 분리
3. item 1, item 3은 app repo로 각각 분리
4. 각 repo의 README 첫 줄은 이 문서를 상위 index로 참조하도록 구성
