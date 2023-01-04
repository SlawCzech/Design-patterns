from factory.full_factory.factories.loader import load_factory

for factory_name in 'chevy_factory', 'ford_factory', 'jeep_factory', 'tesla_factory':
    factory = load_factory(factory_name)
    car = factory.create_auto()
    car.start()
    car.stop()

