# CAD Assembly + Wiring Notes

기존 `sg90_clicker_mount_v0_1.scad` / STL 초안은 유지합니다. 이 문서는 실제 조립과 배선 관점에서 보강한 체크리스트입니다.

## 배치 의도

- SG90: cradle에 세워 고정, horn이 target key/plunger를 짧게 누름
- ESP32-C3 SuperMini: USB-C 접근 가능한 방향으로 shelf에 고정
- Servo cable: horn 회전부와 닿지 않도록 base 측면으로 cable relief 처리
- External 5V servo power: base 밖에서 들어오며 ESP32-C3 GND와 common ground

## 출력 전 실측 필요 치수

- SG90 body: 약 23 × 12 × 24 mm이나 clone별 편차 있음
- SG90 tab hole center 간격과 screw diameter
- ESP32-C3 SuperMini board 폭/길이, USB connector 돌출 방향
- 사용 key/plunger의 실제 클릭 stroke와 필요한 누름 힘

## wiring clearance 체크

- SG90 3-wire connector가 cradle에 간섭하지 않는지 확인
- USB-C cable이 ESP32-C3 shelf에서 직선으로 빠질 수 있는지 확인
- servo horn sweep 영역에 LED wire, jumper wire가 지나가지 않게 routing
- 외부 5V/GND 입력은 strain relief 또는 tape-down 지점 확보

## 첫 조립 안전 순서

1. horn 없이 firmware upload 및 servo 움직임 확인
2. horn을 rest angle에 맞춰 끼우되 target key를 누르지 않게 시작
3. `PRESS_ANGLE`을 작게 증가시키며 클릭에 필요한 최소 각도 찾기
4. 반복 동작 후 SG90이 과열되거나 buzzing하면 각도/기구 간섭을 줄임

관련 배선 그림: `wiring-sg90-esp32c3.svg`
