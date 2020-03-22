# polynomial.py

from utils import (
	parser,
	validate_call
)

class Term:
	# Constructor

	def __init__(self, term_list):
		self.validate_term(term_list)

		self.coefficient = term_list[0]
		self.variable = term_list[1]
		self.power = term_list[2]

	# Dunders
	
	def __str__(self):
		if self.coefficient == None and self.variable == True and self.power == None:
			return 'x'
		elif self.coefficient != None and self.variable == True and self.power == None:
			return f'{self.coefficient}x'
		elif self.coefficient == None and self.variable == True and self.power != None:
			return f'x^{self.power}'
		elif self.coefficient != None and self.variable == True and self.power != None:
			return f'{self.coefficient}x^{self.power}'
		elif self.coefficient != None and self.variable == False and self.power == None:
			return f'{self.coefficient}'

	def __repr__(self):
		if self.coefficient == None and self.variable == True and self.power == None:
			return 'x'
		elif self.coefficient != None and self.variable == True and self.power == None:
			return f'{self.coefficient}x'
		elif self.coefficient == None and self.variable == True and self.power != None:
			return f'x^{self.power}'
		elif self.coefficient != None and self.variable == True and self.power != None:
			return f'{self.coefficient}x^{self.power}'
		elif self.coefficient != None and self.variable == False and self.power == None:
			return f'{self.coefficient}'

	# Public
	
	def derivative(self):
		if self.variable == False:
			return '0'
		elif self.variable == True and self.coefficient and self.power:
			if self.power == 2:
				return f'{self.coefficient*self.power}x'
			else:
				return f'{self.coefficient*self.power}x^{self.power-1}'
		elif self.variable == True and self.coefficient:
			return f'{self.coefficient}'
		elif self.variable == True and self.power:
			if self.power == 2:
				return f'{self.coefficient*self.power}x'
			else:
				return f'{self.power}x^{self.power-1}'
		elif self.variable == True:
			return '1'

	# Static

	@staticmethod
	def validate_term(term_list):
		if type(term_list) is not list:
			raise Exception('Argument must be of "list" type.')
		elif len(term_list) != 3:
			raise Exception('List must contain 3 elements.')
		elif type(term_list[0]) != int and term_list[0] != None:
			raise Exception('First element of list must be of "int" type or None.')
		elif type(term_list[1]) != bool:
			raise Exception('Second element of list must be of "bool" type.')
		elif type(term_list[2]) != int and term_list[2] != None:
			raise Exception('Third element of list must be of "int" type or None.')
		elif term_list[0] == None and term_list[1] == None:
			raise Exception('Cannot initialize term without either coefficent or variable')

class Polynomial:
	# Constructor

	def __init__(self, terms_list):
		self.validate_terms_list(terms_list)

		self.terms_list = terms_list

	# Dunders

	def __str__(self):
		result = ''
		length = len(self.terms_list)

		for index in range(0, length - 1):
			result += str(self.terms_list[index])
			result += '+'

		result += str(self.terms_list[length - 1])

		return result

	# Public

	def derivative(self):
		result = ''
		length = len(self.terms_list)

		for index in range(0, length - 1):
			helper = str(self.terms_list[index].derivative())

			if helper != '0':
				result += helper
			if index + 1 < length - 1:
				result += '+'


		helper = str(self.terms_list[length - 1].derivative())

		if helper != '0':
			if result[:-1] != '+' and result != '':
				result += '+'	
		
		result += helper

		return result

	# Static
	
	@staticmethod
	def validate_terms_list(terms_list):
		if type(terms_list) is not list:
			raise Exception('Argument must be of "list" type')

		for elem in terms_list:
			if type(elem) is not Term:
				raise Exception('Elements must be of "Term" type')