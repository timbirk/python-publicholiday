import sys
import holidays
import click
import logging

from datetime import date


@click.command()
@click.option('--country', '-c', default='UK',
              help='Country you are running in.')
def main(country):
    """Is it a public holiday?"""

    logging.basicConfig(format='[%(levelname)s] %(message)s')
    try:
        my_holidays = getattr(holidays, country)
    except AttributeError:
        logging.error("Country: %s not found." % country)
        sys.exit(127)

    sys.exit(date.today() not in my_holidays())
