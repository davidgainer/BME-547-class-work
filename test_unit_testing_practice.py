#unit_testing_practice

def test_slope_calculation():
    from unit_testing_practice import slope_calculation
    answer = slope_calculation(1,1,2,2,4)
    assert answer == (1, 0)

def test_line_calculation():
    from unit_testing_practice import line_calculation
    answer = line_calculation(1,4,0)
    assert answer == 4
