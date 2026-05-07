# GitHub Issue #2 Comment Response — Hardware/Firmware 정교화

## Comment별 대응표

| 최신 comment 요구 | 대응 |
|---|---|
| scad 초안은 이대로 수립 | 기존 `cad/sg90_clicker_mount_v0_1.scad`, STL, 기존 SVG는 수정하지 않았습니다. |
| servo와 SuperMini ESP32-C3을 어떻게 연결시켜서 구동가능한지 방법을 알려줄 것 | `WIRING_AND_SETUP.md`에 SG90 wire 색상, 외부 5V 전원, common GND, GPIO4 signal 연결, 전원 주의사항을 작성했습니다. `cad/wiring-sg90-esp32c3.svg` 배선도를 추가했습니다. |
| Mac 환경에서 무엇을 설치해야 하는지도 알려줄 것 | `WIRING_AND_SETUP.md`에 Arduino IDE 2.x, esp32 board package URL, ESP32Servo library, board/port/upload 절차를 작성했습니다. PlatformIO 대안도 `platformio.ini`와 함께 추가했습니다. |
| 실제 구동 firmware 예제 필요 | `firmware/sg90_clicker_mock/sg90_clicker_mock.ino`에 AI 완료 mock → LED blink → SG90 click → return 예제를 작성했습니다. |
| CAD는 유지하되 조립/배선 관점 보강 | `cad/ASSEMBLY_WIRING_NOTES.md`와 `cad/wiring-sg90-esp32c3.svg`를 추가했습니다. |

## 생성 파일 목록

- `WIRING_AND_SETUP.md`
- `COMMENT_RESPONSE.md`
- `platformio.ini`
- `firmware/sg90_clicker_mock/sg90_clicker_mock.ino`
- `firmware/sg90_clicker_mock/README.md`
- `cad/ASSEMBLY_WIRING_NOTES.md`
- `cad/wiring-sg90-esp32c3.svg`

## 실행 방법 요약

### Arduino IDE

1. Arduino IDE 2.x 설치
2. Boards Manager URL 추가:
   `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
3. `esp32 by Espressif Systems` board package 설치
4. `ESP32Servo` library 설치
5. Board를 `ESP32C3 Dev Module`로 선택
6. `firmware/sg90_clicker_mock/sg90_clicker_mock.ino` 열기
7. SG90 horn을 분리한 채 upload
8. Serial Monitor 115200 baud에서 6초마다 click mock 확인

### PlatformIO

```bash
cd /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter/item-2-reactive-keyboard-goods
pio run -e esp32c3-supermini -t upload
pio device monitor -b 115200
```

## 검증 결과

완료 전 아래 검증을 수행했습니다.

- 파일 존재 검증: 통과
- Arduino sketch brace balance / 필수 token 검사: 통과
- SVG XML well-formed 검사: 통과
- PlatformIO 설정 파일 존재 및 env 확인: 통과

실제 ESP32-C3 compile/upload는 로컬에 Arduino CLI/PlatformIO 및 보드 연결이 필요하여 문서화 범위로 남겼습니다.
