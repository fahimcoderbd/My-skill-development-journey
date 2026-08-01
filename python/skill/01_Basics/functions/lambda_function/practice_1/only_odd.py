'''
৭. শুধু Odd সংখ্যা বের করো
'''

nums = [1,2,3,4,5,6,7,8]

only_odds = list(filter(lambda x: x % 2 != 0, nums))

print(only_odds)