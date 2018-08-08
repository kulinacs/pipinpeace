"""
Code execution with a pip install
"""
from setuptools import setup
from command import install

setup(
    name='pipinpeace-command',
    packages=['command'],
    cmdclass={
        'install': install,
    },
)
