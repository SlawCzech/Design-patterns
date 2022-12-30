from factory.before_factory.ChevyVolt import ChevyVolt
from factory.before_factory.FordFusion import FordFusion
from factory.before_factory.JeepSahara import JeepSahara
from factory.before_factory.NullCar import NullCar


def getcar(carname):
    if carname == 'Chevy':
        return ChevyVolt()
    elif carname == 'Ford':
        return FordFusion()
    elif carname == 'Jeep':
        return JeepSahara()
    else:
        return NullCar(carname)

for carname in 'Chevy', 'Ford', 'Jeep', 'Tesla':
    car = getcar(carname)
    car.start()
    car.stop()

