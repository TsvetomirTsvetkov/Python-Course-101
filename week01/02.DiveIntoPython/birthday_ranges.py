def birthday_ranges(birthdays, ranges):
	list_ranges = [] 
	result = []
	cnt = 0

	for elem in ranges:
		curr = [i for i in range(elem[0],elem[1] + 1)]
		list_ranges.append(curr)
	
	for i in list_ranges:
		for j in birthdays:
			if j in i :
				cnt += 1
		result.append(cnt) 
		cnt = 0
	
	return result

def main():
	print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
	# Expected output : [2, 3, 4, 5, 2]

	print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))
	# Expected output : [5, 2, 0, 1]

if __name__ == '__main__':
    main()