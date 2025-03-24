from a3_plate import is_valid
import pytest

# 1: start with two letters
# 2: 2-6 chars
# 3: first number cannot be 0
# 4: numbers must be at the end
# 5: no periods, spaces or punct


def test_isvalid_1():
    assert is_valid("APPa") == True
    assert is_valid("A123") == False

def test_isvalid_2():
    assert is_valid("A") == False

def test_isvalid_3():
    assert is_valid("APPA0") == False

def test_isvalid_4():
    assert is_valid("AP3PA") == False

    
def test_isvalid_5():
    assert is_valid("APPa!") == False
    