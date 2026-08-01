#reverse an arra [two pointer method]

#test cases
arr1 = [1,2,3,4]

left = 0
right = len(arr1) - 1

while left < right:
    arr1[left], arr1[right] = arr1[right], arr1[left]

    left += 1
    right -= 1

print(arr1)