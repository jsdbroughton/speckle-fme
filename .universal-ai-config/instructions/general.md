---
description: Project identity, toolchain, and core rules for speckle-fme
alwaysApply: true
---

# Speckle Connector for FME

An **experimental Speckle Next v0** — a native FME Format Reader/Writer plugin (not a Custom Transformer), built exclusively against the Speckle Next data plane (parquet bundle + SGEO). Target: November 2026 as a validation milestone.

## Toolchain

- **Python 3.14.5** — FME 2026.2 embeds Python 3.14.5 at `/Library/FME/2026.2/fmepython314/`. C-2.6 is confirmed closed: pyarrow 25.0.0 ships a `cp314` wheel for macOS arm64, no source build needed.
- **`fme python`** — always use this wrapper (not bare `python3`) for FME runtime installs. Packages land in `~/Library/Application Support/FME/Plugins/Python/python314/`.
- **uv** — dependency management for the project venv (`uv sync`, `uv run`, `uv add`). Never use `pip install` directly in the project venv.
- **pytest** — all tests. `uv run pytest` to run.
- **fme-packager** — builds `.fpkg` distribution artifact. Install via `fme python -m pip install fme-packager`.
- **specklepy[bundle]** — the only Speckle SDK path used. `operations.send()`/`receive()` are NOT used. **Must install from GitHub `main`** (`git+https://github.com/specklesystems/specklepy.git@main`) — the PyPI release does not include `specklepy.bundle`.
- **sgeo.decode WIP** — `specklepy.bundle.sgeo` has `encode()` but `decode()` is not yet on `main`. It exists on a branch (done for Blender receive). Wait for it to land on `main` before implementing the Stage 4 Receive path — do not port from the TypeScript reference or pull from the feature branch.

## Hard constraints

- **Speckle Next only.** No fallback to `operations.send()` or `operations.receive()`. If the server doesn't support v2 bundle endpoints, raise `SpeckleFMEError` with a clear message and stop.
- **Ingestion before conversion.** The server pre-allocates `versionId` at ingestion creation — this must happen before any parquet files are written.
- **One Speckle object → one FME feature.** Multi-part geometry goes into a single `FMEAggregate`. Never split a Speckle object across multiple features.
- **`applicationId` not `id` for object identity.** `id` changes on content change; `applicationId` is stable.
- **`close()` may be called more than once.** Guard with `self._closed`.
- **`open()` in data mode has empty `parameters`.** Always fetch config from `mappingFile`.

## Module layout

```
speckle_fme_core/   # standalone, testable without FME
python/             # FME_createReader / FME_createWriter entry point
formats/            # SPECKLE.fmf metafile
tests/              # pytest — unit + integration
typings/            # fmeobjects stubs (github.com/urbansurgery/fmeobjects)
```

## Issue tracker

GitHub Issues at `github.com/jsdbroughton/speckle-fme/issues`. Not Linear, not Jira.

## File naming

- **snake_case** for Python source files and modules
- **UPPER_CASE** for FME metafile (`SPECKLE.fmf`)
- Keep files under ~300 lines; split if longer
