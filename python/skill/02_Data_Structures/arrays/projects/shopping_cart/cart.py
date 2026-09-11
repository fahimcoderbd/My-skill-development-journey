# Shopping Cart using Python
# Coded by Fahim Abrar
from typing import Any

cart = [
    {
        'name':"macbook",
         'product_id': 1,
         'price': 150000
    },
    {
         'name':"macbook",
         'product_id': 2,
         'price': 160000
    },

    {
        'name':"watch",
        'product_id': 3,
        'price': 150
   },


] #store carts

UI_COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "white": "\033[0m",
    "yellow": "\033[93m"
}

#main ui helpers
def set_color(color: str):
    if color in UI_COLORS: print(UI_COLORS[color], end="")

def show_error_msg(msg:str):
    set_color("red") 
    print(msg)
    set_color("white")

def banner_menu(title:str):
    set_color(color="green")
    print("==" * 20)
    print(f"{title}")
    print("==" * 20)
    set_color(color="white")

#feature ui helpers
def search_product_menu():
     set_color(color="white")
     print("Please select an option for search =>")
     print("1.Search by name =>")
     print("2.Search by id =>")
     print("3.Search by price =>")
     print("\n")

def show_empty_msg():
    set_color("yellow")
    print("Your cart is empty.")
    set_color("white")

def display_search_results(data):
    if not data:
        show_error_msg("Sorry, product not found!")
        return

    # after search showing search results
    banner_menu("Showing search results")
    print(f"Product name: {data['name']}")
    print(f"Product id: {data['product_id']}")
    print(f"Product price: {data['price']}")


def show_filter_results(arr):
    if not arr:return 
    for product in arr:
        print(f"Product: {product['name']}")

# logic helper functions
def check_duplicated_id(product_id:int) -> bool:
    for product in cart:
        if product['product_id'] == product_id:
            return True
    return False

# this will handle product searching feature
def find_product(data:Any, key_name:str): # data is the input from user, key_name is the searching key
    for product in cart:
        value = product[key_name]
        if key_name == "name":
            if isinstance(data, str) and value.lower() == data.lower():
                return product
        else:
            if value == data:
                return product

    return None

#basic feature logic functions
def add_product():
    product_name = input("Enter product name: ")
    if not product_name:
            show_error_msg("Fill required product name")
            return
    try:
        product_id = int(input("Enter your product id: (e.g: 1234)"))

        if check_duplicated_id(product_id):
            show_error_msg("This id exists, try with new one")
            return
        
        product_price = int(input("Enter product price: "))

        if product_id <= 0 or product_price <= 0:
            show_error_msg("Invalid price and product id!")
            return

    except ValueError:
        show_error_msg("Invalid price")
        return

    product = {
        "name": product_name,
        "product_id":product_id,
        "price": product_price
    }

    cart.append(product)

    set_color("green")
    print("✅ Product added successfully!")

    set_color("white")
    show_cart()
     
def show_cart():
    if not cart:
        show_empty_msg()
        set_color(color="white")
        return

    print("\n------ Cart ------")

    for i, product in enumerate(cart, start=1):
        print(
            f"{i}. Name {product['name']}",
            f" id: {product['product_id']}",
            f"Price: {product['price']} Tk"
        )

    print("------------------\n")

def remove_product():
    if not cart:
       print(show_error_msg("Cart is empty"))
       return
    
    set_color(color="white")
    print("Select your product from bellow")
    print("-------------Carts------------------")
    show_cart(),
    try:
        set_color(color="green")
        cart_id = int(input("Enter cart name to delete: "))
        found = False
        for product in cart:
            if product['product_id'] == cart_id:
                found= True
                cart.remove(product)
                set_color(color="yellow")
                print("Your product removed successfully!")
                print("Current products")
                show_cart()
                break
        if not found: show_error_msg("Sorry product not found")
            

    except ValueError:
        set_color(color="red")
        print("Give normal input!")

def apply_discount():
     total_value = calculate_total()
     try:
         discount_value = int(input("Enter discount amount (%): "))
         if discount_value <= 0:
             set_color(color="red")
             print("This can't be accepted")
             return

         final = total_value - (total_value * discount_value / 100)

         set_color(color="yellow")
         print(f"Final amount is: {final}")

     except ValueError:
         set_color(color="red")
         print("Please give a valid value!")

def update_product():
    #showing ui for updating a product
    banner_menu("Update a product =>")

    #showing all products
    
    print("Select a product id from these products =>")
    show_cart()

    #taking the product id needed for update operation
    try:
        if cart:
           banner_menu("Select which fields you wanna update =>")
           print("1.Product name")
           print("2.Product price")
           print("3. All fields")

           menu_choice = int(input("Enter your choice: "))
           product_id = int(input("Enter product id: "))

           for product in cart:
               if product['product_id'] == product_id:
                   #saving previos prouduct data
                   previous_product_name = product['name']
                   previous_product_price = product['price']

                   #updating product name
                   if menu_choice == 1:
                       new_name = input("Enter new name: ")
                       product['name'] = new_name
                       set_color(color="green")
                       print(f"Your product name {previous_product_name} updated to {new_name} successfully!")

                   #updating product price
                   elif menu_choice == 2:
                       new_price = float(input("Enter new price: "))
                       product['price'] = new_price
                       set_color(color="green")
                       print(f"Your product price {previous_product_price} updated to {new_price} successfully!")

                   #updating both product name and price
                   elif menu_choice == 3:
                       new_name = input("Enter new name: ")
                       new_price = float(input("Enter new price: "))
                       product['name'] = new_name
                       product['price'] = new_price
                       set_color(color="green")
                       print(f"Your product name {previous_product_name} updated to {new_name} successfully!")
                       print(f"Your product price {previous_product_price} updated to {new_price} successfully!")

                   else:
                       set_color(color="red")
                       print("Please select a valid option!")
                       
    except ValueError:
         set_color(color="red")
         print("Give a valid product id!")

def search_product():
    #search feature menu
    banner_menu("Search a product =>\n")
    #main menu
    search_product_menu()
    #taking menu selection input
    try:
        set_color(color="yellow")
        user_selection = int(input("Enter your choice: "))

        #handling user selection 
        if user_selection == 1:
              banner_menu("Searching with product name =>")
              set_color(color="yellow")
              name = input("Enter your product name: ")
              product = find_product(name, "name") #data, key
              display_search_results(product)

        elif user_selection == 2:
                banner_menu("Searching with product id =>")
                set_color(color="yellow")
                product_id = int(input("Enter your product id: "))
                product = find_product(product_id, "product_id") #data, key
                display_search_results(product)

        elif user_selection == 3:
                  banner_menu("Searching with product price =>")
                  set_color(color="yellow")
                  price = float(input("Enter your product price: "))
                  product = find_product(price, "price") #data, key
                  display_search_results(product)

        else:
             show_error_msg("Please select a valid option!")

    except ValueError as e:
        set_color(color="red")
        print(f"Please give a valid input")

def show_sorted_results(product_data:dict):
    if not product_data:
        show_error_msg("No product found!")
        return
    return (
        f"Name: {product_data['name']} \n" #product name
        f"Id: {product_data['product_id']} \n"
        f"Price: {product_data['price']}"
    )

#calculation feature logic functions 
def calculate_total():
    total = 0
    for product in cart:
        total += product['price']
    
    set_color(color="yellow")
    print(f"Your cart total is: {total}")
    set_color(color="white")

    return total

def calculate_average():
      total_price = calculate_total()
      cart_length = len(cart)
      if cart_length > 0:
         average = total_price / cart_length
         return f"Your average product price is: {average:.2f}"

def cheapest_product():
    cheapest = cart[0]
    for product in cart:
        if product['price'] < cheapest['price']:
           cheapest = product
           found = True

    if not found:
        show_error_msg("No product found!")

    return f"Your cheapest product is: {cheapest['name']}, price: {cheapest['price']}"

def expensive_product():
    found = False
    expensive_product = cart[0]
    for product in cart:
        if product['price'] > expensive_product['price']:
            expensive_product = product 
            found = True
    if not found: show_error_msg("No product found!")

    return (
       f"Your expensive product: {expensive_product['name']} \n"
       f"Your product id: {expensive_product['product_id']} \n"
       f"Your product price: {expensive_product['price']}"
    )

#filtering feature logic functions
def show_above_price(price:float):
    if not price or price <= 0: show_error_msg("Price must be bigger than zero")
    found = False
    results = []

    for product in cart:
        if product['price'] > price: 
           found = True
           results.append(product)
    if not found: show_error_msg("Products not found! Sorry")
    return results

def show_below_price(price:float):
    if not price or price <= 0: show_error_msg("Price must be bigger than zero")
    found = False
    results = []

    for product in cart:
        if product['price'] < price: 
           found = True
           results.append(product)
    if not found: show_error_msg("Products not found! Sorry")
    return results
 
#sorting feature logic functions
def sort_product(key_data, sort_by):
    product_cart = cart
    if not product_cart:
        return []

    for product in product_cart:
        if sort_by == "name":
            if product['name'] == key_data:
                return show_sorted_results(product)
        elif sort_by == "product_id":
            if product['product_id'] == key_data:
                return show_sorted_results(product)
        elif sort_by == "price":
            if product['price'] == key_data:
                return show_sorted_results(product)

#total products in cart [statistics]
def products_in_cart():
    my_cart = cart
    products_quantity = len(my_cart)
    if not cart: return "No products in cart"
    return f"Total {products_quantity} products in cart"