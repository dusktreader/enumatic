from enumatic.base import Enumatic, EnumaticMeta, auto, autodoc

from auto_name_enum.deprecated import warn_legacy

AutoNameEnum = Enumatic
AutoNameEnumMeta = EnumaticMeta

warn_legacy()

__all__ = ("AutoNameEnum", "AutoNameEnumMeta", "Enumatic", "EnumaticMeta", "auto", "autodoc")
