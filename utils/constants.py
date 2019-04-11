import inspect

URL = "http://localhost:8080"
UN = "admin"
PWD = "manager"


def whoami():
    return inspect.stack()[1][3]
