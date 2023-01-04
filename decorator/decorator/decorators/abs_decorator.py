from abc import ABC

from decorator.decorator.cars.abs_car import AbsCar


class AbsDecorator(AbsCar, ABC):
    def __init__(self, car):
        self._car = car

    @property
    def car(self):
        return self._car

