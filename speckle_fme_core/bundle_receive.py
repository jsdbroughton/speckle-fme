"""
Bundle Receive — download Speckle Next v2 artifacts → parquet → FME features.

Sequence:
  1. GET /api/v2/projects/{p}/models/{m}/versions/{v}/artifacts → presigned URLs
  2. Download needed parquet files to a temp dir
  3. Query via DuckDB:
     - Resolve rel codes from rel_types (never hardcode int codes)
     - Map object_k → feature type via IN_COLLECTION → CONTAINER.name
     - For each object: collect DISPLAY geometry Ks, decode SGEO blobs, build FMEAggregate
     - Fetch EAV properties
  4. Yield (feature_type, application_id, properties, geometry) tuples

See speckle_fme_core.geometry.speckle_to_fme for SGEO → FME geometry conversion.
See .universal-ai-config/instructions/ for full architecture notes.
"""

from __future__ import annotations

# TODO: Stage 4 — implement Receive
# Confirm whether specklepy.bundle.sgeo has decode() / try_decode_mesh() before
# writing the receive path. If absent, port from sgeoDecoder.ts in speckle-server-internal.


def receive(
    client,
    project_id: str,
    model_id: str,
    version_id: str,
    log=None,
):
    """Download a Speckle Next version bundle and yield FME feature data.

    Yields tuples of (feature_type: str, application_id: str, properties: dict, geometry).
    """
    raise NotImplementedError("Stage 4 — Receive not yet implemented")
