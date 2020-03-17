# tests_sort_fractions.py

import unittest
from sort_fractions import (
	validate_ascending,
	sort_fractions
)

class TestValidateAscending(unittest.TestCase):
	def test_validate_ascending_passes_with_correct_input(self):
		ascending = False

		validate_ascending(ascending)

	def test_validate_ascending_raises_exception_if_ascending_not_bool(self):
		ascending = 5
		exc = None

		try:
			validate_ascending(ascending)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Ascending can only be of type "boolean"')

class TestSortFractions(unittest.TestCase):
	def test_sort_fraction_passes_with_correct_input_and_ascending_true(self):
		fractions = [(2, 3), (1, 2), (1, 3)]
		expected_output = [(1, 3), (1, 2), (2, 3)]
		ascending = True

		self.assertEqual(expected_output, sort_fractions(fractions, ascending))

	def test_sort_fraction_passes_with_correct_input_and_ascending_false(self):
		fractions = [(2, 3), (1, 2), (1, 3)]
		expected_output = [(2, 3), (1, 2), (1, 3)]
		ascending = False

		self.assertEqual(expected_output, sort_fractions(fractions, ascending))

if __name__ == '__main__':
	unittest.main()