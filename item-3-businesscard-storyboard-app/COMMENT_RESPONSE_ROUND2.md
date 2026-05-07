# Comment Response Round 2 — Item 3 Web Demo / Deployment

## 대표님 최신 comment별 대응표

| 최신 comment / 문제 | 대응 | 산출물 |
|---|---|---|
| GitHub Pages가 404라 직접 확인 불가 | Pages가 `docs/`만 배포할 때 프로젝트 폴더는 포함되지 않는 점을 원인으로 정리하고, 데모를 `docs/item3/index.html` 단일 파일로 이관 | `docs/item3/index.html`, `TESTING_GUIDE.md` |
| local에 clone/npm 식으로 설치해서 세부적으로 보는 방법 필요 | npm install 없이 `python3 -m http.server --directory docs`, 원본 mockup 서버, `npx serve`, npm scripts까지 문서화 | `TESTING_GUIDE.md`, `package.json` |
| 가볍게 추후 배포 가정하에 Vercel demo 검토 | build 없는 static deploy 구조로 `vercel.json` rewrite(`/`, `/demo`)와 `package.json` scripts 작성. 인증이 없으므로 실제 배포 명령과 Vercel 질문 대응까지 문서화 | `vercel.json`, `package.json`, `TESTING_GUIDE.md` |
| 대표가 바로 볼 수 있는 방법 필요 | GitHub Pages URL 패턴 `/item3/`, local URL, Vercel URL 패턴을 각각 명시 | `TESTING_GUIDE.md` |
| 기존 hip customizer를 웹에서 바로 열리게 | 기존 `mockup/hip-card-customizer.html` 기반으로 외부 asset 없는 단일 HTML demo 생성 | `docs/item3/index.html` |
| 무단 외부 asset 다운로드 금지 | 외부 asset 다운로드 없음. CSS gradient, emoji, inline JS만 사용 | `docs/item3/index.html` |

## 대표님께 전달 가능한 짧은 답변 초안

대표님, GitHub Pages 404 원인은 데모 파일이 `docs/` 배포 폴더 밖에 있었기 때문입니다. 이번에는 `docs/item3/index.html`로 단일 파일 데모를 이관해서 Pages 설정이 `docs/` 기준이면 아래 경로로 바로 보실 수 있게 했습니다.

```text
https://<github-owner>.github.io/<repo-name>/item3/
```

로컬에서는 clone 후 npm 설치 없이도 바로 확인 가능합니다.

```bash
git clone <repo-url>
cd <repo-name>
python3 -m http.server 4173 --directory docs
# http://127.0.0.1:4173/item3/
```

Vercel 배포도 static project로 준비했습니다.

```bash
cd item-3-businesscard-storyboard-app
npx vercel login
npx vercel --prod
```

배포 후에는 Vercel root URL에서 바로 customizer가 열리도록 rewrite를 넣었습니다.

## 변경 파일

- `docs/item3/index.html` — 대표 검토용 GitHub Pages 단일파일 web demo
- `item-3-businesscard-storyboard-app/vercel.json` — Vercel static rewrite/config
- `item-3-businesscard-storyboard-app/package.json` — local serve / Vercel scripts
- `item-3-businesscard-storyboard-app/TESTING_GUIDE.md` — clone/local/npm/Vercel/404 원인 문서
- `item-3-businesscard-storyboard-app/COMMENT_RESPONSE_ROUND2.md` — 본 대응표
- `docs/index.html` — Item3 링크를 Pages-safe 경로(`item3/`)로 수정

## 검증 결과

- HTML parse: 통과
- 필수 파일 존재: 통과
- `docs/item3/index.html` 외부 asset URL 없음: 통과
- local static serving 점검: `python3 -m http.server --directory docs` 기준 `/item3/` 200 OK
