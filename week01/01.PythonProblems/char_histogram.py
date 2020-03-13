def char_histogram(string):
	dict = {}
	
	for elem in string:
		if elem in dict:
			dict[elem] += 1
		else: 
			dict[elem] = 1

	return dict


def main():
	print(char_histogram('Python!'))
	# Expected output : { 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1 }

	print(char_histogram('AAAAaaa!!!'))
	# Expected output : { 'A': 4, 'a': 3, '!": 3 }

if __name__ == '__main__':
	main()