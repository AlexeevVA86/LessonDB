def val_checker(predicate):
    def _val_checker(func):
        @wraps(func)  ## не совсем понял зачем мне здесь это
        def wrapper(*args, **kwargs):
            for arg in args + tuple(kwargs.values()):
                if not predicate(arg):
                    raise ValueError
            return func(*args, **kwargs)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube2(x):
    return x ** 3


print(calc_cube2(2))
