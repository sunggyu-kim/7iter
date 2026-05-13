# Item 2 — One Hardware / Multi-Version Test & SW QA Plan

## Purpose
대표님 comment 반영: Codex 기반 GitHub 문서를 기준으로 **하나의 hardware**에서 여러 HW/FW/SW version을 반복 검증하고, inference signal 품질을 재현 가능하게 공유한다.

## Version matrix
| Layer | Version examples | What changes | Must remain stable |
|---|---|---|---|
| HW base | HW-v0.1, HW-v0.2 | base, SG90 bracket, horn angle, key target geometry | ESP32-C3 pin map, USB power, safe servo travel |
| CAD/Soul module | soul-v0.1..N | top socket ornament, mascot shape | SG90 horn/socket dimensions |
| Firmware | fw-v0.1..N | angle, speed, LED pattern, debounce | `/start`, `/done`, `/error` signal semantics |
| Host SW | sw-v0.1..N | receiver/client wrapper, local agent bridge | JSON event schema, timestamped logs |
| Agent integration | codex/openclaw/gemini/local | completion hook adapter | same start/done/error contract |

## Task list
1. **HW fit test**: mount SG90, verify horn clearance, press depth, no key over-travel.
2. **Signal path test**: send `start -> done -> error` from `inference_signal_client.py` to `inference_signal_server.py`.
3. **Firmware actuation test**: LED sweep + SG90 press/return within configured angle limits.
4. **Regression test**: repeat the same signal script after each CAD/FW/SW change.
5. **Agent adapter test**: wrap Codex/OpenClaw/local completion events so they emit the same JSON schema.
6. **Evidence capture**: save terminal log, firmware config, short video/photo, and version IDs.

## Acceptance criteria
- Receiver logs every event with timestamp and version metadata.
- `start` never triggers servo press; only `done` does.
- `error` uses distinct LED/servo feedback and never looks like success.
- 20 consecutive `done` events complete without servo stall or missed webhook.
- HW-v0.1 and HW-v0.2 can be compared with one shared checklist.

## Reporting format
```markdown
## Item 2 QA run
- Date:
- Hardware version:
- CAD/Soul module version:
- Firmware version:
- Host SW version:
- Agent adapter:
- Result: pass/fail
- Evidence links:
- Regressions found:
- Next fix:
```

## Files referenced
- `software/inference_signal_server.py`
- `software/inference_signal_client.py`
- `SW_SIGNAL_TEST_PLAN.md`
- `ROADMAP.md`
- `cad/sg90_soul_modules_v0_1.scad`
