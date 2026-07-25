---
name: sandbox-git-setup
description: Fix git sandbox issues at the start of any Cowork or Cursor background-agent session that involves git operations, file edits, or code changes. Fixes "dubious ownership" errors and configures GitHub push auth from a credential file stored safely inside .git/.
---

# Sandbox Git Setup

Run these steps immediately at the start of any session involving git or file changes.

## Step 1: Fix ownership

```bash
git config --global --add safe.directory '*'
```

## Step 2: Configure push auth

Check if `.git/sandbox-credentials` exists in the repo:

```bash
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
ls "$REPO_ROOT/.git/sandbox-credentials" 2>/dev/null && echo "found" || echo "missing"
```

**If found** — configure the credential store and verify:

```bash
git config --global credential.helper "store --file $REPO_ROOT/.git/sandbox-credentials"
git -C "$REPO_ROOT" push --dry-run 2>&1
```

If the dry-run succeeds, push will work normally. Say nothing to the user — just proceed.

**If missing** — tell the user once, briefly:

> "To enable push from the sandbox, create `.git/sandbox-credentials` in the repo (inside `.git/` so it's never committed):
> ```
> https://oauth2:YOUR_PAT@github.com
> ```
> Generate a PAT at github.com/settings/tokens with `repo` scope. Until then I'll make the changes and give you the push command at the end."

The file lives inside `.git/` — git never commits its own internals, so no gitignore entry is needed and there's no risk of accidental exposure.

## Step 3: Do the work

Make file changes and commits normally. If credentials are configured, `git push` works directly.

## Step 4: End-of-session (if no credentials)

When credentials are missing and push wasn't possible, close with:

```
Run to push:
git push
```
