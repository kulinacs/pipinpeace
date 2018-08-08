pip in peace - bind
===================

The bind package spawns a tcp bind shell as the user running the install on the port specified by the `--port` flag.

setup.py
--------

```
    python3 setup.py install --port=12345
```

pip
---

Work in progress, currently freezes until connection

```
    pip3 install . --install-option='--port=12345'
```
