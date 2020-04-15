# silence.py
from contextlib import contextmanager


class SilenceException:
    def __init__(self, exc_type, exc_value=None):
        self.exc_type = exc_type
        self.exc_value = exc_value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type == self.exc_type and (str(exc_value) == str(self.exc_value) or self.exc_value is None):
            return True
        else:
            return False


@contextmanager
def silence_exception(exc_type, exc_value=None):
    try:
        yield
    except exc_type as err:
        if str(err) != str(exc_value) and exc_value is not None:
            raise err
