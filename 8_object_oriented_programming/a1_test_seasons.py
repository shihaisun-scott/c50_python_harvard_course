import pytest
from a1_seasons import date_minutes

def test_1():
    assert date_minutes("2024-03-28") == "Five hundred twenty-five thousand, six hundred minutes"

def test_2():
    assert date_minutes("2023-03-28") == "One million, fifty-two thousand, six hundred forty minutes"

def test_3():
    assert date_minutes("appa") == None
