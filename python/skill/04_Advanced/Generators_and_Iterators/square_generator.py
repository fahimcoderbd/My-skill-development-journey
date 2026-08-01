#generate squares of n

def square_generator(n):
    for i in range(1,n+1):
        yield i * i

numbers = square_generator(4)

for num in numbers:
    print(num)