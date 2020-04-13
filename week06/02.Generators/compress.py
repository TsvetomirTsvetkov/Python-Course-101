# compress.py


def compress(iterable, mask):
    result = []

    for elem in zip(iterable, mask):
        if elem[1] is True:
            result.append(elem[0])

    return result


list(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
