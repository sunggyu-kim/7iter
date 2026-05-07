# SG90 Clicker Demo Firmware

Arduino sketch for ESP32-C3 SuperMini + SG90. It now supports both automatic mock clicks and manual Mac serial commands, so a beginner can verify the hardware before any AI integration.

## Default pins

- `GPIO4`: SG90 signal, orange/yellow wire
- `GPIO10`: optional external status LED through 220–1kΩ resistor to GND

If your ESP32-C3 SuperMini does not expose GPIO10, either:
1. move `STATUS_LED_PIN` to another free output pin, or
2. set `STATUS_LED_PIN = -1` to disable LED output.

Keep `SERVO_PIN` on a normal GPIO output. GPIO4 is a safe starter choice for most ESP32-C3 SuperMini boards.

## Behavior

- Every 6 seconds the sketch mocks an AI-completion event and clicks once.
- Serial Monitor commands at `115200` baud:
  - `DONE` or `CLICK`: click once immediately
  - `REST`: move to `REST_ANGLE`
  - `PRESS`: move to `PRESS_ANGLE` and stay there until `REST`
  - `HELP`: print command list

To disable automatic 6-second clicks and use serial-only testing, set:

```cpp
static const uint32_t MOCK_INTERVAL_MS = 0;
```

## Tune these constants

```cpp
REST_ANGLE = 20;
PRESS_ANGLE = 48;
PRESS_MS = 180;
```

Start with the servo horn detached for the first upload. Confirm movement direction, then attach the horn so the rest angle does not press the key/plunger. Increase `PRESS_ANGLE` in 2–5° steps until it just clicks; avoid buzzing or hard stalls.
