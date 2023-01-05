from proxy_.before_proxy.test_data import EMPLOYEES, ACCESSCONTROL


def get_employees_info(empids, reqid):
    for empid in empids:
        if empid not in EMPLOYEES:
            continue
        employee = EMPLOYEES[empid]
        details = f'Employee id: {employee.empid}, name: {employee.name}'

        if reqid in ACCESSCONTROL:
            if ACCESSCONTROL[reqid].can_see_personal:
                details += f', birth date : {employee.birthdate}, salary: {employee.salary:.2f}'

        print(details)


get_employees_info([3, 4], 101)
