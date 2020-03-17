# sort_fractions.py

from collect_fractions import validate_input_collect

def validate_ascending(ascending):
	if type(ascending) is not bool:
		raise Exception('Ascending can only be of type "boolean"')

def sort_fractions(fractions, ascending = True):
	validate_input_collect(fractions)
	validate_ascending(ascending)

	length = len(fractions)

	for i in range(0, length - 1):
		for j in range(0, length - i - 1):
			a = fractions[j]
			b = fractions[j + 1]
			if (a[0] / a[1]) > (b[0] / b[1]):
				helper = fractions[j]
				fractions[j] = fractions[j + 1]
				fractions[j + 1] = helper

	if ascending == False:
		fractions.reverse()

	return fractions

def main():
	print(sort_fractions([(2, 3), (1, 2)]))
	# Expected output: [(1, 2), (2, 3)]

	print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
	# Expected output: [(1, 3), (1, 2), (2, 3)]

	print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
	# Expected output: [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]

if __name__ == '__main__':
	main()