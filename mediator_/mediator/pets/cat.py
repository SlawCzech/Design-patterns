from mediator_.mediator.pets.abs_pet import AbsPet

import random

class Cat(AbsPet):
    def wants_out(self):
        if self.mediator.is_fish_alive():
            print(f'let {self.name} in')
        else:
            print(f'let {self.name} out')

    def is_asleep(self):
        return random.randint(0, 1)

