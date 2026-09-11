nums = [3, 6, 9, 12, 15, 18]

# 1. 10 এর বেশি সংখ্যা বের করো
# 2. সব সংখ্যার square বের করো
# 3. square গুলোর sum বের করো
# 4. check করো সব সংখ্যা 3 দিয়ে divisible কিনা

besi = list(filter(lambda x: x > 10, nums))
square = list(map(lambda x:x ** 2, nums))
sum_of_sqrs = sum(square)
print(besi)
print(square)
print(sum_of_sqrs)
divisible = all(map(lambda x:x % 3 == 0, nums))
print(divisible)