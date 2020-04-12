# silence_decorator.py
# TODO: Fix!


def silence(filename):
    def helper(func):
        def helper2(*args):
            for elem in args:
                try:
                    func(elem)
                except ValueError as err:
                    with open(filename, 'a+') as f:
                        f.write(f"Calling {func.__name__} raised an error - {type(err).__name__}: '{err}'. Provided arguments: {args}\n")
            return
        return helper2
    return helper


@silence('errors.txt')
def foo(x):
    if x > 50:
        raise ValueError('Omg.')


foo(10)
foo(100)

# in errors.txt
# Calling `foo` raised an error - ValueError: 'Omg.'. Provided arguments: (100, ).
