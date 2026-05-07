# COMMENT_RESPONSE_ROUND2 — Item 2 SG90/ESP32-C3 Testability Upgrade

## 이번 라운드 목표

추가 대표님 comment는 없었지만, item1/3/4의 전체 upgrade round에 맞춰 item2도 “설명 문서” 수준에서 끝나지 않고 실제 부품으로 바로 테스트 가능한 상태로 보강했습니다.

## 테스트 가능하게 만든 부분

1. **초보자용 quickstart 강화**
   - `WIRING_AND_SETUP.md`를 준비물 → 배선 → Mac 설치 → 업로드 → Serial Monitor 테스트 → CAD 조립 → troubleshooting 순서로 재정리했습니다.
   - 첫 테스트는 servo horn을 분리한 상태에서 시작하도록 명시해 기구 파손/강제 누름 위험을 줄였습니다.
   - SG90 전원은 별도 5V 1A 권장, ESP32-C3와 공통 GND 필수, 3V3 공급 금지를 반복 명시했습니다.

2. **대표님 브라우저 검토용 one-page guide 추가**
   - `docs/item2/index.html`을 새로 작성했습니다.
   - 부품, 배선표, ASCII wiring, Mac Arduino IDE/PlatformIO 설치, firmware command, CAD/SVG 링크, troubleshooting을 한 화면에서 볼 수 있습니다.
   - `docs/index.html`에서도 `Item2 Test Guide`와 item2 section button으로 바로 연결되게 했습니다.

3. **Firmware를 manual trigger 가능하게 보강**
   - 기존 6초 mock click은 유지했습니다.
   - Serial Monitor에서 `DONE` 또는 `CLICK`을 보내면 즉시 한 번 click하도록 추가했습니다.
   - `REST`, `PRESS`, `HELP` 명령을 추가해 horn 장착 전후 각도/방향 테스트가 쉬워졌습니다.
   - 실제 AI inference 완료 신호는 Mac script가 serial로 `DONE\n`을 보내는 방식으로 바로 연결할 수 있습니다.

4. **Wiring SVG/CAD 연결**
   - `docs/item2/index.html`에서 wiring SVG, assembly render, dimension SVG, SCAD, STL preview를 직접 열 수 있게 연결했습니다.

## 수정/생성 파일

- 수정: `WIRING_AND_SETUP.md`
- 수정: `firmware/sg90_clicker_mock/sg90_clicker_mock.ino`
- 수정: `firmware/sg90_clicker_mock/README.md`
- 생성: `docs/item2/index.html`
- 수정: `docs/index.html`
- 생성: `COMMENT_RESPONSE_ROUND2.md`

## 검증

- HTML parse: `docs/item2/index.html`, `docs/index.html` parse OK
- Firmware token/brace check: Arduino sketch brace balance/token check OK
- PlatformIO config check: `platformio.ini` contains expected env `esp32c3-supermini`, platform `espressif32`, board `esp32-c3-devkitm-1`, framework `arduino`, lib `ESP32Servo`
- PlatformIO CLI build/parse: local `pio` command is not installed in this environment, so full PlatformIO CLI validation was not run
