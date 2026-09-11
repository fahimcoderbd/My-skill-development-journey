
max_num = int(input("Enter a max num: "))
odd_numbers = []

for i in range(max_num+1):
    if i % 2 == 1:
       odd_numbers.append(i)

print(len(odd_numbers))