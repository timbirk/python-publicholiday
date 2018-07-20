import sys
import holidays
import click
import logging

from datetime import date


@click.command()
@click.option('--country', '-c', default='UK',
              help='Supported country name or code.')
def main(country):
    """Is it a public holiday?"""

    logging.basicConfig(format='[%(levelname)s] %(message)s')
    try:
        my_holidays = getattr(holidays, country)
    except AttributeError:
        try:
            # Account for full country names entered in lowercase
            my_holidays = getattr(holidays, country.title())
        except AttributeError:
            try:
                # Account for country code entered lowercase
                my_holidays = getattr(holidays, country.upper())
            except AttributeError:
                logging.error("Country: %s not found." % country)
                sys.exit(127)

    sys.exit(date.today() not in my_holidays())
