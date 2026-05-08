# Async Workflow

## Job States
Backlog → Assigned → Running → Local Review → GitHub Sync Ready → Synced → Representative Review → Done

## Job Record
- Job ID
- Item
- Manager
- Agent
- Prompt
- Inputs
- Expected Output
- Files Allowed
- Files Touched
- Validation
- GitHub Sync Target

## Rules
- Every local agent run gets one job record.
- Every meaningful change appends to item HISTORY.md.
- GitHub issue comments receive only distilled summaries, not raw logs.
- Representative-facing status lives in STATUS.md.
