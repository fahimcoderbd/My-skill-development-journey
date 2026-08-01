def gen():
    yield 1

g = gen()

print(next(g))
print(dir(g))