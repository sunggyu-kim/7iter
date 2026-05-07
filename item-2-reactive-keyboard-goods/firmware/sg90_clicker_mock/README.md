# SG90 Clicker Mock Firmware

Arduino sketch for ESP32-C3 SuperMini + SG90.

## Default pins
- `GPIO4`: SG90 signal, orange/yellow wire
- `GPIO10`: optional external status LED through 220–1kΩ resistor to GND

If your ESP32-C3 SuperMini does not expose GPIO10, either:
1. move `STATUS_LED_PIN` to another free output pin, or
2. set `STATUS_LED_PIN = -1` to disable LED output.

Keep `SERVO_PIN` on a normal GPIO output. GPIO4 is a safe starter choice for most ESP32-C3 SuperMini boards.

## Behavior
Every 6 seconds the sketch mocks an AI-completion event, blinks the LED, moves SG90 from `REST_ANGLE` to `PRESS_ANGLE`, holds briefly, then returns.

Tune these constants after mounting the horn:

```cpp
REST_ANGLE = 20;
PRESS_ANGLE = 48;
PRESS_MS = 180;
```

Start with the servo horn detached for the first upload, confirm movement direction, then attach the horn so the rest angle does not press the key/plunger.
