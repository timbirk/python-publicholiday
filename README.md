# python-publicholiday [![Build Status](https://travis-ci.org/timbirk/python-publicholiday.svg?branch=master)](https://travis-ci.org/timbirk/python-publicholiday)
A cli utility to help run things or not run things based on if it is a public
holiday. The command exits 0 if today is a public holiday and exits 1 if not.

Installation: `pip install publicholiday`

Examples usage:
```
$ publicholiday --help
Usage: publicholiday [OPTIONS]

  Is it a public holiday?

Options:
  -c, --country TEXT  Supported country name or code.
  --help              Show this message and exit.

# Run a script on a public holiday
$ publicholiday && /thing/to/run.sh

# Don't run a thing on public holidays
$ publicholiday || /thing/to/run.sh
```

By default `publicholiday` will check against UK public holidays. You can change
this by passing a supported country:
```
# Run a script on a Argentinian public holiday
$ publicholiday -c Argentina && /thing/to/run.sh

# Don't run a thing on US public holidays
$ publicholiday -c US || /thing/to/run.sh
```

This utility uses the `holidays` pip package, to find out if your country is
supported see: https://pypi.org/project/holidays/
