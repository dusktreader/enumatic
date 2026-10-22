# Enumatic

Enumatic provides string-valued Python enums that automatically assign each member's value from its name.

> **Project rename:** `auto-name-enum` is now `enumatic`, and `AutoNameEnum` is now `Enumatic`. This is a major release.
> Install `enumatic` and change imports to `from enumatic import Enumatic, auto`. Existing `from auto_name_enum import
> AutoNameEnum` imports remain available through a compatibility
> package, but new code should use `enumatic` and `Enumatic`.


## Why Enumatic instead of `StrEnum`

First of all, back when `enumatic` was named `auto-name-enum` and was first released, Python didn't have a `StrEnum`
type that offered builtin `auto()` functionality. So, `AutoNameEnum` (as `Enumatic`
used to be called) provided the boilerplate to enable `auto()`.

After Python 3.11, the standard library `StrEnum` provides a lot of the same functionality as `Enumatic`.
However, there are still some nice things that `Enumatic` provides beyond `StrEnum`.

For example, `Enumatic` preserves the case of your values by defualt, and offers a few helper functions that control how
casing is applied to the values. It also offers the `pretty_list()` helper which nicely formats the list of values as
well as the `rando()` method that randomly chooses one of the values. Finally, `Enumatic`
provides the `autodoc()` helper to provide context to the values automatically.


## Installation

Install the renamed package from PyPI:

```shell
pip install enumatic
```


## Specifying your enum

Import `Enumatic` and its helpers, then define an enum:

```python
from enumatic import Enumatic, auto


class Species(Enumatic):
    JAWA = auto()
    EWOK = auto()
    HUTT = auto()
    PYKE = auto()
```


## Getting values

`auto()` assigns each value from its member name:

```python
>>> print(Species.JAWA.value)
'JAWA'
```

The enum member also behaves like its string value:

```python
>>> print(Species.JAWA)
'JAWA'
```


## Iterating

Python enums may be iterated over:

```python
for species in Species:
    print(f"name: {species.name}, value: {species.value}")
```

For more information on enums and `auto()`, see the [official Python
documentation](https://docs.python.org/3/library/enum.html).


## Mixins

Three mixins change the case of member values for both `auto()` and `autodoc()`:

- `LowerCaseMixin`: values are in all lower-case
- `TitleCaseMixin`: values are in title-case (lower-case except for first letter)
- `KebabCaseMixin`: values are in kebab-case (dashes instead of underscores)

Include a mixin after `Enumatic` in the class inheritance declaration:

```python
class Species(Enumatic, TitleCaseMixin):
    JAWA = auto()
    EWOK = auto()
    HUTT = auto()
    PYKE = auto()
```

Then, you can check how the values are changed:

```python
>>> print(Species.JAWA)
'Jawa'
```


## Documented members with `autodoc()`

The `autodoc()` function works like `auto()`, but also attaches a `description` and/or `display_name` to each enum
member. This is useful for self-documenting enums where members need human-readable explanations or labels:

```python
class Species(Enumatic):
    JAWA = autodoc("A small, rodent-like species from Tatooine")
    EWOK = autodoc("A furry, diminutive species from the forest moon of Endor")
    HUTT = autodoc("A large, slug-like species from Nal Hutta")
    PYKE = autodoc("A secretive, spice-dealing species from Oba Diah")
```

`autodoc()` assigns the value just like `auto()`:

```python
>>> print(Species.JAWA.value)
'JAWA'
```

Access the description via the `.description` property:

```python
>>> print(Species.JAWA.description)
'A small, rodent-like species from Tatooine'
```

A `display_name` can also be attached as a keyword argument:

```python
class Species(Enumatic):
    JAWA = autodoc(description="A small, rodent-like species from Tatooine", display_name="Jawa (Tatooine)")
    EWOK = autodoc(description="A furry, diminutive species from the forest moon of Endor", display_name="Ewok (Endor)")
```

```python
>>> print(Species.JAWA.display_name)
'Jawa (Tatooine)'
```

You can mix `auto()` and `autodoc()` in the same enum. Members created with `auto()`
will return `None` for `.description` and their value for `.display_name`:

```python
class Species(Enumatic):
    JAWA = autodoc("A small, rodent-like species from Tatooine")
    EWOK = auto()
    HUTT = autodoc("A large, slug-like species from Nal Hutta")
```

```python
>>> print(Species.JAWA.description)
'A small, rodent-like species from Tatooine'
>>> print(Species.EWOK.description)
None
>>> print(Species.EWOK.display_name)
'EWOK'
```
