def sum_matrix(m):
	sum_all = 0

	for elem in m:
		sum_all += sum(elem)
	
	return sum_all 

def main():
	print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
	# Expected output : 45

	print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
	# Expected output : 0

	print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
	# Expected output : 55

if __name__ == '__main__':
    main()