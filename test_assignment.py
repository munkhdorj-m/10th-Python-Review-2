import pytest
from assignment import even_numbers, reverse_number, sum_to_n, is_prime, perfect_squares


@pytest.mark.parametrize("expected", [
    (list(range(2, 51, 2)))   # 2, 4, ..., 50
])
def test1(expected):
    assert even_numbers() == expected


@pytest.mark.parametrize("num, expected", [
    (1234, 4321),
    (907, 709),
    (5, 5),
    (1000, 1),
    (456789, 987654)
])
def test2(num, expected):
    assert reverse_number(num) == expected


@pytest.mark.parametrize("num, expected", [
    (5, 15),    # 1+2+3+4+5
    (10, 55),   # 1+...+10
    (1, 1),     
    (0, 0),     
    (7, 28)     # 1+...+7
])
def test3(num, expected):
    assert sum_to_n(num) == expected


@pytest.mark.parametrize("num, expected", [
    (7, True),    # prime
    (12, False),  # not prime
    (1, False),   # 1 is not prime
    (2, True),    # prime
    (19, True),   # prime
    (20, False)   # not prime
])
def test4(num, expected):
    assert is_prime(num) == expected


@pytest.mark.parametrize("expected", [
    ([i*i for i in range(1, 23)])   # 22^2 = 484, last before 500
])
def test5(expected):
    assert perfect_squares() == expected
