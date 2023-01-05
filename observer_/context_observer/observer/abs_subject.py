from abc import ABC

from observer_.context_observer.observer.abs_observer import AbsObserver


class AbsSubject(ABC):
    _observers = set()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        type(self)._observers.clear()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        type(self)._observers |= {observer}

    def detach(self, observer):
        type(self)._observers -= {observer}

    def notify(self, value=None):
        for observer in type(self)._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)
