# Overall Manager Decisions

## 2026-05-08 — Corrected manager model
- Decision: Use one overall manager for all items and forks.
- Rejected: manager1~4 split by item.
- Reason: representative intended one manager to discover/organize all item branches.

## 2026-05-08 — External LLM logging model
- Decision: Do not create per-LLM markdown files.
- Use `external-llm-logs/YYYY-MM-DD.md` entries to record work done by local Codex/OpenClaw/Gemini/etc.
## 2026-05-08 16:06 — Duplicate instruction handling
- Decision: #1/#5 are one merged Item 1-1 work packet; #3/#6 are one merged Item 3-1 work packet.
- Reason: Representative explicitly requested avoiding duplicated subagent work.
- Execution: Overall Manager performs or assigns once, then syncs summaries to all relevant issues.
