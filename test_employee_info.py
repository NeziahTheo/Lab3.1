import employee_info as info

def test_get_employees_by_age_range():
    result = info.get_employees_by_age_range(20,24)
    assert (result == [
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ])
def test_calulate_average_salary():
    assert (361000/6 == info.calculate_average_salary())
def test_get_employees_by_dept():
    result = info.get_employees_by_dept('Engineering')
    assert (result == [
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ])