from factory.full_factory.autos import JeepSahara
from factory.full_factory.factories.abs_factory import AbsFactory


class JeepFactory(AbsFactory):
    def create_auto(self):
        self.jeep = jeep = JeepSahara()
        jeep.name = 'JeepSahara'
        return jeep

