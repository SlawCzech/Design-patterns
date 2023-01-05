from proxy_.proxy.factory import get_employees_collection


def print_employee_details(empids, reqid):
    employees = get_employees_collection(reqid)
    for employee in employees.get_employee_info(empids):
        print(employee.empid, employee.name, employee.birthdate, employee.salary)


print_employee_details([1, 2, 3], 101)
