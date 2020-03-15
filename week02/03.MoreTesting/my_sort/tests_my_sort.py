# tests_my_sort.py

import unittest
from my_sort import (
	my_sort, 
	validate_iterable,
	validate_key,
	validate_ascending
)

class TestValidateIterable(unittest.TestCase):
	def test_iterable_validation_passes_with_list(self):
		iterable = [2, 3, 5, 1, 7, 4]

		validate_iterable(iterable)

	def test_iterable_validation_passes_with_tuple(self):
		iterable = (2, 3, 5, 1, 7, 4)

		validate_iterable(iterable)

	def test_iterable_validation_passes_with_empty_list(self):
		iterable = []

		validate_iterable(iterable)

	def test_iterable_validation_passes_with_empty_tuple(self):
		iterable = ()

		validate_iterable(iterable)

	def test_iterable_validation_raises_exception_if_iterable_is_not_of_tuple_or_list_type(self):
		iterable = {'key1': 5, 'key2': 7, 'key3': 2}
		exc = None

		try:
			validate_iterable(iterable)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Only lists and tuples can be sorted.')	

	def test_iterable_validation_raises_exception_if_iterable_is_none(self):
		iterable = None
		exc = None

		try:
			validate_iterable(iterable)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Argument "iterable" cannot be None.')	

	def test_iterable_validation_raises_exception_if_elements_of_different_type(self):
		iterable = [{'key' : 5}, 1, 3, 2]
		exc = None

		try:
			validate_iterable(iterable)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Cannot compare elements of different type.')

class TestValidateKey(unittest.TestCase):
	def test_key_validation_passes_with_correct_input(self):
		iterable = [{'key': 5}, {'key': 7}, {'key': 2}]
		key = 'key'

		validate_key(iterable, key)

	def test_key_validation_raises_exception_if_no_key_is_given_to_compare_dictionaries(self):
		iterable = [{'key': 5}, {'key': 7}, {'key': 2}]
		key = None

	def test_key_validation_raises_exception_if_key_is_not_string(self):
		iterable = [{'key': 5}, {'key': 7}, {'key': 2}]
		key = 5
		exc = None

		try:
			validate_key(iterable, key)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Key must be of type "string".')

	def test_key_validation_raises_exception_if_the_key_is_not_in_every_elem(self):
		iterable = [{'key': 5}, {'key2': 1}, {'key': 2}]
		key = 'key'
		exc = None

		try:
			validate_key(iterable, key)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Element without expected key. Cannot compare.')

	def test_key_validation_raises_exception_if_elems_are_dictionaries_but_key_is_none(self):
		iterable = [{'key': 5}, {'key': 1}, {'key': 2}]
		key = None
		exc = None

		try:
			validate_key(iterable, key)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Cannot compare dictionaries without key.')

	def test_key_validation_passes_with_elements_that_are_not_dicts_and_none_key(self):
		iterable = [4, 5, 3, 1, 2]
		key = None

		validate_key(iterable, key)


class TestValidateAscending(unittest.TestCase):
	def test_ascending_validation_raises_exception_if_ascending_is_not_boolean(self):
		ascending = 5
		exc = None
		
		try:
			validate_ascending(ascending)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Ascending can only be of type "boolean"')

class TestMySort(unittest.TestCase):
	def test_my_sort_passes_with_list_of_integers_ascending(self):
		iterable_element = [9, 4, 1, 6, 2]
		expected_result = [1, 2, 4, 6, 9]

		sorted_elements = my_sort(iterable = iterable_element, ascending = True)

		self.assertEqual(expected_result, sorted_elements)

	def test_my_sort_passes_with_tuple_of_integers_ascending(self):
		iterable_element = (9, 4, 1, 6, 2)
		expected_result = (1, 2, 4, 6, 9)

		sorted_elements = my_sort(iterable = iterable_element, ascending = True)

		self.assertEqual(expected_result, sorted_elements)

	def test_my_sort_passes_with_list_of_dictionaries_ascending(self):
		iterable_element = [{'key': 6}, {'key': 3}, {'key': 4}, {'key': 2}, {'key': 7}]
		expected_result = [{'key': 2}, {'key': 3}, {'key': 4}, {'key': 6}, {'key': 7}]
		key_element = 'key'
		sorted_elements = my_sort(iterable = iterable_element, ascending = True, key = key_element)

		self.assertEqual(expected_result, sorted_elements)

	def test_my_sort_passes_with_list_of_integers_descending(self):
		iterable_element = [9, 4, 1, 6, 2]
		expected_result = [9, 6, 4, 2, 1]

		sorted_elements = my_sort(iterable = iterable_element, ascending = False)

		self.assertEqual(expected_result, sorted_elements)

	def test_my_sort_passes_with_tuple_of_integers_descending(self):
		iterable_element = (9, 4, 1, 6, 2)
		expected_result = (9, 6, 4, 2, 1)

		sorted_elements = my_sort(iterable = iterable_element, ascending = False)

		self.assertEqual(expected_result, sorted_elements)

	def test_my_sort_passes_with_list_of_dictionaries_descending(self):
		iterable_element = [{'key': 6}, {'key': 3}, {'key': 4}, {'key': 2}, {'key': 7}]
		expected_result = [{'key': 7}, {'key': 6}, {'key': 4}, {'key': 3}, {'key': 2}]
		key_element = 'key'
		sorted_elements = my_sort(iterable = iterable_element, ascending = False, key = key_element)

		self.assertEqual(expected_result, sorted_elements)



if __name__ == '__main__':
	unittest.main()