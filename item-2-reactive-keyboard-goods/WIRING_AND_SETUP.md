# SG90 ↔ ESP32-C3 SuperMini Quickstart

대표님이 실제 부품으로 바로 테스트할 수 있게 정리한 wiring + Mac upload 가이드입니다. 목표는 **10분 안에 “AI 완료 → 딸깍” 동작을 눈으로 확인**하는 것입니다.

## 0. 준비물

| 구분 | 필요 부품 |
|---|---|
| 보드 | ESP32-C3 SuperMini 1개, USB-C data cable |
| 액추에이터 | MicroServo 9g SG90 1개, 기본 servo horn |
| 전원 | SG90용 외부 5V 1A 권장 power bank/adapter/breadboard supply |
| 배선 | jumper wire 3개 이상, 필요 시 breadboard |
| 선택 | 외부 LED 1개 + 220–1kΩ 저항 |
| 소프트웨어 | Arduino IDE 2.x 또는 VS Code + PlatformIO |

> 안전 원칙: SG90 빨간선은 ESP32-C3 `3V3`에 연결하지 않습니다. 전류 부족으로 리셋/오동작/손상 위험이 있습니다.

## 1. 배선 한눈 요약

일반 SG90 wire 색상 기준입니다.

| SG90 wire | 역할 | 연결 |
|---|---|---|
| Brown / Black | GND | 외부 5V 전원 `-` + ESP32-C3 `GND` |
| Red | V+ | 외부 5V 전원 `+` |
| Orange / Yellow | Signal | ESP32-C3 `GPIO4` |

```text
External 5V +  ---- SG90 Red
External 5V -  ---- SG90 Brown/Black ---- ESP32-C3 GND
ESP32-C3 GPIO4 ---- SG90 Orange/Yellow
Mac USB-C      ---- ESP32-C3 USB-C, firmware upload + serial monitor
```

배선 그림: [`cad/wiring-sg90-esp32c3.svg`](cad/wiring-sg90-esp32c3.svg)

## 2. 첫 테스트 순서 — horn 분리 상태

1. SG90 horn을 servo에서 빼 둡니다. 첫 동작 방향을 모르는 상태에서 키를 누르게 만들지 않기 위함입니다.
2. ESP32-C3만 Mac에 USB-C로 연결합니다.
3. SG90 signal 선을 `GPIO4`에 연결합니다.
4. SG90 GND와 ESP32-C3 GND를 연결합니다.
5. 외부 5V 전원 OFF 상태에서 SG90 Red/Brown을 전원에 연결합니다.
6. 외부 5V 전원을 켭니다.
7. firmware를 upload합니다.
8. Serial Monitor `115200` baud를 엽니다.
9. `DONE`을 입력하고 Enter를 눌러 servo가 한 번 움직이는지 확인합니다.
10. 방향과 각도가 맞으면 horn을 rest 위치에 끼우고 CAD cradle/target key로 옮깁니다.

## 3. Mac — Arduino IDE 설치/업로드

### 3-1. 설치

1. Arduino IDE 2.x 설치: <https://www.arduino.cc/en/software>
2. IDE 실행 → `Arduino IDE > Settings`
3. `Additional boards manager URLs`에 추가:

```text
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
```

4. `Tools > Board > Boards Manager...`에서 `esp32` 검색 → `esp32 by Espressif Systems` 설치
5. `Tools > Manage Libraries...`에서 `ESP32Servo` 설치

### 3-2. board 설정 예시

- Board: `ESP32C3 Dev Module`
- USB CDC On Boot: `Enabled`
- Upload Mode: `UART0 / Hardware CDC` 또는 IDE 기본값
- Flash Size: 모르면 `4MB`
- Port: `/dev/cu.usbmodem...` 또는 `/dev/cu.usbserial...`

업로드 실패 시:

- 보드의 `BOOT` 버튼을 누른 채 Upload 시작 → `Connecting...`이 보이면 손을 뗍니다.
- USB 충전 전용 cable이 아닌 **data cable**인지 확인합니다.
- Port가 안 보이면 USB-C 방향/허브/케이블을 바꿔 봅니다.

### 3-3. firmware 실행

1. `firmware/sg90_clicker_mock/sg90_clicker_mock.ino` 열기
2. Upload
3. Serial Monitor 115200 baud 열기
4. 시작 로그 확인: `SG90 ESP32-C3 reactive clicker demo starting`
5. `DONE` 입력 → `serial completion event -> click` 로그와 SG90 동작 확인
6. 6초마다 자동으로 `mock inference complete -> click`도 발생합니다.

Serial Monitor 명령:

| 명령 | 동작 |
|---|---|
| `DONE` 또는 `CLICK` | 즉시 한 번 click |
| `REST` | rest angle로 이동 |
| `PRESS` | press angle로 이동 후 유지 |
| `HELP` | 명령 목록 출력 |

자동 6초 click을 끄고 실제 완료 신호만 테스트하려면 firmware에서 아래처럼 바꿉니다.

```cpp
static const uint32_t MOCK_INTERVAL_MS = 0;
```

## 4. Mac — PlatformIO 대안

VS Code + PlatformIO를 선호하면 이 item 폴더를 그대로 project로 열면 됩니다.

```bash
cd /home/sunggyu/.openclaw/workspace/projects/marketing-seven-iter/item-2-reactive-keyboard-goods
pio run -e esp32c3-supermini
pio run -e esp32c3-supermini -t upload
pio device monitor -b 115200
```

`pio`가 없으면 VS Code PlatformIO terminal을 쓰거나 CLI를 설치합니다.

```bash
python3 -m pip install -U platformio
```

## 5. pin/각도 조정

기본값:

```cpp
static const int SERVO_PIN = 4;
static const int STATUS_LED_PIN = 10;
static const int REST_ANGLE = 20;
static const int PRESS_ANGLE = 48;
```

- `GPIO10`이 보드에 없으면 `STATUS_LED_PIN = -1`로 LED를 끕니다.
- 일부 ESP32-C3 SuperMini clone은 onboard LED가 GPIO8일 수 있습니다. GPIO8/9는 boot strap 성격이 있어 외부 회로를 무겁게 물리지 않는 편이 안전합니다.
- `PRESS_ANGLE`은 2–5도 단위로 늘려 실제 클릭에 필요한 최소 각도만 찾습니다.
- buzzing/떨림/과열이 있으면 horn이 막혀 있거나 press angle이 과합니다.

## 6. CAD 조립 순서

CAD 참고:

- [`cad/assembly-render.svg`](cad/assembly-render.svg)
- [`cad/sg90-clicker-mount-dimensions.svg`](cad/sg90-clicker-mount-dimensions.svg)
- [`cad/sg90_clicker_mount_v0_1.scad`](cad/sg90_clicker_mount_v0_1.scad)
- [`cad/ASSEMBLY_WIRING_NOTES.md`](cad/ASSEMBLY_WIRING_NOTES.md)

조립:

1. horn 없이 firmware upload 및 SG90 움직임 확인
2. cradle에 SG90을 고정하되 wire가 horn sweep 영역을 지나가지 않게 routing
3. rest angle에서 target key/plunger를 누르지 않도록 horn 장착
4. `PRESS`/`REST` serial 명령으로 stroke 확인
5. `PRESS_ANGLE`을 작게 조정해 “딸깍” 직전/직후의 최소 각도 확정
6. 10회 이상 반복 후 SG90 온도, buzzing, ESP32-C3 reset 여부 확인

## 7. 실제 AI 완료 신호로 바꾸는 지점

현재 firmware는 두 가지 trigger를 제공합니다.

1. `mockInferenceComplete()` — 6초마다 자동 완료 mock
2. Serial command `DONE` — Mac에서 실제 작업 완료 후 전송 가능

MVP 데모에서는 Mac script가 inference 완료 후 serial port로 `DONE\n`을 보내는 방식이 가장 단순합니다. 이후 Wi-Fi HTTP endpoint, BLE, MQTT로 확장할 수 있습니다.

## 8. Troubleshooting

| 증상 | 확인할 것 |
|---|---|
| servo가 전혀 안 움직임 | SG90 Red가 외부 5V `+`, Brown/Black이 GND인지 확인. ESP32-C3 GND와 외부 5V GND가 반드시 공통이어야 함 |
| ESP32-C3가 리셋됨 | SG90을 ESP32-C3 3V3/약한 VBUS에서 먹이고 있을 가능성. 별도 5V 1A로 분리 |
| 업로드 `Connecting...` 실패 | BOOT 버튼 누른 채 upload 시작, data cable 확인, Port 재선택 |
| Serial Monitor 글자가 깨짐 | baud를 `115200`으로 설정 |
| servo가 계속 윙윙거림 | horn이 물리적으로 막힘. `PRESS_ANGLE` 낮추고 horn rest 위치 재장착 |
| 키가 안 눌림 | `PRESS_ANGLE`을 2–5도씩 증가, horn 길이/target 높이 조정 |
| 방향이 반대 | horn을 반대 방향으로 재장착하거나 `REST_ANGLE`/`PRESS_ANGLE` 관계를 바꿈 |
