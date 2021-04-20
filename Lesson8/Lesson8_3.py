LOG_FILENAME = r"func.log"


def log_data(log_file_name, func_name, args, kwargs, result):
    with open(log_file_name, "a", encoding="utf-8") as f:
        data = list()
        # Работа с позиционными параметрами
        if len(args):
            for value in args:
                data.append(f"{value}: {type(value)}")
        # Работа с именованными параметрами
        if len(kwargs):
            for key, value in kwargs.items():
                data.append(f"{key}:{value}: {type(value)}")
        data = ", ".join(data)
        f.write(f"{func_name.__name__}({data}) -> {str(result)} {type(result)}\n")


def type_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_data(LOG_FILENAME, func, args, kwargs, result)
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_pow(x, y):
    return x ** y


print(calc_cube(10))
print(calc_pow(5, 2))
print(calc_pow(x=7, y=3))
