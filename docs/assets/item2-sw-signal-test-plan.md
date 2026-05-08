# Item 2 SW Signal Test Plan

## Goal
Receive inference lifecycle signals (`start`, `done`, `error`) from OpenClaw, local Codex, OpenAI/Codex CLI wrappers, or manual experiments so the SG90 clicker can react to AI work completion.

## Current environment observed
- OpenClaw runtime host OS: `Linux 6.17.0-22-generic`
- Machine: `sunggyu-B660M-DS3H-DDR4`
- This environment is Linux. Representative noted Codex/other agents may be Mac; that must be tested separately.

## Recommendation
Use a small local HTTP receiver with explicit host/port.

Default contract:
```text
POST http://127.0.0.1:8765/signal
{"source":"openclaw|codex|openai|manual", "event":"start|done|error", "run_id":"..."}
```

## Why host/port is appropriate
Most agent environments can run a wrapper script or shell hook that calls a local HTTP endpoint before and after inference/tool execution. If direct internal model lifecycle hooks are unavailable, wrapper-based signaling is still testable.

## Local Linux test
```bash
python3 item-2-reactive-keyboard-goods/software/inference_signal_server.py --host 127.0.0.1 --port 8765
python3 item-2-reactive-keyboard-goods/software/inference_signal_client.py --event start --source openclaw-test --run-id demo
python3 item-2-reactive-keyboard-goods/software/inference_signal_client.py --event done --source openclaw-test --run-id demo
cat item-2-reactive-keyboard-goods/software/inference_signal_events.jsonl
```

## Mac/Codex test hypothesis
On Mac, run the same server or point to the Linux host IP if reachable. Wrap Codex/OpenAI command execution:
```bash
python signal_client.py --event start --source codex-mac --run-id "$RUN_ID"
# run codex/openai task
python signal_client.py --event done --source codex-mac --run-id "$RUN_ID"
```

## Unknowns to verify
- Whether Codex exposes native start/done hooks.
- Whether OpenAI/Codex CLI can be wrapped consistently.
- Network route between Mac and Linux host if not same machine.
- Whether firewall allows selected port.

## Next step
Connect `done` event to the existing ESP32/SG90 serial or HTTP bridge after signal reception is stable.
