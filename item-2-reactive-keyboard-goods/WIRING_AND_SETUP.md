# SG90 ↔ ESP32-C3 SuperMini Wiring + Mac Setup Guide

대표님 comment 대응용 하드웨어 구동 가이드입니다. 기존 CAD 초안은 유지하고, 실제 servo/ESP32-C3 연결과 Mac 업로드 절차를 보강합니다.

## 1. 핵심 결론

- ESP32-C3 SuperMini는 **servo 신호만** 담당합니다.
- SG90 전원은 가능하면 **별도 5V 전원(1A 권장)** 을 씁니다.
- ESP32-C3 GND와 SG90 전원 GND는 반드시 **공통 GND** 로 묶습니다.
- SG90 signal은 ESP32-C3의 3.3V GPIO PWM으로 구동 가능합니다.

## 2. SG90 wire 색상

일반 SG90 기준:

| SG90 wire | 역할 | 연결 |
|---|---|---|
| Brown / Black | GND | ESP32-C3 GND + 외부 5V 전원 - |
| Red | V+ | 외부 5V 전원 + |
| Orange / Yellow | Signal | ESP32-C3 GPIO4 예시 |

> 금지: SG90 빨간선을 ESP32-C3 `3V3`에 연결하지 마세요. 전류 부족/리셋/보드 손상 위험이 있습니다.

## 3. 권장 배선

```text
External 5V +  ---- SG90 Red
External 5V -  ---- SG90 Brown/Black ---- ESP32-C3 GND
ESP32-C3 GPIO4 ---- SG90 Orange/Yellow
Mac USB-C      ---- ESP32-C3 USB-C, firmware upload + serial monitor
```

### 전원 옵션

1. **권장: servo 별도 5V 1A 전원**
   - USB power bank, breadboard 5V supply, 또는 안정적인 5V adapter.
   - ESP32-C3는 Mac USB로 전원/업로드.

2. **가능하지만 주의: ESP32-C3 `5V/VBUS` pin에서 SG90 공급**
   - 보드/USB 케이블/포트가 SG90 stall current를 버티는지 불확실합니다.
   - 데모 중 ESP32-C3 리셋이 나면 별도 5V로 분리하세요.

3. **비권장: ESP32-C3 `3V3` pin에서 SG90 공급**
   - 하지 않습니다.

## 4. pin 선택

기본 예제는 다음을 사용합니다.

- `SERVO_PIN = GPIO4`
- `STATUS_LED_PIN = GPIO10` optional external LED

변경 방법:

```cpp
static const int SERVO_PIN = 4;
static const int STATUS_LED_PIN = 10;
```

GPIO10이 보드에 없으면 LED를 끄세요.

```cpp
static const int STATUS_LED_PIN = -1;
```

주의:
- 일부 ESP32-C3 SuperMini clone은 onboard LED가 GPIO8일 수 있습니다. GPIO8/9는 부팅 strap 성격이 있어 외부 회로를 무겁게 물리지 않는 편이 안전합니다.
- servo signal pin은 normal GPIO output이면 됩니다. 부팅 중 servo가 살짝 움직일 수 있으므로 기구 간섭이 없는 rest position에서 시작하세요.

## 5. Mac — Arduino IDE 설치/업로드

### 설치

1. Arduino IDE 2.x 설치: <https://www.arduino.cc/en/software>
2. IDE 실행 → `Arduino IDE > Settings`
3. `Additional boards manager URLs`에 추가:

```text
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
```

4. `Tools > Board > Boards Manager...`에서 `esp32` 검색 → `esp32 by Espressif Systems` 설치
5. `Tools > Manage Libraries...`에서 `ESP32Servo` 설치

### board 설정 예시

- Board: `ESP32C3 Dev Module`
- USB CDC On Boot: `Enabled`
- Upload Mode: `UART0 / Hardware CDC` 또는 IDE가 제안하는 기본값
- Flash Size: 보드 사양에 맞춤, 모르면 `4MB`
- Port: `/dev/cu.usbmodem...` 또는 `/dev/cu.usbserial...`

업로드 실패 시:
- 보드의 `BOOT` 버튼을 누른 채 Upload 시작 → `Connecting...`이 보이면 손을 뗍니다.
- 그래도 실패하면 USB data cable인지 확인합니다.

### 실행

1. `firmware/sg90_clicker_mock/sg90_clicker_mock.ino` 열기
2. SG90 horn을 일단 분리한 상태로 업로드
3. Serial Monitor 115200 baud 열기
4. 6초마다 `mock inference complete -> click` 로그와 servo click 동작 확인
5. 방향/각도 확인 후 horn을 장착하고 `REST_ANGLE`, `PRESS_ANGLE` 조정

## 6. Mac — PlatformIO 대안

### 설치

1. VS Code 설치
2. Extensions에서 `PlatformIO IDE` 설치
3. 이 item 폴더의 `platformio.ini`를 열고 PlatformIO project로 인식시킵니다.

### 업로드

```bash
cd item-2-reactive-keyboard-goods
pio run -e esp32c3-supermini -t upload
pio device monitor -b 115200
```

`pio`가 없으면 VS Code PlatformIO 터미널에서 실행하거나, CLI를 설치합니다.

```bash
python3 -m pip install -U platformio
```

## 7. 기구 조립 순서

1. ESP32-C3만 Mac에 연결하고 firmware upload.
2. SG90 전원 없이 signal/GND 배선만 확인.
3. 별도 5V 전원 OFF 상태에서 SG90 red/brown 연결.
4. ESP32-C3 GND와 5V supply GND 공통 연결 확인.
5. 5V 전원 ON → servo가 rest angle로 이동하는지 확인.
6. horn을 분리한 채 press 방향 확인.
7. CAD cradle에 SG90 고정, horn을 rest angle에서 key/plunger에 닿지 않게 장착.
8. `PRESS_ANGLE`을 2–5도 단위로 올리며 실제 클릭 지점만 찾습니다.

## 8. 실제 inference 완료 신호로 바꾸는 지점

현재 firmware는 `mockInferenceComplete()`가 6초마다 true를 반환합니다. 실제 연동 시 이 함수만 다음 중 하나로 교체합니다.

- USB serial로 Mac script가 `DONE\n` 전송
- Wi-Fi HTTP endpoint 수신
- BLE / MQTT event 수신

MVP 데모에서는 Mac에서 inference 작업 완료 후 serial로 `DONE`을 보내는 방식이 가장 단순합니다.
