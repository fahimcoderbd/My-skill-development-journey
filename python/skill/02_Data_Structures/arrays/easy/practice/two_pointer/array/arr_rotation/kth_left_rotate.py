#k er jonno array left rotate k times
#array er element gulake k man porjonto rotate korbo

array = [1,3,9,10,3]
arr2 = [10,20,30,40,50]
k = 2

def left_rotate(arr,k):
    if not arr:
        return None
    
    
    for i in range(k):
        first_el = arr[0]

        for el_index in range(len(arr) - 1):
            arr[el_index] = arr[el_index+1]

        arr[-1] = first_el

    return arr

print(left_rotate(array,k))
print(left_rotate(arr2,k))