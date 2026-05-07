/*
  SG90 + ESP32-C3 SuperMini reactive clicker demo firmware

  What it proves in 10 minutes:
  - SG90 wiring is correct.
  - ESP32-C3 can drive a safe press/release motion.
  - A real completion event can be tested from a Mac Serial Monitor by sending DONE.

  Flow:
  - Blinks status LED while waiting.
  - Every MOCK_INTERVAL_MS it performs an automatic demo click.
  - If the serial monitor sends DONE or CLICK, it clicks immediately.

  Hardware defaults:
  - SG90 signal: GPIO4
  - Optional external LED: GPIO10 via 220-1k ohm resistor to GND
  - SG90 V+ should be separate 5V, GND shared with ESP32-C3.

  Board target in Arduino IDE:
  - ESP32C3 Dev Module or compatible ESP32-C3 SuperMini profile
*/

#include <Arduino.h>
#include <ESP32Servo.h>

// Change these two pins if your SuperMini breakout/layout differs.
static const int SERVO_PIN = 4;       // SG90 orange/yellow signal wire
static const int STATUS_LED_PIN = 10; // optional external LED + resistor; set to -1 to disable

// SG90 safe starter angles. Tune mechanically after checking horn clearance.
static const int REST_ANGLE = 20;
static const int PRESS_ANGLE = 48;    // about +28 degrees from rest
static const uint16_t PRESS_MS = 180;
static const uint16_t SETTLE_MS = 220;

// Mock completion cadence. Set to 0 to disable automatic demo clicks.
static const uint32_t MOCK_INTERVAL_MS = 6000;
static const uint32_t LED_HEARTBEAT_MS = 500;

Servo clickServo;
uint32_t lastMockAt = 0;
uint32_t lastLedAt = 0;
bool ledOn = false;

void writeStatusLed(bool on) {
  if (STATUS_LED_PIN < 0) return;
  digitalWrite(STATUS_LED_PIN, on ? HIGH : LOW);
}

void printHelp() {
  Serial.println("Commands: DONE/CLICK = click once, REST = rest angle, PRESS = press angle, HELP = this help");
}

bool mockInferenceComplete() {
  if (MOCK_INTERVAL_MS == 0) return false;
  const uint32_t now = millis();
  if (now - lastMockAt >= MOCK_INTERVAL_MS) {
    lastMockAt = now;
    return true;
  }
  return false;
}

void heartbeatLed() {
  if (STATUS_LED_PIN < 0) return;
  const uint32_t now = millis();
  if (now - lastLedAt >= LED_HEARTBEAT_MS) {
    lastLedAt = now;
    ledOn = !ledOn;
    writeStatusLed(ledOn);
  }
}

void clickOnce() {
  // quick attention blink before movement
  for (int i = 0; i < 3; i++) {
    writeStatusLed(true);
    delay(70);
    writeStatusLed(false);
    delay(70);
  }

  clickServo.write(PRESS_ANGLE);
  writeStatusLed(true);
  delay(PRESS_MS);

  clickServo.write(REST_ANGLE);
  delay(SETTLE_MS);
  writeStatusLed(false);
}

void handleSerialCommand(String command) {
  command.trim();
  command.toUpperCase();
  if (command.length() == 0) return;

  if (command == "DONE" || command == "CLICK") {
    Serial.println("serial completion event -> click");
    clickOnce();
  } else if (command == "REST") {
    Serial.println("servo -> REST_ANGLE");
    clickServo.write(REST_ANGLE);
  } else if (command == "PRESS") {
    Serial.println("servo -> PRESS_ANGLE; send REST to release");
    clickServo.write(PRESS_ANGLE);
  } else if (command == "HELP") {
    printHelp();
  } else {
    Serial.print("unknown command: ");
    Serial.println(command);
    printHelp();
  }
}

void setup() {
  Serial.begin(115200);
  delay(300);
  Serial.println("SG90 ESP32-C3 reactive clicker demo starting");
  printHelp();

  if (STATUS_LED_PIN >= 0) {
    pinMode(STATUS_LED_PIN, OUTPUT);
    writeStatusLed(false);
  }

  // SG90 expects ~50Hz servo pulses. Pulse widths are conservative SG90 defaults.
  clickServo.setPeriodHertz(50);
  clickServo.attach(SERVO_PIN, 500, 2400);
  clickServo.write(REST_ANGLE);

  lastMockAt = millis();
}

void loop() {
  heartbeatLed();

  if (Serial.available() > 0) {
    handleSerialCommand(Serial.readStringUntil('\n'));
  }

  if (mockInferenceComplete()) {
    Serial.println("mock inference complete -> click");
    clickOnce();
  }
}
