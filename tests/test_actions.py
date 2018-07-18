from unittest.mock import Mock

import pytest
# from imapclient.testable_imapclient import TestableIMAPClient as IMAPClient

from hauberk.actions import Read, Move, Delete, Archive, Respond, Notify
from hauberk.flags import ImapFlags


@pytest.fixture
def client():
    return Mock()


actions = [Read, Move, Delete, Archive, Respond, Notify]


@pytest.mark.parametrize('action', actions)
def test_all_bad_msgid(action, client):
    pass


@pytest.mark.parametrize('action', actions)
def test_all_server_error(action, client):
    pass


# Read
def test_read_init(client):
    Read()


def test_read(client):
    r = Read()
    r(client, 1, False)
    client.add_flags.assert_called_once_with(1, [ImapFlags.SEEN.value])


def test_read_dry_run(client):
    r = Read()
    r(client, 1, True)
    client.add_flags.assert_not_called()


# Move
def test_move_init(client):
    Move(folder='other')


def test_move(client):
    m = Move(folder='other')
    m(client, 1, False)
    client.move.assert_called_once_with(1, 'other')


def test_move_dry_run(client):
    m = Move(folder='other')
    m(client, 1, True)
    client.move.assert_not_called()


# Delete
def test_delete_init(client):
    Delete()


def test_delete(client):
    d = Delete()
    d(client, 1, False)
    client.delete_messages.assert_called_once_with(1)


def test_delete_dry_run(client):
    d = Delete()
    d(client, 1, True)
    client.delete_messages.assert_not_called()


# Notify
def test_notify_init(client):
    Notify()


def test_notify(client):
    n = Notify()
    n(client, 1, False)


def test_notify_dry_run(client):
    n = Notify()
    n(client, 1, True)


# Archive
def test_archive_init():
    Archive()


def test_archive():
    a = Archive()


def test_archive_dry_run():
    a = Archive()


# Respond
def test_respond_init():
    Respond()


def test_respond():
    r = Respond()


def test_respond_dry_run():
    r = Respond()
