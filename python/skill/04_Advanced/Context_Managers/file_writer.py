# taking text input
user_text = input("Enter your text: ")

def write_file(data):
    if len(data.strip()) == 0:
        print("Please write something!")
        return

    try:
        with open("output.txt", "w") as file:
            file.write(data)
            print("File written successfully!")
    except Exception as e:
        print("Error:", e)

write_file(user_text)