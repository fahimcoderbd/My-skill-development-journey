from contextlib import contextmanager

@contextmanager
def file_logger(file, mode):
    print("Logging started")
    try:
     file = open(file, mode)
     yield file
    finally:
        file.close
        print("Logging finished")

with file_logger('log.txt', mode='w') as log:
     log.write("User logged in\n")
     log.write("User clicked button\n")