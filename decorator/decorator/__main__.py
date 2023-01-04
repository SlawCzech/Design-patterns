from decorator.decorator.cars.luxury import Luxury
from decorator.decorator.cars.premium import Premium
from decorator.decorator.decorators.black import Black
from decorator.decorator.decorators.red_thread import RedThread
from decorator.decorator.decorators.v6 import V6
from decorator.decorator.decorators.vinyl import Vinyl


def show(car):
    print(f'Description: {car.description}, cost: ${car.cost}')


lux_car = RedThread(Black(Vinyl(V6(Premium()))))
show(lux_car)
