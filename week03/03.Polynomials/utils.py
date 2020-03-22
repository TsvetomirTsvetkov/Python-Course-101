# utils.py

def parser(string):
	string = string.replace('*', '')
	string = string.replace(' + ', '+')

	return string.split('+')


def validate_call(argument):
	if type(argument) is not list:
		raise Exception('Argument must be of type "list".')
	if len(argument) != 2:
		raise Exception('The function takes exactly one argument.')

	allowed_symbols = 'x0123456789*+^ '

	for elem in argument[1]:
		if elem not in allowed_symbols:
			raise Exception('Forbidden symbols. Check your input again.')

def term_splitter(string):
	result = []
	found = False
	helper = ''

	for elem in string:
		if elem == 'x' and helper != '':
			found = True
			result.append(int(helper))
			result.append(True)
			helper = ''
			continue
		elif elem == 'x' and helper == '':
			found = True
			result.append(None)
			result.append(True)
			continue
		elif elem == '^':
			if not found:
				raise Exception("Error: Estimates can be made. Recalculate and call the function again.")
			continue

		helper += elem

	if helper != '':
		result.append(int(helper))
	else:
		result.append(None)

	while len(result) == 1:
		result.append(False)
		result.append(None)

	return result