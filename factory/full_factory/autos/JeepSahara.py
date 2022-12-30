from factory.full_factory.autos.abs_auto import AbsAuto


class JeepSahara(AbsAuto):
    def start(self):
        print(f'{self.name} running ruggedly.')

    def stop(self):
        print(f'{self.name} shutting down.')