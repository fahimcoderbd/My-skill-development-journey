'''
📚 Lesson 1: List Comprehension
🤔 What is it?

List comprehension হলো এক লাইনে list তৈরি করার Pythonic উপায়।

Instead of writing:
numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)

we can do this: 
numbers = [i for i in range(1, 6)]
print(numbers)
'''

'''
Structure
[new_value for item in iterable]
'''

