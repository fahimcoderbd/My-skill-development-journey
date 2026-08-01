#specific error dhorbe
#index error

try:
    nums = [1,2,3]
    print(nums[5])
except IndexError:
    print("bro thik thak daw!")

#value error
try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("bro thik thak daw!")