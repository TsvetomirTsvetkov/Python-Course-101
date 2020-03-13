# cat2.py

import sys
from cat import cat

def cat2(arguments):
	length = len(arguments) 
	for index in range(1, length):
		cat(arguments[index])
		if index != length - 1:
			print()

def main():
	if len(sys.argv) < 2:
		raise Exception ('Not enough arguments in function call.')
	else:
		cat2(sys.argv)

if __name__ == '__main__':
	main()