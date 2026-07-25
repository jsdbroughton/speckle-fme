---
name: update-hook
description: Create, update, or manage universal-ai-config hook templates. Handles finding existing hooks, deciding whether to create or modify, and writing the template.
userInvocable: false
---

# Manage Hook Templates

Hooks are lifecycle automation that triggers on specific events during AI sessions. They use JSON format (not markdown).

## Finding Existing Hooks

List files in `<%= hookTemplatePath() %>/` to discover existing hook templates (`.json` files). Read them to understand what events are already handled.

**Note:** Hooks from multiple files are merged by event name during generation. You can organize hooks by concern (e.g. `linting.json`, `security.json`).

## Deciding What to Do

- **Create new file**: for an entirely new concern or automation area
- **Update existing file**: modify handlers or add events to an existing hook file
- **Merge strategy**: since hooks merge by event, you can split hooks across files for better organization without conflicts
- **Delete**: remove a hook file when the automation is no longer needed

## Creating a New Hook

1. Create a `.json` file in `<%= hookTemplatePath() %>/` with a descriptive name (e.g. `linting.json`)
2. Use the standard hook JSON structure

### JSON Structure

```json
{
  "hooks": {
    "eventName": [
      {
        "command": "path/to/script.sh",
        "matcher": "ToolName",
        "timeout": 30,
        "description": "What this hook does"
      }
    ]
  }
}
```

### Events, Handler Fields, and Per-Target Overrides

See the **Hooks** section in `<%= instructionPath('uac-template-guide') %>` for the complete reference: all universal event names with the per-target mapping table (Claude/Copilot/Cursor/Codex columns), handler fields (`command`, `matcher`, `timeout`, `description`, `statusMessage`), and per-target override syntax.

Use camelCase event names (e.g. `sessionStart`, `preToolUse`, `postToolUse`). The CLI maps them to each target's format and silently drops unsupported events.

### Codex notes

Codex supports a strict subset of 6 events (`sessionStart`, `userPromptSubmit`, `preToolUse`, `postToolUse`, `permissionRequest`, `stop`) — all other universal events drop silently for Codex. Codex only reliably supports `type: "command"` handlers; `http`, `mcp_tool`, `prompt`, and `agent` handler types are dropped with a warning. Codex `command` is a single shell string, so any `args` array is flattened with POSIX shell escaping when emitting for Codex.

### Example

```json
{
  "hooks": {
    "postToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "./scripts/format-file.sh",
        "timeout": 60,
        "description": "Auto-format files after edits"
      }
    ],
    "sessionStart": [
      {
        "command": "echo 'Session started at $(date)'",
        "description": "Log session start"
      }
    ]
  }
}
```
