def group(list):
	groups = []
	curr = []

	for elem in list:
		if elem in curr: 
			curr.append(elem)
		elif len(curr) != 0: 
			groups.append(curr) 
			curr = []
			curr.append(elem)
		elif len(curr) == 0: 
			curr.append(elem)
	
	if curr != []:
		groups.append(curr)
	
	return groups

def main():
	print(group([1, 1, 1, 2, 3, 1, 1]))
	# Expected output : [[1, 1, 1], [2], [3], [1, 1]]

	print(group([1, 2, 1, 2, 3, 3]))
	# Expected output : [[1], [2], [1], [2], [3, 3]]

if __name__ == '__main__':
    main()