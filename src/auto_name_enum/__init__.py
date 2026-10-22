from enumatic import Enumatic, KebabCaseMixin, LowerCaseMixin, TitleCaseMixin, auto, autodoc

from auto_name_enum.deprecated import warn_legacy

AutoNameEnum = Enumatic


warn_legacy()

__all__ = (
    "AutoNameEnum",
    "Enumatic",
    "KebabCaseMixin",
    "LowerCaseMixin",
    "TitleCaseMixin",
    "auto",
    "autodoc",
)
