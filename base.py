from enum import Enum, StrEnum

class GrpEnum:
    """
    Base class for hierarchical groupings. Can contain GrpEnum subclasses
    or any valid Enum subclass like StrEnum, IntEnum, Enum.
    """
    @classmethod
    def __iter__(cls):
        if hasattr(cls, "__members__"):
            return iter(cls.__members__.values())
        else:
            for attr in dir(cls):
                group = getattr(cls, attr)
                if isinstance(group, type) and issubclass(group, (GrpEnum, Enum)):
                    yield from group

    @classmethod
    def __contains__(cls, item):
        if hasattr(cls, "__members__"):
            return item in cls.__members__.values()
        else:
            return any(item in group for group in cls._groups())

    @classmethod
    def _groups(cls):
        return [
            getattr(cls, attr) for attr in dir(cls)
            if isinstance(getattr(cls, attr), type) and issubclass(getattr(cls, attr), (GrpEnum, Enum))
        ]

    @classmethod
    def group_of(cls, item):
        for group in cls._groups():
            if item in group:
                return group
        return None

    @classmethod
    def class_name(cls):
        return cls.__name__

    @classmethod
    def values(cls):
        return (v.value for v in cls)

    @classmethod
    def items(cls):
        return ((v.name, v.value) for v in cls)

    @classmethod
    def as_dict(cls):
        return dict(cls.items())

    @classmethod
    def leaf_elems(cls):
        if hasattr(cls, "__members__"):
            yield from cls
        else:
            for group in cls._groups():
                yield from group.leaf_elems()

    @classmethod
    def traverse_all(cls):
        if hasattr(cls, "__members__"):
            yield from cls
        else:
            for group in cls._groups():
                yield group
                yield from group.traverse_all()

    @classmethod
    def leaf_paths(cls):
        def _walk(c, lineage):
            if hasattr(c, "__members__"):
                for leaf in c:
                    yield (leaf, *lineage)
            else:
                for group in c._groups():
                    yield from _walk(group, (group, *lineage))
        return _walk(cls, (cls,))
