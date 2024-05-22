import Lab2.bmi as bmi

def test_bmi_normal_weight():
   result = bmi.calculate_bmi(height=1.90, weight= 75)
   assert(result == 0)

def test_bmi_overweight():
    result = bmi.calculate_bmi(1.2, 90)
    assert(result == 1)
    
def test_bmi_under_weight():  
    result = bmi.calculate_bmi(1.9, 10)
    assert(result == -1)