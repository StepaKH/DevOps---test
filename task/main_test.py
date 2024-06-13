import pytest
from main import add, subtraction, multiplication, division


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2


def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(-1, 1) == -2
    assert subtraction(0, 0) == 0
    assert subtraction(-1, -1) == 0


def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 1) == 0
    assert multiplication(-1, -1) == 1


def test_division():
    assert division(6, 3) == 2
    assert division(-1, 1) == -1
    assert division(1, -1) == -1
    assert division(-1, -1) == 1
    with pytest.raises(ZeroDivisionError):
        division(1, 0)


if __name__ == "__main__":
    pytest.main()
