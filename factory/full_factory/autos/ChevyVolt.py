from factory.full_factory.autos.abs_auto import AbsAuto


class ChevyVolt(AbsAuto):
    def start(self):
        print(f'{self.name} running with shocking power!')

    def stop(self):
        print(f'{self.name} shutting down.')