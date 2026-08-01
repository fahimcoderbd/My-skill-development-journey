# Shopping Cart using Python
# Coded by Fahim Abrar

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
    } #demo product #demo product

] #store carts

UI_COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "white": "\033[0m",
    "yellow": "\033[93m"
}

#main ui helpers
def set_color(color: str):
    if color in UI_COLORS:
        print(UI_COLORS[color], end="")

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

def display_search_results(data):
    #after search showing search results
    banner_menu("Showing search results")
    print(f"Product name: {data['name']}")
    print(f"Product id: {data['product_id']}")
    print(f"Product price: {data['price']}")

#logic helper functions
def check_duplicated_id(product_id:int):
    for product in cart:
        if product['product_id'] == product_id:
            return True
    return False

#this will handle product searching feature
def find_product(data:any, key_name:str): #data is the inut from user, key_name is the searching key
    found = False
    for product in cart:
        if product[key_name] == data.lower():
           found = True
           break 
        if not found:
            show_error_msg("Sorry, Product not found!")  
    return product   

#main logic functions
def add_product():
    product_name = input("Enter product name: ")
    if not product_name:
            set_color("red")
            print("Fill required product name")
            set_color("white")
            return
    try:
        product_id = int(input("Enter your product id: (e.g: 1234)"))

        if check_duplicated_id(product_id):
            set_color("red")
            print("This id exists, try with new one")
            set_color("white")
            return
        
        product_price = int(input("Enter product price: "))

        if product_id <= 0 or product_price <= 0:
            set_color("red")
            print("Invalid price and product id!")
            set_color("white")
            return

    except ValueError:
        set_color("red")
        print("Invalid price!")
        set_color("white")
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
        for product in cart:
            if product['product_id'] == cart_id:
                cart.remove(product)
                set_color(color="yellow")
                print("Your product removed successfully!")
                print("Current products")
                show_cart()
                break
            

    except ValueError:
        set_color(color="red")
        print("Give normal input!")

def calculate_total():
    total = 0
    for product in cart:
        total = sum(product['price'])
    
    set_color(color="yellow")
    print(f"Your cart total is: {total}")
    set_color(color="white")

    return total

def apply_discount():
     total_value = calculate_total()
     try:
         discount_value = int(input("Enter discount amount (%): "))
         if discount_value > 100 or discount_value <= 0:
             set_color(color="red")
             print("This can't be accepted")

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


# ===== MENU =====
while True:

    set_color("green")
    banner_menu("Shopping cart app")

    print("1. Add Product")
    print("2. Remove Product")
    print("3. Show Cart")
    print("4. Calculate total")
    print("5. Apply discount")
    print("6. Update product")
    print("7. Search product")
    print("0. Exit")

    set_color("white")

    try:
        set_color(color="yellow")
        choice = int(input("Enter your choice: "))
    except ValueError:
        set_color("red")
        print("Please enter a number.")
        set_color("white")
        continue

    if choice == 1:
        add_product()

    elif choice == 2:
        remove_product()

    elif choice == 3:
        show_cart()
    
    elif choice == 4:
        calculate_total()

    elif choice == 5:
        apply_discount()

    elif choice == 6:
        update_product()

    elif choice == 7:
        search_product()

    elif choice == 0:
        print("Goodbye 👋")
        break

    else:
        set_color("red")
        print("Invalid choice!")
        set_color("white")