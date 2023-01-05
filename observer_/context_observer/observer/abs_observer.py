from abc import ABC, abstractmethod


class AbsObserver(ABC):

    def __enter__(self):
        return self

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    def update(self, value):
        pass
