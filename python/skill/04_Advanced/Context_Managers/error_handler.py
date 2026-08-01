class ErrorHandler:
    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print("Error occurred")
        print("End")
        return True   # optional: error suppress করবে

# test with error
with ErrorHandler() as obj:
    print("Inside block")
    x = 10 / 0   # error