import time
from contextlib import contextmanager

@contextmanager
def timer():
    print("Checking time")
    start_time = time.time()
    try:
      yield
    finally:
     end_time = time.time()
     time_taken = end_time - start_time
     print(f"Time taken: {time_taken:.4f} seconds")

with timer():
     print(100 * 200)


