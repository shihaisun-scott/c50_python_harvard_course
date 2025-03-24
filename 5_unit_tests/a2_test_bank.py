from a2_bank import value
import pytest

def test_value_1():
    assert value("hello") == "$0"
    assert value("Hello") == "$0"

def test_value_2():
    assert value("Hi") == "$20"

def test_value_3():
    assert value("Whatsup") == "$100"