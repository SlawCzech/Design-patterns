from factory.full_factory.autos import ChevyVolt
from factory.full_factory.factories.abs_factory import AbsFactory


class ChevyFactory(AbsFactory):
    def create_auto(self):
        self.chevy = chevy = ChevyVolt()
        chevy.name = 'Chevy Volt'
        return chevy

