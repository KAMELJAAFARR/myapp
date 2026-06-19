from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Employee:
    employee_id: int
    name: str
    department: str
    email: str
    salary: float


class EmployeeManagementSystem:
    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> bool:
        if employee.employee_id <= 0:
            raise ValueError("Employee ID must be positive")

        if "@" not in employee.email:
            raise ValueError("Invalid email address")

        if employee.salary <= 0:
            raise ValueError("Salary must be positive")

        if self.get_employee_by_id(employee.employee_id):
            return False

        self.employees.append(employee)
        return True

    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def get_employees_by_department(self, department: str) -> List[Employee]:
        return [
            employee for employee in self.employees
            if employee.department.lower() == department.lower()
        ]

    def calculate_average_salary(self) -> float:
        if not self.employees:
            return 0.0

        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary / len(self.employees)

    def total_employees(self) -> int:
        return len(self.employees)


def seed_data(system: EmployeeManagementSystem):
    system.add_employee(Employee(1, "Kamel Jaafar", "DevOps", "kamel@example.com", 1200))
    system.add_employee(Employee(2, "Ahmad Ali", "IT", "ahmad@example.com", 1000))
    system.add_employee(Employee(3, "Daisy Jabbour", "HR", "daisy@example.com", 900))
    system.add_employee(Employee(4, "Riyad Murad", "IT", "riyad@example.com", 1100))


if __name__ == "__main__":
    system = EmployeeManagementSystem()
    seed_data(system)

    print("Employee Management System")
    print("--------------------------")
    print(f"Total Employees: {system.total_employees()}")
    print(f"Average Salary: ${system.calculate_average_salary():.2f}")

    print("\nIT Employees:")
    for employee in system.get_employees_by_department("IT"):
        print(f"- {employee.name} ({employee.email})")
