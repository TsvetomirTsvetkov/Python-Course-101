# tests_fractions.py

import unittest
from fractions import (
	Fraction,
	validate_fractions,
	collect_fractions
)

class TestFractionConstructor(unittest.TestCase):
	def test_constructor_creates_an_object_with_valid_input(self):
		nominator = 5
		denominator = 4
		fraction_tuple = (nominator, denominator)

		test = Fraction(fraction_tuple)

		self.assertEqual(test.nominator, 5)
		self.assertEqual(test.denominator, 4)

	def test_constructor_raises_exception_if_argument_is_not_of_type_tuple(self):
		nominator = 5
		denominator = 4
		fraction_tuple = [nominator, denominator]
		exc = None

		try:
			test = Fraction(fraction_tuple)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Fraction must be of type "tuple".')

	def test_constructor_raises_exception_if_length_of_argument_is_not_two(self):
		nominator = 5
		denominator = 4
		new_element = 3
		fraction_tuple = (nominator, denominator, new_element)
		exc = None

		try:
			test = Fraction(fraction_tuple)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Fraction must contain two elements.')


	def test_constructor_raises_exception_if_nominator_is_not_of_type_int(self):
		nominator = 'c'
		denominator = 5
		fraction_tuple = (nominator, denominator)
		exc = None

		try:
			test = Fraction(fraction_tuple)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Nominator must be of type "int".')

	def test_constructor_raises_exception_if_denominator_is_not_of_type_int(self):
		nominator = 5
		denominator = 'c'
		fraction_tuple = (nominator, denominator)
		exc = None

		try:
			test = Fraction(fraction_tuple)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Denominator must be of type "int".')

	def test_constructor_raises_exception_if_denominator_is_zero(self):
		nominator = 5
		denominator = 0
		fraction_tuple = (nominator, denominator)
		exc = None

		try:
			test = Fraction(fraction_tuple)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Denominator cannot be zero.')	

class TestSimplifyFraction(unittest.TestCase):
	def test_simplify_fraction_passes_with_with_nominator_equal_to_zero(self):
		test = Fraction((0, 8))
		expected_result = Fraction((0,1))
		
		test.simplify_fraction()
		
		self.assertEqual(expected_result, test)

	def test_simplify_fraction_passes_with_simplified_fraction(self):
		test = Fraction((3, 5))
		expected_result = Fraction((3, 5))

		test.simplify_fraction()

		self.assertEqual(expected_result, test)

	def test_simplify_fraction_passes_with_not_simplified_fraction(self):
		test = Fraction((4, 8))
		expected_result = Fraction((1, 2))

		test.simplify_fraction()

		self.assertEqual(expected_result, test)

class TestValidateFractions(unittest.TestCase):
	def test_validate_fractions_passes_with_correct_input(self):
		fractions = [Fraction((1, 3)), Fraction((1, 4))]

		validate_fractions(fractions)
		validate_fractions([])

	def test_validate_fractions_raises_exception_if_argument_not_of_type_list(self):
		fractions = (Fraction((1, 3)), Fraction((1, 4)))
		exc = None

		try:
			validate_fractions(fractions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Fractions must be of type "list".')

	def test_validate_fractions_raises_exception_if_element_of_list_not_fraction(self):
		fractions = [Fraction((1, 3)), (1, 4)]
		exc = None

		try:
			validate_fractions(fractions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Elements must be of type "Fraction".')

class TestCollectFractions(unittest.TestCase):
	def test_collect_fractions_passes_with_only_one_element_in_list(self):
		fractions = [Fraction((1, 7))]
		expected_result = Fraction((1,7))

		self.assertEqual(expected_result, collect_fractions(fractions))

	def test_collect_fractions_passes_with_more_than_one_element_in_list(self):
		fractions = [Fraction((1, 4)), Fraction((1, 2))]
		expected_result = Fraction((3, 4))

		self.assertEqual(expected_result, collect_fractions(fractions))

	def test_collect_fractions_passes_with_empty_list(self):

		fractions = []
		expected_result = Fraction((0, 1))

		self.assertEqual(expected_result, collect_fractions(fractions))

class TestFractionStrDunder(unittest.TestCase):
	def test_fraction_string_representation_is_as_expected_one(self):
		
		test1 = Fraction((1, 3))
		test2 = Fraction((-1, 3))
		test3 = Fraction((2, 4))

		self.assertEqual('1/3', str(test1))
		self.assertEqual('-1/3', str(test2))
		self.assertEqual('2/4', str(test3))

class TestFractionEqDunder(unittest.TestCase):
	def test_eq_passes_with_equal_fractions(self):
		test1 = Fraction((1, 3))
		test2 = Fraction((1, 3))

		self.assertEqual(test1, test2)

	def test_eq_does_not_pass_if_one_fraction_is_simplified_version_of_the_other(self):
		test1 = Fraction((2, 6))
		test2 = Fraction((1, 3))

		self.assertNotEqual(test1, test2)

class TestFractionAddDunder(unittest.TestCase):
	def test_add_passes_with_fractions_with_equal_denominators(self):
		test1 = Fraction((2, 6))
		test2 = Fraction((1, 6))

		result = test1 + test2

		self.assertEqual(result, Fraction((18, 36)))

	def test_add_passes_with_fractions_with_not_equal_denominators(self):
		test1 = Fraction((2, 5))
		test2 = Fraction((1, 6))

		result = test1 + test2

		self.assertEqual(result, Fraction((17, 30)))

class TestFractionAddiDunder(unittest.TestCase):
	def test_addi_passes_with_fractions_with_equal_denominators(self):
		test1 = Fraction((2, 6))
		test2 = Fraction((1, 6))

		test1 += test2

		self.assertEqual(test1, Fraction((18, 36)))

	def test_addi_passes_with_fractions_with_not_equal_denominators(self):
		test1 = Fraction((2, 5))
		test2 = Fraction((1, 6))

		test1 += test2

		self.assertEqual(test1, Fraction((17, 30)))

class TestFractionGeDunder(unittest.TestCase):
	def test_ge_correctly_compares_non_equal_fractions(self):
		test1 = Fraction((2, 6))
		test2 = Fraction((1, 6))

		self.assertGreaterEqual(test1, test2)

	def test_ge_correctly_compares_equal_fractions(self):
		test1 = Fraction((2, 6))
		test2 = Fraction((2, 6))

		self.assertGreaterEqual(test1, test2)

class TestFractionLtDunder(unittest.TestCase):
	def test_lt_correctly_compares_non_equal_fractions(self):
		test1 = Fraction((2, 6))
		test2 = Fraction((3, 6))

		self.assertLess(test1, test2)

class TestFractionReprDunder(unittest.TestCase):
	def test_fraction_repr_representation_is_as_expected_one(self):
		test1 = Fraction((1, 3))
	
		self.assertEqual(repr(test1),'1/3' )

if __name__ == '__main__':
	unittest.main()