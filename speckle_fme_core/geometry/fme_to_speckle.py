"""
FME → Speckle geometry conversion (Publish path).

Converts FMEGeometry objects to specklepy geometry objects suitable for
sgeo.encode(). The encoded bytes are then passed to
ObjectsArtifactPipeline.add_geometry().

Two aggregate cases (check before iterating parts):
  - getGeometryDefinitionReference() is set  → block instance
    Emit: DEFINITION node + INSTANCE node + DISPLAY_INSTANCE edge
  - getGeometryDefinitionReference() is None → compound object
    Emit: one DISPLAY edge per part

MVP: FMEFace / FMEMesh → Speckle Mesh is the only required path.
"""

from __future__ import annotations

# TODO: Stage 2 — implement FME → Speckle geometry
# Reference: specklepy.objects.geometry for Mesh, Point, Line, etc.
# sgeo.encode() dispatches on type(geometry).__name__


def fme_geometry_to_speckle(fme_geometry, units: str = "m"):
    """Convert a single FMEGeometry part to a specklepy geometry object.

    Returns None if the geometry type has no SGEO mapping (log as conversion error,
    do not abort the feature).
    """
    raise NotImplementedError("Stage 2 — FME → Speckle geometry not yet implemented")


def get_instance_ref(fme_aggregate) -> str | None:
    """Return the geometry definition reference from an FMEAggregate, or None."""
    try:
        return fme_aggregate.getGeometryDefinitionReference()
    except Exception:
        return None
