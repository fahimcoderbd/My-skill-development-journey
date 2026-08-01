def infinite_numbers():
    i = 0
    while True:
        yield i
        i += 2

number = infinite_numbers()
print(next(number))
print(next(number))