# solution.py

import sys
from utils import validate_call, parser, term_splitter
from polynomial import (
	Polynomial,
	Term
)

def main():
	validate_call(sys.argv)
	my_list = parser(sys.argv[1])
	
	term_list = []

	for elem in my_list:
		term = term_splitter(elem)
		term_list.append(Term(term))

	function = Polynomial(term_list)
	
	print(f"The derivative of f(x) = {function}")
	print(f"f'(x) = {function.derivative()}")

if __name__ == '__main__':
	main()