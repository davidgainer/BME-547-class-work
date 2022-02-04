#test_blood_calculator.py
import pytest
def test_check_HDL():
    from blood_calculator import check_HDL
    answer = check_HDL(70)
    assert answer == "Normal"
    

def test_check_HDL1():
    from blood_calculator import check_HDL
    answer = check_HDL(45)
    assert answer == "Borderline Low"


def test_check_HDL2():
    from blood_calculator import check_HDL
    answer = check_HDL(35)
    assert answer == "Low"


#Note that you can run all test in one function but it is not standard because it doesnt give info for failures
#The below way is the correct way to run multiple tests within one function 
@pytest.mark.parametrize("input_HDL, expected", [
    [70,"Normal"],
    [45, "Borderline Low"],
    [20, "Low"]
])
def test_check_HDL(input_HDL, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_HDL)
    assert answer == expected