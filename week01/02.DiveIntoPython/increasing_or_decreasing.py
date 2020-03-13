def increasing_or_decreasing(seq):
	is_up = False 
	is_down = False
	length = len(seq)
	
	if length == 1:
		return False
	
	if seq[0] > seq[1]:
		is_down = True
	elif seq[0] < seq[1]:
		is_up = True
	
	for i in range(1, length - 1):
		if(seq[i] > seq[i + 1] and is_up) or \
		  (seq[i] < seq[i + 1] and is_down) or \
		  (seq[i] == seq[i + 1]): 
			return False

	if is_up:
		return 'Up!'

	if is_down:
		return 'Down!'

def main():
	print(increasing_or_decreasing([1,2,3,4,5]))
	# Expected output : Up!

	print(increasing_or_decreasing([5,6,-10]))
	# Expected output : False

	print(increasing_or_decreasing([1,1,1,1]))
	# Expected output : False

	print(increasing_or_decreasing([9,8,7,6]))
	# Expected output : Down!

if __name__ == '__main__':
	main()