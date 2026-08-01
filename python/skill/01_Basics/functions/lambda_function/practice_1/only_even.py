'''
৬. শুধু Even সংখ্যা বের করো

filter() এবং lambda ব্যবহার করো।
'''

nums = [1,2,3,4,5,6,7,8]

only_evens = list(filter(lambda x: x % 2 == 0, nums))

print(only_evens)