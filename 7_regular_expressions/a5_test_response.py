import pytest

from a5_response import valid_email

def test_1():
    assert valid_email("malan@harvard.edu") == "Valid"

def test_1():
    assert valid_email("shsun@mgh.harvard.edu") == "Valid"

def test_1():
    assert valid_email("malan@@@harvard.edu") == "Invalid"

def test_1():
    assert valid_email("appas@a@big@dumdum@harvard.edu") == "Invalid"
