import pytest
import numpy as np
from assignment import perform_operations, check_even_odd, compare_numbers


def test1(capsys):
    greet()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
    
def test2():
    assert perform_operations(10, 2) == (12, 8, 20, 5)
    assert perform_operations(5, 5) == (10, 0, 25, 1)
    assert perform_operations(7, 3) == (10, 4, 21, 7/3)

@pytest.mark.parametrize("input, expected", [(2, "Even"), (3, "Odd"), (0, "Even"), (-5, "Odd")])
def test3(input, expected):
    assert check_even_odd(input) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 5),
    (2, 7, 7),
    (4, 4, "Equal")
])
def test4(num1, num2, expected):
    assert compare_numbers(num1, num2) == expected

@pytest.mark.parametrize("input, expected", [(253, 30), (123, 6), (999, 729), (321, 6)])
def test5(input, expected):
    assert check_even_odd(input) == expected
