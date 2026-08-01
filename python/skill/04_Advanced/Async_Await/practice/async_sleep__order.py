#Async Sleep & Order

import asyncio

#task 1 async function
async def task1():
      await asyncio.sleep(2)
      print("Task 1 done")

#task 1 async function
async def task2():
      await asyncio.sleep(1)
      print("Task 2 done")

#gathering all functions and running
async def main():
          await asyncio.gather(
           task1(),
           task2()
           )
          
#run all tasks
asyncio.run(main())
