import time
from flask import current_app as app


def execution_time(func):
    """Decorator that logs the execution time."""

    def wrap(*args, **kwargs):
        start = time.time()
        response = func(*args, **kwargs)
        end = time.time()

        app.logger.info("{} executed in {} sec".format(func.__name__, end - start))
        return response

    return wrap
