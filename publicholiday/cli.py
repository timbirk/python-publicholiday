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

    country_methods = holidays.__dict__.keys()
    country_name = next((x for x in country_methods if
                         country.lower() == x.lower()), '')

    try:
        country_holidays = getattr(holidays, country_name)
        try:
            isinstance(country_holidays(), holidays.HolidayBase)
        except TypeError:
            raise AttributeError

    except AttributeError:
        logging.error("Country: %s not found." % country)
        sys.exit(127)

    sys.exit(date.today() not in country_holidays())
