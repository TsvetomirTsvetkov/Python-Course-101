def group(list):
    groups = []
    curr = []

    for elem in list:
        if elem in curr: 
            curr.append(elem)
        elif len(curr) != 0: 
            groups.append(curr) 
            curr = []
            curr.append(elem)
        elif len(curr) == 0: 
            curr.append(elem)
    
    if curr != []:
        groups.append(curr)
    
    return groups

# We assume that the input is correct.

def numbers_to_message(pressed_sequence):
    list_sequence = group(list(pressed_sequence))
    message = ''
    helper = ''
    capital = False
    hashmap = { 0:' ', 2:'abc', 3:'def',\
                4:'ghi', 5:'jkl', 6:'mno',\
                7:'pqrs', 8:'tuv', 9:'wxyz'}

    for elem in list_sequence:
        if elem[0] == 1:
            capital = True 
            continue  
        
        if elem[0] == -1:
            continue

        index = len(elem)
        helper = hashmap[elem[0]]

        if index > len(helper):
            index //= len(helper)

        if (not capital): 
            message += helper[index - 1]
        else:
            helper = helper.upper() 
            message += helper[index - 1] 
            capital = False
    
    return message

def main():
    print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
    # Expected output : abc

    print(numbers_to_message([2, 2, 2, 2]))
    # Expected output : a
    
    print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))
    # Expected output : Ivo e Panda

if __name__ == '__main__':
    main()