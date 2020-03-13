def is_number_balanced(number):
    l_sum = 0 
    r_sum = 0
    my_number = list(str(number))
    length = len(my_number)

    for x in range(0, (int)(length/2)):
        l_sum += (int)(my_number[x])
        r_sum += (int)(my_number[length - x - 1])
    
    return l_sum == r_sum

def main():
	print(is_number_balanced(9))
	# Expected output : True

	print(is_number_balanced(4518))
	# Expected output : True

	print(is_number_balanced(28471))
	# Expected output : False

	print(is_number_balanced(1238033))
	# Expected output : True

if __name__ == '__main__':
	main()