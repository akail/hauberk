#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `hauberk` package."""

from types import SimpleNamespace
from unittest.mock import Mock

import pytest

import hauberk.core
from hauberk.core import Message, Hauberk
from hauberk.flags import FetchFlags


def test_creating_message():
    envelope = SimpleNamespace(date=None, subject=None,
                               from_=list(), sender=None,
                               reply_to=None, to=None,
                               cc=None, bcc=None, in_reply_to=None,
                               message_id=None)
    body = 'body'

    m = Message(envelope=envelope, body=body)
    assert m.body == body
    for key in envelope.__dict__.keys():
        assert getattr(envelope, key) == getattr(m, key)


def test_hauberk():
    h = Hauberk()
    assert not h.dry
    assert not len(h.rules)
    h = Hauberk(dry_run=True)
    assert h.dry


def test_login(monkeypatch):
    h = Hauberk()
    monkeypatch.setattr(hauberk.core, 'IMAPClient', Mock())
    h.login('testing', 'pass', 'myhost')
    h.client.login.assert_called_once_with('testing', 'pass')


def test_add_rule():
    h = Hauberk()
    h.add_rule(filters=[1], actions=[2])
    assert h.rules[0].filters[0] == 1
    assert h.rules[0].actions[0] == 2


def test_add_rule_no_filters():
    h = Hauberk()
    with pytest.raises(Exception):
        h.add_rule(filters=[], actions=[2])


def test_add_rule_no_actions():
    h = Hauberk()
    with pytest.raises(Exception):
        h.add_rule(filters=[1], actions=[])


def test_select_folder():
    h = Hauberk()
    h.client = Mock()
    h.select_folder("INBOX")
    h.client.select_folder.assert_called_once_with("INBOX")


@pytest.mark.skip("Not sure how to test yet")
def test_select_folder_bad_folder():
    pass


def test_existing_folders_list():
    h = Hauberk()
    h.client = Mock()
    h.existing_folders('other')
    h.client.folder_exists.assert_called_once_with('other')


def test_existing_folders_multiple():
    h = Hauberk()
    h.client = Mock()
    h.existing_folders(['other', 'another'])
    h.client.folder_exists.call_count == 2


def test_existing_folders_added():
    h = Hauberk()
    h.client = Mock()
    h.client.folder_exists.return_value = False
    h.existing_folders(['other', 'another'])
    h.client.create_folder.call_count == 2


def test_run():
    h = Hauberk()
    h.client = Mock()
    h.client.search.return_value = list(range(10))

    envelope = SimpleNamespace(date=None, subject=None,
                               from_=list(), sender=None,
                               reply_to=None, to=None,
                               cc=None, bcc=None, in_reply_to=None,
                               message_id=None)

    h.client.fetch.return_value = {1: {FetchFlags.BODY.value: 'testing',
                                       FetchFlags.ENVELOPE.value: envelope}}

    h.add_rule(filters=[lambda x: True], actions=[lambda x, y, z: True])

    h.run()
