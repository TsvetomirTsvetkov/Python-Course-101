# tests_utils.py

import unittest
from utils import (
	parser,
	validate_call,
	term_splitter
)

class TestParser(unittest.TestCase):
	def test_parser_converts_string_into_list_of_substrings(self):
		test1 = '2x^3 + 3x + 1'
		test2 = 'x^4 + 10*x^3'

		self.assertEqual(parser(test1), ['2x^3', '3x', '1'])
		self.assertEqual(parser(test2), ['x^4', '10x^3'])

class TestValidateCall(unittest.TestCase):
	def test_validate_call_raises_exception_if_argument_type_is_not_list(self):
		test_argument = 'solution.py'
		exc = None

		try:
			validate_call(test_argument)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Argument must be of type "list".')

	def test_validate_call_raises_exception_if_argument_length_is_not_two(self):
		test_argument = ['solution.py']
		exc = None

		try:
			validate_call(test_argument)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'The function takes exactly one argument.')

	def test_validate_call_raises_exception_if_given_polynomial_has_forbidden_symbol(self):
		test_argument = ['solution.py', '2x^3 + 3x + 1p']
		exc = None

		try:
			validate_call(test_argument)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Forbidden symbols. Check your input again.')

	def test_validate_call_passes_with_correct_input(self):
		test_argument = ['solution.py', '2x^3 + 3x + 1']

		validate_call(test_argument)

class TestTermSplitter(unittest.TestCase):
	def test_term_spitter_passes_with_coefficient_only(self):
		test_term = '24'

		self.assertEqual(term_splitter(test_term), [24, False, None])

	def test_term_spitter_passes_with_variable_and_coefficient_only(self):
		test_term = '24x'

		self.assertEqual(term_splitter(test_term), [24, True, None])

	def test_term_spitter_passes_with_variable_coefficient_and_power(self):
		test_term = '24x^2'

		self.assertEqual(term_splitter(test_term), [24, True, 2])

	def test_term_spitter_passes_with_variable_and_power_only(self):
		test_term = 'x^2'

		self.assertEqual(term_splitter(test_term), [None, True, 2])

	def test_term_spitter_raises_exception_with_coefficient_and_power_only(self):
		test_term = '2^2'
		exc = None

		try:
			term_splitter(test_term)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), "Error: Estimates can be made. Recalculate and call the function again.")

if __name__ == '__main__':
	unittest.main()