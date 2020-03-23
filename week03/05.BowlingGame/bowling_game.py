# bowling_game.py

class Frame:
	# Constructor

	def __init__(self, first_chance, second_chance = 0):
		self.validate_input(first_chance, second_chance)

		self.first_chance = first_chance
		self.second_chance = second_chance

	# Dunder

	def __str__(self):
		if self.first_chance == 10:
			return '[Strike]'
		elif self.first_chance + self.second_chance == 10:
			return '[Spare]'
		elif self.first_chance + self.second_chance < 10:
			return '[Open Frame]'
	
	def __eq__(self, other):
		return 	self.first_chance == other.first_chance and\
				self.second_chance == other.second_chance 

	# Static

	@staticmethod
	def validate_input(first_chance, second_chance):
		if type(first_chance) is not int:
			raise Exception('First argument must be of "int" type.')
		elif type(second_chance) is not int:
			raise Exception('Second argument must be of "int" type.')
		elif first_chance < 0 or first_chance > 10:
			raise Exception("Invalid number of pins submitted for your first try.")
		elif second_chance < 0 or second_chance > 10:
			raise Exception("Invalid number of pins submitted for your second try.")
		elif first_chance + second_chance > 10 and first_chance != 10:
			raise Exception("You can't take down more than 10 pins in one frame.")

class BowlingGame:
	# Constructor

	def __init__(self, pins_knocked):
		self.validate_input(pins_knocked)		
		self.frames = []

		length = len(pins_knocked)
		flag = False

		if length % 2 != 0:
			for index in range(0, length):
				if index + 1 > length - 1:
					self.frames.append(Frame(pins_knocked[index], 0))
					break
				elif flag == True:
					flag = False
					continue
				elif pins_knocked[index] == 10:
					self.frames.append(Frame(10, 0))
				else:
					self.frames.append(Frame(pins_knocked[index], pins_knocked[index+1]))
					flag = True
		else:
			for index in range(0, length - 1):
				if flag == True:
					flag = False
					continue
				elif pins_knocked[index] == 10:
					self.frames.append(Frame(10, 0))
				else:
					self.frames.append(Frame(pins_knocked[index], pins_knocked[index+1]))
					flag = True
			if pins_knocked[length - 1] == 10:
				self.frames.append(Frame(10, 0))
	# Dunders

	def __str__(self):
		result = ''
		for elem in self.frames:
			if self.frames.index(elem) != len(self.frames) - 1:
				result += (str(elem) + ' ')
			else:
				result += str(elem)

		return result
	
	# Public
	# TODO: TESTS
	def result(self):
		result = 0
		length = len(self.frames)
		cnt = 0
		helper = ''

		if length % 2 != 0:
			return 'Invalid number of frames.'
		else:
			for index in range(0, length - 2):
				if index == length - 3:
					helper += str(self.frames[index])
				if str(self.frames[index]) == '[Strike]':
					result += (getattr(self.frames[index], 'first_chance') + getattr(self.frames[index], 'second_chance'))
					result += (getattr(self.frames[index+1], 'first_chance') + getattr(self.frames[index+1], 'second_chance'))
					result += (getattr(self.frames[index+2], 'first_chance') + getattr(self.frames[index+2], 'second_chance'))
				elif str(self.frames[index]) == '[Spare]':
					result += (getattr(self.frames[index], 'first_chance') + getattr(self.frames[index], 'second_chance'))
					result += (getattr(self.frames[index+1], 'first_chance') + getattr(self.frames[index+1], 'second_chance'))
				else:
					result += (getattr(self.frames[index], 'first_chance') + getattr(self.frames[index], 'second_chance'))
				cnt += 2

			if helper != '[Strike]' and helper != '[Spare]':
				result += (getattr(self.frames[length - 2], 'first_chance') + getattr(self.frames[length - 2], 'second_chance'))
				result += (getattr(self.frames[length - 1], 'first_chance') + getattr(self.frames[length - 1], 'second_chance'))
				cnt += 2
			
			return str(result)
			
	# Static

	@staticmethod
	def validate_input(pins_knocked):
		if type(pins_knocked) is not list:
			raise Exception('Argument must be of "list" type.')
		elif len(pins_knocked) < 10:
			raise Exception('Cannot have less than 10 throws.')
		elif len(pins_knocked) > 20:
			raise Exception('Cannot have more than 20 throws.')
		for elem in pins_knocked:
			if type(elem) is not int:
				raise Exception('Number of knocked pins must be of "int" type.')