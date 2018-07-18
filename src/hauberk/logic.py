
import logging

logger = logging.getLogger(__name__)


class And():
    def __init__(self, *args):
        if len(args) < 2:
            raise Exception("Invalid number of arguments")
        self.filters = args

    def __call__(self, message):
        for f in self.filters:
            if not f(message):
                return False
        return True


class Or():
    def __init__(self, *args):
        if len(args) < 2:
            raise Exception("Invalid number of arguments")
        self.filters = args

    def __call__(self, message):
        for f in self.filters:
            if f(message):
                return True

        return False

# Not?
