# simplify_fraction.py

def validate_input_simplify(fraction):
	if type(fraction) is not tuple:
		raise Exception('Argument can only be of type "tuple".')
	if len(fraction) != 2:
		raise Exception('Tuple can only contain 2 elements.')
	if type(fraction[0]) != int or type(fraction[1]) != int:
		raise Exception('Tuple can only contain integers.')
	if fraction[1] == 0:
		raise Exception('Cannot devide by zero.')

def gcd(nominator, denominator):
	if nominator == denominator:
		return nominator
	elif nominator > denominator:
		return gcd(nominator - denominator, denominator)
	else:
		return gcd(nominator, denominator - nominator)

def simplify_fraction(fraction):
	validate_input_simplify(fraction)

	nominator = fraction[0]
	denominator = fraction[1]
	
	if nominator == 0:
		return (nominator, 1)

	res = gcd(nominator, denominator)

	while res != 1:
		nominator //= res
		denominator //= res
		res = gcd(nominator, denominator)

	return (nominator, denominator)


def main():
	
	print(simplify_fraction((3,9)))
	# Expected output: (1,3)

	print(simplify_fraction((1,7)))
	# Expected output: (1,7)

	print(simplify_fraction((4,10)))
	# Expected output: (2,5)

	print(simplify_fraction((462,63)))
	# Expected output: (22,3)

if __name__ == '__main__':
	main()