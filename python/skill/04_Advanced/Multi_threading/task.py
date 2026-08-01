import threading
import time

def task():
    for i in range(5):
        print("Task running:", i)
        time.sleep(1)

#single thread
t1 = threading.Thread(target=task)

#multiple threads
t2 = threading.Thread(target=task)
t3 = threading.Thread(target=task)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Done!")