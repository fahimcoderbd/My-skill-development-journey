'''
📚 Lesson 2: Lambda Functions
What is Lambda?

Lambda হলো এক লাইনের ছোট function।
'''

#instead of
def square(x:int) -> int:
    return x * x

#usage
print(square(5))

#lambda function
sq2 = lambda x: x * x 
print(sq2(5))