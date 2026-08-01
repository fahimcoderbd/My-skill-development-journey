import asyncio
import random

async def fetch_data(id):
    random_time = random.randint(1, 3)
    await asyncio.sleep(random_time)
    return f"Data from API {id}"

async def main():
    ids = [1, 2, 3, 4, 5]

    # Create multiple tasks
    tasks = [fetch_data(i) for i in ids]

    # Process as they complete
    for finished_task in asyncio.as_completed(tasks):
        result = await finished_task
        print(result)

asyncio.run(main())
     
