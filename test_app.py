import pytest
from app import Employee, EmployeeManagementSystem, seed_data


def test_add_employee_successfully():
    system = EmployeeManagementSystem()
    employee = Employee(1, "Kamel Jaafar", "DevOps", "kamel@example.com", 1200)

    result = system.add_employee(employee)

    assert result is True
    assert system.total_employees() == 1


def test_duplicate_employee_not_added():
    system = EmployeeManagementSystem()
    employee = Employee(1, "Kamel Jaafar", "DevOps", "kamel@example.com", 1200)

    system.add_employee(employee)
    result = system.add_employee(employee)

    assert result is False


def test_invalid_email_raises_error():
    system = EmployeeManagementSystem()
    employee = Employee(2, "Ahmad Ali", "IT", "ahmadexample.com", 1000)

    with pytest.raises(ValueError):
        system.add_employee(employee)


def test_filter_employees_by_department():
    system = EmployeeManagementSystem()
    seed_data(system)

    it_employees = system.get_employees_by_department("IT")

    assert len(it_employees) == 2


def test_average_salary():
    system = EmployeeManagementSystem()
    seed_data(system)

    assert system.calculate_average_salary() == 1050
