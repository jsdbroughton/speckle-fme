---
name: ai-config-compress
description: >
  Compress LLM instruction sets, system prompts, rules, and guidelines to reduce
  token count while preserving behavioral intent. Use this skill whenever the user
  wants to shorten, truncate, optimize, or compress prompts, system instructions,
  CLAUDE.md files, custom instructions, rules, guidelines, or any instruction set
  meant for an LLM. Also trigger when users mention "too many tokens," "prompt is
  too long," "reduce prompt size," or ask to make instructions more concise.
---

# Prompt Compress

Compress LLM instructions with calibrated risk. Research shows ~60% of instruction
tokens are removable without degrading output quality — and compression often
_improves_ performance by concentrating model attention.

## Core Principles

1. **Instructions are the most sensitive prompt component.** Apply maximum
   compression to examples and context, moderate compression to structure,
   minimal compression to core behavioral rules.
2. **Semantic equivalence ≠ behavioral equivalence.** Two phrasings that mean the
   same thing to a human can produce different model behavior. Every change
   beyond mechanical cleanup carries nonzero risk.
3. **Compress in tiers.** Apply safest changes first, present riskier changes as
   suggestions. The user decides how far to go.

## Workflow

### 1. Analyze

Before compressing anything, analyze the input:

- Count tokens (estimate: words × 1.3 for English)
- Identify sections by function: safety, formatting, tone, behavior, examples,
  context, metadata
- Detect duplicates: rules that express the same constraint in different words
- Flag filler: politeness markers, hedging, verbose connectives
- Note structural issues: scattered related rules, inconsistent formatting
- Identify examples and assess whether they're redundant with stated rules

Present a brief analysis summary with estimated savings per tier.

### 2. Compress in Tiers

Apply changes tier by tier. For each tier, show a diff and token savings.

#### Tier 1 — Mechanical (auto-apply, safe)

These changes preserve exact meaning. Apply all of them:

- Fix typos and inconsistent punctuation
- Normalize whitespace (double spaces, trailing spaces, excessive blank lines)
- Apply word-level substitutions from `references/substitutions.md`
- Remove pure filler: "please note that," "it is important to," "keep in mind"
- Remove politeness in system prompts: "please," "kindly," "if you don't mind"
- Strip unnecessary articles in imperative instructions ("Write the response" → "Write response")
- Remove self-referential meta-commentary ("The following rules govern your behavior:" → just list the rules)

#### Tier 2 — Structural (recommend, low-medium risk)

These reorganize without changing meaning, but removal of "redundant" rules
may remove useful reinforcement:

- **Deduplicate**: Merge rules expressing the same constraint. Keep the most
  specific version. Example: "Be professional" + "Maintain professional tone" +
  "Always respond professionally" → "Maintain professional tone."
- **Group by function**: Collect scattered rules under section headers.
  Consolidating related rules eliminates repetitive framing ("When responding...",
  "In your responses...", "Your responses should...").
- **Flatten conditionals**: Convert nested if-else to flat patterns.
  "If user asks X, check Y, and if Y then Z" → "X + Y → Z; X + ¬Y → W"
- **Remove hedging on directives**: "You should try to ensure responses are
  accurate" → "Be accurate." Only where the hedge adds no real nuance.
- **Trim verbose examples**: If 5+ examples illustrate the same pattern, keep
  2-3 that cover distinct cases. Flag which ones you'd cut and why.

#### Tier 3 — Semantic (suggest only, medium-high risk)

These change wording while attempting to preserve intent. Present as suggestions
with explicit risk notes. Never auto-apply:

- **Telegraphic style**: Drop articles, pronouns, connectives from behavioral
  rules. "When the user asks you a question, you should provide a clear and
  concise answer" → "Answer questions clearly and concisely."
- **Principalize examples**: Replace remaining examples with a principle
  statement. "Example: 'Hello!' → 'Hi there!' / 'Hey' → 'Hello!'" →
  "Mirror greeting energy, match formality level."
- **Merge overlapping rules**: Combine rules that address related behaviors.
  Only where the merged version clearly covers both originals.
- **Remove examples entirely**: If the rule is clear without them. Flag as
  HIGH RISK — few-shot examples reduce prompt sensitivity by ~30%.
- **Reorder sections**: Move most critical rules to beginning and end of prompt
  (attention U-curve). Flag as MEDIUM RISK — reordering alone can cause
  significant behavioral shifts.

#### Tier 4 — Aggressive (flag only, high risk)

Only mention these as possibilities. Never draft them without explicit user request:

- Removing safety/guardrail instructions
- Changing role/persona framing
- Switching prompting strategies (zero-shot ↔ chain-of-thought)
- SPR-style compression (reducing to associative priming cues)
- Removing entire sections deemed low-value

### 3. Present Results

Output a compression report with this structure:

```
## Compression Report

**Original**: ~{n} tokens ({word_count} words)

### Tier 1 — Mechanical [{savings}% reduction]
{compressed text with changes}

### Tier 2 — Structural [{cumulative savings}% reduction]
{compressed text with Tier 1+2 applied}
Changes made:
- {change 1}: {rationale}
- {change 2}: {rationale}

### Tier 3 — Suggestions [{potential additional savings}%]
- [ ] {suggestion 1} — saves ~{n} tokens — RISK: {level} — {why risky}
- [ ] {suggestion 2} — saves ~{n} tokens — RISK: {level} — {why risky}

### Tier 4 — Aggressive options [{potential savings}%]
- {option}: {what it would save} — {what might break}

**Summary**: Tier 1+2 achieves ~{n}% reduction ({old} → {new} tokens).
Tier 3 suggestions could reach ~{n}% total if accepted.
```

### 4. Deliver

- If the user wants a specific tier applied, produce the final compressed text
  with all changes through that tier
- If they want to cherry-pick Tier 3 suggestions, apply only selected ones
- Always provide the final compressed version as a clean, copy-pasteable block

## Important Caveats to Communicate

- Compression effectiveness depends on the target model. What works for Claude
  may not work identically for GPT or Gemini.
- Larger/newer models tolerate more compression. If targeting smaller models,
  be more conservative.
- The only real validation is testing compressed prompts against actual tasks.
  This skill optimizes for likely preservation, not guaranteed preservation.
- Examples are disproportionately valuable. Cutting examples saves the most tokens
  but carries the most risk.

## Reference Files

- Read `references/substitutions.md` for the mechanical substitution dictionary
  used in Tier 1. Load this before applying Tier 1 changes.
- Read `references/examples.md` for before/after compression examples across
  different instruction types. Consult when unsure about a compression decision.
