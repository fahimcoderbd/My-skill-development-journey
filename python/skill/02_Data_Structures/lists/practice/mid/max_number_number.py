def max_number_number(numbers):
    max_number = numbers[0]
    if not numbers:
        return
    for number in numbers:
        if number > max_number:
           max_number = number

    return f"Max number: {max_number}"

finder = max_number_number([10, 5, 20, 8])
print(finder)
    
