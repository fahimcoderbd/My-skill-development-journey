#list looping
numbers = [5, 10, 15, 20]

for num in numbers:
    print(num * 2)

#2nd method
doubled = [num * 2 for num in numbers]
print(doubled)