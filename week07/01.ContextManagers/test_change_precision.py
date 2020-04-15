# test_change_precision.py
# TODO: Handle type of precision
import unittest
from decimal import *
from change_precision import ChangePercision, change_precision


class ChangePrecisionClassTests(unittest.TestCase):
    def test_change_precision_class_init_initializes_object_as_expected_with_correct_input(self):
        default_precision = 28
        test_precision = 2

        with ChangePercision(test_precision) as cp:
            self.assertEqual(getattr(cp, 'old_precision'), default_precision)
            self.assertEqual(getattr(cp, 'new_precision'), test_precision)

    def test_change_precision_class_init_initializes_object_as_expected_with_invalid_input(self):
        default_precision = 28
        test_precision = -2

        with ChangePercision(test_precision) as cp:
            self.assertEqual(getattr(cp, 'old_precision'), default_precision)
            self.assertEqual(getattr(cp, 'new_precision'), default_precision)

    def test_change_precision_class_changes_precision_only_of_current_block(self):
        default_precision = 28
        test_precision = 2

        self.assertEqual(getcontext().prec, default_precision)

        with ChangePercision(test_precision):
            self.assertEqual(getcontext().prec, test_precision)

        self.assertEqual(getcontext().prec, default_precision)

    def test_change_precision_class_changes_precision_back_to_that_of_the_current_scope(self):
        scope_precision = 11
        default_precision = 28
        test_precision = 2

        getcontext().prec = scope_precision

        with ChangePercision(test_precision):
            self.assertEqual(getcontext().prec, test_precision)

        self.assertEqual(getcontext().prec, scope_precision)

        getcontext().prec = default_precision


class ChangePrecisionFunctionTests(unittest.TestCase):
    def test_change_precision_func_does_not_change_precision_when_invalid_input(self):
        default_precision = 28
        test_precision = -2

        self.assertEqual(getcontext().prec, default_precision)

        with change_precision(test_precision):
            self.assertEqual(getcontext().prec, default_precision)

        self.assertEqual(getcontext().prec, default_precision)

    def test_change_precision_func_changes_precision_only_of_current_block(self):
        default_precision = 28
        test_precision = 2

        self.assertEqual(getcontext().prec, default_precision)

        with change_precision(test_precision):
            self.assertEqual(getcontext().prec, test_precision)

        self.assertEqual(getcontext().prec, default_precision)

    def test_change_precision_func_changes_precision_back_to_that_of_the_current_scope(self):
        scope_precision = 11
        default_precision = 28
        test_precision = 2

        getcontext().prec = scope_precision

        with change_precision(test_precision):
            self.assertEqual(getcontext().prec, test_precision)

        self.assertEqual(getcontext().prec, scope_precision)

        getcontext().prec = default_precision


if __name__ == '__main__':
    unittest.main()
