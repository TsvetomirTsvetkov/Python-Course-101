# my_sort.py

def validate_iterable(iterable):
	if iterable == None:
		raise Exception('Argument "iterable" cannot be None.')
	
	if type(iterable) != list and type(iterable) != tuple:
		raise Exception('Only lists and tuples can be sorted.')

	if iterable != [] and iterable != ():
		type_of_elem = type(iterable[0])
		length = len(iterable)

		for index in range(1, length):
			if type(iterable[index]) != type_of_elem:
				raise Exception('Cannot compare elements of different type.')

def validate_key(iterable, key):
	if type(key) != str and key != None:
		raise Exception('Key must be of type "string".')

	for elem in iterable:
		if key == None: 
			if type(elem) != dict:
				continue

			if type(elem) == dict:
				raise Exception('Cannot compare dictionaries without key.')
			
		if key != None: 
			if type(elem) != dict:
				raise Exception('Not all elements are of type "dictionary".')

			if key not in elem.keys():
				raise Exception('Element without expected key. Cannot compare.')

			if key in elem.keys():
				continue

def validate_ascending(ascending):
	if type(ascending) != bool:
		raise Exception('Ascending can only be of type "boolean"')

def my_sort(iterable = None, ascending = True, key = None):
	validate_iterable(iterable)
	validate_ascending(ascending)
	validate_key(iterable, key)

	if iterable == [] or iterable == ():
		return iterable

	iter_type = type(iterable)
	elem_type = type(iterable[0])		
	length = len(iterable)
	iterable = (list)(iterable)

	for i in range(0, length - 1):
		for j in range(0, length - i - 1):
			if elem_type != dict:
				if iterable[j] > iterable[j + 1]:
					helper = iterable[j]
					iterable[j] = iterable[j + 1]
					iterable[j + 1] = helper
			else:
				if iterable[j][key] > iterable[j + 1][key]:
					helper = iterable[j]
					iterable[j] = iterable[j + 1]
					iterable[j + 1] = helper

	if ascending == False:
		iterable.reverse() 

	if type(iterable) != iter_type:
		return (iter_type)(iterable)
	else:
		return iterable

def main():
	print(my_sort((10,8,9,10,100)))
	# Expected output: (8, 9, 10, 10, 100)

	print(my_sort([10, 8, 9, 10, 100], False))
	# Expected output: [100, 10, 10, 9, 8]

	print(my_sort(iterable=[{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}], key='age'))
	# Expected output: [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]

if __name__ == '__main__':
	main()