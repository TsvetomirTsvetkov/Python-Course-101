def palindrome(n):
    string = str(n)
    length = len(string)

    for x in (0, length - 1):
    	if(string[x] != string[length - 1 - x]): 
    		return False
    
    return True

def main():
	print(palindrome(121))
	# Expected output : True

	print(palindrome("kapak"))
	# Expected output : True

	print(palindrome("baba"))
	# Expected output : False

if __name__ == '__main__':
    main()