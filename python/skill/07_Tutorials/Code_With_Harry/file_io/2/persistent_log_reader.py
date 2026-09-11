def run_app():
    #opening file
    with open('code_with_harry\\file_io\\2\\server.log', 'r') as file:
          print(file.read(100))

          #bookmarking the reading line
          book_mark = file.tell()
          print(f"Bookmark: {book_mark}")

          file.close()
          
          f = open('code_with_harry\\file_io\\2\\server.log', 'r')
          f.seek(book_mark)
          print("Resuming from log 3")
          print(f.read())
if __name__ == "__main__":
    run_app()
