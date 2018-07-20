"""
Is it a public holiday?
"""
from setuptools import find_packages, setup

dependencies = [
    'click==6.7',
    'holidays==0.9.5'
]

setup(
    name='publicholiday',
    version='0.1.0',
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
