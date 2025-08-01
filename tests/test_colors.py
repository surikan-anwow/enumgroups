from enumgroups.base import GrpEnum, as_values
from enum import StrEnum


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
    assert COLORS.WARM.PRIM.RED != "green"


def test_as_values_membership():
    assert "green" in as_values(COLORS.COOL.SEC)
    assert "red" not in as_values(COLORS.COOL.SEC)
    assert "red" in as_values(COLORS)


def test_group_of():
    assert COLORS.group_of("orange") is COLORS.WARM.SEC
    assert COLORS.group_of("xxxx") is None
    assert COLORS.group_of("xxxx") is not COLORS.WARM.SEC


def test_leaf_paths_include_root():
    for path in COLORS.leaf_paths():
        assert path[-1] is COLORS


def test_leaf_paths_includes_all():
    leafs = tuple(COLORS.leaf_paths())
    leafs_expected = (
        (COLORS.COOL.PRIM.BLUE, COLORS.COOL.PRIM, COLORS.COOL, COLORS),
        (COLORS.COOL.SEC.GREEN, COLORS.COOL.SEC, COLORS.COOL, COLORS),
        (COLORS.COOL.SEC.PURPLE, COLORS.COOL.SEC, COLORS.COOL, COLORS),
        (COLORS.WARM.PRIM.RED, COLORS.WARM.PRIM, COLORS.WARM, COLORS),
        (COLORS.WARM.PRIM.YELLOW, COLORS.WARM.PRIM, COLORS.WARM, COLORS),
        (COLORS.WARM.SEC.ORANGE, COLORS.WARM.SEC, COLORS.WARM, COLORS),
    )
    assert leafs == leafs_expected


def test_as_values_all_values():
    vals = set(as_values(COLORS))
    assert {"red", "orange", "yellow"}.issubset(vals)
    assert {"red", "orange", "yellow", "blue", "green", "purple"}.issubset(vals)
    assert not {"red", "orange", "xxxx", "blue", "green", "purple"}.issubset(vals)
    assert not {"red", "orange", "yellow", "xxxx", "blue", "green", "purple"}.issubset(vals)
