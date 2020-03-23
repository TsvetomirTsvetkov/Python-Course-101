# solution.py

from bowling_game import (
	Frame,
	BowlingGame
)

def main():
	game = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])	# 20
	print(game.result()) # 65

	game = BowlingGame([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] )	# 20
	print(game.result()) # 0

	game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])	# 12
	print(game.result()) # 300

	game = BowlingGame([5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6])		# 13
	print(game.result()) # invalid number of frames	

if __name__ == '__main__':
	main()