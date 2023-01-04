from decorator.decorator.cars.abs_car import AbsCar


class Premium(AbsCar):
    @property
    def description(self):
        return 'Premium'

    @property
    def cost(self):
        return 25000.00

