'''
৫. List এর সব সংখ্যার square বের করো

map() এবং lambda ব্যবহার করো।
'''

nums = [1, 2, 3, 4, 5]

sqrs = list(map(lambda x: x **2 , nums))
print(sqrs)