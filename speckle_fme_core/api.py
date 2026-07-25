"""
API helpers — thin wrappers around specklepy client resources.

Keeps FME-specific code out of specklepy call sites and centralises
error handling for common operations.
"""

from __future__ import annotations

import httpx
from specklepy.api.client import SpeckleClient


class SpeckleFMEError(Exception):
    """Raised for connector-level errors that should surface to the FME log."""


def get_latest_version_id(client: SpeckleClient, project_id: str, model_id: str) -> str:
    """Return the ID of the most recent version on a model.

    Raises SpeckleFMEError if no versions exist.
    """
    model = client.model.get_with_versions(
        model_id=model_id,
        project_id=project_id,
        versions_limit=1,
    )
    items = (model.versions.items if model and model.versions else [])
    if not items:
        raise SpeckleFMEError(
            f"No versions found for model '{model_id}' in project '{project_id}'."
        )
    return items[0].id


def fetch_pre_allocated_version_id(
    account, project_id: str, ingestion_id: str
) -> str | None:
    """Query the Speckle Next GraphQL API for the pre-allocated versionId.

    Returns None if the server does not support v2 bundle endpoints (older server).
    """
    query = (
        "query($p:String!,$i:ID!){ project(id:$p){ ingestion(id:$i){ versionId } } }"
    )
    try:
        resp = httpx.post(
            account.serverInfo.url.rstrip("/") + "/graphql",
            headers={"Authorization": f"Bearer {account.token}"},
            json={"query": query, "variables": {"p": project_id, "i": ingestion_id}},
            timeout=30,
        )
        body = resp.json()
    except Exception:
        return None

    if body.get("errors"):
        return None

    return (
        (((body.get("data") or {}).get("project") or {}).get("ingestion") or {})
        .get("versionId")
    )
