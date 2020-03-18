# cashdesk.py

class Bill:
	# Constructor

	def __init__(self, amount):
		if type(amount) is not int:
			raise TypeError('Amount must be of type "int".')
		if amount < 0:
			raise ValueError('Amount cannot be negative.')

		self.amount = amount

	# Dunders

	def __str__(self):
		return f'A {self.amount}$ bill'

	def __repr__(self):
		return f'A {self.amount}$ bill'

	def __int__(self):
		return self.amount

	def __eq__(self, other):
		return self.amount == other.amount

	def __hash__(self):
		return self.amount

	# We need to override __lt__ to use sorted in CashDesk.

	def __lt__(self, other):
		return self.amount < other.amount

class BillBatch:
	# Constructor

	def __init__(self, bills):
		if type(bills) is not list:
			raise TypeError('Amount must be of type "list".')

		self.batch = bills

	# Dunders

	def __getitem__(self, index):
		return self.batch[index]

	def __len__(self):
		return len(self.batch)

	# Public

	def total(self):
		sum = 0

		for elem in self.batch:
			sum += (int)(elem)

		return sum 


class CashDesk:
	# Constructor

	def __init__(self):
		self.cash = {}

	# Public

	def take_money(self, money):
		if type(money) is Bill:
			if money in self.cash.keys():
				self.cash[money] += 1
			else:
				self.cash[money] = 1
		elif type(money) is BillBatch:
			for elem in money:
				if elem in self.cash.keys():
					self.cash[elem] += 1
				else:
					self.cash[elem] = 1
		else: 
			raise TypeError('Money must be of type "Bill" or type "BillBatch".')

	def total(self):
		total_sum = 0
		
		for elem in self.cash.keys():
			total_sum += self.cash[elem] * int(elem)

		return total_sum

	def inspect(self):
		print(f'We have a total of {self.total()}$ in the desk')
		print('We have the following count of bills, sorted in ascending order:')
		
		keys = sorted(self.cash.keys())
		
		for key in keys:
			print(f'{int(key)}$ bills - {self.cash[key]}')
		

def main():
	# Testing Bill

	a = Bill(10)
	b = Bill(5)
	c = Bill(10)

	int(a) # 10
	str(a) # "A 10$ bill"
	print(a) # A 10$ bill

	a == b # False
	a == c # True

	money_holder = {}

	money_holder[a] = 1 # We have one 10% bill

	if c in money_holder:
	    money_holder[c] += 1

	print(money_holder) # { "A 10$ bill": 2 }
	print()

	# Testing BatchBill

	values = [10, 20, 50, 100]
	bills = [Bill(value) for value in values]

	batch = BillBatch(bills)

	for bill in batch:
	    print(bill)

	# Expected output:
	# A 10$ bill
	# A 20$ bill
	# A 50$ bill
	# A 100$ bill

	# Testing CashDesk

	values = [10, 20, 50, 100, 100, 100]
	bills = [Bill(value) for value in values]

	batch = BillBatch(bills)

	desk = CashDesk()

	desk.take_money(batch)
	desk.take_money(Bill(10))

	print(desk.total()) # 390
	desk.inspect()

if __name__ == '__main__':
	main()