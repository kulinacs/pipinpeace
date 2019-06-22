Automatic Backdoor
==================

A proof of concept at automatically backdooring Python code. In this example, a snippet is inserted into setup.py to cause code execution upon install. Functioning correctly, `/tmp/backdoor` will be created with the username of the executing user.

Usage
-----

Usage is simple, run `python3 auto.py <name_of_project_directory>`. It's not robust script yet, but it works with jinja2 and my test case at least.
