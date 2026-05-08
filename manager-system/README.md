# 7iter Manager System

## Purpose
Repo-native project memory and control layer for Item 1~4 plus forked items such as Item 1-1 and Item 3-1.

## Manager Map
- manager1: Item 1, Item 1-1
- manager2: Item 2
- manager3: Item 3, Item 3-1
- manager4: Item 4

## Async Update Loop
Representative comment → manager queue → local async agent → reviewed artifact → item HISTORY/STATUS update → GitHub issue/project sync.

## GitHub Project Integration
GitHub Issues remain the public tracker. `manager-system/` preserves local context so Codex/OpenClaw/Gemini/Claude/OpenAI/Grok/Blender-style work can be merged without losing intent.
