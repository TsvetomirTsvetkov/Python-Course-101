# change_precision.py
from contextlib import contextmanager
from decimal import *


class ChangePercision:
    def __init__(self, precision):  # Handle negative precisions?
        self.old_precision = getcontext().prec

        if precision < 1:
            print("Error. Couldn't change precision.")
            print('Precision has not been changed.')
            precision = self.old_precision

        self.new_precision = precision

    def __enter__(self):
        getcontext().prec = self.new_precision
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        getcontext().prec = self.old_precision


@contextmanager
def change_precision(precision):
    try:
        old_precision = getcontext().prec
        getcontext().prec = precision
        yield
    except Exception:  # Handling negative precisions?
        print("Error. Couldn't change precision.")
        print('Precision has not been changed.')
        yield
    finally:
        getcontext().prec = old_precision


with change_precision(-2):
    print(Decimal('1.123132132') + Decimal('2.23232'))  # 3.4

print(Decimal('1.123132132') + Decimal('2.23232'))  # 3.355452132
