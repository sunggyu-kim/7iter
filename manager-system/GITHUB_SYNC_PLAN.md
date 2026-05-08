# GitHub Sync Plan

## Issue mapping
- #1 → Item 1
- #5 → Item 1-1
- #2 → Item 2
- #3 → Item 3
- #6 → Item 3-1
- #4 → Item 4
- #11 → Overall Manager

## Labels
- `manager` — controlled by the overall manager
- `async-managed` — requires context/history workflow
- `external-llm-log` — external/local LLM updates must be logged
- `fork` — forked item/project
- `item:1-1`, `item:3-1` — fork item labels

## Project rule
Every active item/fork issue and the Overall Manager issue must be present in the GitHub Project. Obsolete manager1~4 issues are retired.

## Comment template
Use `manager-system/templates/github-comment.md` for distilled manager sync comments.
