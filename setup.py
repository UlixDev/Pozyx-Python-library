# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='pypozyx',
    packages=['pypozyx', 'pypozyx.definitions',
              'pypozyx.structures', 'pypozyx.tests'],
    version='0.1.0',
    description='Python library for Pozyx',
    author='Laurent Van Acker',
    author_email='laurent@pozyx.io',
    url='www.pozyx.io',
    download_url='www.pozyx.io',
    keywords=['pozyx', 'serial', 'positioning', 'localisation'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended audience :: End Users/Developers',
        'Operating System :: OS independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Positioning :: Pozyx',
    ],
    long_description="""\
    Pozyx Python library, used to interface with the Pozyx without need of an arduino.
    Currently supports USB (serial), planned I2C support.

    This version requires Python 3 or later. A Python 2 version is available separately.
    """
)
