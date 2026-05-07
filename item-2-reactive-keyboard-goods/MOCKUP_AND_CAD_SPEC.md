# Item 2 Mockup + CAD Spec — Reactive SG90 Clicker

## 반영된 구매 현황
- Motor: MicroServo 9g **SG90**
- Controller: USB/WiFi **ESP32-C3 SuperMini**

## 이번 정교화
- `docs/index.html`에 SG90 clicker mock section 추가
- `cad/sg90_clicker_mount_v0_1.scad` 작성
- `cad/sg90_clicker_mount_preview_v0_1.stl` 작성
- `cad/sg90-clicker-mount-dimensions.svg` 작성
- `cad/assembly-render.svg` 작성

## 기구 컨셉
- 90×70×3mm base plate
- SG90 vertical cradle
- ESP32-C3 SuperMini shelf + cable relief
- servo horn이 target key/plunger를 짧게 누르는 구조
- 기본 동작: AI 완료 이벤트 → LED sweep → servo 약 28도 press → return

## 주의
- SG90/ESP32-C3 실물 치수를 캘리퍼로 재확인해야 최종 출력 가능
- 현재 STL은 preview/배치 확인용이며, 실제 출력 전 SCAD 치수 보정 필요
