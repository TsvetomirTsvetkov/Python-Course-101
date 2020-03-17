# collect_fractions.py

from simplify_fraction import (
	validate_input_simplify,
	gcd,
	simplify_fraction
)

def validate_input_collect(fractions):
	if type(fractions) is not list:
		raise Exception('Argument can only be of type "list".')
	
	if len(fractions) == 0:
		raise Exception('List cannot be empty.')

	for elem in fractions:
		validate_input_simplify(elem)

def lcm(a, b):
	return (a * b) // gcd(a, b)

def collect_fractions(fractions):
	validate_input_collect(fractions)

	lcmultiplier = 0
	length = len(fractions)

	if length == 1:
		return simplify_fraction(fractions[0])

	for index in range(0, length - 1):
		pretender = lcm(fractions[index][1], fractions[index + 1][1])
		if pretender > lcmultiplier:
			lcmultiplier = pretender

	sum = 0

	for elem in fractions:
		if elem[0] != 0:
			sum += elem[0] * (lcmultiplier // elem[1]) 

	return simplify_fraction((sum, lcmultiplier))

def main():
	print(collect_fractions([(1, 4), (1, 2)]))
	# Expected output: (3,4)

	print(collect_fractions([(1, 7), (2, 6)]))
	# Expected output: (10,21)
	
if __name__ == '__main__':
	main()