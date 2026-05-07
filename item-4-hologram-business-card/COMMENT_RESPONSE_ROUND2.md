# Issue #4 Comment Response — Round 2

## Comment-by-comment response table

| Latest comment / requirement | Response in this round | Files |
|---|---|---|
| item3와 동일한 이유로 대표님이 웹에서 바로 볼 수 있어야 함 | GitHub Pages publish root인 `docs/` 아래에 item4 전용 interactive page를 추가했습니다. | `docs/item4/index.html` |
| Vercel처럼 최종 배포가 쉬운 방식으로 사용자들이 볼 수 있는 목업 필요 | item4 폴더에 Vercel-compatible static build setup을 추가했습니다. `npm run build`가 Pages와 동일한 소스를 `dist/`로 복사합니다. | `package.json`, `vercel.json`, `scripts/build-static.mjs` |
| 기존 `mockup/holo-trading-card/index.html`를 바탕으로 docs에서 바로 동작하게 만들 것 | 기존 3D tilt/foil/secret reveal 구조를 유지하면서 docs용 single-file HTML로 이관하고, UX를 데모 페이지 형태로 확장했습니다. | `docs/item4/index.html` |
| 효과를 더 직관적으로 업그레이드 | tier selector, photo URL, name/role/description editing, hidden reveal text editing, auto-tilt button, reduced-motion button, motion/tilt 안내문을 추가했습니다. | `docs/item4/index.html` |
| GitHub Pages 404/상대경로 원인과 수정 내용 문서화 | Pages root가 `docs/`라서 source folder 상대경로가 404가 되는 원인과 해결 URL을 문서화했습니다. | `PAGES_404_FIX.md` |
| local clone/npm/serve 방식 TESTING_GUIDE 작성 | Git clone 후 `python3 -m http.server --directory docs`, item4 폴더 `npm run serve`, Vercel build 방법을 정리했습니다. | `TESTING_GUIDE.md` |
| 포켓몬/유희왕 상표/캐릭터/로고 사용 금지 | demo copy와 visual 모두 generic holo/collectible identity card grammar만 사용했습니다. 특정 상표/캐릭터/로고는 포함하지 않았습니다. | `docs/item4/index.html` |
| 검증 실행 | HTML token/script check, required file existence, npm build, local HTTP 200 확인을 수행했습니다. | `scripts/validate-static.mjs` |

## Representative review URLs

GitHub Pages expected URL:

```text
https://sunggyu-kim.github.io/7iter/item4/
```

Local docs root:

```bash
cd /path/to/7iter
python3 -m http.server 4174 --directory docs
# open http://localhost:4174/item4/
```

Vercel project root option:

```bash
cd item-4-hologram-business-card
npm run build
# Vercel output directory: dist
```

## Notes

- No git push or issue comment was performed.
- Scope kept to item4 folder, `docs/item4`, and Pages-safe link update in `docs/index.html`.
