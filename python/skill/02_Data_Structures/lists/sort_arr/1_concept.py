#sort arrange data into ascending and descending format

#Ascending order [1,2,3]
age = [10, 18, 20, 30]
age.sort()
print(age)
#descending order
age.sort(reverse=True)
print(age)

#string
names = ["fahim", "rahib", "mahir"]
names.sort(key=len)
print(names)

names.sort(key=len, reverse=True)
print(names)

