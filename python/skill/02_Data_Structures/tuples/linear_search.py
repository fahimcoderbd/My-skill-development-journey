colors = ("red", "green", "blue")

give_color = input("Enter a color: ")

#linear search
if give_color in colors:
    print(f"{give_color}, exists!")
else:
    print(f"{give_color}, not exists!")