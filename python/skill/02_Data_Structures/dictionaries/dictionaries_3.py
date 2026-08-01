text = "python is easy and python is powerful"
words = text.split()

count = {}

for char in words:
    count[char] = count.get(char, 0) + 1

print(count)