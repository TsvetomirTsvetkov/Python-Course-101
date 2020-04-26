# deep_compare.py
from collections import Iterable


def deep_compare(obj1, obj2):
    if type(obj1) is not type(obj2):
        return False

    if len(obj1) != len(obj2):
        return False

    if obj1 != obj2:
        return False

    if type(obj1) is dict:
        for index in obj1.keys():
            if obj1[index] is iter and index in obj2.keys() and obj1[index] == obj2[index]:
                return True and deep_compare(obj1[index], obj2[index])
            elif obj1[index] is not iter and index in obj2.keys() and obj1[index] == obj2[index]:
                return True

    if isinstance(obj1, Iterable):
        length = len(obj1)
        for index in range(length):
            if obj1[index] is iter and obj1[index] == obj2[index]:
                return True and deep_compare(obj1[index], obj2[index])
            elif obj1[index] is not iter and obj1[index] == obj2[index]:
                return True


testing1 = [1, [2, 8, 9], [3], 4, [5], 6]
testing2 = [1, [2, 8, 9], [3], 4, [5], 6]

testing3 = {'key1': 1, 'key2': {'key3': 3, 'key4': 4}}
testing4 = {'key1': 1, 'key2': {'key3': 3, 'key4': 4}}

testing5 = (1, 2, 3)
testing6 = (1, 2, 3)

print('LIST:')
print(deep_compare(testing1, testing2))
print('DICT:')
print(deep_compare(testing3, testing4))
print('Iterable(TUPLE):')
print(deep_compare(testing5, testing6))
