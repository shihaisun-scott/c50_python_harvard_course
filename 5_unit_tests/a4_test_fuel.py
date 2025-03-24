import pytest
from a4_fuel import gauge, convert

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"

def test_convert():
    assert convert("1/1") == 100 
    assert convert("0/1") == 0
    assert convert("5/10") == 50  