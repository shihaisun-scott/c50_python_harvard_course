# testing the calculator script
# use assert instead of ifs
# use pytest test_calculator.py
from calculator import square
import pytest

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

# separate into pos, neg and zero to get more information from the test
def test_square_pos():
    assert square(2) == 4
    assert square(3) == 9


def test_square_neg():
    assert square(-2) == 4
    assert square(-3) == 9

def test_square_zero():
    assert square(0) == 0

def test_square_str():
    with pytest.raises(TypeError):
        square("cat")
        

if __name__ == "__main__":
    main()