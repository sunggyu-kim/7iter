# 2026-05-08 Round 4 — Pages 404 root-cause and link audit

대표님 최신 comment 기준으로 Item 2의 CAD/SVG/STL 링크 404 원인을 수정했습니다.

## 원인
GitHub Pages는 repository root가 아니라 `/docs`를 publish root로 쓰고 있습니다. 기존 버튼은 `/item-2-reactive-keyboard-goods/...` 또는 `../../item-2...` 형태로 `/docs` 밖 파일을 참조해 404가 발생했습니다.

## 수정
- CAD/SVG/STL/firmware/scad guide 파일을 `docs/item2/assets/` 또는 `docs/assets/`로 복사
- `docs/item2/index.html`의 모든 사용자 클릭 링크를 Pages-safe 상대경로로 교체
- embedded wiring SVG도 `assets/wiring-sg90-esp32c3.svg`로 교체

## 검증 대상
- `/item2/`
- `/item2/assets/wiring-sg90-esp32c3.svg`
- `/item2/assets/assembly-render.svg`
- `/item2/assets/sg90-clicker-mount-dimensions.svg`
- STL placeholder URL removed in Round 7; export from latest SCAD after dimensional validation.
- `/item2/assets/sg90_clicker_mock.ino`
- `/item2/assets/sg90_clicker_mount_v0_1.scad`
- `/assets/item2-wiring-and-setup.md`
