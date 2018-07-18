
from datetime import datetime, timedelta
import logging
import re

logger = logging.getLogger(__name__)


class Age():
    def __init__(self, days):
        self.days = days

    def __call__(self, message):

        expire_date = message.date + timedelta(days=self.days)
        now = datetime.now()

        if expire_date < now:
            return True

        return False

    def __repr__(self):  # pragma: no cover
        return "{}: Days={}".format(self.__class__.__name__, self.days)


class Subject():
    def __init__(self, regex):
        self.regex = regex
        self.compiled = re.compile(regex, flags=re.IGNORECASE)

    def __call__(self, message):
        if self.compiled.search(message.subject):
            return True
        return False

    def __repr__(self):  # pragma: no cover
        return "{}: Regex={}".format(self.__class__.__name__, self.regex)


class Body():
    def __init__(self, regex):
        self.regex = regex
        self.compiled = re.compile(regex, flags=re.IGNORECASE)

    def __call__(self, message):
        if self.compiled.search(message.body):
            return True
        return False

    def __repr__(self):  # pragma: no cover
        return "{}: Regex={}".format(self.__class__.__name__, self.regex)


class From():
    def __init__(self, regex):
        self.regex = regex
        self.compiled = re.compile(regex, flags=re.IGNORECASE)

    def __call__(self, message):
        for address in message.from_:
            email = str(address)
            if self.compiled.search(email):
                return True
        return False

    def __repr__(self):  # pragma: no cover
        return "{}: Regex={}".format(self.__class__.__name__, self.regex)
