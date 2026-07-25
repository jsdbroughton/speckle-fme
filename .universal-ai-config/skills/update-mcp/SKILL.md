---
name: update-mcp
description: Create, update, or manage universal-ai-config MCP server templates. Handles finding existing configs, deciding whether to create or modify, and writing the template.
userInvocable: false
---

# Manage MCP Server Templates

MCP (Model Context Protocol) server configurations define external tool servers available to AI tools. They use JSON format (not markdown), similar to hooks.

## Finding Existing MCP Configs

List files in `<%= mcpTemplatePath() %>/` to discover existing MCP templates (`.json` files). Read them to understand what servers are already configured.

**Note:** Servers from multiple files are merged by server name during generation (last-wins for duplicates). You can organize servers by concern (e.g. `github.json`, `databases.json`).

## Deciding What to Do

- **Create new file**: for an entirely new server or group of related servers
- **Update existing file**: modify server config, add servers to an existing file
- **Merge strategy**: since servers merge by name, you can split them across files for better organization
- **Delete**: remove an MCP config file when the server is no longer needed

## Creating a New MCP Config

1. Create a `.json` file in `<%= mcpTemplatePath() %>/` with a descriptive name (e.g. `github.json`)
2. Use the standard MCP JSON structure

### JSON Structure

```json
{
  "mcpServers": {
    "server-name": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@some/mcp-server"],
      "env": {
        "API_KEY": "${API_KEY}"
      }
    }
  }
}
```

### Server Fields

See the **MCP Servers → Server Fields** section in `<%= instructionPath('uac-template-guide') %>` for the complete reference, including all 13 Codex-specific fields (`cwd`, `envVars`, `enabledTools`, `disabledTools`, `bearerTokenEnvVar`, `envHttpHeaders`, `startupTimeoutSec`, `startupTimeoutMs`, `toolTimeoutSec`, `enabled`, `required`, `oauthResource`, `scopes`, `experimentalEnvironment`).

Key cross-target fields:

| Field     | Type                     | Description                                                           |
| --------- | ------------------------ | --------------------------------------------------------------------- |
| `command` | `string`                 | Command to launch the server (stdio transport)                        |
| `args`    | `string[]`               | Arguments for the command                                             |
| `env`     | `Record<string, string>` | Environment variables                                                 |
| `url`     | `string`                 | Server URL (HTTP transport)                                           |
| `headers` | `Record<string, string>` | HTTP headers. **Codex:** renames to `http_headers`                    |
| `type`    | `string`                 | Transport type. **Codex:** dropped — inferred from `command` vs `url` |

A server must have either `command` (stdio) or `url` (HTTP). If neither is present after per-target override resolution, the server is dropped for that target.

### Codex notes

- Codex output emits **TOML** (`.codex/config.toml`) merged into the `[mcp_servers.*]` table. Other top-level keys in `config.toml` (`[profiles.*]`, `[model_providers.*]`, `[permissions.*]`, `personality`, etc.) are preserved across regenerates — uac only owns `[mcp_servers.*]`.
- Auth model differs: Codex uses `bearerTokenEnvVar` + `oauthResource` + `scopes` instead of Claude's `oauth` object or Cursor's `auth` object. Claude/Cursor auth fields are dropped with a warning when emitting for Codex; use per-target overrides for Codex-specific auth.
- Per-server tool restriction lives at the MCP server level via `enabledTools` (allowlist) and `disabledTools` (denylist) — agent-level `tools` fields are not applicable for Codex.

### Variable Interpolation

Use `{{variableName}}` syntax to reference variables from the config file. Variables support **typed resolution**: when the entire JSON value is `"{{varName}}"`, it resolves to the raw typed value (array, object, number, boolean). When embedded in other text, it does string interpolation.

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": "{{playwrightArgs}}",
      "env": {
        "API_HOST": "{{apiHost}}"
      }
    }
  }
}
```

Variables are defined in `universal-ai-config.config.ts`:

```typescript
export default defineConfig({
  variables: {
    playwrightArgs: ["-y", "@playwright/mcp@latest"],
    apiHost: "api.example.com",
  },
});
```

For environment-specific values, use `universal-ai-config.overrides.ts` (gitignored):

```typescript
export default defineConfig({
  variables: {
    playwrightArgs: [
      "-y",
      "@playwright/mcp@latest",
      "--headless",
      "--executable-path",
      "/usr/bin/chromium",
    ],
  },
});
```

**Important:** `{{varName}}` is for uac config variables. Use `${ENV_VAR}` for runtime environment variable references that should be passed through to the generated output unchanged.

### Per-Target Overrides

Any server field can have per-target values using the same override syntax as hooks:

```json
{
  "mcpServers": {
    "my-server": {
      "command": {
        "default": "npx",
        "cursor": "node"
      },
      "args": {
        "default": ["-y", "@my/server"],
        "cursor": ["./mcp-server.js"]
      },
      "type": {
        "claude": "stdio",
        "copilot": "stdio"
      }
    }
  }
}
```

If `command` (and `url`) resolve to `undefined` for a target, the entire server is dropped for that target. This lets you define target-exclusive servers.

### Copilot Inputs

For Copilot, you can include an `inputs` array for interactive secret prompts:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${input:github-token}"
      }
    }
  },
  "inputs": [
    {
      "type": "promptString",
      "id": "github-token",
      "description": "GitHub Personal Access Token",
      "password": true
    }
  ]
}
```

The `inputs` array is only included in Copilot output — Claude and Cursor ignore it.

### Output Paths

Generated MCP files are placed at root-relative paths (not inside the target's output directory):

| Target  | Output Path        | Wrapper Key  |
| ------- | ------------------ | ------------ |
| Claude  | `.mcp.json`        | `mcpServers` |
| Copilot | `.vscode/mcp.json` | `servers`    |
| Cursor  | `.cursor/mcp.json` | `mcpServers` |

**Note:** Cursor omits the `type` field from generated output (it infers transport from the presence of `command` vs `url`).

### Example

```json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "postgres": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "{{dbConnectionString}}"]
    }
  }
}
```
