'''
৮. নামগুলো Length অনুযায়ী Sort করো

sorted() এবং lambda ব্যবহার করো।
'''

names = ["Fahim", "Ali", "Abrar", "Python"]

sorted_names = sorted(names, key=len)

print(sorted_names)