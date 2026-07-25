"""
Integration tests — end-to-end Publish against next.speckle.dev.

Requires environment variables (see conftest.py). Run with:
  pytest tests/test_bundle_publish.py -v

Each test creates its own model via the test_model fixture and cleans up on teardown.

TODO: Stage 1 — implement once bundle_publish.publish() exists.
"""

import pytest


@pytest.mark.skip(reason="Stage 1 — bundle_publish.publish() not yet implemented")
def test_publish_creates_version(speckle_client, test_model, test_project_id):
    """Publishing a minimal feature set produces a visible Speckle Next version."""
    pass


@pytest.mark.skip(reason="Stage 1 — bundle_publish.publish() not yet implemented")
def test_publish_requires_speckle_next(speckle_client, test_project_id):
    """Connecting to a v3 server raises SpeckleFMEError, not a silent fallback."""
    pass
