# -*- coding: utf-8 -*-

import logging

from hauberk.flags import ImapFlags

logger = logging.getLogger(__name__)


class Read():
    def __call__(self, client, msgid, dry):
        logger.info("Marking message %s as read", msgid)
        if not dry:
            client.add_flags(msgid, [ImapFlags.SEEN.value])

    def __repr__(self):  # pragma: no cover
        return "{}".format(self.__class__.__name__)


class Move():
    def __init__(self, folder):
        self.folder = folder

    def __call__(self, client, msgid, dry):
        logger.info("Moving message %s to folder %s", msgid, self.folder)
        if not dry:
            client.move(msgid, self.folder)

    def __repr__(self):   # pragma: no cover
        return "{}: Folder={}".format(self.__class__.__name__, self.folder)


class Delete():
    def __call__(self, client, msgid, dry):
        logger.info("Deleting message %s", msgid)
        if not dry:
            client.delete_messages(msgid)

    def __repr__(self):   # pragma: no cover
        return "{}".format(self.__class__.__name__)


class Archive():
    pass


class Respond():
    pass


class Notify():
    def __call__(self, client, msgid, dry):
        logger.info("Sending text for message %s", msgid)

    def __repr__(self):   # pragma: no cover
        return "{}".format(self.__class__.__name__)
