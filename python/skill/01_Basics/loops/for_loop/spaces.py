n = 5

for i in range(n):
    # spaces
    for j in range(i):
        print(" ", end="")
    
    # stars
    for j in range(n - i):
        print("*", end="")
    
    print()