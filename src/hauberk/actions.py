# -*- coding: utf-8 -*-  # noqa: D400
"""
hauberk.actions
~~~~~~~~~~~~~~~

Actions are triggered after a series of rules have been met.

"""

import logging

from hauberk.flags import ImapFlags

logger = logging.getLogger(__name__)


class Read():
    """Read message action.

    This action marks a message as read.
    """

    def __call__(self, client, msgid, dry):
        """Add SEEN flag to message.

        :param client: ImapClient
        :param msgid: Message Id
        :param dry: Dry run. If true don't commit change
        """
        logger.info("Marking message %s as read", msgid)
        if not dry:
            client.add_flags(msgid, [ImapFlags.SEEN.value])

    def __repr__(self):  # pragma: no cover # noqa: D401, D105
        """String representation."""
        return "{}".format(self.__class__.__name__)


class Move():
    """Move message to a new folder.


    :param folder: Folder to move message to
    """

    def __init__(self, folder):
        self.folder = folder

    def __call__(self, client, msgid, dry):
        """Move message from inbox to folder.

        :param client: ImapClient
        :param msgid: Message Id
        :param dry: Dry run. If true don't commit change
        """
        logger.info("Moving message %s to folder %s", msgid, self.folder)
        if not dry:
            client.move(msgid, self.folder)

    def __repr__(self):   # pragma: no cover # noqa: D401, D105
        return "{}: Folder={}".format(self.__class__.__name__, self.folder)


class Delete():
    """Delete message.

    This action marks a message as read.
    """

    def __call__(self, client, msgid, dry):
        """Delete message.

        :param client: ImapClient
        :param msgid: Message Id
        :param dry: Dry run. If true don't commit change
        """
        logger.info("Deleting message %s", msgid)
        if not dry:
            client.delete_messages(msgid)

    def __repr__(self):   # pragma: no cover # noqa: D401, D105
        return "{}".format(self.__class__.__name__)


class Archive():
    """Archive message."""

    pass


class Respond():
    """Auto respond."""

    pass


class Notify():
    """Notify through external means.

    This is just a placeholder right now
    """
    # def __init__(self, notifiers):



    def __call__(self, client, msgid, dry):
        """Notify via a log message.

        :param client: ImapClient
        :param msgid: Message Id
        :param dry: Dry run. If true don't commit change
        """
        logger.info("Sending text for message %s", msgid)

    def __repr__(self):   # pragma: no cover # noqa: D401, D105
        return "{}".format(self.__class__.__name__)


class Trash():
    """Mark item as read and move to trash.

    This combines the actions for Read and Move('Trash')
    """

    def __call__(self, client, msgid, dry):
        """Call read and move

        :param client: ImapClient
        :param msgid: Message Id
        :param dry: Dry run. If true don't commit change
        """
        logger.info("Marking message %s as read", msgid)
        Read()(client, msgid, dry)
        Move('Trash')(client, msgid, dry)


    def __repr__(self):  # pragma: no cover # noqa: D401, D105
        """String representation."""
        return "{}".format(self.__class__.__name__)


