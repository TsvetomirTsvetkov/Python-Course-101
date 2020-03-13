def how_many_bombed(value, x, y, matrix, n, m):
	my_sum = 0

	for i in range(0, n):
		for j in range (0, m):
			if i in range(x - 1, x + 2) and j in range(y - 1, y + 2) and (i != x or j != y):
				if matrix[i][j] - value <= 0:
					continue 
				else: 
					my_sum += matrix[i][j] - value
			else:
				my_sum += matrix[i][j]
		
	return my_sum

def matrix_bombing_plan():
	matrix = []

	n = (int)(input('Input n: '))
	m = (int)(input('Input m: '))
	
	for i in range (0, n):
		line = input()
		line = list(map((int),line.split()))
		if len(line) != m:
			print('Wrong input!')
			return {}
		else:
			matrix.append(line)

	dictionary = {}
	n = len(matrix)
	m = len(matrix[0])
	
	for i in range(0, n):
		for j in range (0, m):
			dictionary[(i,j)] = how_many_bombed(matrix[i][j], i, j, matrix, n, m)
	
	return dictionary

def main():
	print(matrix_bombing_plan())
	# Test1 : print(matrix_bombing_plan([[1,2,3],[4,5,6],[7,8,9]]))
	# Expected output : {(0, 0): 42,
	#					 (0, 1): 36,
	#					 (0, 2): 37,
	#					 (1, 0): 30,
	#					 (1, 1): 15,
	#					 (1, 2): 23,
	#					 (2, 0): 29,
	#					 (2, 1): 15,
	#					 (2, 2): 26}
	
if __name__ == '__main__':
    main()