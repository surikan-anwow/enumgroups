# enumgroups

**Hierarchical Enums in Python** — powered by `StrEnum` and recursive class grouping.

`enumgroups` lets you define deeply nested, human-readable enums with Python's class structure.  
It supports arbitrary nesting, grouping, lookup, and traversal — all while preserving enum semantics.

---

## 🚀 Features

- Nest `StrEnum`, `IntEnum`, or standard `Enum` under any `GrpEnum`
- Retrieve enum members via dotted access: `COLORS.WARM.PRIM.RED`
- Support for:
  - Membership testing: `"red" in COLORS"`
  - Lookup by value: `COLORS.group_of("purple")`
  - Recursive iteration: `list(COLORS)`
  - Path introspection: `leaf_paths()`, `traverse_all()`, etc.
  - Conversion to `dict` with `.as_dict()`

---

## 📦 Installation

> Requires Python **3.11+** (for `StrEnum`)

```bash
uv pip install -e .
```

---

## 🎨 Example

```python
from enum import StrEnum
from enumgroups import GrpEnum

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

### 🔍 Usage

```python
COLORS.WARM.PRIM.RED        # "red"
"purple" in COLORS.COOL     # True
"red" in COLORS             # True
COLORS.group_of("green")    # COLORS.COOL.SEC

list(COLORS)                # All color values
list(COLORS.leaf_paths())   # Full ancestry tuples
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📁 Project Layout

```
enumgroups/
├── base.py            # Core GrpEnum logic
├── __init__.py
├── examples/
│   └── colors_demo.py
├── tests/
│   └── test_colors.py
├── README.md
└── pyproject.toml
```

---

## 📄 License

MIT License  
© 2025 [surikan.anwow](https://github.com/surikan.anwow)
