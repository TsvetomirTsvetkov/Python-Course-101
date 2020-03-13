def anagrams():
	word1 = input('Enter first word: ')
	word2 = input('Enter second word: ')
	dict1 = {} 
	dict2 = {}

	for elem in word1:
		if elem >= 'A' and elem <= 'Z':
			elem.upper()
		if elem in dict1:
			dict1[elem] += 1
		else:
			dict1[elem] = 1

	for elem in word2:
		if elem >= 'A' and elem <= 'Z':
			elem.upper()
		if elem in dict2:
			dict2[elem] += 1
		else:
			dict2[elem] = 1
	
	if dict1 == dict2:
		print('ANAGRAMS')
	else:
		print('NOT ANAGRAMS')

def main():
	anagrams()
	# Test1 : anagrams ('TOP_CODER', 'COTO_PRODE')
	# Expected output : NOT ANAGRAMS

	anagrams()
	# Test2 : anagrams('kilata', 'cvetelina_yaneva')
	# Expected output : NOT ANAGRAMS

	anagrams()
	# Test3 : anagrams('BRADE', 'BEARD')
	# Expected output : ANAGRAMS

if __name__ == '__main__':
    main()