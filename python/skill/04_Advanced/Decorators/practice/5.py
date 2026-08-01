def decorator(func):
    def wrapper():
        result = func() * 2
        return result
    return wrapper


@decorator
def number_result():
    number = 2
    return number


print(number_result())