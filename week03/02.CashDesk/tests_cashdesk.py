# tests_cashdesk.py

import unittest
from cashdesk import (
	Bill,
	BillBatch,
	CashDesk
)

# Testing: Bill

class TestBillInit(unittest.TestCase):
	def test_bill_init_raises_exception_if_amount_is_not_of_type_int(self):
		exc = None

		try:
			test = Bill(20.0)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(type(exc), TypeError)
		self.assertEqual(str(exc), 'Amount must be of type "int".')

	def test_bill_init_raises_exception_if_amount_is_negative(self):
		exc = None

		try:
			test = Bill(-5)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(type(exc), ValueError)
		self.assertEqual(str(exc), 'Amount cannot be negative.')

	def test_bill_init_inicializes_bill_with_amount(self):
		test = Bill(5)

		self.assertEqual(test.amount, 5)

class TestBillStrDunder(unittest.TestCase):
	def test_bill_str_representation_is_as_expected_one(self):
		test = Bill(5)

		self.assertEqual(str(test), 'A 5$ bill')

class TestBillReprDunder(unittest.TestCase):
	def test_bill_repr_representation_is_as_expected_one(self):
		test = Bill(5)

		self.assertEqual(repr(test), 'A 5$ bill')

class TestBillIntDunder(unittest.TestCase):
	def test_bill_int_representation_is_as_expected_one(self):
		test = Bill(5)

		self.assertEqual((int)(test), 5)

class TestBillEqDunder(unittest.TestCase):
	def test_bill_eq_comparison_is_as_expected_one(self):
		test1 = Bill(5)
		test2 = Bill(5)
		test3 = Bill(6)

		self.assertEqual(test1, test2)
		self.assertNotEqual(test2, test3)

class TestBillHashDunder(unittest.TestCase):
	def test_bill_hash_dunder_works_as_expected(self):
		test1 = Bill(5)
		test2 = Bill(5)
		money_holder = {}

		money_holder[test1] = 1

		if test2 in money_holder:
		    money_holder[test2] += 1

		self.assertEqual(money_holder[test1], 2)

class TestBillLtDunder(unittest.TestCase):
	def test_bill_lt_dunder_compares_bills_correctly(self):
		test1 = Bill(5)
		test2 = Bill(6)

		self.assertLess(test1, test2)

# Testing: BillBatch

class TestBillBatchInit(unittest.TestCase):
	def test_billbatch_init_raises_exception_if_bills_is_not_of_type_list(self):
		exc = None
		bills = (Bill(5), Bill(3), Bill(1))

		try:
			test = BillBatch(bills)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(type(exc), TypeError)
		self.assertEqual(str(exc), 'Amount must be of type "list".')

	def test_billbatch_init_inicializes_batchbill_with_bills(self):
		bills = [Bill(5), Bill(3), Bill(1)]
		test = BillBatch(bills)

		self.assertEqual(test.batch, bills)

class TestBillBatchGetItemDunder(unittest.TestCase):
	def test_billbatch_indexation_is_as_expected(self):
		bills = [Bill(5), Bill(3), Bill(1)]

		test = BillBatch(bills)

		self.assertEqual(test[0], Bill(5))
		self.assertEqual(test[1], Bill(3))
		self.assertEqual(test[2], Bill(1))

class TestBillBatchLenDunder(unittest.TestCase):
	def test_billbatch_len_dunder_calculates_length_of_batchbill_as_expected(self):
		bills1 = [Bill(5), Bill(3), Bill(1)]
		bills2 = []

		test1 = BillBatch(bills1)
		test2 = BillBatch(bills2)
		
		self.assertEqual(len(test1), 3)
		self.assertEqual(len(test2), 0)

class TestBillBatchTotal(unittest.TestCase):
	def test_billbatch_total_calculates_total_amount_of_bills_in_batch(self):
		bills = [Bill(5), Bill(3), Bill(2)]
		
		test = BillBatch(bills)

		self.assertIsNotNone(test.total())
		self.assertEqual(test.total(), 10)

# Testing: CashDesk

class TestCashDeskInit(unittest.TestCase):
	def test_cashdesk_init_is_inicialized_as_expected(self):
		test = CashDesk()

		self.assertEqual(test.cash, {})

class TestCashDeskTakeMoney(unittest.TestCase):
	def test_cashdesk_take_money_raises_exception_if_money_is_not_of_type_bill_or_billbatch(self):
		money = 50
		exc = None

		test = CashDesk()

		try:
			test.take_money(money)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(type(exc), TypeError)
		self.assertEqual(str(exc), 'Money must be of type "Bill" or type "BillBatch".')

	def test_cashdesk_take_money_works_as_expected_with_empty_desk_and_bill(self):
		cash_desk = CashDesk()
		test1 = Bill(10)

		cash_desk.take_money(test1)

		self.assertEqual(cash_desk.cash, {test1: 1})

	def test_cashdesk_take_money_works_as_expected_with_empty_desk_and_billbatch(self):
		cash_desk = CashDesk()
		bill_batch = BillBatch([Bill(10), Bill(15)])

		cash_desk.take_money(bill_batch)

		self.assertEqual(cash_desk.cash, {Bill(10): 1, Bill(15): 1})

	def test_cashdesk_take_money_works_as_expected_with_one_type_of_bill_in_desk(self):
		cash_desk = CashDesk()
		test1 = Bill(10)
		test2 = Bill(10)

		cash_desk.take_money(test1)
		cash_desk.take_money(test2)


		self.assertEqual(cash_desk.cash, {test2 : 2})

	def test_cashdesk_take_money_works_as_expected_with_more_than_one_type_of_bill_in_desk(self):
		cash_desk = CashDesk()
		test1 = Bill(10)
		test2 = Bill(10)
		test3 = Bill(15)

		cash_desk.take_money(test1)
		cash_desk.take_money(test2)
		cash_desk.take_money(test3)
		
		self.assertEqual(cash_desk.cash, {test2: 2, test3: 1})

class TestCashDeskTotal(unittest.TestCase):
	def test_cashdesk_total_works_as_expected_when_bill_appears_only_once(self):
		cash_desk = CashDesk()
		bill1 = Bill(5)
		bill2 = Bill(10)
		bill3 = Bill(20)

		cash_desk.take_money(bill1)
		cash_desk.take_money(bill2)
		cash_desk.take_money(bill3)

		self.assertEqual(cash_desk.total(), 35)

	def test_cashdesk_total_works_as_expected_when_bill_appears_more_than_once(self):
		cash_desk = CashDesk()
		bill1 = Bill(10)
		bill2 = Bill(10)
		bill3 = Bill(20)
		bill4 = Bill(20)

		cash_desk.take_money(bill1)
		cash_desk.take_money(bill2)
		cash_desk.take_money(bill3)
		cash_desk.take_money(bill4)

		self.assertEqual(cash_desk.total(), 60)

if __name__ == '__main__':
	unittest.main()