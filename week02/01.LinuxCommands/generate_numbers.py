# generate_numbers.py

import sys
from random import randint

def generate_numbers(filename, numbers):
	num = (int)(numbers)
	
	with open(filename, 'w') as f:
		for index in range(0, num):
			f.write(str(randint(1, 1000)))
			f.write(' ')

def main():
	if len(sys.argv) > 3:
		raise Exception ('Too many arguments in function call.')
	elif len(sys.argv) < 3:
		raise Exception ('Not enough arguments in function call.')
	else:
		generate_numbers(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()