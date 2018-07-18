# Needs to be renamed to rules

from types import SimpleNamespace
from datetime import datetime, timedelta

import pytest

from hauberk.filters import Subject, Age, Body, From


@pytest.fixture
def message():
    return SimpleNamespace(date=None, subject=None,
                           from_=list(), body=None)


# age
def test_age_old(message):
    message.date = datetime.now() - timedelta(days=100)
    _f = Age(days=7)
    assert _f(message)


def test_age_new(message):
    message.date = datetime.now()
    _f = Age(days=7)
    assert not _f(message)


@pytest.mark.parametrize('filter_,field', [
    (Subject, 'subject'),
    (Body, 'body')
])
def test_regex_match(filter_, field, message):
    _f = filter_(regex='match')
    setattr(message, field, 'matched')
    assert _f(message)


@pytest.mark.parametrize('filter_,field', [
    (Subject, 'subject'),
    (Body, 'body')
])
def test_regex_nomatch(filter_, field):
    _f = filter_(regex='match')
    setattr(message, field, 'different')
    assert not _f(message)


@pytest.mark.parametrize('filter_,field', [
    (Subject, 'subject'),
    (Body, 'body')
])
def test_regex_case_sensitive_match(filter_, field):
    _f = filter_(regex='match')
    setattr(message, field, 'MATCHED')
    assert _f(message)


@pytest.mark.parametrize('filter_,field', [
    (Subject, 'subject'),
    (Body, 'body')
])
def test_regex_case_sensitive_match_reverse(filter_, field):
    _f = filter_(regex='MATCH')
    setattr(message, field, 'matched')
    assert _f(message)


def test_from_match(message):
    _f = From(regex='match')
    message.from_ = ['matched']
    assert _f(message)


def test_from_no_match(message):
    _f = From(regex='match')
    message.from_ = ['matc']
    assert not _f(message)


def test_from_match_uppercase(message):
    _f = From(regex='MATCH')
    message.from_ = ['matched']
    assert _f(message)


def test_from_match_uppercase_inverted(message):
    _f = From(regex='match')
    message.from_ = ['MATCHED']
    assert _f(message)


def test_from_no_from(message):
    _f = From(regex='match')
    message.from_ = []
    assert not _f(message)
