from types import SimpleNamespace

import pytest


@pytest.fixture
def message():
    return SimpleNamespace(date=None, subject=None,
                           from_=list(), sender=None,
                           reply_to=None, to=None,
                           cc=None, bcc=None, in_reply_to=None,
                           message_id=None, body=None)
