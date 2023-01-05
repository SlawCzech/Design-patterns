from abc import ABC, abstractmethod


class AbsObserver(ABC):
    @abstractmethod
    def update(self, value):
        pass
