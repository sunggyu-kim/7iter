# 2026-05-08 Round 7 — STL cleanup and SW signal plan

## HW cleanup
- Removed suspicious/placeholder STL review links from public Item 2 page.
- Removed placeholder STL files from docs/cad paths.
- Kept latest SCAD/SVG review assets and marked STL export as next dimensional-validation step.

## SW plan
- Added local HTTP signal receiver/client for inference `start` / `done` / `error` events.
- OpenClaw environment is Linux; Codex/other agent environment is assumed Mac until tested separately.
- Added test plan and roadmap.

## Files
- `item-2-reactive-keyboard-goods/software/inference_signal_server.py`
- `item-2-reactive-keyboard-goods/software/inference_signal_client.py`
- `item-2-reactive-keyboard-goods/SW_SIGNAL_TEST_PLAN.md`
- `item-2-reactive-keyboard-goods/ROADMAP.md`
