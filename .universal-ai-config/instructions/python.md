---
description: Python coding conventions for speckle-fme
globs: ["**/*.py"]
---

# Python conventions

## Type hints — first priority

Type hints are the primary documentation in this codebase. They are more valuable than comments. When in doubt, add a type, not a comment.

- **Every function signature gets full type hints** — parameters and return type, no exceptions. If a function is hard to type, that's a signal the interface needs rethinking.
- **Every module-level variable and class attribute gets a type annotation.** No bare `x = []` or `data = {}`.
- Use `from __future__ import annotations` at the top of every module — enables forward references and deferred evaluation without runtime cost.
- Python ≥3.10 syntax everywhere: `X | None` not `Optional[X]`, `list[str]` not `List[str]`, `dict[str, int]` not `Dict[str, int]`.
- `Any` is a last resort. When used, add `# type: ignore[assignment]` or a narrow cast rather than widening the whole expression. Never use `Any` for "I'll fix this later" — use a concrete type or `object`.
- Use `TypeAlias` for complex repeated types: `ObjectKey: TypeAlias = int` at module level so the intent is clear across the codebase.
- Use `TypedDict` for bundle row shapes, API response dicts, and any dict that has a fixed schema. Don't pass `dict[str, Any]` when you know the keys.
- Use `Protocol` for duck-typed interfaces (e.g. anything FME-adjacent that can't import `fmeobjects` at type-check time).
- `@overload` for functions with meaningfully different return types depending on argument type — don't hide that in a `Union` return.
- `Final` for constants: `VERSION_ID_PREFIX: Final = "binary-"`.
- `Literal` for constrained string/int values: `NodeKind = Literal["CONTAINER", "MATERIAL", "COLOR", "LEVEL", "DEFINITION", "INSTANCE"]`.

### specklepy types

Import and use specklepy's own types directly — they are fully annotated and should flow through the codebase:

```python
from specklepy.bundle.spec import Rel, NodeKind
from specklepy.bundle.pipeline import ObjectsArtifactPipeline
from specklepy.api.client import SpeckleClient
from specklepy.objects.geometry import Mesh, Line, Point
```

Don't re-type what specklepy already types. Let inference carry it.

### Type narrowing over comments

Instead of:
```python
# geo_k is an int returned by intern_object
geo_k = p.intern_object(app_id)
```

Write:
```python
geo_k: int = p.intern_object(app_id)
```

Or better — rely on the return annotation of `intern_object` and let the type flow.

### Return types always explicit

Never omit return type annotations. `-> None` is explicit and required. `-> int | None` is better than a docstring saying "returns int or None".

## Style

- Named parameters over positional for functions with more than 2 args.
- Constants in `UPPER_SNAKE_CASE` at module level with `Final`.
- Dataclasses or named tuples over bare tuples for structured return values.

## Error handling

- Define `SpeckleFMEError(Exception)` as the project's base exception. Raise it (not raw `Exception`) for all connector-specific errors.
- Catch broad exceptions only at the boundary (FME lifecycle methods: `open`, `read`, `write`, `close`). Log with `fmeobjects.FMELogFile` before re-raising or returning.
- Never silently swallow errors. A comment like `# best-effort telemetry` is required on intentional bare `except` blocks.

## Imports

- Standard library → third-party → local, separated by blank lines.
- Avoid star imports. Prefer explicit named imports.
- `fmeobjects` is only importable inside FME's runtime — guard any top-level import with `try/except ImportError` in modules used outside FME (e.g. `speckle_fme_core`). Use `TYPE_CHECKING` for type-only imports:

```python
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import fmeobjects
```

## Speckle SDK usage

- Always import from `specklepy.bundle` for the data pipeline. Never import from `specklepy.api.operations` for send/receive.
- Feature-detect `specklepy.bundle` with `try/except ImportError` at the top of modules that use it, so the module can be imported for type-checking without the optional dep installed.

## Docstrings

Docstrings supplement types — they explain *why*, not *what*. The type signature already says what.

- Omit if the function name + type signature is self-explanatory.
- One-line docstring for functions with non-obvious behaviour.
- Multi-line only for public API functions where the *why* isn't obvious: edge cases, preconditions, side effects. Never repeat what the type annotation already says.
