# tests_music_library.py

import unittest
from music_library import (
	Duration,
	Song,
	Playlist
)

# Duration

class TestDurationValidateLength(unittest.TestCase):
	def test_length_validation_raises_exception_if_less_than_4_characters(self):
		length = ':22'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Length cannot be less than 4 symbols.')

	def test_length_validation_raises_exception_if_no_dots(self):
		length = '5555'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Length must have ":" to distinguish seconds, minutes and hours.')

	def test_length_validation_raises_exception_if_more_than_2_dots(self):
		length = '5:3:5:'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Length can only include seconds, minutes and hours.')

	def test_length_validation_raises_exception_if_dots_are_not_placed_correctly(self):
		length = '5::5'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Error: Found ":" in an unexpected position.')

	def test_length_validation_raises_exception_if_minutes_greater_than_sixty(self):
		length = '63:05'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Minutes cannot be more than 59.')

	def test_length_validation_raises_exception_if_minutes_less_than_zero(self):
		length = '-63:05'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Minutes cannot be negative.')

	def test_length_validation_raises_exception_if_seconds_greater_than_sixty(self):
		length = '20:65'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Seconds cannot be more than 59.')

	def test_length_validation_raises_exception_if_seconds_less_than_zero(self):
		length = '5:-25'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Seconds cannot be negative.')

	def test_length_validation_raises_exception_if_seconds_not_represented_by_two_digits(self):
		length = '45:2'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Two digits represent seconds.')

	def test_length_validation_raises_exception_if_hours_less_than_zero(self):
		length = '-3:45:2'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Hours cannot be negative.')

	def test_length_validation_raises_exception_if_Duration_length_is_zero(self):
		length = '00:00'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), "Duration's length cannot be zero.")

	def test_length_validation_raises_exception_if_mins_not_represented_by_two_digits_if_hour(self):
		length = '1:5:22'
		exc = None

		try:
			Duration.is_valid_length(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), "Two digits represent minutes, if duration is more than an hour.")
	
	def test_length_validation_passes_with_correct_input(self):
		Duration.is_valid_length('0:01')
		Duration.is_valid_length('50:21')
		Duration.is_valid_length('1:10:01')
		Duration.is_valid_length('10:00')
		Duration.is_valid_length('0:55')

class TestDurationInit(unittest.TestCase):
	def test_duration_init_correctly_initializes_an_object(self):
		test1 = Duration('5:55')
		test2 = Duration('6:23:11')

		self.assertEqual(test1.hours, '0')
		self.assertEqual(test1.minutes, '5')
		self.assertEqual(test1.seconds, '55')

		self.assertEqual(test2.hours, '6')
		self.assertEqual(test2.minutes, '23')
		self.assertEqual(test2.seconds, '11')

class TestDurationStrDunder(unittest.TestCase):
	def test_duration_str_dunder_representation_is_as_expected(self):
		test1 = Duration('5:55')
		test2 = Duration('6:23:11')

		self.assertEqual(str(test1), '5:55')
		self.assertEqual(str(test2), '6:23:11')

class TestDurationEqDunder(unittest.TestCase):
	def test_duration_eq_dunder_correctly_compares_duration_objects(self):
		test1 = Duration('5:55')
		test2 = Duration('5:55')
		test3 = Duration('6:23:11')
		self.assertEqual(test1, test2)
		self.assertNotEqual(test2, test3)

# Song

class TestSongValidateArguments(unittest.TestCase):		# TODO!!!
	def test_song_validate_argument_passes_with_correct_input(self):
		test = 'Test'

		Song.validate_argument(test)

	def test_song_validate_argument_raises_exception_if_argument_type_not_str(self):
		test = 5
		exc = None

		try:
			Song.validate_argument(test)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'All arguments must be of "str" type.')

	def test_song_validate_argument_raises_exception_if_argument_is_empty_string(self):
		test = ''
		exc = None

		try:
			Song.validate_argument(test)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Empty string cannot be an argument.')

class TestSongInit(unittest.TestCase):
	def test_song_init_correctly_inicializes_object(self):
		test = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		
		self.assertEqual(test.title, 'Odin')
		self.assertEqual(test.artist, 'Manowar')
		self.assertEqual(test.album, 'The Sons of Odin')		
		self.assertEqual(str(test._length), '3:44')

class TestSongStrDunder(unittest.TestCase):
	def test_song_str_dunder_representation_is_as_expected(self):
		test = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

		self.assertEqual(str(test), 'Manowar - Odin from The Sons of Odin - 3:44')


class TestSongEqDunder(unittest.TestCase):
	def test_song_eq_dunder_correctly_compares_objects(self):
		test1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		test2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		test3 = Song(title="Metric", artist="Empty", album="Live It Out", length="5:55")

		self.assertEqual(test1, test2)
		self.assertNotEqual(test2, test3)

class TestSongHashDunder(unittest.TestCase):
	def test_song_hash_dunder_works_as_expected_when_adding_same_key(self):
		test1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		test2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		
		songs = {}

		songs[test1] = 1

		if test2 in songs:
		    songs[test2] += 1

		self.assertEqual(songs[test1], 2)
		self.assertEqual(len(songs), 1)

	def test_song_hash_dunder_works_as_expected_when_adding_key_the_first_time(self):
		test = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		
		songs = {}

		songs[test] = 1

		self.assertEqual(songs[test], 1)

class TestSongLen(unittest.TestCase):
	def test_song_len_correctly_returns_seconds_when_called_with_seconds(self):
		test = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

		self.assertEqual(test.length(seconds = True), '224')
	
	def test_song_len_correctly_returns_minutes_when_called_with_minutes(self):
		test1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		test2 = Song(title="TEST", artist="TEST", album="TEST", length="2:43:44")

		self.assertEqual(test1.length(minutes = True), '3')
		self.assertEqual(test2.length(minutes = True), '163')

	
	def test_song_len_correctly_returns_hours_when_called_with_hours(self):
		test1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		test2 = Song(title="TEST", artist="TEST", album="TEST", length="2:43:44")
		
		self.assertEqual(test1.length(hours = True), '0')
		self.assertEqual(test2.length(hours = True), '2')

	def test_song_len_correctly_returns_str_representation_when_called_without_arguments(self):
		test = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

		self.assertEqual(test.length(), '3:44')

	def test_song_len_raises_exception_when_called_with_wrong_arguments(self):
		test = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		exc = None

		try:
			self.assertEqual(test.length(seconds = False), '')
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Argument mismatch in function call.')

# Playlist

class TestPlaylistValidateName(unittest.TestCase):
	def test_playlist_validate_name_raises_exception_if_name_not_str(self):
		test = 5
		exc = None

		try:
			Playlist.validate_name(test)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Name must be of "str" type.')

	def test_playlist_validate_name_raises_exception_if_name_is_empty_str(self):
		test = ''
		exc = None

		try:
			Playlist.validate_name(test)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Empty string cannot be a name.')

	def test_playlist_validate_name_passes_with_correct_input(self):
		test = 'code'

		Playlist.validate_name(test)

class TestPlaylistValidateRepeat(unittest.TestCase):
	def test_playlist_validate_repeat_raises_exception_if_repeat_not_bool(self):
		test = 5
		exc = None

		try:
			Playlist.validate_repeat(test)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Repeat must be of "bool" type.')

	def test_playlist_validate_repeat_passes_with_correct_input(self):
		test = True

		Playlist.validate_repeat(test)

class TestPlaylistValidateShuffle(unittest.TestCase):
	def test_playlist_validate_shuffle_raises_exception_if_shuffle_not_bool(self):
		test = 5
		exc = None

		try:
			Playlist.validate_shuffle(test)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Shuffle must be of "bool" type.')

	def test_playlist_validate_shuffle_passes_with_correct_input(self):
		test = True

		Playlist.validate_shuffle(test)

class TestPlaylistInit(unittest.TestCase):
	def test_playlist_init_initializes_object_correctly(self):
		code_songs = Playlist(name="Code", repeat=True, shuffle=False)

		self.assertEqual(code_songs.name, 'Code')
		self.assertEqual(code_songs.repeat, True)
		self.assertEqual(code_songs.shuffle, False)

class TestPlaylistAddSong(unittest.TestCase):
	def test_playlist_add_song_adds_song_to_object_list_of_songs(self):
		test = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		my_playlist = Playlist(name="Code", repeat=True, shuffle=True)

		my_playlist.add_song(test)

		assert test in my_playlist.songs

	def test_playlist_add_song_raises_excpetion_if_song_already_in_playlist(self):
		test1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		test2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		my_playlist = Playlist(name="Code", repeat=True, shuffle=True)
		exc = None

		my_playlist.add_song(test1)

		try:
			my_playlist.add_song(test2)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Song is already in the playlist.')

class TestPlaylistRemoveSong(unittest.TestCase):
	def test_playlist_remove_song_removes_song_from_object_list_of_songs(self):
		test = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		my_playlist = Playlist(name="Code", repeat=True, shuffle=True)

		my_playlist.add_song(test)
		my_playlist.remove_song(test)

		self.assertEqual(my_playlist.songs, [])

	def test_playlist_remove_song_raises_exception_if_song_not_in_object_list_of_songs(self):
		test = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		my_playlist = Playlist(name="Code", repeat=True, shuffle=True)
		exc = None

		try:
			my_playlist.remove_song(test)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), f'{test.title} is not in this playlist.')


class TestPlaylistArtists(unittest.TestCase):
	def test_playlist_artists_works_as_expected(self):
		my_playlist = Playlist(name="Code", repeat=True, shuffle=True)
		test = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		
		my_playlist.add_song(test)

		self.assertEqual(my_playlist.artists(), {'Manowar' : 1})


class TestPlaylistTotalLength(unittest.TestCase):
	def test_playlist_total_length_is_calculated_correctly_without_any_songs(self):
		my_playlist = Playlist(name="Code", repeat=True, shuffle=True)

		self.assertEqual(my_playlist.total_length(), '0:00')

	def test_playlist_total_length_is_calculated_correctly_with_songs_under_a_minute(self):
		my_playlist = Playlist(name="Code", repeat=True, shuffle=True)
		test1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="0:44")
		test2 = Song(title="Empty", artist="Metric", album="Live It Out", length="0:10")

		my_playlist.add_song(test1)
		my_playlist.add_song(test2)

		self.assertEqual(my_playlist.total_length(), '0:54')

	def test_playlist_total_length_is_calculated_correctly_with_songs_sum_over_minute(self):
		my_playlist = Playlist(name="Code", repeat=True, shuffle=True)
		test1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="0:44")
		test2 = Song(title="Empty", artist="Metric", album="Live It Out", length="0:55")

		my_playlist.add_song(test1)
		my_playlist.add_song(test2)

		self.assertEqual(my_playlist.total_length(), '1:39')

	def test_playlist_total_length_is_calculated_correctly_with_songs_sum_over_hour(self):
		my_playlist = Playlist(name="Code", repeat=True, shuffle=True)
		test1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="55:44")
		test2 = Song(title="Empty", artist="Metric", album="Live It Out", length="5:16")
		
		my_playlist.add_song(test1)
		my_playlist.add_song(test2)

		self.assertEqual(my_playlist.total_length(), '1:01:00')

class TestPlaylistNextSong(unittest.TestCase):
	def test_playlist_next_song_works_as_expected_with_repeat_and_no_shuffle(self):
		f = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		s = Song(title="Empty", artist="Metric", album="Live It Out", length="5:55")
		q = Song(title="Superman", artist="Eminem", album="The Eminem Show", length="5:50")
		code_songs = Playlist(name="Code", repeat=True, shuffle=False)

		code_songs.add_song(f)
		code_songs.add_song(s)
		code_songs.add_song(q)

		code_songs.next_song()
		code_songs.next_song()
		
		self.assertEqual(code_songs.next_song(), f)

	def test_playlist_next_song_works_as_expected_with_no_repeat_and_no_shuffle(self):
		f = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		s = Song(title="Empty", artist="Metric", album="Live It Out", length="5:55")
		q = Song(title="Superman", artist="Eminem", album="The Eminem Show", length="5:50")
		code_songs = Playlist(name="Code", repeat=False, shuffle=False)

		code_songs.add_song(f)
		code_songs.add_song(s)
		code_songs.add_song(q)

		code_songs.next_song()
		code_songs.next_song()
		
		self.assertEqual(code_songs.next_song(), 'There are no more songs in your playlist.')

	def test_playlist_next_song_works_as_expected_with_no_repeat_and_shuffle(self):
		f = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		s = Song(title="Empty", artist="Metric", album="Live It Out", length="5:55")
		q = Song(title="Superman", artist="Eminem", album="The Eminem Show", length="5:50")
		code_songs = Playlist(name="Code", repeat=False, shuffle=True)
		test = Playlist(name="Code2", repeat=False, shuffle=True)

		code_songs.add_song(f)
		code_songs.add_song(s)
		code_songs.add_song(q)


		test.add_song(code_songs.next_song())
		test.add_song(code_songs.next_song())
		test.add_song(code_songs.next_song())
		
		self.assertEqual(code_songs, test)

	def test_playlist_next_song_works_as_expected_with_repeat_and_shuffle(self):
		f = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		s = Song(title="Empty", artist="Metric", album="Live It Out", length="5:55")
		q = Song(title="Superman", artist="Eminem", album="The Eminem Show", length="5:50")
		code_songs = Playlist(name="Code", repeat=True, shuffle=True)
		test = Playlist(name="Code2", repeat=True, shuffle=True)

		code_songs.add_song(f)
		code_songs.add_song(s)
		code_songs.add_song(q)


		test.add_song(code_songs.next_song())
		test.add_song(code_songs.next_song())
		test.add_song(code_songs.next_song())

		code_songs.next_song()
		
		assert code_songs.next_song() in getattr(test, 'songs')


if __name__ == '__main__':
	unittest.main()