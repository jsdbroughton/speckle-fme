# Developer Setup — Speckle Connector for FME

This guide covers setting up a fresh development environment on macOS for the Speckle FME connector. The connector targets FME ≥2026.1 and Speckle Next (`next.speckle.dev`).

## Prerequisites

- FME 2026.x installed with a **developer licence** (required for Pluginbuilder/Python format access)
- Git
- [uv](https://docs.astral.sh/uv/) (`brew install uv`)

---

## 1. FME paths (macOS)

On macOS, FME installs as `.app` bundles in `/Applications/FME <version>/`. The actual engine lives in `/Library/FME/<version>/`.

Add the FME CLI and its Python runtime to your PATH:

```bash
echo 'export PATH="/Library/FME/2026.2/bin:/Library/FME/2026.2/fmepython314/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

> **Version note:** Replace `2026.2` with your installed version. Check `ls /Library/FME/` if unsure.

Verify:

```bash
fme python -c "import sys; print(sys.version)"
# Expected: 3.14.x (Clang ...)
```

### Important: `fme python` vs bare `python3`

`fme python` is a wrapper that adds FME-specific entries to `sys.path`. It is **not** the same as calling `/Library/FME/2026.2/fmepython314/bin/python3` directly — the latter lacks FME's plugin paths. Always use `fme python` for anything FME-related.

Packages installed via `fme python -m pip install` land in:
```
~/Library/Application Support/FME/Plugins/Python/python314/
```
This directory is already on FME's `sys.path` at runtime.

---

## 2. Install Python dependencies into FME's runtime

```bash
# specklepy must come from GitHub main — the PyPI release lacks specklepy.bundle
fme python -m pip install --upgrade \
  "specklepy[bundle] @ git+https://github.com/specklesystems/specklepy.git@main"
```

> **Why not PyPI?** `specklepy.bundle` (the parquet pipeline) is in the `main` branch but not yet in a PyPI release. Install from GitHub until a release ships that includes it.

Verify the full dependency chain:

```bash
fme python -c "
import pyarrow; print('pyarrow', pyarrow.__version__)
import duckdb; print('duckdb', duckdb.__version__)
from specklepy.bundle.pipeline import ObjectsArtifactPipeline; print('ObjectsArtifactPipeline OK')
from specklepy.bundle.upload import ArtifactPipeline; print('ArtifactPipeline OK')
from specklepy.bundle import sgeo; print('sgeo OK, encode:', hasattr(sgeo, 'encode'))
from specklepy.bundle.spec import Rel; print('Rel OK')
"
```

Expected output (versions may differ):
```
pyarrow 25.0.0
duckdb 1.5.5
ObjectsArtifactPipeline OK
ArtifactPipeline OK
sgeo OK, encode: True
Rel OK
```

> **Known gap:** `sgeo.decode` is not yet on `main` — it exists on a branch (implemented for Blender receive, WIP). Wait for it to land before implementing Stage 4. This does not block Stage 1 (Publish).

---

## 3. Install fme-packager

```bash
fme python -m pip install fme-packager
```

---

## 4. Clone and set up the repo

```bash
git clone https://github.com/jsdbroughton/speckle-fme
cd speckle-fme

# fmeobjects stub typings for IDE autocomplete (FME's .so has no docstrings)
git submodule update --init --recursive

# Project Python env for unit tests (separate from FME's runtime)
uv sync
```

---

## 5. IDE configuration (VS Code)

Add to `.vscode/settings.json`:

```json
{
  "python.analysis.stubPath": "typings",
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"
}
```

---

## 6. Environment variables

Create a `.env` at the repo root (not committed):

```bash
SPECKLE_SERVER_URL=https://next.speckle.dev
SPECKLE_TOKEN=<your PAT from next.speckle.dev account settings>
SPECKLE_TEST_PROJECT_ID=<a project you own on next.speckle.dev>
SPECKLE_TEST_MODEL_ID=<a model in that project>
```

---

## 7. Dev loop — symlink approach (fast iteration)

Symlink source into FME's plugin directory so edits are picked up on restart without a build step:

```bash
FME_PLUGINS="$HOME/Library/Application Support/FME/Plugins"
mkdir -p "$FME_PLUGINS/python"

# Metafile — FME reads this at startup to register the format in the gallery
cp formats/SPECKLE.fmf "$FME_PLUGINS/"

# Python source — symlinked so edits are live without re-copying
ln -sf "$(pwd)/python/speckle_reader_writer.py" "$FME_PLUGINS/python/"
ln -sf "$(pwd)/speckle_fme_core" "$FME_PLUGINS/python/"
```

After any Python change: **restart FME Workbench**. FME loads plugins once at startup.
After any `.fmf` change: re-copy the file and restart.

---

## 8. Run tests

```bash
# Unit tests — no network, no FME runtime required
uv run pytest tests/test_geometry.py tests/test_bundle_schema.py -v

# Integration tests — requires .env with valid credentials
uv run pytest tests/test_bundle_publish.py tests/test_bundle_receive.py -v
```

---

## Confirmed version matrix (FME 2026.2, macOS arm64)

| Component | Version | Notes |
|---|---|---|
| FME | 2026.2 | Developer licence required |
| FME Python runtime | 3.14.5 | `/Library/FME/2026.2/fmepython314/` |
| pyarrow | 25.0.0 | `cp314-macosx_12_0_arm64` wheel — no source build needed |
| duckdb | 1.5.5 | `cp314-macosx_11_0_arm64` wheel |
| specklepy | 2026.6.1.dev1 | Install from GitHub `main`, not PyPI |
| sgeo.encode | ✅ | Available in `specklepy.bundle.sgeo` |
| sgeo.decode | ⏳ | WIP on a branch (Blender receive), not yet on `main` — wait for merge |
