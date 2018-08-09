"""
Code execution with a pip install
"""
from setuptools import setup
from env import install

setup(
    name='pipinpeace-env',
    packages=['env'],
    cmdclass={
        'install': install,
    },
)
