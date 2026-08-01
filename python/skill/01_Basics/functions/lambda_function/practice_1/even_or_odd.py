'''
৪. জোড় না বিজোড়

একটি lambda function লিখো যা সংখ্যা জোড় হলে "Even" এবং বিজোড় হলে "Odd" রিটার্ন করবে।
'''

check = lambda x : "Even" if x % 2 == 0 else "Odd"
print(check(7))