import pytest
from app.models.employee import Employee

# filepath: c:\Users\heblasco\VScode\copilotdemo\github-copilot-workshops-labs\troubleshootinganddoc\python\employee-management\app\models\test_employee.py

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup: Clear the employees list before each test
    Employee.employees = []
    yield
    # Teardown: Clear the employees list after each test
    Employee.employees = []

def test_create_employee():
    employee_data = {'id': 1, 'name': 'John Doe', 'position': 'Developer', 'department': 'Engineering'}
    created_employee = Employee.create_employee(employee_data)
    assert created_employee == employee_data
    assert len(Employee.employees) == 1
    assert Employee.employees[0].to_dict() == employee_data

def test_remove_employee():
    employee_data = {'id': 1, 'name': 'John Doe', 'position': 'Developer', 'department': 'Engineering'}
    Employee.create_employee(employee_data)
    Employee.remove_employee(1)
    assert len(Employee.employees) == 0

def test_modify_employee():
    employee_data = {'id': 1, 'name': 'John Doe', 'position': 'Developer', 'department': 'Engineering'}
    Employee.create_employee(employee_data)
    updated_data = {'name': 'Jane Doe', 'position': 'Senior Developer', 'department': 'Engineering'}
    modified_employee = Employee.modify_employee(1, updated_data)
    assert modified_employee['name'] == 'Jane Doe'
    assert modified_employee['position'] == 'Senior Developer'
    assert modified_employee['department'] == 'Engineering'
    assert len(Employee.employees) == 1
    assert Employee.employees[0].to_dict() == {'id': 1, 'name': 'Jane Doe', 'position': 'Senior Developer', 'department': 'Engineering'}