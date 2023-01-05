from mediator_.mediator.pets.abs_pet import AbsPet


class Dog(AbsPet):
    def wants_walk(self):
        if self.mediator.is_cat_asleep():
            print(f'walk {self.name}')

