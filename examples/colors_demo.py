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


if __name__ == "__main__":

    print("🍊 Direct access:", 
          COLORS.WARM.SEC.ORANGE)
    
    print("✅ Membership test:", 
          "green" in as_values(COLORS))
    
    print("🔎 Group of 'purple':", 
          COLORS.group_of("purple"))
    
    print("🌿 Leaf elements:", 
          list(COLORS.leaf_elems()))
    
    print("🧭 Leaf paths: str()")
    for path in COLORS.leaf_paths():
        print(" → ".join(str(cls) for cls in path))
