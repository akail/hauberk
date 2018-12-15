# -*- coding: utf-8 -*-

"""Main module."""

import logging
from collections import namedtuple

from imapclient import IMAPClient

from hauberk.flags import FetchFlags

logger = logging.getLogger(__name__)

Rule = namedtuple('Rule', ['filters', 'actions'])


class Message():
    def __init__(self, envelope, body):
        self.envelope = envelope
        self.body = body

        self.date = envelope.date
        self.subject = envelope.subject
        self.from_ = envelope.from_
        self.sender = envelope.sender
        self.reply_to = envelope.reply_to
        self.to = envelope.to
        self.cc = envelope.cc
        self.bcc = envelope.bcc
        self.in_reply_to = envelope.in_reply_to
        self.message_id = envelope.message_id


class Hauberk():
    def __init__(self, dry_run=False):

        self.rules = list()
        self.dry = dry_run

    def login(self, username, password, server):
        logger.info("Connecting to Server")
        self.client = IMAPClient(server, use_uid=True)
        self.client.login(username, password)
        logger.info("Connected")

    def add_rule(self, filters, actions):
        self.rules.append(Rule(filters=filters, actions=actions))
        if not filters:
            raise Exception("Must define filters in rule")
        if not actions:
            raise Exception("Must define actions in rule")
        logger.info("Added rule number %s", len(self.rules))

    def run(self):
        messages = self.client.search()
        logger.info("%s messages to process", len(messages))
        for msgid, data in self.client.fetch(messages, [FetchFlags.ENVELOPE.value,
                                                        FetchFlags.BODY.value]).items():
            envelope = data[FetchFlags.ENVELOPE.value]
            body = data[FetchFlags.BODY.value]
            message = Message(envelope, body)
            logger.debug("Processing message %s: %s", msgid, message.subject)
            done = False
            for rule in self.rules:
                for _filter in rule.filters:
                    logger.debug("Running filter %s", _filter)
                    if _filter(message):
                        logger.debug("Match found!")
                        # log here that there was a match
                        for action in rule.actions:
                            logger.debug("Running action %s", action)
                            action(self.client, msgid, self.dry)
                        done = True
                        break
                if done:
                    break

    def select_folder(self, folder):
        """Select working folder.

        :param folder: Folder rules should be applied to
        """
        logger.info("Running in folder %s", folder)
        self.client.select_folder(folder)

    def existing_folders(self, folders):
        """Make sure certain folders exist client side.

        :param folders: List of folder names
        """
        logger.info("Checking for existing folders")

        if not isinstance(folders, list):
            folders = [folders]

        for folder in folders:
            logger.debug("Checking for existance of folder %s" % folder)
            if not self.client.folder_exists(folder):
                logger.warning("Folder %s does not exist, creating" % folder)
                if not self.dry:
                    self.client.create_folder(folder)
