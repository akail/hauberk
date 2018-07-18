import logging

import colorlog


def setup_logger(logger=None, log_level='INFO'):
    if not logger:
        logger = logging.getLogger()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(name)s:%(message)s'))

    logger.addHandler(handler)

    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % log_level)
    logger.setLevel(numeric_level)
