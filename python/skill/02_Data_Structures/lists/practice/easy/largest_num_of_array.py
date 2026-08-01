'''Problem 1 (Easy) – Find Maximum Number 

তোমাকে একটি array/list দেওয়া থাকবে।
তোমাকে সেই array থেকে সবচেয়ে বড় সংখ্যাটি বের করতে হবে।

Example

Input:

arr = [5, 12, 3, 9, 21, 7]

Output:

21
Rules

max() function ব্যবহার করা যাবে না

Loop ব্যবহার করতে হবে'''

#sollution

def largest_num_of_array(arr):
    #checking arr is empty or not
    if not arr:
        return None
    #suppost largest num = first element of the array
    largest_num = arr[0] #first num
    #looping the array and checking with the largest
    for num in arr[1:]:
        if num > largest_num:
            #updating largest number
            largest_num = num
    return largest_num

#testing
arr = [5, 12 ,3 , 9, 21, 7]
print(largest_num_of_array(arr))