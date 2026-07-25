"""
Geometry conversion between FME and Speckle.

fme_to_speckle  — FMEGeometry → specklepy geometry objects → sgeo.encode()
speckle_to_fme  — SGEO blobs → FMEGeometry (Receive path)

MVP scope: Mesh ↔ FMEFace / FMEAggregate only.
Other geometry types (Line, Arc, Curve, Point, Box, Instance) are additive.
"""
