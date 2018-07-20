# python-publicholiday
CLI tool to test if it is a public holiday or not.

After installing with `pip install publicholiday`, a command `publicholiday` will be available and can be used to add logic to running tasks on or on not public holidays.

Examples:
```
# Run a script on a public holiday
$ publicholiday && /thing/to/run.sh

# Don't run a thing on public holidays
$ publicholiday || /thing/to/run.sh
```
