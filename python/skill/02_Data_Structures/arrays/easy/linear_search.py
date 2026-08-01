#Linear search— return index
#sollution

def linear_search(arr,target):
    if not arr:
        return None
    
    for i,el in enumerate(arr):
        if el == target:
            return i
        
#test cases
arr1 = [1,2,3]
print(linear_search(arr1,3))
