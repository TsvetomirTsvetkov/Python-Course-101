def sum_of_digits(n):
	if n < 0:
		n = abs(n)

	if n <= 9:
		return n

	return n%10 + sum_of_digits(n//10)

def main():
	print(sum_of_digits(1325132435356))
	# Expected output : 43

	print(sum_of_digits(123))
	# Expected output : 6

	print(sum_of_digits(6))
	# Expected output : 6

	print(sum_of_digits(-10))
	# Expected output : 1

if __name__ == '__main__':
    main()