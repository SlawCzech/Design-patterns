from decorator.decorator.decorators.abs_decorator import AbsDecorator


class RedThread(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', red thread'

    @property
    def cost(self):
        return self.car.cost + 2000.00
