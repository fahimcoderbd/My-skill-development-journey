def process_numbers(num_arr):
    for num in num_arr:
        if num > 10:
          yield num * 2

my_nums = process_numbers([5, 12, 8, 20])
for num in my_nums:
    print(num)