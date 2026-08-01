try:
 file = open("file_handling/notes.txt" ,"r")
 file_content = file.read()
 print(file_content)
 file.close()
except FileNotFoundError:
   print("File not exists")