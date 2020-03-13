def to_number(digits):
	result = ""

	for elem in digits:
		result += str(elem)

	return (int)(result)

def main():
	print(to_number([1,2,3]))
	# Expected output : 123

	print(to_number([9,9,9,9,9]))
	# Expected output : 99999

	print(to_number([1,2,3,0,2,3]))
	# Expected output : 123023

	print(to_number([21, 2, 33]))
	# Expected output : 21233

if __name__ == '__main__':
    main()