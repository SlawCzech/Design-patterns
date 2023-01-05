import time
from random import random, randint

from mediator_.mediator.pet_mediator import PetMediator
from mediator_.mediator.pets.cat import Cat
from mediator_.mediator.pets.dog import Dog
from mediator_.mediator.pets.fish import Fish


def main():
    cat = Cat('Alik')
    dog = Dog('Tofik')
    fish = Fish('Nemo')

    pm = PetMediator(cat, dog, fish)

    cat.mediator = pm
    dog.mediator = pm
    fish.mediator = pm

    time.sleep(random())
    option = randint(-1, 1)

    pm.time_of_day(option)



main()
