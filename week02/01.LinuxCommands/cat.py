# cat.py

import sys

def cat(arguments):
	with open(arguments, 'r') as f:
		print(f.read())

def main():
	if len(sys.argv) > 2:
		raise Exception ('Too many arguments in function call.')
	elif len(sys.argv) < 2:
		raise Exception ('Not enough arguments in function call.')
	else:
		cat(sys.argv[1])

if __name__ == '__main__':
	main()