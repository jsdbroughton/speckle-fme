"""
Schema helpers — readSchema() support.

Provides container names (→ FME feature types) and EAV attribute paths
for a given Speckle Next version.
"""

from __future__ import annotations

import io

import httpx
import pyarrow.parquet as pq


def get_container_names(
    server_url: str, token: str, project_id: str, model_id: str, version_id: str
) -> list[str]:
    """Download the envelope.nodes parquet and return all CONTAINER names."""
    artifact_url = (
        f"{server_url.rstrip('/')}/api/v2/projects/{project_id}"
        f"/models/{model_id}/versions/{version_id}/artifacts"
    )
    resp = httpx.get(
        artifact_url,
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    files = {f["name"]: f["url"] for f in resp.json().get("files", [])}

    nodes_key = f"{version_id}.envelope.nodes.parquet"
    nodes_url = files.get(nodes_key)
    if not nodes_url:
        return []

    data = httpx.get(nodes_url, timeout=60).content
    table = pq.read_table(io.BytesIO(data))

    names = []
    for row in table.to_pylist():
        if row.get("kind") == "CONTAINER" and row.get("name"):
            names.append(row["name"])
    return list(dict.fromkeys(names))  # deduplicate, preserve order


def get_eav_paths(
    server_url: str, token: str, project_id: str, model_id: str, version_id: str
) -> list[str]:
    """Download the eav.paths parquet and return all property path strings."""
    artifact_url = (
        f"{server_url.rstrip('/')}/api/v2/projects/{project_id}"
        f"/models/{model_id}/versions/{version_id}/artifacts"
    )
    resp = httpx.get(
        artifact_url,
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    files = {f["name"]: f["url"] for f in resp.json().get("files", [])}

    paths_key = f"{version_id}.eav.paths.parquet"
    paths_url = files.get(paths_key)
    if not paths_url:
        return []

    data = httpx.get(paths_url, timeout=60).content
    table = pq.read_table(io.BytesIO(data))
    return [row["path"] for row in table.to_pylist() if row.get("path")]
