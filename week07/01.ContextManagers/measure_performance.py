# measure_performance.py
import time
from timeit import default_timer as timer


class measure_performance:
    def __init__(self):
        self.start = 0
        self.all = 0
        self.counter = 1

    def __enter__(self):
        self.start = timer()
        self.all = self.start
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        end = timer()
        print('Finished for:', end - self.all)

    def benchmark(self, msg=None, restart=False):
        assert msg is None or type(msg) is str, 'Message must be of "str" type!'
        assert type(restart) is bool, 'Restart must be of "bool" type!'

        if msg is None:
            result_message = f'Benchmark No.{self.counter}: '
        else:
            result_message = msg + ': '

        self.counter += 1

        print(result_message, timer() - self.start)

        if restart is True:
            self.start = timer()


with measure_performance() as p:
    time.sleep(1)
    p.benchmark('1st step')

    time.sleep(2)
    p.benchmark('2nd step', restart=True)

    time.sleep(3)
    p.benchmark()
