# wc.py

import sys

def wc(command, filename):
	with open(filename, 'r') as f:
		text = f.read()

		if command == 'chars':
			print(len(text))
		elif command == 'words':
			print(len(text.split()))
		elif command == 'lines':
			print(len(text.split('\n')))	
		else:
			raise Exception('Invalid option.')

def main():
	if len(sys.argv) > 3:
		raise Exception ('Too many arguments in function call.')
	elif len(sys.argv) < 3:
		raise Exception ('Not enough arguments in function call.')
	else:
		wc(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()