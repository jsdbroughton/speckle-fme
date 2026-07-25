"""
Bundle Publish — FME features → Speckle Next parquet bundle → upload.

Build sequence (MeFi Publish first):
  1. Create model ingestion (pre-allocates versionId)
  2. Walk FME features → ObjectsArtifactPipeline
     - intern_object(application_id)
     - add_properties(application_id, properties_dict)
     - add_geometry(geo_app_id, speckle_geometry)      → geometry K
     - pipeline.display(obj_k, geo_k)
     - pipeline.in_collection(obj_k, coll_k)
  3. pipeline.complete() → parquet files in temp dir
  4. ArtifactPipeline.upload_dir(version_id, root_id, object_count)

See speckle_fme_core.geometry.fme_to_speckle for FME → Speckle geometry conversion.
See .universal-ai-config/instructions/ for full architecture notes.
"""

from __future__ import annotations

# TODO: Stage 1 — implement MeFi Publish
# Reference: specklesystems/speckle-blender branch bilal/parquet-bundle-migration
#   bpy_speckle/connector/operations/bundle_publish.py


def publish(
    client,
    project_id: str,
    model_id: str,
    features,  # iterable of FMEFeature
    commit_message: str = "",
    log=None,
) -> str:
    """Publish FME features as a Speckle Next version.

    Returns the created versionId.
    Raises SpeckleFMEError if the server does not support Speckle Next v2 endpoints.
    """
    raise NotImplementedError("Stage 1 — MeFi Publish not yet implemented")
