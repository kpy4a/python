def val_checker(callback_func):
    def _checker(func):
        def wrapper(*args, **kwargs):
            if not callback_func(args[0]):
                raise ValueError(f"Wrong value {args[0]}")
            return func(*args, **kwargs)

        return wrapper

    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))