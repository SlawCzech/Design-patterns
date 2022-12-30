from abstract_factory.abstract_factory.autos.gm.cadillac import CadillacCTS
from abstract_factory.abstract_factory.autos.gm.camaro import ChevyCamaro
from abstract_factory.abstract_factory.autos.gm.spark import ChevySpark
from abstract_factory.abstract_factory.factories.abs_factory import AbsFactory


class GMFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return ChevySpark()

    @staticmethod
    def create_sport():
        return ChevyCamaro()

    @staticmethod
    def create_luxury():
        return CadillacCTS()