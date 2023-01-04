

from adapter.object_adapter.mock_customers import MOCKCUSTOMERS
from adapter.object_adapter.mock_vendors import MOCKVENDORS

all_ = MOCKCUSTOMERS + MOCKVENDORS

def main():
    for pers in all_:
        print('Name: %s; Address: %s' %
              (pers.name, pers.address))

if __name__ == '__main__':
    main()