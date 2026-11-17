# Import the function
from employee import employee_details


# Test employee details function
def test_employee_details():

    result = employee_details("Keerti", 150, "IT", 30000)

    expected = (
        "Employee Name: Keerti\n"
        "Employee ID: 150\n"
        "Department: IT\n"
        "Salary: 30000"
    )

    assert result == expected