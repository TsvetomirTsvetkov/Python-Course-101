# accepts_decorator.py
def accepts(*args1):
    def helper(func):
        def helper2(*args2):
            for elem1, elem2 in zip(args1, args2):
                if elem1 != type(elem2):
                    raise TypeError(f'Argument {elem2} is not {elem1.__name__}!')
                return func(*args2)
        return helper2
    return helper
