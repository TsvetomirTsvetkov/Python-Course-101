# tests_polynomial.py

import unittest
from polynomial import (
	Polynomial,
	Term
)

# Term

class TestTermValidateTerm(unittest.TestCase):
	def test_term_validate_term_raises_exception_if_argument_not_of_list_type(self):
		test_list = (1, True, 3)
		exc = None

		try:
			Term.validate_term(test_list)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Argument must be of "list" type.')

	def test_term_validate_term_raises_exception_if_length_of_list_is_not_three(self):
		test_list = [1, True, 3, 5]
		exc = None

		try:
			Term.validate_term(test_list)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'List must contain 3 elements.')

	def test_term_validate_term_raises_exception_if_first_elem_of_list_not_int_or_none(self):
		test_list = ['3', True, 3]
		exc = None

		try:
			Term.validate_term(test_list)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'First element of list must be of "int" type or None.')

	def test_term_validate_term_raises_exception_if_second_elem_of_list_not_bool_or_none(self):
		test_list = [1, 'False', 3]
		exc = None

		try:
			Term.validate_term(test_list)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Second element of list must be of "bool" type.')

	def test_term_validate_term_raises_exception_if_third_elem_of_list_not_int_or_none(self):
		test_list = [1, True, '3']
		exc = None

		try:
			Term.validate_term(test_list)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Third element of list must be of "int" type or None.')

	def test_term_validate_term_passes_with_correct_input(self):
		test_list = [1, True, 3]

		Term.validate_term(test_list)


class TestTermInit(unittest.TestCase):
	def test_term_init_initializes_objects_as_expected(self):
		test_list = [1, True, 3]
		test_obj = Term(test_list)

		self.assertEqual(getattr(test_obj, 'coefficient'), 1)
		self.assertEqual(getattr(test_obj, 'variable'), True)
		self.assertEqual(getattr(test_obj, 'power'), 3)

class TestTermStrDunder(unittest.TestCase):
	def test_term_str_representation_is_as_expected_with_only_coefficient(self):
		test_list = [1, False, None]
		test_obj = Term(test_list)

		self.assertEqual(str(test_obj),'1')

	def test_term_str_representation_is_as_expected_with_only_variable(self):
		test_list = [None, True, None]
		test_obj = Term(test_list)

		self.assertEqual(str(test_obj),'x')

	def test_term_str_representation_is_as_expected_with_only_variable_and_power(self):
		test_list = [None, True, 3]
		test_obj = Term(test_list)

		self.assertEqual(str(test_obj),'x^3')

	def test_term_str_representation_is_as_expected_with_only_coefficient_and_variable(self):
		test_list = [3, True, None]
		test_obj = Term(test_list)

		self.assertEqual(str(test_obj),'3x')

	def test_term_str_representation_is_as_expected_with_coeffiecient_variable_and_power(self):
		test_list = [2, True, 5]
		test_obj = Term(test_list)

		self.assertEqual(str(test_obj),'2x^5')
	
class TestTermReprDunder(unittest.TestCase):
	def test_term_repr_representation_is_as_expected_with_only_coefficient(self):
		test_list = [1, False, None]
		test_obj = Term(test_list)

		self.assertEqual(repr(test_obj),'1')

	def test_term_repr_representation_is_as_expected_with_only_variable(self):
		test_list = [None, True, None]
		test_obj = Term(test_list)

		self.assertEqual(repr(test_obj),'x')

	def test_term_repr_representation_is_as_expected_with_only_variable_and_power(self):
		test_list = [None, True, 3]
		test_obj = Term(test_list)

		self.assertEqual(repr(test_obj),'x^3')

	def test_term_repr_representation_is_as_expected_with_only_coefficient_and_variable(self):
		test_list = [3, True, None]
		test_obj = Term(test_list)

		self.assertEqual(repr(test_obj),'3x')

	def test_term_repr_representation_is_as_expected_with_coeffiecient_variable_and_power(self):
		test_list = [2, True, 5]
		test_obj = Term(test_list)

		self.assertEqual(repr(test_obj),'2x^5')

class TestTermDerivative(unittest.TestCase):
	def test_term_derivative_is_calculated_as_expected_with_only_coefficient(self):
		test_list = [1, False, None]
		test_obj = Term(test_list)

		self.assertEqual(test_obj.derivative(),'0')

	def test_term_derivative_is_calculated_as_expected_with_only_variable(self):
		test_list = [None, True, None]
		test_obj = Term(test_list)

		self.assertEqual(test_obj.derivative(),'1')

	def test_term_derivative_is_calculated_as_expected_with_only_variable_and_power(self):
		test_list = [None, True, 3]
		test_obj = Term(test_list)

		self.assertEqual(test_obj.derivative(),'3x^2')

	def test_term_derivative_is_calculated_expected_with_only_coefficient_and_variable(self):
		test_list = [3, True, None]
		test_obj = Term(test_list)

		self.assertEqual(test_obj.derivative(),'3')

	def test_term_derivative_is_calculated_as_expected_with_coeffiecient_variable_and_power(self):
		test_list = [2, True, 5]
		test_obj = Term(test_list)

		self.assertEqual(test_obj.derivative(),'10x^4')
	
# Polynomial

class TestPolynomialInit(unittest.TestCase):
	def test_polynomial_init_initializes_objects_as_expected(self):
		term_obj1 = Term([1, True, 2])
		term_obj2 = Term([1, True, None])

		test_obj = Polynomial([term_obj1, term_obj2])

		self.assertEqual(getattr(test_obj,'terms_list'), [term_obj1, term_obj2])

class TestPolynomialStrDunder(unittest.TestCase):
	def test_polynomial_str_representation_is_as_expected_with_one_term(self):
		term_obj1 = Term([3, True, 2])

		test_obj = Polynomial([term_obj1])

		self.assertEqual(str(test_obj), '3x^2')

	def test_polynomial_str_representation_is_as_expected_with_more_than_one_term(self):
		term_obj1 = Term([3, True, 2])
		term_obj2 = Term([1, True, None])

		test_obj = Polynomial([term_obj1, term_obj2])

		self.assertEqual(str(test_obj), '3x^2+1x')

class TestPolynomialDerivative(unittest.TestCase):
	def test_polynomial_derivative_calculates_derivative_as_expected_with_one_term(self):
		term_obj1 = Term([3, True, 2])

		test_obj = Polynomial([term_obj1])

		self.assertEqual(test_obj.derivative(), '6x')

	def test_polynomial_derivative_calculates_derivative_as_expected_with_more_than_one_term(self):
		term_obj1 = Term([3, True, 2])
		term_obj2 = Term([8, True, None])

		test_obj = Polynomial([term_obj1, term_obj2])

		self.assertEqual(test_obj.derivative(), '6x+8')

class TestPolynomialValidateTermsList(unittest.TestCase):
	def test_polynomial_validate_terms_list_raises_exception_if_terms_are_not_of_list_type(self):
		exc = None

		try:
			test_obj = Polynomial((3, True, 2))
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Argument must be of "list" type')

	def test_polynomial_validate_terms_list_raises_exception_if_element_is_not_of_term_type(self):
		exc = None
		term_obj1 = Term([3, True, 2])

		try:
			test_obj = Polynomial([term_obj1, (1, 2, 3)])
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Elements must be of "Term" type')	

	def test_polynomial_validate_terms_list_passes_with_correct_input(self):
		term_obj1 = Term([3, True, 2])
		term_obj2 = Term([8, True, None])

		test_obj = Polynomial([term_obj1, term_obj2])

if __name__ == '__main__':
	unittest.main()