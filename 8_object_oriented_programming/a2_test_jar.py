from a2_jar import Jar
import pytest

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪"
    

def test_init_negative():
    try:
        jar = Jar(-1)
        assert False  # ❌ If no error, test should fail
    except ValueError as e:
        assert str(e) == "Negative number"

def test_deposit_too_many():
    jar = Jar(3)
    try:
        jar.deposit(4)
        assert False
    except ValueError as e:
        assert str(e) == "Too many cookies"

def test_withdraw_too_many():
    jar = Jar(3)
    jar.deposit(2)
    try:
        jar.withdraw(3)
        assert False
    except ValueError as e:
        assert str(e) == "Too few cookies"