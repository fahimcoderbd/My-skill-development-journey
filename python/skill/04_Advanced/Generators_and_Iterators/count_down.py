#count down generator

def count_down(n):
    for i in range(n,0,-1):
        yield i

counter = count_down(5)

for count in counter:
    print(count)
        