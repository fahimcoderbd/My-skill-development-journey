#custom for loop

""" def custom_loop(data):
    it = iter(data)
    while True:
     try:
        interated_data = next(it)
        print(interated_data)
     except StopIteration:
        print(f"Sorry value has finished!")
        break

custom_loop([1,2,3]) """

#custom data filtering
""" def custom_filter_loop(data):

      it = iter(data)
      while True:
       try:
          numbers = next(it)
          if numbers % 2 == 0:
             print(numbers)
       except StopIteration:
         print("Sorry, we can only print odd numbers!")
         break

custom_filter_loop([1, 2, 3, 4, 5, 6]) """
       
def custom_limit_loop(data, limit):
    
    it = iter(data)
    counter = 0

    while True:
       try:
        if counter == limit:
           break

        value  = next(it)
        counter += 1
        if counter <= limit:
           print(value)
           
       except StopIteration:
          print("Limit reached!")
          break
       
custom_limit_loop([10, 20, 30, 40, 50], 3)   
