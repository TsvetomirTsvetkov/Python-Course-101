def is_vowel(char):
	return char == 'a' or char == 'e' or char == 'i' or \
	       char == 'o' or char == 'u' or char == 'y' or \
	       char == 'A' or char == 'E' or char == 'I' or \
	       char == 'O' or char == 'U' or char == 'Y'

def count_consonants(str):
	cnt = 0
	
    for x in str:
		if (not is_vowel(x)) and ((x >= 'a' and x <= 'z') or (x >= 'A' and x <='Z')):
            cnt += 1
	
    return cnt

def main():
	print(count_consonants("Python"))
	# Expected output : 4

	print(count_consonants("Theistareykjarbunga"))
	# Expected output : 11

	print(count_consonants("grrrrgh!"))
	# Expected output : 7

	print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
	# Expected output : 44

	print(count_consonants("A nice day to code!"))
	# Expected output : 6

if __name__ == '__main__':
	main()