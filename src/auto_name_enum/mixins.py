from enumatic.mixins import KebabCaseMixin, LowerCaseMixin, TitleCaseMixin

from auto_name_enum.deprecated import warn_legacy

warn_legacy()

__all__ = ("KebabCaseMixin", "LowerCaseMixin", "TitleCaseMixin")
