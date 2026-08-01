nums = [i for i in range(10)]
print(nums)

squares = [num **2 for num in nums]

final = [num if num > 5 else "smaller" for num in squares]

print(final)