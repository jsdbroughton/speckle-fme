# Speckle Connector for FME

A native FME Format Reader/Writer for [Speckle Next](https://next.speckle.dev) — reads and writes Speckle projects as a first-class FME format using the Speckle Next data plane (parquet bundle + SGEO geometry).

> **Status:** Stage 1 — MeFi Publish. November 2026 milestone.

## Overview

This connector is built as an [FME Packages SDK](https://docs.safe.com/fme/html/fmepython/) plugin (Python Pluginbuilder API) and distributed as an `.fpkg` via FME Hub. It targets **Speckle Next** (`next.speckle.dev`) exclusively and the three-artefact parquet bundle format — not the legacy v3 object graph.

Key design choices:

- **Format Reader/Writer, not a transformer pair** — gallery presence, native parameter dialogs, Web Connections support
- **Bundle pipeline** (`specklepy[bundle]`) for geometry — does not use `operations.send()` / `operations.receive()`
- **DuckDB + EAV parquet** for attribute queries and schema discovery
- **`speckle_fme_core`** is a standalone, FME-free module that can be unit tested independently

## Requirements

- FME ≥ 2026.1 with a developer licence
- FME 2026.2 embeds Python 3.14.5 — see [docs/installation.md](docs/installation.md) for PATH setup
- `specklepy[bundle]` installed from GitHub `main` (not PyPI) — `pyarrow>=17`, `duckdb>=1.1`
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
docs/installation.md  Full developer setup guide
package.yml           fme-packager manifest
pyproject.toml        Python project / dependency definition (uv)
```

## Development Setup

See **[docs/installation.md](docs/installation.md)** for the full setup guide, including FME PATH configuration and the confirmed version matrix.

```bash
git clone https://github.com/jsdbroughton/speckle-fme
cd speckle-fme
uv venv && uv sync
cp .env.example .env   # fill in SPECKLE_TOKEN and test project IDs
```

### Unit tests (no FME, no server)

```bash
uv run pytest tests/test_geometry.py tests/test_bundle_schema.py -v
```

### Integration tests (requires Speckle Next credentials in `.env`)

```bash
uv run pytest tests/test_bundle_publish.py tests/test_bundle_receive.py -v
```

### Loading in FME Workbench (dev loop)

```bash
# Symlink for fast iteration (macOS) — restart Workbench after any change
FME_FORMATS_DIR="$HOME/Library/Application Support/FME/Plugins"
cp formats/SPECKLE.fmf "$FME_FORMATS_DIR"
ln -sf "$(pwd)/python/speckle_reader_writer.py" "$FME_FORMATS_DIR/python/"
ln -sf "$(pwd)/speckle_fme_core" "$FME_FORMATS_DIR/python/"

# Or build and install the .fpkg
fme-packager build
fme package install speckle-0.1.0.fpkg
```

## Build Sequence

| Stage | Focus | Status |
|-------|-------|--------|
| 0 | Toolchain validation — pyarrow in FME runtime, `fme-packager` hello-world, auth against `next.speckle.dev` | ✅ Complete |
| 1 | MeFi Publish — `ObjectsArtifactPipeline` → `ArtifactPipeline.upload_dir()` | **Current** |
| 2 | FMEWriter + FMEReader skeleton, FME feature → Speckle Mesh conversion | Pending |
| 3 | HiFi Publish — expanded geometry types, materials, levels, collection hierarchy | Pending |
| 4 | Receive — v2 artifacts download, SGEO decode, EAV → FME attributes | Pending |
| 5 | Round-trip tests, large-model performance, error handling | Pending |
| 6 | `.fpkg` packaging, FME Hub publish | Pending |
| 7 | Launch | November 2026 |

## Open Contracts

| ID | What's uncertain | Status |
|----|-----------------|--------|
| C-2.6 | `pyarrow>=17` in FME's embedded Python runtime | ✅ Closed — pyarrow 25.0.0, Python 3.14.5, `cp314` wheel confirmed |
| C-2.3 | `DataObject.properties` shape consistency across connector versions | ❓ Open |
| C-3.5 | GraphQL fields exposing bundle status / artifact availability for a version | ❓ Open |
| C-7.1 | Does `complete` endpoint work for new unregistered connector types? | ❓ Open |
| sgeo.decode | `specklepy.bundle.sgeo.decode()` not yet on `main` (WIP, exists on branch) | ⏳ Waiting — blocks Stage 4 only |

## Legacy

The previous v2 Custom Transformer-based connector (Speckle 2.0, PythonCaller approach) is preserved on the [`legacy/v2-custom-transformers`](../../tree/legacy/v2-custom-transformers) branch for reference only. That codebase is not maintained.

## Issues

Tracked at [github.com/jsdbroughton/speckle-fme/issues](https://github.com/jsdbroughton/speckle-fme/issues).
