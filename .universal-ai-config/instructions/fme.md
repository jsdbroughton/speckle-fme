---
description: FME Pluginbuilder patterns and metafile conventions
globs: ["python/**/*.py", "speckle_fme_core/**/*.py", "formats/*.fmf"]
---

# FME conventions

## FMEReader / FMEWriter lifecycle

- `open()` in data mode receives **empty** `parameters`. Fetch all config via `self.mappingFile.fetchWithPrefix(...)`.
- `read()` / `readSchema()` are mutually exclusive per `open()` call.
- `close()` may be called multiple times — always guard: `if self._closed: return; self._closed = True`.
- Raise `fmeobjects.FMEException` to signal errors; FME surfaces these in the log panel.

## Geometry

- One Speckle object → one FME feature. Multi-mesh `displayValue` → one `FMEAggregate` with `appendPart()` per mesh. Never split into multiple features.
- Before iterating `FMEAggregate` parts on Publish: check `getGeometryDefinitionReference()`.
  - Returns a value → block instance path: emit DEFINITION + INSTANCE + DISPLAY_INSTANCE.
  - Returns `None` → compound object: iterate parts, one DISPLAY edge per part.
- Empty `displayValue` is valid — emit an attribute-only feature with no geometry.
- Always check `units` before geometry math. Normalise to metres at the conversion boundary.

## Attributes

- Use `feature.setSequencedAttribute(name, fme_type)` in `readSchema()`.
- Null values: use `setAttributeNullWithType(name, FME_ATTR_STRING)` — not `setAttribute(name, None)`.
- Check `isAttributeNull()` and `isAttributeMissing()` separately; handle both.

## Logging and progress

```python
import fmeobjects
log = fmeobjects.FMELogFile()
log.logMessageString("Speckle: message", fmeobjects.FME_INFORM)
log.logMessageString("Speckle: error", fmeobjects.FME_ERROR)
# Progress (updates FME status bar):
log.logMessageString(f"FMEMSG 0 {pct}", fmeobjects.FME_INFORM)
```

Emit progress after every 100 features during conversion. Always log at start and end of publish/receive.

## Metafile (.fmf)

- Keywords prefixed `-` in `SOURCE_READER` are available at schema time only — not written to mapping files.
- Use `ATTRIB_CHANGE` (not `GEOM_CHANGE`) — Speckle feature types are heterogeneous.
- Geometry type strings in `GEOM_MAP`: `fme_solid`, `fme_surface`, `fme_point`, `fme_line`, `fme_no_geom`.

## fmeobjects availability

`fmeobjects` is a compiled `.so` only available inside FME's runtime. Any module in `speckle_fme_core/` must guard top-level FME imports:

```python
try:
    import fmeobjects
    _FME_AVAILABLE = True
except ImportError:
    _FME_AVAILABLE = False
```
