from facade.facade.get_employees import PROVIDER
from facade.facade.get_employees.facade_factory import FacadeFactory

facade = FacadeFactory.create_facade(PROVIDER)
facade.get_employees()

