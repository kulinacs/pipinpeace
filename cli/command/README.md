pip in peace - command
======================

The command package allows arbitrary command execution as the user running the install with the `--command` flag.

setup.py
--------

```
    python3 setup.py install --command=whoami
```

pip
---

For pip, the standard out of the command module is not printed. If you want to view the output, you'll need to redirect to a file you can read after.

```
    pip3 install . --install-option='--command=whoami > /tmp/whoami'
```
