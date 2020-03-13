def nan_expand(n):
	if n == 0: 
		return ""
	if n == 1: 
		return "Not a NaN"
	else: 
		return "Not a " + nan_expand(n - 1)

def main():
	print(nan_expand(0))
	# Expected output : ""

	print(nan_expand(1))
	# Expected output : "Not a NaN"

	print(nan_expand(2))
	# Expected output : "Not a Not a NaN"

	print(nan_expand(3))
	# Expected output : "Not a Not a Not a NaN"

if __name__ == '__main__':
    main()