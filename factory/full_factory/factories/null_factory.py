from factory.full_factory.autos import NullCar
from factory.full_factory.factories.abs_factory import AbsFactory


class NullFactory(AbsFactory):
    def create_auto(self):
        self.nullcar = nullcar = NullCar()
        nullcar.name = 'Unknown'
        return nullcar

