---
description: Test conventions for speckle-fme
alwaysApply: true
---

# Testing conventions

## Structure

- `tests/test_geometry.py` — unit tests for SGEO encode/decode and FME geometry conversion. No server, no FME runtime required.
- `tests/test_bundle_schema.py` — unit tests for parquet schema validation and EAV queries using synthetic data.
- `tests/test_bundle_publish.py` — integration tests: full publish against `next.speckle.dev`. Requires `SPECKLE_TOKEN`, `SPECKLE_TEST_PROJECT_ID`, `SPECKLE_TEST_MODEL_ID`.
- `tests/test_bundle_receive.py` — integration tests: download + reconstruct features from a real bundle.

## Running tests

```bash
uv run pytest tests/test_geometry.py tests/test_bundle_schema.py -v   # unit only
uv run pytest tests/ -v                                                 # all (needs env vars)
uv run pytest -x -q                                                     # fail-fast, quiet
```

## Fixtures (conftest.py)

- `speckle_client` — session-scoped; authenticates from env vars.
- `test_model` — function-scoped; creates a timestamped model, yields it, deletes it on teardown. Never reuse between tests.
- `bundle_dir` — function-scoped; `tempfile.TemporaryDirectory` for parquet output. Cleaned up automatically.

## Rules

- Unit tests must run with no network access and no `fmeobjects` available.
- Integration tests must clean up after themselves (delete created versions/models).
- Never share state between tests via module-level variables.
- Parametrize geometry round-trip tests over all supported SGEO types (Mesh, Line, Polyline, Arc, Circle, Point).
- Mark integration tests with `@pytest.mark.integration` so they can be skipped in CI unit-only runs.
