def to_digits(n):
	list = []

	while n:
		list.append(n%10)
		n //= 10

	list.reverse()
	
	return list
	
def main():
	print(to_digits(123))
	# Expected output : [1, 2, 3]

	print(to_digits(99999))
	# Expected output : [9, 9, 9, 9, 9]

	print(to_digits(123023))
	# Expected output : [1, 2, 3, 0, 2, 3]

if __name__ == '__main__':
    main()