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

def max_consecutive(list):
	return max(map(len, group(list)))

def main():
	print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
	# Expected output : 4

	print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
	# Expected output : 3

if __name__ == '__main__':
    main()