# python-isholiday
CLI tool to test if it is a public holiday or not.

After installing with `pip install isholiday`, a command `isholiday` will be available and can be used to add logic to running tasks on or on not public holidays.

Examples:
```
# Run a script on a public holiday
$ isholiday && /thing/to/run.sh

# Don't run a thing on public holidays
$ isholiday || /thing/to/run.sh
```
