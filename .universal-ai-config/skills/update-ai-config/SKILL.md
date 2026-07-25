---
name: update-ai-config
description: Create, update, or manage AI configuration templates. Analyzes what the user needs and delegates to the appropriate template-specific skill.
---

# Manage AI Config Templates

**IMPORTANT:** This project uses universal-ai-config (`uac`). All AI configuration lives in the `<%= config.templatesDir %>/` directory as universal templates. NEVER edit generated target-specific files (e.g. `.claude/`, `.github/copilot-instructions.md`, `.cursor/`, `.codex/`, `AGENTS.md` at root, `.agents/skills/`) directly — those are overwritten on every `uac generate` run. Always modify the source templates in `<%= config.templatesDir %>/`.

When the user wants to add or change AI configuration for this project, follow these steps:

## 1. Understand the Request

Read the template guide at `<%= instructionPath('uac-template-guide') %>` to understand the available template types and when to use each.

## 2. Determine the Template Type

Based on the user's request, decide which type of template to work with:

- **Persistent context, rules, or guidelines** → Instruction template
- **Repeatable task, workflow, or slash command** → Skill template
- **Specialized AI persona with restricted tools** → Agent template
- **Automatic lifecycle automation (on events)** → Hook template
- **MCP server configuration** → MCP template

Examples:

- "Add a rule about error handling" → Instruction
- "Create a deploy workflow" → Skill
- "Set up a code reviewer" → Agent
- "Run linting after file edits" → Hook
- "Add an MCP server for GitHub" → MCP

If the intent is ambiguous, ask the user to clarify before proceeding.

## 3. Delegate

Read the detailed guide for the chosen template type and follow its instructions:

- **Instructions** → `<%= skillPath('update-instruction') %>`
- **Skills** → `<%= skillPath('update-skill') %>`
- **Agents** → `<%= skillPath('update-agent') %>`
- **Hooks** → `<%= skillPath('update-hook') %>`
- **MCP** → `<%= skillPath('update-mcp') %>`

These skills primarily create or modify files inside `<%= config.templatesDir %>/`. They may also modify files in directories listed under `additionalTemplateDirs` in the config — but only with explicit user confirmation, since those are shared templates that may affect other projects. Never edit generated output files in `.claude/`, `.cursor/`, `.github/`, `.codex/`, `AGENTS.md` at root, `.agents/skills/`, or similar target-specific directories — those are regenerated from templates and any direct changes will be lost.

## Additional Template Directories

This project may have additional template directories configured via `additionalTemplateDirs`. To find them, search the project root for **all** config files matching `universal-ai-config.*` (e.g. `universal-ai-config.config.ts`, `universal-ai-config.overrides.config.ts`, and any other variants) and read the `additionalTemplateDirs` field from each. If the user asks to update a template that doesn't exist in the main templates directory, or explicitly refers to shared/global/external templates:

1. Read all `universal-ai-config.*` config files in the project root to find `additionalTemplateDirs` paths
2. Search those directories for the relevant template
3. **IMPORTANT:** Before editing any file outside the main `<%= config.templatesDir %>/` directory, ask the user for explicit confirmation — these are shared templates that may affect other projects

## Writing Style

Every token in a template costs model attention — ~60% of instruction tokens are typically removable without degrading output quality. When writing or editing any template, apply these rules:

- **Use imperative sentences.** "Use strict mode" not "You should try to ensure that strict mode is used."
- **Cut filler phrases.** Drop "please note that", "it is important to", "keep in mind that", "remember to always" — just state the rule.
- **Remove hedging on directives.** "Be accurate" not "You should try to ensure responses are accurate."
- **Deduplicate.** If two rules express the same constraint in different words, keep only the most specific version. "Be professional" + "Maintain professional tone" + "Always respond professionally" → "Maintain professional tone."
- **Drop self-referential framing.** "The following rules govern your behavior:" adds nothing — just list the rules.
- **Strip unnecessary articles in imperatives.** "Write response" not "Write the response."
- **Flatten verbose conditionals.** "If user asks X, check Y, and if Y then Z" → "X + Y → Z"
- **Minimize examples.** 1–2 examples covering distinct cases beat 5 illustrating the same pattern. If a rule is clear without examples, omit them — but note that cutting examples carries the most risk since few-shot examples significantly reduce prompt sensitivity.

## After Changes

Run `uac generate` to regenerate target-specific config files and verify the output.
