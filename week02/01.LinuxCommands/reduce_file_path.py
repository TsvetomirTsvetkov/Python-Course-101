# reduce_file_path.py

def reduce_file_path(path):
	path = path.replace('/', ' / ')
	path_list = path.split()
	result_path = []
	
	for elem in path_list:
		if elem == '.':
			continue
		elif elem == '..':
			if len(result_path) != 0:
				result_path.pop()
			else:
				continue
			if len(result_path) != 0:
				result_path.pop()
			else:
				continue
		elif len(result_path) != 0 and result_path[-1] == elem and result_path[-1] == '/':
			continue
		else:
			result_path.append(elem)

	if len(result_path) > 1 and result_path[-1] == '/':
		result_path.pop()
	
	result = ''

	for elem in result_path:
		result += str(elem)

	return result

def main():
	print(reduce_file_path("/"))
	# Expected output : "/"

	print(reduce_file_path("/srv/../"))
	# Expected output : "/"

	print(reduce_file_path("/srv/www/htdocs/wtf/"))
	# Expected output : "/srv/www/htdocs/wtf"

	print(reduce_file_path("/srv/www/htdocs/wtf"))
	# Expected output : "/srv/www/htdocs/wtf"

	print(reduce_file_path("/srv/./././././"))
	# Expected output : "/srv"

	print(reduce_file_path("/etc//wtf/"))
	# Expected output : "/etc/wtf"

	print(reduce_file_path("/etc/../etc/../etc/../"))
	# Expected output : "/"

	print(reduce_file_path("//////////////"))
	# Expected output : "/"

	print(reduce_file_path("/../"))
	# Expected output : "/"

if __name__ == '__main__':
	main()