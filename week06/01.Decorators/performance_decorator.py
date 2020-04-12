# performance_decorator.py
from time import *
import timeit


def performance(filename):
    def helper(func):
        with open(filename, 'a+') as f:
            start = timeit.default_timer()
            func
            stop = timeit.default_timer()
            f.write(f'{func.__name__} was called and took {float(str(stop - start)[:4])} seconds to complete\n')
            return func
    return helper


@performance('log.txt')
def something_heavy():
    sleep(2)
    return "I am done!"


print(something_heavy())
