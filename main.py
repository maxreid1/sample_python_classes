
from src.employee import Employee
from src.department import Department

def main():
    # Create instances of Employee
    employee1 = Employee("Alice Johnson", "E001", "Software Engineer")
    employee2 = Employee("Bob Smith", "E002", "Product Manager")

    # Create a Department instance
    tech_department = Department("Technology")

    # Add employees to the department
    tech_department.add_employee(employee1)
    tech_department.add_employee(employee2)

    # Display the employees in the department
    tech_department.display_employees()

if __name__ == "__main__":
    main()
