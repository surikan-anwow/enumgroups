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

if __name__ == "__main__":
    for c in COLORS:
        print("Color:", c)

    for path in COLORS.leaf_paths():
        print("Path:", " → ".join(cls.__name__ for cls in path))
