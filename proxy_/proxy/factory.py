
from proxy_.proxy.employees import Employees
from proxy_.proxy.proxy import Proxy


def get_employees_collection(reqid):
    return Proxy(Employees(), reqid)
