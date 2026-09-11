# kth rotate array for both left and right

# arrays
arr1 = [1,2,3,4,5]
arr2 = []
arr3 = [1]

# value of k
k1 = 0
k2 = -2
k3 = 1000


def right_rotate(arr, k):
    # check empty arr
    if not arr:
        return None

    # if len(arr) < 2
    if len(arr) < 2:
        return arr

    # if k = 0
    if k == 0:
        return arr

    # getting modded value of k
    k = k % len(arr)

    # rotating arr by k side
    for i in range(k):
        last = arr[-1]

        # FIXED: reverse direction shift
        for el in range(len(arr)-1, 0, -1):
            arr[el] = arr[el-1]

        arr[0] = last

    return arr


def left_rotate(arr, k):

    # check empty arr
    if not arr:
        return None

    # if len(arr) < 2
    if len(arr) < 2:
        return arr

    # if k = 0
    if k == 0:
        return arr

    # negative k means right rotate
    if k < 0:
        return right_rotate(arr, abs(k))

    # getting modded value of k
    k = k % len(arr)

    # rotating arr by k side
    for i in range(k):
        first = arr[0]

        for el in range(len(arr)-1):
            arr[el] = arr[el+1]

        arr[-1] = first

    return arr
    

    