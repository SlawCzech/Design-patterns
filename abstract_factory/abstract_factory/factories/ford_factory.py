from abstract_factory.abstract_factory.autos.ford.fiesta import FordFiesta
from abstract_factory.abstract_factory.autos.ford.lincoln import LincolnMKS
from abstract_factory.abstract_factory.autos.ford.mustang import FordMustang
from abstract_factory.abstract_factory.factories.abs_factory import AbsFactory


class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()

    @staticmethod
    def create_luxury():
        return LincolnMKS()
