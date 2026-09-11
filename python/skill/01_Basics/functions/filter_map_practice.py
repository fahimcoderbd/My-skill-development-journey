nums = [10, 15, 20, 25, 30]

# 1. list এর length বের করো
# 2. max এবং min বের করো
# 3. শুধু even সংখ্যা বের করো
# 4. সব সংখ্যাকে 2 দিয়ে গুণ করো

length = len(nums)
maximum = max(nums)
minimum = min(nums)
even = list(filter(lambda x: x % 2 == 0, nums))
doubled = list(map(lambda x: x * 2, nums))

print("Length:", length)
print("Max:", maximum)
print("Min:", minimum)
print("Even numbers:", even)
print("Doubled numbers:", doubled)
