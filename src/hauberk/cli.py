# -*- coding: utf-8 -*-

"""Console script for hauberk."""
import logging
import sys

import click
import yaml

from hauberk.log import setup_logger

logger = logging.getLogger(__name__)


@click.command()
@click.argument('input', type=click.File('rb'))
@click.option('--dry', is_flag=True, help="Dry run of rules")
@click.option('--format', help="Input file format")
@click.option('--log-level', help="Log level", default="INFO")
def main(input, dry, format, log_level):
    """Console script for hauberk."""

    setup_logger(
        log_level=log_level
    )

    # data = yaml.load(input)
    yaml.load(input)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
