# cycle.py
def cycle(iterable):
    index = 0
    length = len(iterable)
    while True:
        for index in range(length):
            yield index


endless = cycle(range(0, 10))

for item in endless:
    print(item)
