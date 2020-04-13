# book_generator.yp
from random import randint
from book_reader import book_reader
from zipfile import ZipFile


def book_generator(chapters_count, chapter_length_range):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    diversity = {0: '. ', 1: '\n'}
    chapter_number = 1
    result = ''

    with open('book.txt', '+a') as f:
        for current_chapter in range(chapters_count):
            result = f'# Chapter {chapter_number}\n'
            chapter_number += 1
            to_upper = True

            for index in range(chapter_length_range):
                length = randint(1, 10)
                word = ''
                for char in range(length):
                    word += characters[randint(0, 25)]
                if to_upper:
                    to_list = list(word)
                    to_list[0] = to_list[0].upper()
                    word = ''.join(to_list)
                    to_upper = False
                random_symbol = randint(0, 10)
                if random_symbol != 7:
                    result += word + ' '
                else:
                    result += word
                    symbol = diversity[randint(0, 1)]
                    to_upper = True
                    if symbol == '\n':
                        symbol = '.' + symbol
                    result += symbol
                word = ''
            if result[len(result) - 1] != '.' and result[len(result) - 1] != '\n':
                result += '.\n\n'
            else:
                result += '\n'

            f.write(result)

            yield result
            result = ''


def main():
    book = book_generator(4, 50)
    for chapter in book:
        pass

    with ZipFile('Book2.zip', 'w') as new_book:
        new_book.write('book.txt')

    read_book = book_reader('Book2.zip')
    for chapter in read_book:
        print(chapter)
        test = input()
        if test == ' ':
            continue
        else:
            print(f"Unrecognized command: '{str(test)}'")
            break


if __name__ == '__main__':
    main()
