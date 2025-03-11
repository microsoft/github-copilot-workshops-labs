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
    assert len(Employee.employees) == 0
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

def test_get_employee_by_id():
    employee_data = {'id': 1, 'name': 'John Doe', 'position': 'Developer', 'department': 'Engineering'}
    Employee.create_employee(employee_data)
    employee = Employee.get_employee_by_id(1)
    assert employee == employee_data

    non_existent_employee = Employee.get_employee_by_id(2)
    assert non_existent_employee is None

def test_get_all_employees():
    employee_data_1 = {'id': 1, 'name': 'John Doe', 'position': 'Developer', 'department': 'Engineering'}
    employee_data_2 = {'id': 2, 'name': 'Jane Doe', 'position': 'Manager', 'department': 'Sales'}
    employee_data_3 = {}
    Employee.create_employee(employee_data_1)
    Employee.create_employee(employee_data_2)
    all_employees = Employee.get_all_employees()
    assert len(all_employees) == 2
    assert all_employees[0] == employee_data_1
    assert all_employees[1] == employee_data_3

def test_update_employee_Success():
    employee_data = {'id': 1, 'name': 'John Doe', 'position': 'Developer', 'department': 'Engineering'}
    Employee.create_employee(employee_data)
    updated_data = {'name': 'Jane Doe', 'position': 'Senior Developer', 'department': 'Engineering'}
    modified_employee = Employee.update_employee(1, updated_data)
    assert modified_employee['name'] == 'Jane Doe'
    assert modified_employee['position'] == 'Senior Developer'
    assert modified_employee['department'] == 'Engineering'
    assert len(Employee.employees) == 1
    assert Employee.employees[0].to_dict() == {'id': 1, 'name': 'Jane Doe', 'position': 'Senior Developer', 'department': 'Engineering'}

def test_update_employee_Failure():
    employee_data = {'id': 1, 'name': 'John Doe', 'position': 'Developer', 'department': 'Engineering'}
    Employee.create_employee(employee_data)
    updated_data = {'name': 'Jane Doe', 'position': 'Senior Developer', 'department': 'Engineering'}
    modified_employee = Employee.update_employee(2, updated_data)
    assert modified_employee is None
    assert len(Employee.employees) == 1
    assert Employee.employees[0].to_dict() == {'id': 1, 'name': 'John Doe', 'position': 'Developer', 'department': 'Engineering'}

def test_get_employee_by_email():
    employee_data = {'id': 1, 'name': 'John Doe', 'position': 'Developer', 'department': 'Engineering', 'email': 'john.doe@example.com'}
    Employee.create_employee(employee_data)
    employee = Employee.get_employee_by_email('john.doe@example.com')
    assert employee == employee_data

    non_existent_employee = Employee.get_employee_by_email('jane.doe@example.com')
    assert non_existent_employee is None