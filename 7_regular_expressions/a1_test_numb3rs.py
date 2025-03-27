from a1_numb3rs import validate
import pytest

def test_1():
    assert validate("1.1.1.1") == True
    assert validate("127.0.0.1") == True

def test_2():
    assert validate("cat") == False

def test_3():
    assert validate("1.1") == False
    assert validate("512.512.512.512") == False