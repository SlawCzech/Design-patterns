from decorator.subclasses.economy_4cyl_white_vinyl import Economy4CylWhiteVinyl
from decorator.subclasses.economy_6cyl_white_vinyl import Economy6CylWhiteVinyl


def main():
    car1 = Economy4CylWhiteVinyl()
    car2 = Economy6CylWhiteVinyl()

    print(car1.description, car1.cost)
    print(car2.description, car2.cost)


if __name__ == '__main__':
    main()
