# test_accepts_decorator.py

import unittest
from accepts_decorator import accepts


class TestAcceptsDecorator(unittest.TestCase):
    def test_accepts_decorator_raises_typeerror_if_argument_type_mismatch(self):
        exc = None

        @accepts(str)
        def say_hello(name):
            return "Hello, I am {}".format(name)

        try:
            say_hello(4)
        except TypeError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Argument 4 is not str!')

    def test_accepts_works_as_expected_with_correct_input(self):
        @accepts(str, int)
        def deposit(name, money):
            return ("{} sends {} $!".format(name, money))

        expected_output = deposit('Marto', 10)

        self.assertEqual(expected_output, 'Marto sends 10 $!')


if __name__ == '__main__':
    unittest.main()
