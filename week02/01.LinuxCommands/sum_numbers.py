# sum_numbers.py

import sys

def sum_numbers(filename):
	with open(filename, 'r') as f:
		list_str = f.read().split()
		print(sum(map(int, var)))

def main():
	if len(sys.argv) > 2:
		raise Exception ('Too many arguments in function call.')
	elif len(sys.argv) < 2:
		raise Exception ('Not enough arguments in function call.')
	else:
		sum_numbers(sys.argv[1])

if __name__ == '__main__':
	main()