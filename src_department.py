
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        if not self.employees:
            print(f"The {self.department_name} department is empty.")
        else:
            print(f"Employees in {self.department_name} Department:")
            for employee in self.employees:
                print(employee)
