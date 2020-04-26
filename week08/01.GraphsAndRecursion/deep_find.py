# deep_find.py


def deep_find_bfs(data, key):
    assert type(data) is dict, 'Data must be of "dict" type.'
    bfs = {}

    def iter(data, key, bfs):
        if type(data) is not dict:
            return
        for x in data.keys():
            bfs[x] = data[x]
            iter(data[x], key, bfs)
        return bfs
    iter(data, key, bfs)

    if key in bfs.keys():
        return bfs[key]


def deep_find_dfs(data, key):
    assert type(data) is dict, 'Data must be of "dict" type.'
    dfs = {}

    def iter(data, key, dfs):
        if type(data) is not dict:
            return

        for x in data.keys():
            if type(data) is dict:
                iter(data[x], key, dfs)
                dfs[x] = data[x]

    iter(data, key, dfs)

    if key in dfs.keys():
        return dfs[key]


testing1 = {'key1': 1, 'key2': 2, 'key3': 3}
testing2 = {'key1': {'key4': 4, 'key5': 5}, 'key2': 2, 'key3': 3}
testing3 = {'key1': {'key4': 4, 'key5': 5}, 'key2': 2, 'key3': {'key6': 6, 'key7': 7}}

print('BFS Solution:')
print(deep_find_bfs(testing1, 'key3'))
print(deep_find_bfs(testing2, 'key5'))
print(deep_find_bfs(testing3, 'key7'))

print('DFS Solution:')
print(deep_find_dfs(testing1, 'key3'))
print(deep_find_dfs(testing2, 'key5'))
print(deep_find_dfs(testing3, 'key7'))
