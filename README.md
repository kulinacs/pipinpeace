pip in peace
============

> WARNING: Running pip install with root privileges is generally not a good idea. Try `pip install --user` instead.

Although it is generally known running `pip` as root is bad practice, often people still do it. With `pip` hash checking feeling like an after thought and signed packages not supported, arbitrary code execution can be a real concern.

While this is nothing new, this project attempts ease the creation of backdoored Python packages and strengthen exploitation opportunities for testers able to run `pip` with administrative privileges.

Disclaimer
----------

This is designed to better survey Python supply chain management and its downfalls. This should not be used for unauthorized activity.
