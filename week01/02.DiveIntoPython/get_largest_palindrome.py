def get_largest_palindrome(n):
	my_list = str(n - 1)
	n -= 1
	
	while n:
		if my_list == ''.join(reversed(my_list)):
			return n
		n -= 1
		my_list = str(n)

def main():
	print(get_largest_palindrome(99))
	# Expected output : 88

	print(get_largest_palindrome(252))
	# Expected output : 242

	print(get_largest_palindrome(994687))
	# Expected output : 994499

	print(get_largest_palindrome(754649)) 
	# Expected output : 754457

if __name__ == '__main__':
    main()