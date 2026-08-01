def print_triangle(height, i=1):
    if i > height:
        return
    print("*" * i)
    print_triangle(height, i + 1)

# Call function
print_triangle(5)