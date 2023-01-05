import time
from random import random, randint

from mediator_.before_mediator.pets import Cat, Dog, Fish
from mediator_.before_mediator.times import morning, noon, night


def main():
    cat = Cat('Alik')
    dog = Dog('Tofik')
    fish = Fish('Nemo')

    cat.fish = fish
    dog.cat = cat

    time.sleep(random())
    option = randint(-1, 1)
    if option < 0:
        morning(cat, dog, fish)
    elif option == 0:
        noon(cat, dog, fish)
    elif option > 0:
        night(cat, dog, fish)

main()