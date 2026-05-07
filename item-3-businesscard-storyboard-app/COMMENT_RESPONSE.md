# Representative Comment Response — Item 3 Business Card / Storyboard App

## Comment-by-comment response table

| 대표님 comment | 대응 방향 | 산출물 |
|---|---|---|
| 타깃: 20~30대 | 모바일 9:16, SNS 공유, 자기 브랜딩/크리에이터 감성 중심으로 UX 재정의 | `DESIGN_UX_PLAN.md`, `mockup/hip-card-customizer.html` |
| 힙한 느낌의 asset 보유, Magnific 참고 | 외부 asset은 무단 다운로드/재배포하지 않고 무드만 참고. 직접 만든 CSS/emoji placeholder로 힙한 card dressing room 구현 | `mockup/hip-card-customizer.html` |
| 무료 글꼴(영어, 한글) 중 다양한 글꼴 보유 | Pretendard/Inter, Gmarket/Poppins, SUITE/Montserrat, Nanum/Roboto 등 후보와 라이선스 체크포인트 정리 | `FONT_PACK.md` |
| 정보입력 전 디자인 단계에서 게임 캐릭터 꾸미듯 명함을 꾸미는 부분 필요 | Style preset → font mood → sticker/asset slot → background/card preview 순서의 “Card Dressing Room” 설계 및 인터랙티브 구현 | `DESIGN_UX_PLAN.md`, `mockup/hip-card-customizer.html` |
| 정보입력시 보안화 가능 | Secure mode 기본 ON, blur/masking, encrypted draft, publish consent sheet, 공개 범위 설계 | `QR_SOCIAL_NFC_ARCHITECTURE.md`, mockup secure toggle |
| 태깅/QR촬영시 insta, youtube, meta(thread), X 연동가능 | SocialLink 데이터 모델, URL normalize/allowlist, QR profile hub social bar 설계 | `QR_SOCIAL_NFC_ARCHITECTURE.md`, mockup social bar |
| airdrop(연락처) 가능 | Web MVP는 vCard 생성/다운로드 + Web Share API, 네이티브 iOS는 contact share sheet/AirDrop 확장 | `QR_SOCIAL_NFC_ARCHITECTURE.md`, mockup vCard 저장 데모 |
| 향후 실물발급: NFC카드, 태깅기능, 태깅정보 수정가능 | NFC에는 raw 개인정보가 아니라 redirect URL/tagId만 저장. 앱에서 profile/tag 정보 수정 가능 | `QR_SOCIAL_NFC_ARCHITECTURE.md` |
| 디자인과 UI/UX를 살려 제작 진행 | 실제 브라우저에서 볼 수 있는 offline HTML 프로토타입과 MVP screen/flow 정리 | `mockup/hip-card-customizer.html`, `DESIGN_UX_PLAN.md` |

## Created / updated files

- `mockup/hip-card-customizer.html` — 직접 열어볼 수 있는 interactive mockup. 스타일/폰트/스티커/보안 입력/SNS/vCard/NFC alert 포함.
- `DESIGN_UX_PLAN.md` — 20~30대 힙한 명함 앱 UX flow 및 MVP screen plan.
- `FONT_PACK.md` — 무료 한글/영문 font pack 후보 및 라이선스 주의사항.
- `QR_SOCIAL_NFC_ARCHITECTURE.md` — QR/social/AirDrop/vCard/NFC/보안 구조 설계.
- `COMMENT_RESPONSE.md` — 대표님 comment별 대응표와 실행 명령.

## How to view

```bash
cd /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter/item-3-businesscard-storyboard-app
python3 -m http.server 4173
# browser: http://127.0.0.1:4173/mockup/hip-card-customizer.html
```

브라우저 없이 파일 직접 열기도 가능합니다.

```bash
xdg-open /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter/item-3-businesscard-storyboard-app/mockup/hip-card-customizer.html
```

## Suggested next implementation steps

1. HTML mockup을 React/Vite 또는 Next.js prototype으로 분리.
2. `Profile`, `SocialLink`, `VisibilityPolicy` 데이터 모델 확정.
3. QR profile hub route `/p/[profileId]`와 NFC redirect route `/n/[tagId]` 구현.
4. vCard 생성 API와 Web Share API fallback 구현.
5. 폰트 라이선스 원문 확인 후 self-host font pack 구성.
6. 외부 asset pack은 구매/라이선스 확보 전까지 placeholder만 사용.

## Validation

- HTML 문법/구조 검증: Python `html.parser`로 parse 완료.
- 링크/파일 존재 확인: 생성 파일 5개 확인 완료.
- 외부 asset 다운로드 없음. HTML은 외부 네트워크 dependency 없이 동작하도록 작성.
