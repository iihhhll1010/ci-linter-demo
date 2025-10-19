from calculator import add
from calculator import subtract


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 0) == 0


def test_subtract_positive():
    assert subtract(5, 3) == 2