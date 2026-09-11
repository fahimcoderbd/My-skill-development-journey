'''User থেকে 5টা number নাও →
 list এ রাখো → max বের করো'''

num_list = [] #store numbers

for i in range(1,6):
    num = int(input(f"Enter num {i}: "))
    num_list.append(num) 

print(f"The max is, {max(num_list)}")