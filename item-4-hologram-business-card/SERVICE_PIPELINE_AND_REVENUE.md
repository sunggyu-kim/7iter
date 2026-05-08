# Item 4 Service Pipeline and Revenue Plan

## Status
Design/mockup draft is treated as roughly complete. Next work is service operation, GPT pipeline, and revenue validation.

## Scenario 1 — Photo + MBTI
### Input
- photo
- MBTI
- optional job/role/name

### GPT output
- Attack / 공격
- Ability / 특성
- Weakness / 약점
- Defense Mechanism / 방어기제
- short card description

### Prompt draft
```text
You are generating an IP-safe collectible business card. Based on the user's MBTI, job/role, and photo description, create:
1. Attack: witty job/personality move
2. Ability: passive trait
3. Weakness: playful but not insulting limitation
4. Defense Mechanism: how the user protects focus/energy
Tone: premium, fun, respectful, usable for personal branding.
Return Korean and English versions.
```

## Scenario 2 — Name + birthday / 사주 entertainment
### Input
- name
- birth date/time if available
- optional gender/timezone disclaimer

### GPT output
- entertainment-only 사주 summary
- character archetype
- Attack / Ability / Weakness / Defense Mechanism
- visual generation brief

### Prompt draft
```text
Use the provided name and birth date for entertainment-only saju-inspired character design. Do not make deterministic claims about fate, health, finance, or relationships. Generate an IP-safe collectible card character and card traits: Attack, Ability, Weakness, Defense Mechanism. Make it premium and shareable.
```

## Required tests
- Cost per generation using GPT-5.5 / fallback model.
- Safety filter for insulting/defamatory traits.
- Korean/English quality review.
- Photo privacy and deletion policy.
- Conversion test: free preview → paid export.

## Revenue model
- Free preview with watermark.
- Paid high-res PNG/PDF export.
- Premium holo animation / rarity packs.
- Physical NFC card upsell.
- Team/event bulk generation package.

## Platform recommendation
- Korea: KakaoTalk share, Kakao Channel, Naver SmartStore for physical card.
- Global: web app, Instagram/TikTok share video, Shopify/Etsy physical fulfillment.
- MVP: manual GPT-backed concierge generation before full automation.
