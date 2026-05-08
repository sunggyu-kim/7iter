# Async Workflow

## Purpose
Track asynchronous updates performed outside the current OpenClaw session, e.g. local Codex, another OpenClaw run, Gemini, Claude, OpenAI, Grok, Blender/3D tooling, or manual edits.

## Job States
Backlog → Assigned → Running → Local Review → GitHub Sync Ready → Synced → Representative Review → Done

## Required records
For every meaningful async update:
1. Append or create an item job in `manager-system/items/<item>/JOBS.md`.
2. Append a concise tool/environment log in `manager-system/external-llm-logs/YYYY-MM-DD.md`.
3. Append item-level summary in `manager-system/items/<item>/HISTORY.md`.
4. Update `STATUS.md` if the visible/reviewable state changed.
5. Post distilled summary to GitHub only after local review.

## External LLM log fields
- Time
- Item(s)
- Environment/tool name
- Source location/session/repo path if available
- Prompt/request summary
- Files touched
- Validation evidence
- Manager decision
- GitHub sync target

## Rule
The log records what happened in another LLM/tool. It does not create a separate documentation file for that LLM.
