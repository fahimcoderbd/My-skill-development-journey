#iterable list
my_names = ["Fahim", "Niloy", "Abrar"]

#iterable => iterator
name = iter(my_names)

#printing values
print(next(name)) #Fahim
print(next(name)) #Niloy
print(next(name)) #Abrar