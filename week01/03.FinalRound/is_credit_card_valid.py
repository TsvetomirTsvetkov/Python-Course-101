def is_credit_card_valid(number):
	length = len(number)

	if length % 2 == 0:
		return False

	new_number = ''
	rev = number[::-1]

	for index in range(0,length):
		if index % 2 == 0:
			new_number += rev[index]
		else:
			new_number += (str)((int)(rev[index]) + (int)(rev[index]))
	
	return sum(map(int, list(new_number))) % 10 == 0

def main():
	print(is_credit_card_valid('79927398713'))
	# Expected output : VALID (True)

	print(is_credit_card_valid('79927398715'))
	# Expected output : INVALID (False)

if __name__ == '__main__':
    main()