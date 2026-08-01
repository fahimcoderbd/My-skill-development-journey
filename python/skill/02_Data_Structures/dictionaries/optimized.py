'''
1️⃣ Count characters

Problem:
Given a string,
 count how many times each character appears using a dictionary.
'''

text = "banana"
count = {}

""" for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1 """

#optimized
for char in text:
    count[char] = count.get(char ,0) + 1

print(count)

