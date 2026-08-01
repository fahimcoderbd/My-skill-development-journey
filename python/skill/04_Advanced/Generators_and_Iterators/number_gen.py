def number_gen():
    num = 0
    while True:
      num += 1
      yield num

num = number_gen()
print(next(num)) #1
print(next(num)) #2
print(next(num)) #3
print(next(num)) #4