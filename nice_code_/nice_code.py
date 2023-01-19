import abc
from collections.abc import Iterable


class AbsNonStringIterable(abc.ABC):
    @abc.abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is AbsNonStringIterable:
            if issubclass(subclass, str):
                return False
            if hasattr(subclass, '__iter__') and (subclass.__iter__ is not None):
                return True
        return NotImplemented


arr = [[2, 3, [6, (1, 4, 7), 8]], [5, 6, 7], [8, 9]]
arr_str = ['ala', 'ula', 'ola']


def flatten(items):
    for item in items:
        if isinstance(item, AbsNonStringIterable):
            yield from flatten(item)
        else:
            yield item


print(list(flatten(arr)))
print(list(flatten(arr_str)))
