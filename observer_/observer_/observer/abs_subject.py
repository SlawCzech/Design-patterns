from abc import ABC

from observer_.observer_.observer.abs_observer import AbsObserver


class AbsSubject(ABC):
    _observers = set()

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
