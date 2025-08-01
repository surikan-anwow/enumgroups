from typing import Union, Generator, Type, Any
from enum import Enum, StrEnum
from typing import Union, Generator, Any, Type


class GrpEnum:
    @classmethod
    def __iter__(cls):
        if hasattr(cls, "__members__"):
            yield from cls.__members__.values()
        else:
            for attr in dir(cls):
                group = getattr(cls, attr)
                if isinstance(group, type) and issubclass(group, (GrpEnum, Enum)):
                    yield from group

    @classmethod
    def __contains__(cls, item):
        try:
            return any(item == elem.value for elem in cls)
        except Exception:
            return False

    @classmethod
    @property
    def __members__(cls):
        return {attr: getattr(cls, attr) for attr in dir(cls) if not attr.startswith("_") and (
            isinstance(getattr(cls, attr), Enum) or (
                isinstance(getattr(cls, attr), type) and issubclass(getattr(cls, attr), (GrpEnum, Enum))))}

    @classmethod
    def group_of(cls, item):
        for member in cls.__members__.values():
            if isinstance(member, type) and issubclass(member, GrpEnum):
                found = member.group_of(item)
                if found:
                    return found
            elif isinstance(member, type) and issubclass(member, Enum):
                if item in (m.value for m in member):
                    return member
            elif isinstance(member, Enum) and member.value == item:
                return cls
        return None

    @classmethod
    def _groups(cls):
        return (getattr(cls, attr) for attr in dir(cls) if
        isinstance(getattr(cls, attr), type) and issubclass(getattr(cls, attr), (GrpEnum, Enum)))

    @classmethod
    def class_name(cls):
        return cls.__name__

    @classmethod
    def values(cls):
        for v in cls:
            yield v.value

    @classmethod
    def items(cls):
        for v in cls:
            yield v.name, v.value

    @classmethod
    def as_dict(cls):
        return dict(cls.items())

    @classmethod
    @classmethod
    def leaf_elems(cls):
        if (hasattr(cls, "__members__") and all(isinstance(m, Enum) for m in cls.__members__.values())):
            yield from cls.__members__.values()
            return

        for group in cls._groups():
            if isinstance(group, type) and issubclass(group, GrpEnum):
                yield from group.leaf_elems()
            elif isinstance(group, type) and issubclass(group, Enum):
                yield from group.__members__.values()

    @classmethod
    def leaf_paths(cls):
        def _walk(c, lineage):
            if (hasattr(c, "__members__") and all(isinstance(m, Enum) for m in c.__members__.values())):
                for leaf in c.__members__.values():
                    yield (leaf, *lineage)
            else:
                for group in c._groups():
                    yield from _walk(group, (group, *lineage))

        return _walk(cls, (cls,))


def as_values(enum_or_group: Union[Type[Enum], Type[GrpEnum]]) -> Generator[Any, None, None]:
    """
    Returns a flat generator of .value from a standard Enum or nested GrpEnum.
    """
    if hasattr(enum_or_group, "leaf_elems"):
        return (member.value for member in enum_or_group.leaf_elems())
    elif hasattr(enum_or_group, "__members__"):
        return (member.value for member in enum_or_group.__members__.values())
    else:
        raise TypeError(f"{enum_or_group} is not an Enum or GrpEnum.")
