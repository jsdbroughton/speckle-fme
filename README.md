# Speckle Connector for FME

A native FME Format Reader/Writer for [Speckle Next](https://next.speckle.dev) — reads and writes Speckle projects as a first-class FME format using the Speckle Next data plane (parquet bundle + SGEO geometry).

> **Status:** Stage 0 — toolchain validation. November 2026 milestone.

## Overview

This connector is built as an [FME Packages SDK](https://docs.safe.com/fme/html/fmepython/) plugin (Python Pluginbuilder API) and distributed as an `.fpkg` via FME Hub. It targets **Speckle Next** (`next.speckle.dev`) exclusively and the three-artefact parquet bundle format — not the legacy v3 object graph.

Key design choices:

- **Format Reader/Writer, not a transformer pair** — gallery presence, native parameter dialogs, Web Connections support
- **Bundle pipeline** (`specklepy[bundle]`) for geometry — does not use `operations.send()` / `operations.receive()`
- **DuckDB + EAV parquet** for attribute queries and schema discovery
- **`speckle_fme_core`** is a standalone, FME-free module that can be unit tested independently

## Requirements

- FME ≥ 2026.1
- Python ≥ 3.10 (matching FME's embedded runtime — see open contract C-2.6)
- `specklepy[bundle]` — `pyarrow>=17`, `duckdb>=1.1`
- Speckle Next account and Personal Access Token

## Repository Structure

```
formats/              FME metafile (.fmf) — format registration and GUI dialogs
python/               FME plugin entry point (FME_createReader / FME_createWriter)
speckle_fme_core/     Core module — auth, bundle pipeline, geometry, schema
  auth.py             SpeckleClient factory and token resolution
  api.py              Thin wrappers around specklepy client resources
  bundle_publish.py   FME features → ObjectsArtifactPipeline → upload
  bundle_receive.py   v2 artifacts → parquet → FME features
  schema.py           readSchema() helpers (EAV paths, container names)
  geometry/
    fme_to_speckle.py FMEGeometry → Speckle geometry → sgeo.encode()
    speckle_to_fme.py SGEO blobs → FMEGeometry
  reader.py           FMEReader Pluginbuilder class
  writer.py           FMEWriter Pluginbuilder class
tests/
  conftest.py         pytest fixtures (client, test model lifecycle)
  test_geometry.py    SGEO encode/decode round-trips (no FME, no server)
  test_bundle_publish.py  End-to-end Publish (integration, requires server)
  test_bundle_receive.py  End-to-end Receive (integration, requires server)
typings/fmeobjects/   fmeobjects stub typings for IDE type-checking
package.yml           fme-packager manifest
pyproject.toml        Python project / dependency definition (uv)
```

## Development Setup

```bash
git clone https://github.com/jsdbroughton/speckle-fme
cd speckle-fme
uv venv && uv sync
cp .env.example .env   # fill in SPECKLE_TOKEN and test project IDs
```

### Unit tests (no FME, no server)

```bash
uv run pytest tests/test_basic_speckle_installation_check.py tests/test_geometry.py -v
```

### Integration tests (requires Speckle Next credentials in `.env`)

```bash
uv run pytest tests/test_bundle_publish.py tests/test_bundle_receive.py -v
```

### Loading in FME Workbench (dev loop)

```bash
# Build and install the .fpkg
fme-packager build
fme package install speckle-0.1.0.fpkg

# Or symlink for fast iteration (macOS)
FME_FORMATS_DIR="$HOME/Library/Application Support/FME/Plugins"
cp formats/SPECKLE.fmf "$FME_FORMATS_DIR"
ln -s "$(pwd)/python/speckle_reader_writer.py" "$FME_FORMATS_DIR/python/"
ln -s "$(pwd)/speckle_fme_core" "$FME_FORMATS_DIR/python/"
```

## Build Sequence

| Stage | Focus | Status |
|-------|-------|--------|
| 0 | Toolchain validation — pyarrow in FME runtime (C-2.6), `fme-packager` hello-world, auth against `next.speckle.dev` | **Current** |
| 1 | MeFi Publish — `ObjectsArtifactPipeline` → `ArtifactPipeline.upload_dir()` | Pending |
| 2 | FMEWriter + FMEReader skeleton, FME feature → Speckle Mesh conversion | Pending |
| 3 | HiFi Publish — expanded geometry types, materials, levels, collection hierarchy | Pending |
| 4 | Receive — v2 artifacts download, SGEO decode, EAV → FME attributes | Pending |
| 5 | Round-trip tests, large-model performance, error handling | Pending |
| 6 | `.fpkg` packaging, FME Hub publish | Pending |
| 7 | Launch | November 2026 |

## Open Contracts

| ID | What's uncertain |
|----|-----------------|
| C-2.6 | `pyarrow>=17` in FME's embedded Python runtime — test with `fme python -c "import pyarrow; print(pyarrow.__version__)"` |
| C-2.3 | `DataObject.properties` shape consistency across connector versions |
| C-3.5 | GraphQL fields exposing bundle status / artifact availability for a version |
| C-7.1 | Does `complete` endpoint work for new unregistered connector types? |

## Legacy

The previous v2 Custom Transformer-based connector (Speckle 2.0, PythonCaller approach) is preserved on the [`legacy/v2-custom-transformers`](../../tree/legacy/v2-custom-transformers) branch for reference only. That codebase is not maintained.

## Issues

Tracked at [github.com/jsdbroughton/speckle-fme/issues](https://github.com/jsdbroughton/speckle-fme/issues).
