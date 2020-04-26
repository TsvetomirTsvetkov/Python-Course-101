# frogs.py


def create_swamp(number_of_lilypads, sign1, sign2):
    frogs_count = (int(number_of_lilypads) // 2)

    frogs_left = sign1 * frogs_count
    frogs_right = sign2 * frogs_count

    return f'{frogs_left}_{frogs_right}'


def lists_to_strings(lists_to_convert):
    for curr_list in lists_to_convert:
        helper = ''
        for character in curr_list:
            helper += character
        print(helper)


def change_frogs_positions(lilypads, old_index, new_index):
    tmp = lilypads[old_index]
    lilypads[old_index] = lilypads[new_index]
    lilypads[new_index] = tmp
    return lilypads


def frogs(number_of_lilypads):
    assert number_of_lilypads % 2 != 0 and number_of_lilypads >= 3, 'Lilypads must be an odd number >= 3.'
    beginning = list(create_swamp(number_of_lilypads, '>', '<'))
    end = list(create_swamp(number_of_lilypads, '<', '>'))
    index = number_of_lilypads // 2
    helper = [beginning[:]]

    def find_path(beginning, end, index, helper):
        if beginning == end:
            lists_to_strings(helper)
            print(len(beginning) * '=')
            return

        if index - 1 >= 0 and beginning[index - 1] == '>':
            beginning = change_frogs_positions(beginning, index, index - 1)
            index -= 1
            if beginning not in helper:
                helper.append(beginning)
            find_path(beginning[:], end, index, helper)
            helper.pop()
            beginning = change_frogs_positions(beginning, index, index + 1)
            index += 1

        if index - 2 >= 0 and beginning[index - 2] == '>':
            beginning = change_frogs_positions(beginning, index, index - 2)
            index -= 2
            if beginning not in helper:
                helper.append(beginning)
            find_path(beginning[:], end, index, helper)
            helper.pop()
            beginning = change_frogs_positions(beginning, index, index + 2)
            index += 2

        if index + 1 < len(beginning) and beginning[index + 1] == '<':
            beginning = change_frogs_positions(beginning, index, index + 1)
            index += 1
            if beginning not in helper:
                helper.append(beginning)
            find_path(beginning[:], end, index, helper)
            helper.pop()
            beginning = change_frogs_positions(beginning, index, index - 1)
            index -= 1

        if index + 2 < len(beginning) and beginning[index + 2] == '<':
            beginning = change_frogs_positions(beginning, index, index + 2)
            index += 2
            if beginning not in helper:
                helper.append(beginning)
            find_path(beginning[:], end, index, helper)
            helper.pop()
            beginning = change_frogs_positions(beginning, index, index - 2)
            index -= 2
    find_path(beginning, end, index, helper)


def main():
    number_of_lilypads = input('Enter number of lilypads: ')
    frogs(int(number_of_lilypads))


if __name__ == '__main__':
    main()
