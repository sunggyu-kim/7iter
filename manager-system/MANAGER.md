# Overall Manager — 7iter item/project controller

## Scope
The manager owns Item 1~4 and all forked/derived items (`1-1`, `3-1`, future `N-1`, `N-2`, etc.).

## Responsibilities
1. Discover and register new forked items.
2. Maintain GitHub issue/project mapping.
3. Maintain each item `CONTEXT.md`, `HISTORY.md`, `STATUS.md`, `JOBS.md`, and `GITHUB.md`.
4. Track asynchronous updates from other environments/tools by appending to `external-llm-logs/`.
5. Summarize only reviewed results back to GitHub.
6. Prevent context loss when local Codex/OpenClaw/Gemini/other LLMs independently modify the repo.

## GitHub
- Manager issue: #11
- Project: `@sunggyu-kim's 7iter project`

## Important correction
There are no separate manager1~4 roles. The previous split-manager structure was removed as incorrect.
