from abc import ABC


class AbsPet(ABC):
    def __init__(self, name):
        self.name = name
        self.mediator = None


## mediator do psa i ryby