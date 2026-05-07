# Hip Business Card App — Design / UX Plan

## Target

- **20~30대 크리에이터, 프리랜서, 주니어/창업가**가 첫 네트워킹에서 “평범한 명함보다 기억나는 자기소개”를 만들게 한다.
- 톤: 힙하지만 과장된 AI 아바타 앱이 아니라, **카드형 자기 브랜딩 + SNS 프로필 허브 + 향후 NFC 실물 카드**.

## Core UX Principle

정보를 먼저 입력시키지 않는다. 사용자는 먼저 **게임 캐릭터 꾸미기처럼 카드의 세계관을 만든 뒤**, 필요한 정보만 안전하게 연결한다.

## Flow

### 1. Card Dressing Room

- Style preset: `Neo Club`, `Clean Gen-Z`, `Retro Pixel` 등 3개로 시작.
- Font mood: 무료 한글/영문 폰트 조합을 선택.
- Sticker/asset slots: 별, 번개, 픽셀, 하트, 플라워 등 직접 제작한 SVG/emoji 기반 placeholder.
- Background: gradient, noise, frame, glow intensity.
- Avatar/object: 얼굴 사진보다 취향 오브젝트를 우선. 향후 AI asset 생성/사용자 업로드 확장.

### 2. Secure Profile Input

- 이름/활동명, 역할, 한 줄 포지셔닝, 연락처, SNS 링크를 입력.
- 입력 중 `Secure mode` 기본 ON:
  - 화면상 계정 일부 blur/masking.
  - autosave는 민감정보 제외 또는 encrypted draft로 분리.
  - 발행 직전 공개 범위 consent sheet.
- 공개 범위: `전체 공개`, `QR/NFC로 접근한 사람만`, `직접 공유 링크만`, `비공개`.

### 3. Live Preview

- 9:16 모바일 스토리 비율 우선.
- 카드 1장 + 3컷 storyboard preview.
- SNS bar: Instagram, YouTube, Threads, X.
- QR placeholder: 실제 구현 시 profile hub URL 또는 share token URL.

### 4. Share / Save / Issue Physical

- QR 촬영: web profile hub open.
- AirDrop/연락처: vCard 생성 + Web Share API, 네이티브 앱에서는 iOS contact share sheet.
- NFC card: `/p/{profileId}` redirect URL만 write. 사용자는 앱에서 태깅 후 노출 정보 수정.
- Paid conversion: watermark 제거, 고해상도 export, NFC 카드 발급, premium asset pack.

## Prototype

- 파일: `mockup/hip-card-customizer.html`
- 특징:
  - 외부 asset 다운로드 없음.
  - 직접 만든 CSS/emoji placeholder 사용.
  - 스타일/폰트/스티커/정보 입력/보안 마스킹/vCard 다운로드 데모 포함.

## UI Screens for MVP

1. Landing: “명함을 캐릭터처럼 꾸미고, 태그 한 번으로 공유.”
2. Dressing Room: style/font/sticker/card mood.
3. Secure Input: profile/social/contact with privacy preview.
4. Result Preview: card + storyboard + social hub.
5. Publish Sheet: 공개 범위, QR, link, vCard, AirDrop.
6. NFC Order: physical card design, redirect URL, editable tag info.

## Design Notes

- Magnific 참고 링크는 **무드 레퍼런스만** 사용. 이미지/PSD 다운로드, 재배포, 트레이싱 금지.
- MVP asset은 내부 제작 벡터/emoji/SVG placeholder로 시작하고, 정식 asset pack은 별도 라이선스 확보 후 추가.
- 초기는 편집 자유도를 제한해 결과물 완성도를 우선한다.
