# 2026-05-08 Round 6 — Item 3-1 Jellyfish asset detail upgrade

## Goal
Item 3-1의 transparent jellyfish card를 단순 CSS 오브젝트에서 Blender/3D asset처럼 보이는 web-safe inline SVG/CSS 오브젝트로 고도화한다.

## Implementation direction
- 외부 이미지/asset 다운로드 없이 inline SVG + CSS filter/gradient만 사용
- jellyfish를 shell, rim, inner volume, caustics, oral arms, tentacles, bubbles 레이어로 분리
- pointer 위치에 따라 card glass highlight와 jellyfish parallax가 함께 반응
- prefers-reduced-motion 대응 유지

## Files
- `docs/item3-1/index.html`
- `item-3-businesscard-storyboard-app/JELLYFISH_ASSET_SPEC.md`
