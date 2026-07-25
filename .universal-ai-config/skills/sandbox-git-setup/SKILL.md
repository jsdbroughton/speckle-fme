---
name: sandbox-git-setup
description: Fix git sandbox issues at the start of any Cowork or Cursor background-agent session that involves git operations, file edits, or code changes. Fixes "dubious ownership" errors and sets correct expectations about GitHub push auth limitations.
---

# Sandbox Git Setup

Run these steps immediately at the start of any session involving git or file changes.

## Step 1: Fix ownership

```bash
git config --global --add safe.directory '*'
```

This fixes the "dubious ownership" error git throws when the sandbox user doesn't own the mounted volume. Safe to run even when not needed.

## Step 2: Verify git works

Run `git status` in the repo. If it still fails, note the error and continue — file changes still work, git staging/committing just won't.

## Step 3: Tell the user once, briefly

One sentence is enough: *"I've fixed the git ownership issue — I'll make the changes and give you the push command at the end."*

Don't apologise or over-explain. The user knows the sandbox has limits.

## Step 4: Do the work

Make file changes and commits as normal. Do NOT attempt `git push` — the sandbox has no access to SSH keys, macOS Keychain, or any credential store. This is a hard limit of the sandbox design.

## Step 5: End-of-session push block

When work is done, close with a ready-to-paste block:

```
Run to push:
git push
```

Expand if needed — e.g. `git push origin <branch>` or a note about setting upstream. Keep it minimal.
