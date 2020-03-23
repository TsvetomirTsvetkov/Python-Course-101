# music_library.py

"""
For my solution, I've decided not to use the datetime library.
"""

from random import randint
import json
import os

def serialize_song(obj):
   if isinstance(obj, Song):
	   info = obj.title + "-" + obj.artist + "-" + obj.album + "-" + str(obj._length)
	   return info
   else:
	   raise TypeError ("Type not serializable")

class Duration:
	# Constructor

	def __init__(self, length):
		self.is_valid_length(length)

		list_len = length.split(':')

		if len(list_len) == 2:
			list_len.insert(0, '0')

		self.hours = list_len[0]
		self.minutes = list_len[1]
		self.seconds = list_len[2]

	# Dunders

	def __str__(self):
		if self.hours != '0':
			return f'{self.hours}:{self.minutes}:{self.seconds}'
		else:
			return f'{self.minutes}:{self.seconds}'
	
	def __eq__(self, other):
		return 	self.hours == other.hours and\
				self.minutes == other.minutes and\
				self.seconds == other.seconds

	# Static

	@staticmethod
	def is_valid_length(length):
		if len(length) < 4:
			raise Exception('Length cannot be less than 4 symbols.')
		elif ':' not in length:
			raise Exception('Length must have ":" to distinguish seconds, minutes and hours.')
		elif length.count(':') > 2:
			raise Exception('Length can only include seconds, minutes and hours.')

		list_len = length.split(':')

		if '' in list_len:
			raise Exception('Error: Found ":" in an unexpected position.')

		size = len(list_len)
		shift = 0

		if size == 3:
			shift = 1
			if int(list_len[0]) < 0:
				raise Exception('Hours cannot be negative.')
			if len(list_len[1]) != 2:
				raise Exception("Two digits represent minutes, if duration is more than an hour.")

		if int(list_len[0 + shift]) < 0: 
			raise Exception('Minutes cannot be negative.')
		elif int(list_len[0 + shift]) > 59:
			raise Exception('Minutes cannot be more than 59.')

		if int(list_len[1 + shift]) < 0:	 
			raise Exception('Seconds cannot be negative.')
		elif int(list_len[1 + shift]) > 59:
			raise Exception('Seconds cannot be more than 59.')
			
		if len(list_len[1 + shift]) != 2 :
			raise Exception('Two digits represent seconds.')

		time = [int(elem) == 0 for elem in list_len]
		
		if all(time):
			raise Exception("Duration's length cannot be zero.")

class Song:
	# Constructor
	
	def __init__(self, title, artist, album, length):
		self.validate_argument(title)
		self.validate_argument(artist)
		self.validate_argument(album)

		self._length = Duration(length)
		self.title = title
		self.artist = artist
		self.album = album

	# Dunders

	def __str__(self):
		return f'{self.artist} - {self.title} from {self.album} - {self._length}'

	def __eq__(self, other):
		return 	self.artist == other.artist and\
				self.title == other.title and\
				self.album == other.album and\
				self._length == other._length

	def __hash__(self):
		return int(getattr(self._length, 'seconds'))

	# Public

	def length(self, hours = None, minutes = None, seconds = None):
		if hours == True and minutes == None and seconds == None:
			result =getattr(self._length, 'hours')	
		elif minutes == True and hours == None and seconds == None:
			result =int(getattr(self._length, 'hours')) * 60 +\
					int(getattr(self._length, 'minutes'))	
		elif seconds == True and hours == None and minutes == None:
			result =int(getattr(self._length, 'seconds')) +\
					int(getattr(self._length, 'minutes')) * 60 +\
					int(getattr(self._length, 'hours')) * 3600
		elif hours == None and minutes == None and seconds == None:
			return str(self._length)
		else:
			raise Exception('Argument mismatch in function call.')

		return str(result)

	# Static

	@staticmethod
	def validate_argument(argument):
		if type(argument) is not str:
			raise Exception('All arguments must be of "str" type.')
		if argument == '':
			raise Exception('Empty string cannot be an argument.')

class Playlist:
	__played_songs = []

	# Constructor

	def __init__(self, name, repeat = False, shuffle = False):
		self.validate_name(name)
		self.validate_repeat(repeat)
		self.validate_shuffle(shuffle)

		self.name = name
		self.repeat = repeat
		self.shuffle = shuffle
		self.songs = []
		self.index = 0

	# Dunders

	def __eq__(self, other):
		for elem in self.songs:
			if elem not in other.songs:
				return False

		return True

	# Public

	def add_song(self, song):
		if song in self.songs:
			raise Exception('Song is already in the playlist.')

		self.songs.append(song)

	def remove_song(self, song):
		if song in self.songs:
			self.songs.remove(song)
		else:
			raise Exception(f'{song.title} is not in this playlist.')

	def total_length(self):
		if self.songs == []:
			return '0:00'

		total_seconds = 0

		for elem in self.songs:
			total_seconds += int(getattr(getattr(elem, '_length'), 'hours')) * 3600
			total_seconds += int(getattr(getattr(elem, '_length'), 'minutes')) * 60
			total_seconds += int(getattr(getattr(elem, '_length'), 'seconds'))

		total_hours = total_seconds // 3600 
		total_seconds = total_seconds - (total_hours * 3600) 
		total_minutes = total_seconds // 60
		total_seconds = total_seconds - (total_minutes * 60)
		
		if total_hours == 0:
			return f'{total_minutes}:{total_seconds}'
		else:
			if total_minutes < 10:
				if total_seconds < 10:
					return f'{total_hours}:0{total_minutes}:0{total_seconds}'
				else:
					return f'{total_hours}:0{total_minutes}:{total_seconds}'
			else:
				return f'{total_hours}:{total_minutes}:{total_seconds}'

	def artists(self):
		histogram = {}

		for elem in self.songs:
			if getattr(elem, 'artist') in histogram.keys():
				histogram[getattr(elem, 'artist')] += 1
			else:
				histogram[getattr(elem, 'artist')] = 1

		return histogram

	def next_song(self):
		if 	self.repeat == True and self.shuffle == False:
			if self.index == len(self.songs) - 1:
				self.index = 0
				return self.songs[self.index]
			else:
				self.index += 1
				return self.songs[self.index]
		elif self.repeat == False and self.shuffle == False:
			if self.index == len(self.songs) - 1:
				return 'There are no more songs in your playlist.'
				
			else:
				self.index += 1
				return self.songs[self.index]

		elif self.repeat == False and self.shuffle == True:
			if len(self.__played_songs) == len(self.songs):
				return 'There are no more songs in your playlist.'
				 
			else:
				while True:
					random = randint(0, len(self.songs) - 1)

					if self.songs[random] not in self.__played_songs:
						self.index += 1
						self.__played_songs.append(self.songs[random])
						return self.songs[random]
						break
		else:
			if len(self.__played_songs) == len(self.songs):
				self.__played_songs = []
				random = randint(0, len(self.songs) - 1)
				self.__played_songs.append(self.songs[random])
				return self.songs[random]
			else:
				while True:
					random = randint(0, len(self.songs) - 1)

					if self.songs[random] not in self.__played_songs:
						self.__played_songs.append(self.songs[random])
						return self.songs[random]

	def save(self):
		my_dir = '/home/sktuan/Documents/Python-Course-101/week03/04.MusicLibrary/playlist-data'
		
		playlist_name = self.name.replace(' ', '-')
		fname = os.path.join(my_dir, playlist_name)
		
		with open(fname, 'w') as f:
			json_data = json.dumps(self.__dict__, indent=4, default=serialize_song)
			f.write(json_data)
			
	# Static

	@staticmethod		
	def load(path = '/home/sktuan/Documents/Python-Course-101/week03/04.MusicLibrary/playlist-data/Code.txt'):
		my_dir = '/home/sktuan/Documents/Python-Course-101/week03/04.MusicLibrary/playlist-data/'
		
		with open(my_dir + str(path), 'r') as f:
			# Reads example.json file
			my_read_object = json.load(f)
			
			new_obj = Playlist(	name = my_read_object['name'],\
								repeat = my_read_object['repeat'],\
								shuffle = my_read_object['shuffle'])
		
			loaded_songs = my_read_object['songs']

			for elem in loaded_songs:
				to_add = elem.split('-')
				new_song = Song(to_add[0], to_add[1], to_add[2], to_add[3])
				new_obj.add_song(new_song)

			return new_obj

	@staticmethod
	def validate_name(name):
		if type(name) is not str:
			raise Exception('Name must be of "str" type.')
		if name == '':
			raise Exception('Empty string cannot be a name.')

	@staticmethod
	def validate_repeat(repeat):
		if type(repeat) is not bool:
			raise Exception('Repeat must be of "bool" type.')

	@staticmethod
	def validate_shuffle(shuffle):
		if type(shuffle) is not bool:
			raise Exception('Shuffle must be of "bool" type.')

def main():
	f = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
	s = Song(title="Empty", artist="Metric", album="Live It Out", length="5:55")
	q = Song(title="Superman", artist="Eminem", album="The Eminem Show", length="5:50")
	code_songs = Playlist(name="Code", repeat=True, shuffle=True)

	code_songs.add_song(f)
	code_songs.add_song(s)
	code_songs.add_song(q)

	print(f.length(seconds = True))

	print(code_songs.artists())

	print(code_songs.total_length())

	print(code_songs.next_song())
	print(code_songs.next_song())
	print(code_songs.next_song())
	print(code_songs.next_song())
	print(code_songs.next_song())
	print(code_songs.next_song())
	print(code_songs.next_song())
	print(code_songs.next_song())
	print(code_songs.next_song())

	code_songs.save()
	code_songs2 = Playlist.load('Code')
	
	print(code_songs == code_songs2)

if __name__ == '__main__':
	main()