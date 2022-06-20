def type_logger(func):
    def wrapper(*args, **kwargs):
        _args = []
        for arg in args + tuple(kwargs.values()):
            _args.append(f'{arg}: {type(arg)}')
        print(f'{func.__name__}({", ".join(_args)})')
        result = func(*args, **kwargs)
        print(type(result))
        return result

    return wrapper


@type_logger
def calc_cube(x, y):
    return x ** 3


print(calc_cube(3, 5))
