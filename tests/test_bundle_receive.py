"""
Integration tests — end-to-end Receive against next.speckle.dev.

Requires environment variables (see conftest.py). Run with:
  pytest tests/test_bundle_receive.py -v

TODO: Stage 4 — implement once bundle_receive.receive() exists.
"""

import pytest


@pytest.mark.skip(reason="Stage 4 — bundle_receive.receive() not yet implemented")
def test_receive_yields_features(speckle_client, test_project_id):
    """Receiving a known version yields at least one feature with geometry."""
    pass


@pytest.mark.skip(reason="Stage 4 — bundle_receive.receive() not yet implemented")
def test_receive_feature_types_from_collections(speckle_client, test_project_id):
    """Feature types map to IN_COLLECTION container names, not speckle_type."""
    pass
