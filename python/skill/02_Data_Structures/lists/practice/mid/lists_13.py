arr = [2, 7, 11, 15]
target = 9
seen = {}

for index, num in enumerate(arr):
    other = target - num
    
    if other in seen:
        print([seen[other], index])
        break
    
    seen[num] = index