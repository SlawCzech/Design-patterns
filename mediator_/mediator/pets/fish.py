from mediator_.mediator.pets.abs_pet import AbsPet
import random


class Fish(AbsPet):
    def needs_food(self):
        print(f'feed {self.name}')

    def is_alive(self):
        return random.randint(0, 1)
