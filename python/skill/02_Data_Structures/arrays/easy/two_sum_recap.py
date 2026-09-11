#two sum
def two_sum(arr, target):
    seen = {}

    for i,num in enumerate(arr):
        next_num = target - num

        if next_num in seen:
            return [seen[next_num] , i]
        
        seen[num] = i

    return [] #no sollution

