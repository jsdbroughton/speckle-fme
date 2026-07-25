---
description: Project identity, toolchain, and core rules for speckle-fme
alwaysApply: true
---

# Speckle Connector for FME

An **experimental Speckle Next v0** — a native FME Format Reader/Writer plugin (not a Custom Transformer), built exclusively against the Speckle Next data plane (parquet bundle + SGEO). Target: November 2026 as a validation milestone.

## Toolchain

- **Python ≥3.10** — match FME's embedded runtime version (confirm C-2.6 before committing)
- **uv** — dependency management (`uv sync`, `uv run`, `uv add`). Never use `pip install` directly.
- **pytest** — all tests. `uv run pytest` to run.
- **fme-packager** — builds `.fpkg` distribution artifact
- **specklepy[bundle]** — the only Speckle SDK path used. `operations.send()`/`receive()` are NOT used.

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

## Local repo path

`/Users/jonathonbroughton/Documents/repos/Jonathon/speckle-fme`

## Issue tracker

GitHub Issues at `github.com/jsdbroughton/speckle-fme/issues`. Not Linear, not Jira.

## File naming

- **snake_case** for Python source files and modules
- **UPPER_CASE** for FME metafile (`SPECKLE.fmf`)
- Keep files under ~300 lines; split if longer
