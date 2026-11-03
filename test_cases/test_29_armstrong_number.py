import importlib

module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong


def test_armstrong_153():
    assert is_armstrong(153) == True


def test_not_armstrong_123():
    assert is_armstrong(123) == False


def test_single_digit_number():
    assert is_armstrong(7) == True


def test_zero():
    assert is_armstrong(0) == True


def test_negative_number():
    assert is_armstrong(-153) == False


def test_four_digit_armstrong():
    assert is_armstrong(9474) == True


def test_two_digit_number():
    assert is_armstrong(10) == False