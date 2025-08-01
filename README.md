# enumgroups

`enumgroups` is a lightweight Python utility for defining **hierarchical enums** using standard `Enum`, `StrEnum`, or `IntEnum` types inside nested groupings called `GrpEnum`.

`enumgroups` lets you define deeply nested, human-readable enums with Python's class structure.  
It supports arbitrary nesting, grouping, lookup, and traversal — all while preserving enum semantics.


## 🚀 Features

- Nest `StrEnum`, `IntEnum`, or standard `Enum` under any `GrpEnum`
- Retrieve enum members via dotted access: `COLORS.WARM.PRIM.RED`
- Support for:
  - Membership testing: `"red" in as_values(COLORS)"`
  - Lookup by value: `COLORS.group_of("purple")`
  - Recursive iteration: `list(COLORS)`
  - Path introspection: `leaf_paths()`, `traverse_all()`, etc.

## 📦 Installation

> Requires Python **3.11+** (for `StrEnum`)

```
uv pip install git+https://github.com/surikan-anwow/enumgroups.git@v.0.1.1
```

## 📦 Example

```python
from enum import StrEnum
from enumgroups.base import GrpEnum, as_values

class COLORS(GrpEnum):
    class WARM(GrpEnum):
        class PRIM(StrEnum):
            RED = "red"
            YELLOW = "yellow"
        class SEC(StrEnum):
            ORANGE = "orange"

    class COOL(GrpEnum):
        class PRIM(StrEnum):
            BLUE = "blue"
        class SEC(StrEnum):
            GREEN = "green"
            PURPLE = "purple"
```

## 🧪 Usage

```python
COLORS.WARM.PRIM.RED              # 'red'
"green" in as_values(COLORS.COOL)        # True
"red" in as_values(COLORS)               # True
COLORS.group_of("orange")        # COLORS.WARM.SEC
list(COLORS.leaf_elems())        # All final enum items
list(COLORS.leaf_paths())        # Full ancestry for each leaf

# Also for normals Enums
"green" in as_values(COLORS.COOL.SEC)        # True
```

---

## 📄 License
Author: surikan.anwow  
Created: May 12, 2025  
License: MIT
