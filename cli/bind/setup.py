"""
Bind shell with a pip install
"""
from setuptools import setup
from bind import install

setup(
    name='pipinpeace-bind',
    packages=['bind'],
    cmdclass={
        'install': install,
    },
)
