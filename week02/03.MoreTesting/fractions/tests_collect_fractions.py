# tests_collect_fractions.py

import unittest

from collect_fractions import (
	validate_input_collect,
	lcm,
	collect_fractions
)

class TestValidateInputCollect(unittest.TestCase):
	def test_validation_passes_with_correct_input(self):
		fractions = [(1, 3), (4, 5)]

		validate_input_collect(fractions)

	def test_validation_raises_exception_with_empty_list(self):
		fractions = []
		exc = None

		try:
			validate_input_collect(fractions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'List cannot be empty.')

	def test_validation_raises_exception_if_fractions_is_not_of_type_list(self):
		fractions = ((1, 3), (4, 5))
		exc = None

		try:
			validate_input_collect(fractions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Argument can only be of type "list".')

	def test_validation_raises_exception_if_length_of_element_is_not_two(self):
		fractions = [(1, 2), (1, 3, 4)]
		exc = None

		try:
			validate_input_collect(fractions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Tuple can only contain 2 elements.')

	def test_validation_raises_exception_if_one_of_the_elements_of_the_tuples_is_not_integer(self):
		fractions = [(1, 5), (1, 2.0)]
		exc = None

		try:
			validate_input_collect(fractions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Tuple can only contain integers.')

	def test_validation_raises_exception_if_one_of_the_elements_has_denominator_zero(self):
		fractions = [(1, 2), (1, 0)]
		exc = None

		try:
			validate_input_collect(fractions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Cannot devide by zero.')

class TestCollectFractions(unittest.TestCase):
	def test_collect_fractions_passes_with_only_one_element_in_list(self):
		fractions = [(1, 7)]
		
		self.assertEqual((1, 7), collect_fractions(fractions))

	def test_collect_fraction_passes_with_more_than_one_element_in_list(self):
		fractions = [(1, 4), (1, 2)]

		self.assertEqual((3, 4), collect_fractions(fractions))
if __name__ == '__main__':
	unittest.main()