from unittest.mock import Mock

import pytest

from hauberk.logic import And, Or


@pytest.fixture
def client():
    return Mock()


def test_and_exception():
    with pytest.raises(Exception):
        And(2)


def test_and_2_true(message):
    a = And(lambda x: True, lambda x: True)
    assert a(message)


def test_and_3_true(message):
    a = And(lambda x: True, lambda x: True, lambda x: True)
    assert a(message)


def test_and_false_left(message):
    a = And(lambda x: False, lambda x: True)
    assert not a(message)


def test_and_false_right(message):
    a = And(lambda x: True, lambda x: False)
    assert not a(message)


def test_and_false_both(message):
    a = And(lambda x: False, lambda x: False)
    assert not a(message)


def test_or_exception():
    with pytest.raises(Exception):
        Or(2)


def test_or_2_true(message):
    a = Or(lambda x: True, lambda x: True)
    assert a(message)


def test_or_3_true(message):
    a = Or(lambda x: True, lambda x: True, lambda x: True)
    assert a(message)


def test_or_true_left(message):
    a = Or(lambda x: False, lambda x: True)
    assert a(message)


def test_or_true_right(message):
    a = Or(lambda x: True, lambda x: False)
    assert a(message)


def test_or_false_2(message):
    a = Or(lambda x: False, lambda x: False)
    assert not a(message)


def test_or_false_3(message):
    a = Or(lambda x: False, lambda x: False, lambda x: False)
    assert not a(message)
