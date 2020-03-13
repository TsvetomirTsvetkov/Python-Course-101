def sum_of_numbers(input_string):
	length = len(input_string)
	curr = ''
	sum_list = []
	
	for i in range(0,length):
		if input_string[i] >= '0' and input_string[i] <= '9': 
			curr += input_string[i]
		elif (curr != ''): 
			sum_list.append((int)(curr))
			curr = ''
	
	if curr != '': 
		sum_list.append((int)(curr))
	
	return sum(sum_list)

def main():
	print(sum_of_numbers("ab125cd3"))
	# Expected output : 128

	print(sum_of_numbers("ab12"))
	# Expected output : 12

	print(sum_of_numbers("ab"))
	# Expected output : 0

	print(sum_of_numbers("1101"))
	# Expected output : 1101

	print(sum_of_numbers("1111O"))
	# Expected output : 1111

	print(sum_of_numbers("1abc33xyz22"))
	# Expected output : 56

	print(sum_of_numbers("0hfabnek"))
	# Expected output : 0

if __name__ == '__main__':
    main()