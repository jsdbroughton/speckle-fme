"""
Auth — SpeckleClient factory and token resolution.

Resolution order (first non-empty wins):
  1. FME mappingFile parameter SPECKLE_TOKEN
  2. Environment variable SPECKLE_TOKEN

Server URL resolution order:
  1. FME mappingFile parameter SPECKLE_SERVER_URL
  2. Environment variable SPECKLE_SERVER_URL
  3. Default: https://next.speckle.dev
"""

from __future__ import annotations

import os

from specklepy.api.client import SpeckleClient


_DEFAULT_SERVER = "https://next.speckle.dev"


def client_from_mapping_file(
    mapping_file,
    keyword_prefix: str,
    type_prefix: str,
) -> SpeckleClient:
    """Build and authenticate a SpeckleClient from FME mapping file parameters."""
    token = (
        mapping_file.fetchWithPrefix(keyword_prefix, type_prefix, "SPECKLE_TOKEN")
        or os.environ.get("SPECKLE_TOKEN", "")
    )
    server_url = (
        mapping_file.fetchWithPrefix(keyword_prefix, type_prefix, "SPECKLE_SERVER_URL")
        or os.environ.get("SPECKLE_SERVER_URL", _DEFAULT_SERVER)
    )

    if not token:
        raise ValueError(
            "No Speckle token found. Set SPECKLE_TOKEN in the connector dialog "
            "or as an environment variable."
        )

    client = SpeckleClient(host=server_url)
    client.authenticate_with_token(token)
    return client


def client_from_env() -> SpeckleClient:
    """Build and authenticate a SpeckleClient from environment variables only.

    Used in tests and CI where there is no FME mapping file.
    """
    token = os.environ.get("SPECKLE_TOKEN", "")
    server_url = os.environ.get("SPECKLE_SERVER_URL", _DEFAULT_SERVER)

    if not token:
        raise ValueError("SPECKLE_TOKEN environment variable is not set.")

    client = SpeckleClient(host=server_url)
    client.authenticate_with_token(token)
    return client
