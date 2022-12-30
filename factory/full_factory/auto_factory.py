from inspect import getmembers, isclass, isabstract

from factory.simple_factory import autos
from factory.simple_factory.autos import AbsAuto


class AutoFactory:
    autos = {}

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(autos, lambda x: isclass(x) and not isabstract(x))

        for name, class_ in classes:
            if isclass(class_) and issubclass(class_, AbsAuto):
                self.autos.update([(name, class_)])

    def create_instance(self, car_name):
        if car_name in self.autos:
            return self.autos[car_name]()
        return autos.NullCar(car_name)

