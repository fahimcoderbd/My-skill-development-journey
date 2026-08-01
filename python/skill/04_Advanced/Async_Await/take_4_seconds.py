""" #normal code
#take 4 seconds
import time

def task():
    print("Start")
    time.sleep(2)
    print("End")

task()
task() """


#async code
#make code faster take 2 seconds

import asyncio

async def task():
       print("task started")
       await asyncio.sleep(2)
       print("ending task")

async def main():
       await asyncio.gather(task(),task())

asyncio.run(main())
       