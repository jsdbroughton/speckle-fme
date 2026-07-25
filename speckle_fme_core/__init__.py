"""
speckle_fme_core — standalone Python module for the Speckle FME connector.

Targets Speckle Next (next.speckle.dev) exclusively via the three-artefact
parquet bundle (SGEO + EAV + envelope). Does NOT use operations.send() /
operations.receive() — those are v3/legacy paths.

Sub-modules
-----------
auth            SpeckleClient factory and token resolution
api             Thin wrappers around specklepy client resources
bundle_publish  FME features → ObjectsArtifactPipeline → ArtifactPipeline upload
bundle_receive  Download v2 artifacts → parquet → FME features
schema          readSchema() helpers (EAV paths, container names)
geometry/       FME ↔ Speckle geometry conversion
reader          FMEReader Pluginbuilder class
writer          FMEWriter Pluginbuilder class
"""
