# deep_find_all.py


def deep_find_all_bfs(data, key):
    assert type(data) is dict, 'Data must be of "dict" type.'
    bfs_values = []

    def iter(data, key, bfs_values):
        if type(data) is not dict:
            return
        for x in data.keys():
            if x == key:
                bfs_values.append(data[x])
            iter(data[x], key, bfs_values)
    iter(data, key, bfs_values)
    return bfs_values


def deep_find_all_dfs(data, key):
    assert type(data) is dict, 'Data must be of "dict" type.'
    dfs_values = []

    def iter(data, key, dfs_values):
        if type(data) is not dict:
            return

        for x in data.keys():
            if type(data) is dict:
                iter(data[x], key, dfs_values)
                if x == key:
                    dfs_values.append(data[x])
    iter(data, key, dfs_values)
    return dfs_values


testing1 = {'key1': 1, 'key2': 2, 'key3': 3}
testing2 = {'key1': {'key4': 4, 'key3': 5}, 'key2': 2, 'key3': 3}
testing3 = {'key1': {'key7': 4, 'key3': 5}, 'key2': 2, 'key3': {'key6': 6, 'key7': 7}}

print('BFS Solution:')
print(deep_find_all_bfs(testing1, 'key3'))
print(deep_find_all_bfs(testing2, 'key5'))
print(deep_find_all_bfs(testing3, 'key7'))

print('DFS Solution:')
print(deep_find_all_dfs(testing1, 'key3'))
print(deep_find_all_dfs(testing2, 'key5'))
print(deep_find_all_dfs(testing3, 'key7'))
