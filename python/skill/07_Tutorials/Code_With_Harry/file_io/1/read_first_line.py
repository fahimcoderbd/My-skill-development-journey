def read_first_line(file_path):
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline()
            return first_line if first_line else "File is empty"
    except FileNotFoundError:
        return "File not found"


def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Added parentheses to call the method
            print(f"Total lines: {len(lines)}")
            for i, line in enumerate(lines):
                print(f"{i}: {line.rstrip()}")  # Remove trailing newlines
    except FileNotFoundError:
        print("File not found")


def save_user_input(file_path='code_with_harry\\file_io\\1\\output.txt'):
    try:
        with open(file_path, 'w') as file:
            for i in range(1, 4):
                user_input = input(f"Enter line {i}: ")
                file.write(user_input + "\n")
        print("File created successfully!")
    except IOError as e:
        print(f"Error writing to file: {e}")



if __name__ == "__main__":
    first_line = read_first_line('code_with_harry\\file_io\\1\\data.txt')
    print(first_line)
    
    count_lines('code_with_harry\\file_io\\1\\data.txt')
    
    save_user_input()