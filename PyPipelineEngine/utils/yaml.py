from __future__ import annotations

from typing import TYPE_CHECKING, Any, BinaryIO, TextIO, cast

if TYPE_CHECKING:
    from yaml.error import MarkedYAMLError, YAMLError  # noqa: F401


def safe_load(stream: bytes | str | BinaryIO | TextIO) -> Any:
    """Like yaml.safe_load, but use the C libyaml for speed where we can."""
    # delay import until use.
    from yaml import load as orig

    try:
        from yaml import CSafeLoader as SafeLoader
    except ImportError:
        from yaml import SafeLoader  # type: ignore[assignment, no-redef]

    return orig(stream, SafeLoader)


def dump(data: Any, **kwargs) -> str:
    """Like yaml.safe_dump, but use the C libyaml for speed where we can."""
    # delay import until use.
    from yaml import dump as orig

    try:
        from yaml import CSafeDumper as SafeDumper
    except ImportError:
        from yaml import SafeDumper  # type: ignore[assignment, no-redef]

    return cast(str, orig(data, Dumper=SafeDumper, **kwargs))
