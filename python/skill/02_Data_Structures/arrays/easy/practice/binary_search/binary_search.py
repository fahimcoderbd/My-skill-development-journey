#binary search algorithm

arr = [1,2,3,4,5,11,17,20]
target = 17 #output 7

def binary_search(arr,target):
    low = 0
    high = len(arr) - 1

    while low <= high:
         
         mid = (low + high) // 2

         if arr[mid] == target:
              return mid
         
         elif arr[mid] < target:
              low = mid + 1
        
         else:
              high = mid - 1

    return -1

print(binary_search(arr, target))
              