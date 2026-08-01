#shopping cart
def checkout(*items_price, **user_info):
    total_price = sum(items_price)
    for key,data in user_info.items():
        print(f"{key} : {data}")

    print(f"Total Bill: {total_price}")

checkout(100, 250, 50, name="Fahim", city="Dhaka")