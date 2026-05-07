# Free Font Pack Candidates

> 목적: 20~30대 타깃의 힙한 디지털 명함/스토리카드 UI에 바로 쓸 수 있는 한글·영문 무료 폰트 후보. 실제 배포 전에는 각 폰트의 최신 라이선스 원문과 서브셋/웹폰트 재배포 조건을 재확인해야 합니다.

## 추천 조합

| Mood | Korean | English | 사용처 | 라이선스 주의 |
|---|---|---|---|---|
| App default / clean | Pretendard | Inter | 기본 UI, 긴 텍스트, 입력폼 | 둘 다 오픈소스 계열. 파일 내 라이선스 고지 포함 권장 |
| Bold creator / ad-like | Gmarket Sans | Poppins | 카드 이름, CTA, 프로모션 문구 | Gmarket Sans는 BI/로고 변형 오해 방지. Poppins는 SIL OFL 고지 |
| Trendy portfolio | SUITE | Montserrat | 크리에이터/디자이너 카드 | 배포 패키지에 OFL/라이선스 파일 포함 |
| Friendly Korean | NanumSquare / Nanum Gothic | Roboto | 안정적인 일반 사용자 템플릿 | 네이버 나눔글꼴 라이선스 고지 확인 |
| Editorial premium | Noto Sans KR | Space Grotesk | founder/consultant premium 카드 | Google/Noto OFL 고지, 웹폰트 self-host 시 license 포함 |
| Retro/Youth accent | DungGeunMo 또는 NeoDunggeunmo | Barlow Condensed | pixel/retro sticker 템플릿 | 폰트별 재배포·수정 조건 확인 필수 |

## MVP 적용 전략

1. **앱 UI 기본 폰트**: Pretendard + Inter fallback.
2. **카드 템플릿 폰트 슬롯**: `headlineFont`, `bodyFont`, `accentFont` 3개로 제한.
3. **서버 렌더링/PNG export**: 폰트 파일을 backend renderer에 설치하고, 산출물 하단 또는 settings에 font license notice 링크 제공.
4. **사용자 업로드 폰트는 MVP 제외**: 저작권 리스크와 렌더링 불안정이 큼.
5. **라이선스 검수 체크리스트**
   - 상업적 사용 가능 여부
   - 웹폰트 self-host 가능 여부
   - 앱 번들/서버 번들 재배포 가능 여부
   - 폰트명 변경 조건
   - OFL/라이선스 파일 동봉 의무

## Prototype 반영

`mockup/hip-card-customizer.html`은 실제 웹폰트를 다운로드하지 않고 시스템 fallback으로만 폰트 무드를 시뮬레이션합니다. 외부 폰트 파일은 포함하지 않았습니다.
