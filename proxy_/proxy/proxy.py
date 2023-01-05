from proxy_.proxy.abs_employees import AbsEmployees
from proxy_.proxy.access_controls import AccessControls
from proxy_.proxy.employee import Employee


class Proxy(AbsEmployees):

    def __init__(self, employees, reqid):
        self._employees = employees
        self._reqid = reqid

    def get_employee_info(self, empids):
        acc = AccessControls.get_access_control()
        for employee in self._employees.get_employee_info(empids):
            if employee.empid == self._reqid or (self._reqid in acc and acc[self._reqid].can_see_personal):
                yield Employee(employee.empid, employee.name, employee.birthdate, f'{employee.salary:.2f}')
            else:
                yield Employee(employee.empid, employee.name, '*****', '***')
