from factory.full_factory.autos import FordFusion
from factory.full_factory.factories.abs_factory import AbsFactory


class FordFactory(AbsFactory):
    def create_auto(self):
        self.ford = ford = FordFusion()
        ford.name = 'Ford Fusion'
        return ford

