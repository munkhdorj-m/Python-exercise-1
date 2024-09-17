import pytest
import numpy as np
from assignment import perform_operations, check_even_odd, compare_numbers

def test1():
    # Test for different pairs of numbers
    assert perform_operations(10, 2) == (12, 8, 20, 5)
    assert perform_operations(5, 5) == (10, 0, 25, 1)
    assert perform_operations(7, 3) == (10, 4, 21, 7/3)

@pytest.mark.parametrize("input, expected", [(2, "Even"), (3, "Odd"), (0, "Even"), (-5, "Odd")])
def test2(input, expected):
    # Test for even and odd numbers
    assert check_even_odd(input) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, "5 is greater than 3"),
    (2, 7, "7 is greater than 2"),
    (4, 4, "Both numbers are equal")
])
def test3(num1, num2, expected):
    # Test for comparing two numbers
    assert compare_numbers(num1, num2) == expected
