# fractions.py

from math import gcd

"""
In my version of the solution, adding fractions does not
automatically mean that the result is simplified.
It's actually quite the opposite.
That is a personal preference and is due to the way I
decided to implement the __add__ & __iadd__ dunders.

The reason "collect_fractions" returns the simplified
fraction is due to the expected output we had been
given for the same function the previous week.

Since we haven't been given an example of how
collect_fractions works with empty lists,
I've decided that in my solution,
the function will return Fraction((0, 1))
(which is still 0).
"""

def validate_fractions(fractions):
	if type(fractions) is not list:
		raise Exception('Fractions must be of type "list".')

	for elem in fractions:
		if type(elem) != Fraction:
			raise Exception('Elements must be of type "Fraction".')

def collect_fractions(fractions):
	validate_fractions(fractions)

	fraction_sum = Fraction((0, 1))

	for elem in fractions:
		fraction_sum += elem

	fraction_sum.simplify_fraction()
	
	return fraction_sum


class Fraction:
	# Constructor

	def __init__(self, fraction_tuple):
		if type(fraction_tuple) is not tuple:
			raise Exception('Fraction must be of type "tuple".')
		if len(fraction_tuple) != 2:
			raise Exception('Fraction must contain two elements.')

		nominator = fraction_tuple[0]
		denominator = fraction_tuple[1]

		if type(nominator) is not int:
			raise Exception('Nominator must be of type "int".')
		if type(denominator) is not int:
			raise Exception('Denominator must be of type "int".')
		if denominator == 0:
			raise Exception('Denominator cannot be zero.')

		self.nominator = nominator
		self.denominator = denominator

	# Dunders

	def __str__(self):
		return f'{self.nominator}/{self.denominator}'

	def __eq__(self, other):
		return self.nominator == other.nominator and self.denominator == other.denominator

	def __add__(self, other):
		denom = self.denominator * other.denominator
		nomin = (self.nominator * other.denominator) + (other.nominator * self.denominator)

		return Fraction((nomin, denom))

	def __iadd__(self, other):														
		self.nominator = (self.nominator * other.denominator + other.nominator * self.denominator)
		self.denominator = self.denominator * other.denominator

		return self

	def __ge__(self, other):
		return (self.nominator / self.denominator) >= (other.nominator / other.denominator)

	def __lt__(self, other):
		return (self.nominator / self.denominator) < (other.nominator / other.denominator) 

	def __repr__(self):
		return f'{self.nominator}/{self.denominator}'

	# Public

	def simplify_fraction(self):
		if self.nominator == 0:
			self.denominator = 1

		res = gcd(self.nominator, self.denominator)

		while res != 1:
			self.nominator //= res
			self.denominator //= res
			res = gcd(self.nominator, self.denominator)

def main():
	fractions = [Fraction((1, 7)), Fraction((2, 6))]
	
	print(collect_fractions(fractions))
	# Expected output: 10/21

	print(sorted([Fraction((2, 3)), Fraction((1, 2))]))
	# Expected output: [1/2, 2/3]

if __name__ == '__main__':
	main()