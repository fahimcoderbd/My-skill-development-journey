if __name__ == '__main__':
     arr = [1, 5, 6, 8]

     result = []
     result = set()
    
     for nums in arr:
        result.add(nums)
    
     first_position = max(result)
     result.remove(first_position)
     runner_up = max(result)
     print(runner_up)