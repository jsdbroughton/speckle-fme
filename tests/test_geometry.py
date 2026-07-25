"""
Unit tests for SGEO encode/decode and FME ↔ Speckle geometry conversion.

No FME runtime required — fmeobjects is imported lazily only where needed.
No Speckle server required.

TODO: Stage 2 — add round-trip tests once fme_to_speckle.py is implemented.
TODO: Stage 4 — add SGEO decode tests once speckle_to_fme.py is implemented.
"""

import pytest


@pytest.mark.skip(reason="Stage 2 — not yet implemented")
def test_fme_mesh_to_speckle_mesh():
    """FMEFace → Speckle Mesh → sgeo.encode() round-trip."""
    pass


@pytest.mark.skip(reason="Stage 4 — not yet implemented")
def test_sgeo_mesh_decode():
    """SGEO mesh blob → FMEFace vertices/faces match source."""
    pass
