# tests_simplify_fraction.py

import unittest
from simplify_fraction import (
	validate_input_simplify,
	gcd,
	simplify_fraction
)

class TestValidateInputSimplify(unittest.TestCase):
	def test_validation_passes_with_correct_input(self):
		fraction = (1, 3)

		validate_input_simplify(fraction)

	def test_validation_raises_exception_if_type_of_the_argument_is_not_tuple(self):
		fraction = [1, 3]

		exc = None

		try:
			validate_input_simplify(fraction)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Argument can only be of type "tuple".')

	def test_validation_raises_exception_if_length_of_tuple_is_not_two(self):
		fraction = (1, 3, 4)
		exc = None

		try:
			validate_input_simplify(fraction)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Tuple can only contain 2 elements.')

	def test_validation_raises_exception_if_one_of_the_arguments_is_not_integer(self):
		fraction = (1, 2.0)
		exc = None

		try:
			validate_input_simplify(fraction)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Tuple can only contain integers.')

	def test_validation_raises_exception_if_denominator_is_zero(self):
		fraction = (1, 0)
		exc = None

		try:
			validate_input_simplify(fraction)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Cannot devide by zero.')

class TestGCD(unittest.TestCase):
	def test_gcd_passes_when_nominator_equals_denominator(self):
		nominator = 5
		denominator = 5

		self.assertEqual(5, gcd(nominator, denominator))

	def test_gcd_passes_when_nominator_does_not_equal_denominator(self):
		nominator = 21
		denominator = 7

		self.assertEqual(7, gcd(nominator, denominator))

class TestSimplifyFraction(unittest.TestCase):
	def test_simplify_fraction_passes_when_nominator_equals_zero(self):
		fraction = (0, 24)

		self.assertEqual((0, 1), simplify_fraction(fraction))

	def test_simplify_fraction_passes_with_correct_input(self):
		fraction = (7, 28)

		self.assertEqual((1, 4), simplify_fraction(fraction))

if __name__ == '__main__':
	unittest.main()