import asyncio
import random

async def worker(time, message):
    rand_time = random.randint(*time)
    print(f"{message} started")
    await asyncio.sleep(rand_time)
    print(f"{message} done")

async def prepare_food():
    await worker((2,5), "🍳 Preparing food")

async def assign_rider():
    await worker((1,3), "🛵 Assigning rider")

async def process_payment():
    # random fail
    if random.choice([True, False]):
        raise Exception("Payment Failed ❌")
    await worker((1,4), "💳 Processing payment")

async def main():
    try:
        await asyncio.wait_for(
            asyncio.gather(
                prepare_food(),
                assign_rider(),
                process_payment()
            ),
            timeout=4
        )
        print("✅ Order Delivered Successfully!")

    except asyncio.TimeoutError:
        print("⏰ Order Failed: Timeout!")

    except Exception as e:
        print(f"❌ Order Failed: {e}")

asyncio.run(main())