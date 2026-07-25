---
name: update-skill
description: Create, update, or manage universal-ai-config skill templates. Handles finding existing skills, deciding whether to create or modify, and writing the template.
userInvocable: false
---

# Manage Skill Templates

Skills are reusable actions or workflows invocable as slash commands or auto-triggered by the AI.

## Finding Existing Skills

List directories in `<%= skillTemplatePath() %>/` to discover existing skills. Each skill is a directory containing a `SKILL.md` file. Read the `SKILL.md` frontmatter to understand what each skill does.

## Deciding What to Do

- **Create new**: when the task/workflow is distinct from existing skills
- **Update existing**: when a skill covers similar ground but needs changes — modify its `SKILL.md` or supporting files
- **Delete**: remove the entire skill directory when a skill is obsolete

## Creating a New Skill

1. Create a directory: `<%= skillTemplatePath() %>/{skill-name}/`
2. Create `SKILL.md` inside it with frontmatter and instructions
3. Optionally add supporting files (templates, scripts, examples) in the same directory

### Frontmatter Fields

See the **Skills** section in `<%= instructionPath('uac-template-guide') %>` for the complete field reference and per-target override syntax. Key fields: `name`, `description`, `disableAutoInvocation`, `userInvocable`, `allowedTools`, `model`, `hooks`, `version`, `author`, `codex`.

### Codex-specific UI metadata

For Codex-only UI metadata (display name, icons, brand color, invocation policy, MCP tool dependencies), use the nested `codex.*` frontmatter object. uac emits a sidecar `agents/openai.yaml` next to `SKILL.md` automatically when any `codex.*` field — or `disableAutoInvocation` — is set. See the **Codex skill metadata** sub-table in `<%= instructionPath('uac-template-guide') %>`.

### Supporting Files

Skills can include additional files in their directory. These are automatically copied to generated output during `uac generate`. `.md` extra files are rendered through EJS (with access to `target`, `config`, path helpers), while non-`.md` files are copied as-is.

```
my-skill/
├── SKILL.md          # Main instructions (required)
├── template.md       # Template for the AI to fill in (EJS rendered)
├── examples/
│   └── sample.md     # Example output (EJS rendered)
└── scripts/
    └── helper.sh     # Script the AI can execute (copied raw)
```

Reference supporting files from `SKILL.md` so the AI knows they exist.

### Example

```markdown
---
name: create-component
description: Scaffold a new React component with tests and styles
argumentHint: "[component-name]"
---

Create a new React component named $ARGUMENTS:

1. Create the component file in src/components/
2. Add unit tests
3. Add a Storybook story
4. Export from the components index
```
