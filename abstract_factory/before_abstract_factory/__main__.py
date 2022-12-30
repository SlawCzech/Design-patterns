from random import randint

from abstract_factory.before_abstract_factory.ford import FordFiesta, FordMustang, LincolnMKS
from abstract_factory.before_abstract_factory.gm import ChevySpark, ChevyCamaro, CadillacCTS

makers = ('gm', 'ford')
editions = ('Economy', 'Sport', 'Luxury')
maker = makers[randint(0, 1)]
edition = editions[randint(0, 2)]

if maker == 'gm':
    if edition == 'Economy':
        car = ChevySpark()
    elif edition == 'Sport':
        car = ChevyCamaro()
    elif edition == 'Luxury':
        car = CadillacCTS()
    else:
        raise ValueError("Unknown car")
elif maker == 'ford':
    if edition == 'Economy':
        car = FordFiesta()
    elif edition == 'Sport':
        car = FordMustang()
    elif edition == 'Luxury':
        car = LincolnMKS()
    else:
        raise ValueError("Unknown car.")
else:
    raise ValueError("Unknown maker.")

car.start()
car.stop()