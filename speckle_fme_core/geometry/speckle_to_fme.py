"""
Speckle → FME geometry conversion (Receive path).

Decodes SGEO binary blobs from the geometries parquet into FMEGeometry objects.

SGEO header layout (16 bytes):
  0x00  4  magic = "SGEO"
  0x04  1  version = 1
  0x05  1  primitive_type (0=mesh, 1=line, 2=polyline, ...)
  0x06  2  flags (u16)
  0x08  2  units_code (u16) — 1=mm, 3=m
  0x0A  2  reserved
  0x0C  4  crc32(body)
  0x10  →  body

Mesh body:
  vertex_count  u32
  face_index_count  u32
  vertices  flat float64 [x0,y0,z0, x1,y1,z1, ...]
  faces     flat int32   [n, i0, i1, ..., n, i0, i1, ...]

MVP: decode SGEO mesh blobs → FMEFace parts → FMEAggregate.
"""

from __future__ import annotations

# TODO: Stage 4 — implement SGEO decode → FMEGeometry
# First confirm whether specklepy.bundle.sgeo has decode() / try_decode_mesh().
# If present, use it. If absent, implement here from the SGEO spec above
# (reference: sgeoDecoder.ts in speckle-server-internal).


def sgeo_blob_to_fme(blob: bytes):
    """Decode an SGEO binary blob to an FMEGeometry object.

    Returns None if the blob cannot be decoded (log as conversion error).
    """
    raise NotImplementedError("Stage 4 — SGEO → FMEGeometry not yet implemented")
