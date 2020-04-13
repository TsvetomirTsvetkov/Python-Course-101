# book_reader.py
import os
from zipfile import ZipFile


def clear():
    os.system('clear')


def book_reader(filename):
    found_chapter = 0
    result = ''

    with ZipFile(filename, 'r') as book:
        list_of_files = book.namelist()

        for elem in list_of_files:
            clear()

            with open(elem, 'r') as f:
                for row in f:
                    if row[0] == '#':
                        found_chapter += 1
                    if found_chapter == 2:
                        found_chapter = 1
                        yield result
                        clear()
                        result = ''
                    result += row


def main():
    book = book_reader('Book.zip')

    for chapter in book:
        print(chapter)
        test = input()
        if test == ' ':
            continue
        else:
            print(f"Unrecognized command: '{str(test)}'")
            break


if __name__ == '__main__':
    main()
