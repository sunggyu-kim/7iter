# Item 3 Testing / Deployment Guide — Hip Story Card Customizer

## 1) 대표님이 웹에서 바로 보는 방법: GitHub Pages

이번 라운드에서 `docs/item3/index.html`을 새로 만들었습니다. GitHub Pages가 이 저장소의 `docs/` 폴더를 publish source로 쓰면 아래 URL로 바로 열립니다.

```text
https://<github-owner>.github.io/<repo-name>/item3/
```

7iter docs 홈에서도 `Item3 Customizer` 링크가 `item3/`로 연결되도록 수정합니다.

### 기존 GitHub Pages 404 원인

이전 링크는 대략 아래처럼 `docs/` 바깥의 프로젝트 폴더를 가리켰습니다.

```text
../item-3-businesscard-storyboard-app/mockup/hip-card-customizer.html
```

GitHub Pages가 `docs/` 폴더만 배포하는 설정이면 `item-3-businesscard-storyboard-app/`는 배포 결과물에 포함되지 않습니다. 그래서 로컬 파일은 있어도 Pages URL에서는 404가 납니다.

### 이번 수정

- `mockup/hip-card-customizer.html` 기반 단일 파일을 `docs/item3/index.html`로 이관
- 외부 asset 없이 HTML/CSS/JS만 사용
- 상대 링크는 `../` docs home 정도만 사용
- Pages에서는 `/item3/` 경로로 접근 가능

## 2) Local clone 후 바로 확인하는 방법 — npm install 없이

```bash
git clone <repo-url>
cd <repo-name>
python3 -m http.server 4173 --directory docs
# browser: http://127.0.0.1:4173/item3/
```

프로젝트 폴더의 원본 mockup도 직접 확인할 수 있습니다.

```bash
cd <repo-name>/item-3-businesscard-storyboard-app
python3 -m http.server 4173
# browser: http://127.0.0.1:4173/mockup/hip-card-customizer.html
```

## 3) Local clone 후 npx serve 방식

Node.js가 있으면 별도 dependency 설치 없이 `npx serve`로 정적 서빙할 수 있습니다.

```bash
git clone <repo-url>
cd <repo-name>/item-3-businesscard-storyboard-app
npx serve . -l 4173
# browser: http://127.0.0.1:4173/mockup/hip-card-customizer.html
# root rewrite는 Vercel용이므로 local serve에서는 위 파일 경로를 직접 여는 것이 확실합니다.
```

`package.json` 스크립트도 추가했습니다.

```bash
cd <repo-name>/item-3-businesscard-storyboard-app
npm run preview
# or
npm run serve
```

## 4) Vercel demo로 웹에서 바로 보는 방법

정적 프로젝트로 바로 배포 가능하도록 `vercel.json`과 `package.json`을 추가했습니다. 실제 배포에는 Vercel 계정 로그인과 프로젝트 연결이 필요합니다.

```bash
cd <repo-name>/item-3-businesscard-storyboard-app
npx vercel login
npx vercel --prod
```

Vercel 질문 예시:

- Set up and deploy? `Y`
- Which scope? 대표님 또는 회사 Vercel account 선택
- Link to existing project? 처음이면 `N`
- Project name? 예: `item-3-hip-story-card-demo`
- Directory? 현재 디렉토리 `./`
- Build command? 비워두기 또는 `None`
- Output directory? 비워두기 또는 `.`

배포 후 root URL은 `vercel.json` rewrite로 `/mockup/hip-card-customizer.html`을 보여줍니다.

```text
https://item-3-hip-story-card-demo.vercel.app/
https://item-3-hip-story-card-demo.vercel.app/demo
```

## 5) 빠른 체크리스트

- [ ] GitHub Pages source가 `docs/`로 설정되어 있는지 확인
- [ ] `https://<owner>.github.io/<repo>/item3/` 접속
- [ ] style preset, font mood, sticker toggle, secure mode toggle 동작 확인
- [ ] vCard 저장 데모 클릭 시 `.vcf` 다운로드 확인
- [ ] Vercel 배포 시 root URL이 customizer로 rewrite되는지 확인
