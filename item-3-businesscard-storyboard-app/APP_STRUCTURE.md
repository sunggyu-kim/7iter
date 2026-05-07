# APP_STRUCTURE

## 1. 목표
구현 전에 과도한 설계 없이, 빠르게 데모 가능한 구조를 잡기 위한 최소 앱 뼈대 제안.

## 2. 추천 구조

```text
app/
  page.tsx                    # 랜딩
  create/page.tsx             # 입력 폼
  result/[sessionId]/page.tsx # 생성 결과
  checkout/[sessionId]/page.tsx
  api/
    generate/route.ts         # 카피/스토리/템플릿 선택
    checkout/route.ts         # 결제 세션 생성
    unlock/route.ts           # 결제 후 결과 해금
components/
  input-form.tsx
  business-card-preview.tsx
  storyboard-preview.tsx
  pricing-box.tsx
lib/
  prompts.ts                  # 생성 프롬프트
  template-engine.ts          # preset 선택/데이터 매핑
  render.ts                   # 이미지/PDF 렌더링
  db.ts
  storage.ts
```

## 3. 데이터 모델 최소안

### generation_sessions
- id
- input_json
- style_preset
- generated_copy_json
- preview_asset_url
- paid_asset_url
- payment_status
- created_at

## 4. 생성 파이프라인
1. 폼 입력 저장
2. LLM이 명함 카피 + 컷별 텍스트 생성
3. 스타일 preset 선택
4. HTML/CSS 템플릿에 데이터 바인딩
5. preview 이미지 생성
6. 결과 페이지 노출
7. 결제 후 고해상도/PDF 해금

## 5. 프로토타입 구현 팁
- 첫 버전은 드래그 편집 없이 “생성 결과 고르기”에 집중
- 템플릿은 2개만 만들어도 충분
- 이미지 생성보다 **레이아웃 좋은 텍스트 카드**가 더 빠르고 안정적임
- 실제 판매 전에는 Gumroad/Stripe payment link 같은 더 단순한 결제 방식도 가능
