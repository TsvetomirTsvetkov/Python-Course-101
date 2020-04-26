# deep_update.py


def deep_update(data, key, val):
    assert type(data) is dict, 'Data must be of "dict" type.'

    def iter(data, key, val):
        if type(data) is not dict:
            return
        for x in data.keys():
            if x == key:
                data[x] = val
            iter(data[x], key, val)
    iter(data, key, val)
    return data


testing1 = {'key1': 1, 'key2': 2, 'key3': 3}
testing2 = {'key9': {'key1': 4, 'key5': 5}, 'key2': 2, 'key1': 3}
testing3 = {'key1': {'key4': 4, 'key5': 5}, 'key4': 2, 'key3': {'key4': 6, 'key7': 7}}

print(deep_update(testing1, 'key1', 5))
print(deep_update(testing2, 'key1', 5))
print(deep_update(testing3, 'key4', 42))
