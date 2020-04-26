# frogs.py


def create_swamp(number_of_lilypads, sign1, sign2):
    frogs_count = (int(number_of_lilypads) // 2)

    frogs_left = sign1 * frogs_count
    frogs_right = sign2 * frogs_count

    return f'{frogs_left}_{frogs_right}'


def lists_to_strings(lists_to_convert):
    for curr_list in lists_to_convert:
        print(''.join(curr_list))


def change_frogs_positions(lilypads, old_index_free_lilypad, new_index_free_lilypad):
    tmp = lilypads[old_index_free_lilypad]
    lilypads[old_index_free_lilypad] = lilypads[new_index_free_lilypad]
    lilypads[new_index_free_lilypad] = tmp
    return lilypads


def frogs(number_of_lilypads):
    assert number_of_lilypads % 2 != 0 and number_of_lilypads >= 3, 'Lilypads must be an odd number >= 3.'
    beginning = list(create_swamp(number_of_lilypads, '>', '<'))
    end = list(create_swamp(number_of_lilypads, '<', '>'))
    index_free_lilypad = number_of_lilypads // 2
    jumps_list = [beginning[:]]

    def find_next_jump(beginning, end, index_free_lilypad, jumps_list, new_index_free_lilypad):
        beginning = change_frogs_positions(beginning, index_free_lilypad, new_index_free_lilypad)
        hold_index = index_free_lilypad
        index_free_lilypad = new_index_free_lilypad
        if beginning not in jumps_list:
                jumps_list.append(beginning)
        find_path(beginning[:], end, index_free_lilypad, jumps_list)
        jumps_list.pop()
        beginning = change_frogs_positions(beginning, index_free_lilypad, hold_index)
        index_free_lilypad = hold_index

    def find_path(beginning, end, index_free_lilypad, jumps_list):
        if beginning == end:
            lists_to_strings(jumps_list)
            print(len(beginning) * '=')
            return

        if index_free_lilypad - 1 >= 0 and beginning[index_free_lilypad - 1] == '>':
            find_next_jump(beginning, end, index_free_lilypad, jumps_list, index_free_lilypad - 1)

        if index_free_lilypad - 2 >= 0 and beginning[index_free_lilypad - 2] == '>':
            find_next_jump(beginning, end, index_free_lilypad, jumps_list, index_free_lilypad - 2)

        if index_free_lilypad + 1 < len(beginning) and beginning[index_free_lilypad + 1] == '<':
            find_next_jump(beginning, end, index_free_lilypad, jumps_list, index_free_lilypad + 1)

        if index_free_lilypad + 2 < len(beginning) and beginning[index_free_lilypad + 2] == '<':
            find_next_jump(beginning, end, index_free_lilypad, jumps_list, index_free_lilypad + 2)
    find_path(beginning, end, index_free_lilypad, jumps_list)


def main():
    number_of_lilypads = input('Enter number of lilypads: ')
    frogs(int(number_of_lilypads))


if __name__ == '__main__':
    main()
