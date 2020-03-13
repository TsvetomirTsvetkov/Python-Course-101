def is_vowel(char):
	return char == 'a' or char == 'e' or char == 'i' or \
	       char == 'o' or char == 'u' or char == 'y' or \
	       char == 'A' or char == 'E' or char == 'I' or \
	       char == 'O' or char == 'U' or char == 'Y'

def count_vowels(str):
    cnt = 0
    
    for x in str:
        if is_vowel(x):
            cnt += 1
    
    return cnt

def main():
    print(count_vowels("Python"))
    # Expected output : 2

    print(count_vowels("Theistareykjarbunga"))
    # Expected output : 8

    print(count_vowels("grrrrgh!"))
    # Expected output : 0

    print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    # Expected output : 22

    print(count_vowels("A nice day to code!"))
    # Expected output : 8

if __name__ == '__main__':
    main()