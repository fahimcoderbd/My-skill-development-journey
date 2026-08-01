#fake async based api fetching

import asyncio

async def fetch_data(name):
      print(f"Fetching data: {name}")
      await asyncio.sleep(2)
      print("Fetching done")

async def main():
      await asyncio.gather(
            fetch_data("user_name"),
            fetch_data("password"),
            fetch_data("posts")
      )

#running async function
asyncio.run(main())