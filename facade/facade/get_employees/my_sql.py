import pyodbc

from facade import CONNSTR, QUERY
from facade.facade.get_employees.abs_facade import AbsFacade


class GetEmployeesFacade(AbsFacade):
    def get_employees(self):
        connection = pyodbc.connect(CONNSTR)
        cursor = connection.cursor()
        cursor.execute(QUERY)
        for row in cursor:
            print(row.FirstName, row.LastName)
        connection.commit()
        connection.close()

