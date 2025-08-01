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


def test_individual_access():
    assert COLORS.WARM.PRIM.RED == "red"
    assert COLORS.COOL.SEC.GREEN == "green"


def test_membership():
    assert "green" in COLORS.COOL.SEC
    assert "red" in COLORS


def test_group_of():
    assert COLORS.group_of("orange") is COLORS.WARM.SEC


def test_leaf_paths_include_root():
    for path in COLORS.leaf_paths():
        assert path[-1] is COLORS
