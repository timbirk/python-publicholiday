"""
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
"""
from setuptools import find_packages, setup

dependencies = [
    'click==6.7',
    'holidays==0.9.5'
]

setup(
    name='publicholiday',
    version='0.1.1',
    url='https://github.com/timbirk/python-publicholiday',
    license='BSD',
    author='Tim Birkett',
    author_email='tim.birkett@devopsmakers.com',
    description='Is it a public holiday?',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'publicholiday = publicholiday.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Topic :: Utilities',
        'Environment :: Console',
        #'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        #'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
