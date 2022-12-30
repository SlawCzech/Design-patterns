from factory.full_factory.autos.abs_auto import AbsAuto


class FordFusion(AbsAuto):
    def start(self):
        print(f'Cool {self.name} running smoothly.')

    def stop(self):
        print(f'{self.name} shutting down.')