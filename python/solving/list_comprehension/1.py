a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
m = int(input("Enter a number: "))

#store the final 3d list
final_list = []

for i in range(a+1): #slow ghurbe
     for j in range(b+1): #medium ghurbe
         for k in range(c+1): #fast ghurbe
              if i * j * k != m:
                   final_list.append([i,j,k])

print(final_list)