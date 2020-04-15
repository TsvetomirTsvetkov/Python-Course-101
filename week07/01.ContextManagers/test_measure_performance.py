# test_measure_performance,py

import unittest
import time
from measure_performance import measure_performance
from timeit import default_timer as timer


class TestMeasurePerformance(unittest.TestCase):
    def test_measure_performance_init_initalizses_object_as_expected(self):
        expected_start = 0
        expected_all = 0
        expected_counter = 1
        mp = measure_performance()

        self.assertEqual(getattr(mp, 'start'), expected_start)
        self.assertEqual(getattr(mp, 'all'), expected_all)
        self.assertEqual(getattr(mp, 'counter'), expected_counter)

    def test_measure_performance_benchmark_passes_without_arguments(self):
        with measure_performance() as mp:
            mp.benchmark()

    def test_measure_perfeormance_benchmark_raises_exception_if_msg_not_str_or_none(self):
        with self.assertRaises(AssertionError, msg='Message must be of "str" type!'):
            with measure_performance() as mp:
                mp.benchmark(3)

    def test_measure_perfeormance_benchmark_raises_exception_if_restart_not_bool(self):
        with self.assertRaises(AssertionError, msg='Restart must be of "bool" type!'):
            with measure_performance() as mp:
                mp.benchmark('Benchmark', 3)

    def test_measure_performance_benchmark_resets_start_if_restart_is_true(self):
        with measure_performance() as mp:
            time.sleep(3)
            mp.benchmark('2nd step', restart=True)
            self.assertLess(getattr(mp, 'start'), timer() + 2)  # Checking if start has been reset?

    def test_measure_performance_benchmark_updates_counter_on_every_call(self):
        with measure_performance() as mp:
            time.sleep(3)
            mp.benchmark('2nd step', restart=True)
            self.assertEqual(getattr(mp, 'counter'), 2)


if __name__ == '__main__':
    unittest.main()
