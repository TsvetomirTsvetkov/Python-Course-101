def is_prime(n):
	for elem in range(2, n):
		if n % elem == 0:
			return False
	
	return True

def goldbach(n):
	tuples = []
	
	for elem in range(2, n//2 + 1):
		if is_prime(elem) and is_prime(n - elem):
			tuples.append((elem, n - elem)) 
	
	return tuples

def main():
	print(goldbach(4))
	# Expected output : [(2,2)]

	print(goldbach(6))
	# Expected output : [(3,3)]

	print(goldbach(8))
	# Expected output : [(3,5)]

	print(goldbach(10))
	# Expected output : [(3,7), (5,5)]

	print(goldbach(100))
	# Expected output : [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]

if __name__ == '__main__':
    main()