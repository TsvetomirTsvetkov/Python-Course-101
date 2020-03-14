# tests_cancellation_policy.py

import unittest
from datetime import datetime, timedelta
from cancellation_policy import (
	validate_conditions,	
	ensure_conditions,		
	pair_conditions,		
	cancellation_policy,	
	get_current_condition,	
	sort_conditions			
)

class TestValidateConditions(unittest.TestCase):
	def test_validation_passes_with_valid_conditions(self):
		conditions = [
			{ 'hours': 24, 'percent': 10 },
			{ 'percent': 100 }
		]

		validate_conditions(conditions)

	def test_validation_raises_exception_if_all_conditions_have_hours(self):
		conditions = [
			{ 'hours': 24, 'percent': 10 },
			{ 'hours': 12, 'percent': 50 }
		]

		exc = None

		try:
			validate_conditions(conditions)
		except Exception as err:
			exc = err
		
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid conditions.')

	def test_validation_raises_exception_if_unexpected_key(self):
		conditions = [
			{ 'hours': 24, 'perc': 10 },
			{ 'hours': 12, 'percent': 50 }
		]

		exc = None

		try:
			validate_conditions(conditions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid key.')

	def test_validation_raises_exception_with_more_than_one_percent_per_hour(self):
		conditions = [
			{ 'hours': 24, 'percent': 10 },
			{ 'hours': 24, 'percent': 30 },
			{ 'percent': 100 }
		]

		exc = None

		try:
			validate_conditions(conditions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Value error.')

	def test_validation_raises_exception_with_more_than_24_hours(self):
		conditions = [
			{ 'hours': 24, 'percent': 10 },
			{ 'hours': 28, 'percent': 30 },
			{ 'percent': 100 }
		]

		exc = None

		try:
			validate_conditions(conditions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Value error.')

	def test_validation_raises_typeerror_with_elements_that_are_not_dict(self):
		conditions = [
			{ 'hours': 24, 'percent': 10 },
			[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
			{ 'percent': 100 }
		]

		exc = None

		try:
			validate_conditions(conditions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Only elements of type dictionary allowed')

class TestEnsureConditions(unittest.TestCase):
	def test_all_conditions_have_hours(self):
		cond1 = {'hours': 10, 'percent': 10}
		cond2 = {'percent': 100}
		conditions = [cond1, cond2]

		ensure_conditions(conditions)

		self.assertEqual(cond1['hours'], 10)
		self.assertEqual(cond2['hours'], 0)

class TestPairConditions(unittest.TestCase):
	def test_pair_passes_with_even_number_of_conditions(self):
		conditions = [
			{ 'hours': 24, 'percent': 10 },
			{ 'hours': 12, 'percent': 50 },
			{ 'hours': 6, 'percent': 70 },
			{ 'hours': 0, 'percent': 100 }
		]

		expected = [
			({ 'hours': 24, 'percent': 10 }, { 'hours': 12, 'percent': 50 }),
			({ 'hours': 12, 'percent': 50 }, { 'hours': 6, 'percent': 70 }),
			({ 'hours': 6, 'percent': 70 }, { 'hours': 0, 'percent': 100 })
		]

		result = pair_conditions(conditions)
		
		self.assertEqual(result, expected)

	def test_pair_passes_with_odd_number_of_conditions(self):
		conditions = [
			{ 'hours': 24, 'percent': 10 },
			{ 'hours': 12, 'percent': 50 },
			{ 'hours': 6, 'percent': 70 },
			{ 'hours': 3, 'percent': 85 },
			{ 'hours': 0, 'percent': 100}
		]

		expected = [
			({ 'hours': 24, 'percent': 10 }, { 'hours': 12, 'percent': 50 }),
			({ 'hours': 12, 'percent': 50 }, { 'hours': 6, 'percent': 70 }),
			({ 'hours': 6, 'percent': 70 }, { 'hours': 3, 'percent': 85 }),
			({ 'hours': 3, 'percent': 85 }, { 'hours': 0, 'percent': 100})
		]

		result = pair_conditions(conditions)
		
		self.assertEqual(result, expected)

class TestGetCurrentCondition(unittest.TestCase):
	# Taken from the solution uploaded in the course's repository.

	def test_with_current_date_before_min_condition_date_should_return_min_condition_percent(self):
		conditions = [
			({'hours': 24, 'percent': 0}, {'hours': 18, 'percent': 20}),
			({'hours': 18, 'percent': 20}, {'hours': 12, 'percent': 50}),
			({'hours': 12, 'percent': 50}, {'hours': 6, 'percent': 80}),
			({'hours': 6, 'percent': 80}, {'hours': 0, 'percent': 100})
		]
		booking_start = datetime.now()
		now = booking_start - timedelta(hours=100)

		result = get_current_condition(conditions, booking_start, now)

		self.assertEqual(result, 0)

	def test_with_current_date_in_condition_interval_should_return_higher_condition_percent(self):
		conditions = [
			({'hours': 24, 'percent': 0}, {'hours': 18, 'percent': 20}),
			({'hours': 18, 'percent': 20}, {'hours': 12, 'percent': 50}),
			({'hours': 12, 'percent': 50}, {'hours': 6, 'percent': 80}),
			({'hours': 6, 'percent': 80}, {'hours': 0, 'percent': 100})
		]
		booking_start = datetime.now()
		now = booking_start - timedelta(hours=10)

		result = get_current_condition(conditions, booking_start, now)

		self.assertEqual(result, 80)

	def test_with_current_date_equal_to_condition_hours_should_return_interval_upper_boundary_percent(self):
		conditions = [
			({'hours': 24, 'percent': 0}, {'hours': 18, 'percent': 20}),
			({'hours': 18, 'percent': 20}, {'hours': 12, 'percent': 50}),
			({'hours': 12, 'percent': 50}, {'hours': 6, 'percent': 80}),
			({'hours': 6, 'percent': 80}, {'hours': 0, 'percent': 100})
		]
		booking_start = datetime.now()
		now = booking_start - timedelta(hours=6)

		result = get_current_condition(conditions, booking_start, now)

		self.assertEqual(result, 100)

class TestSortConditions(unittest.TestCase):
	def test_all_conditions_are_sorted(self):
		conditions = [
			{ 'hours': 12, 'percent': 50 },
			{ 'hours': 0, 'percent': 100 },
			{ 'hours': 24, 'percent': 10 },
			{ 'hours': 6, 'percent': 70 }
		]

		expected = [
			{ 'hours': 24, 'percent': 10 },
			{ 'hours': 12, 'percent': 50 },
			{ 'hours': 6, 'percent': 70 },
			{ 'hours': 0, 'percent': 100 }
		]

		result = sort_conditions(conditions)

		self.assertEqual(expected, result)

class TestCancellationPolicy(unittest.TestCase):
	def test_cancellation_raises_exception_if_the_booking_has_already_started(self):
		price = 50
		start = datetime.now()
		now = start + timedelta(hours=10)
		conditions = [
			{ 'hours': 24, 'percent': 10 },
			{ 'percent': 100 }
		]

		exc = None

		try:
			cancellation_policy(conditions, price, start, now)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid booking start.')

	def test_cancellation_raises_exception_if_the_time_now_equals_start_time(self):
		price = 50
		start = datetime.now()
		now = start
		conditions = [
			{ 'hours': 24, 'percent': 10 },
			{ 'percent': 100 }
		]

		exc = None

		try:
			cancellation_policy(conditions, price, start, now)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid booking start.')

if __name__ == '__main__':
	unittest.main()