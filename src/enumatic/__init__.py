from typing import Any

from deprecated import deprecated

from enumatic.base import Enumatic, auto, autodoc
from enumatic.mixins import KebabCaseMixin, LowerCaseMixin, TitleCaseMixin


@deprecated(reason="auto_name_enum was renamed to enumatic; use enumatic instead")
def _legacy_auto_name_enum() -> type[Enumatic]:
    return Enumatic


def __getattr__(name: str) -> Any:
    if name == "AutoNameEnum":
        return _legacy_auto_name_enum()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = (
    "auto",
    "autodoc",
    "Enumatic",
    "AutoNameEnum",
    "KebabCaseMixin",
    "LowerCaseMixin",
    "TitleCaseMixin",
)
