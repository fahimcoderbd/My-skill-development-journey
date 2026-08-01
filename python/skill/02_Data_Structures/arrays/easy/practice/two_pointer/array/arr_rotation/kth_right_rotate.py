#k er jonno array right rotate k times
#array er element gulake k man porjonto rotate korbo

#example cases
arr1 = [1,2,3,4,6]
k1 = 2

arr2 = []
k2 = 1

arr3 = [5,4,3,1,2]
k3 = 5

arr4 = [4,2,1,5]
k4 = 0


def right_rotate(arr, k):
    if not arr:
        return arr
    if k == 0:
        return arr
    
    #getting rotation number
    k = k % len(arr)

    #rotating arr for k times

    for _ in range(k):
        last = arr[-1]

        for el in range(len(arr) - 1, 0, -1):
            arr[el] = arr[el-1] #moving right side

        arr[0] = last

    return arr

print(right_rotate(arr1, k1))
print(right_rotate(arr2, k2))
print(right_rotate(arr3, k3))
print(right_rotate(arr4, k4))