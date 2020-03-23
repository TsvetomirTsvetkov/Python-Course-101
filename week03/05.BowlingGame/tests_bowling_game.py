# tests_bowling_game.py

import unittest
from bowling_game import (
	Frame,
	BowlingGame
)

# Frame

class TestFrameValidateInput(unittest.TestCase):
	def test_frame_validation_raises_exception_if_first_chance_negative(self):
		exc = None

		try:
			test = Frame(-5, 6)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), "Invalid number of pins submitted for your first try.")
	def test_frame_validation_raises_exception_if_first_chance_greater_than_ten(self):
		exc = None

		try:
			test = Frame(11, 6)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), "Invalid number of pins submitted for your first try.")
	def test_frame_validation_raises_exception_if_second_chance_negative(self):
		exc = None

		try:
			test = Frame(5, -6)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), "Invalid number of pins submitted for your second try.")
	def test_frame_validation_raises_exception_if_second_chance_greater_than_ten(self):
		exc = None

		try:
			test = Frame(3, 16)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), "Invalid number of pins submitted for your second try.")
	def test_frame_validation_raises_exception_if_sum_of_chances_greater_than_ten(self):
		exc = None

		try:
			test = Frame(3, 8)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), "You can't take down more than 10 pins in one frame.")

	def test_frame_validation_raises_exception_if_first_argument_is_not_int(self):
		exc = None

		try:
			test = Frame('3', 8)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'First argument must be of "int" type.')

	def test_frame_validation_raises_exception_if_second_argument_is_not_int(self):
		exc = None

		try:
			test = Frame(3, '8')
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Second argument must be of "int" type.')

	def test_frame_validation_passes_with_correct_input(self):
		test1 = Frame(3, 6)
		test2 = Frame(4, 6)
		test3 = Frame(0, 6)
		test4 = Frame(0, 0)

class TestFrameInit(unittest.TestCase):
	def test_frame_init_initializes_object_as_expected(self):
		test_frame1 = Frame(4, 6)
		test_frame2 = Frame(10, 0)

		self.assertEqual(getattr(test_frame1,'first_chance'), 4)
		self.assertEqual(getattr(test_frame1,'second_chance'), 6)

		self.assertEqual(getattr(test_frame2,'first_chance'), 10)
		self.assertEqual(getattr(test_frame2,'second_chance'), 0)

class TestFrameStrDunder(unittest.TestCase):
	def test_frame_str_representation_is_as_expected(self):
		test_frame1 = Frame(4, 6)
		test_frame2 = Frame(10, 8)
		test_frame3 = Frame(3, 4)

		self.assertEqual(str(test_frame1), '[Spare]')
		self.assertEqual(str(test_frame2), '[Strike]')
		self.assertEqual(str(test_frame3), '[Open Frame]')

class TestFrameEqDunder(unittest.TestCase):
	def test_frame_eq_comparison_is_as_expected(self):
		test_frame1 = Frame(4, 6)
		test_frame2 = Frame(4, 6)
		test_frame3 = Frame(2, 5)

		self.assertEqual(test_frame1, test_frame2)
		self.assertNotEqual(test_frame2, test_frame3)

# BowlingGame

class TestBowlingGameValidateInput(unittest.TestCase):
	def test_bowling_game_validation_raises_excpetion_if_argument_is_not_list(self):
		test_argument = (1, 2, 3, 1, 4, 6, 1, 8, 2, 3)
		exc = None

		try:
			test_game = BowlingGame(test_argument)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Argument must be of "list" type.')

	def test_bowling_game_validation_raises_exception_if_less_than_10_frames(self):
		test_argument = [1, 2, 3, 1, 4, 6, 1, 8, 2]
		exc = None

		try:
			test_game = BowlingGame(test_argument)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Cannot have less than 10 throws.')

	def test_bowling_game_validation_raises_exception_if_more_than_20_frames(self):
		test_argument = [1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2, 6]
		exc = None

		try:
			test_game = BowlingGame(test_argument)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Cannot have more than 20 throws.')

	def test_bowling_game_validation_raises_exception_if_elem_in_list_not_int(self):
		test_argument = [1, 2, 3, 1, 4, 6, 1, 8, 2, '3']
		exc = None

		try:
			test_game = BowlingGame(test_argument)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Number of knocked pins must be of "int" type.')

	def test_bowling_game_validation_passes_with_correct_input(self):
		test_argument = [1, 2, 3, 1, 4, 6, 1, 8, 2, 3]

		test_game = BowlingGame(test_argument)

class TestBowlingGameInit(unittest.TestCase):
	def test_bowling_game_init_initializes_object_as_expected(self):
		test_argument = [1, 2, 3, 1, 4, 6, 1, 8, 2, 3]
		test_game = BowlingGame(test_argument)

		self.assertEqual(getattr(test_game, 'frames'), [Frame(1, 2), Frame(3, 1), Frame(4, 6), Frame(1, 8), Frame(2, 3)])

class TestBowlingStrDunder(unittest.TestCase):
	def test_bowling_game_str_representation_is_as_expected(self):
		test_argument = [1, 2, 3, 1, 4, 6, 1, 8, 2, 3]
		test_game = BowlingGame(test_argument)

		self.assertEqual(str(test_game), '[Open Frame] [Open Frame] [Spare] [Open Frame] [Open Frame]')

class TestBowlingResult(unittest.TestCase):
	def test_bowling_game_result_calculates_the_score_of_the_game_correctly(self):
		test_game1 = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])
		test_game2 = BowlingGame([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
		test_game3 = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
		test_game4 = BowlingGame([5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6])

		self.assertEqual(test_game1.result(), '65')
		self.assertEqual(test_game2.result(), '0')
		self.assertEqual(test_game3.result(), '300')
		self.assertEqual(test_game4.result(), 'Invalid number of frames.')
if __name__ == '__main__':
	unittest.main()