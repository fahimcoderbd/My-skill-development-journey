#ui here
from cart import set_color, banner_menu #ui components
from cart import (
    add_product, remove_product, show_cart, apply_discount, update_product,search_product, #basic features
    calculate_total,calculate_average,cheapest_product,expensive_product, #calculation features
    show_above_price,show_below_price,show_filter_results #filtering features
)

def run_app():
    # ===== MENU =====
  while True:

    set_color("green")
    banner_menu("Shopping cart app")

    print("1. Add Product")
    print("2. Remove Product")
    print("3. Show Cart")
    print("4. Apply discount")
    print("5. Update product")
    print("6. Search product")

    print("=="*20)
    set_color(color="yellow")
    print("Calculation features =>")
    set_color(color="white")
    print("7. Calculate total")
    print("8. Calculate average")
    print("9. Most cheapest product")
    print("10. Most expensive product")

    print("=="*20)
    set_color(color="yellow")
    print("Filtering features =>")
    set_color(color="white")
    print("11. Show products above price")
    print("12. Show products below price")
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
        apply_discount()

    elif choice == 5:
        update_product()

    elif choice == 6:
        search_product()

    elif choice == 7:
        calculate_total()

    elif choice == 8:
        set_color(color="yellow")
        print(calculate_average())

    elif choice == 9:
         set_color(color="green")
         print(cheapest_product())

    elif choice == 10:
        set_color(color="green")
        print(expensive_product())

    elif choice == 11:
        set_color(color="green")
        #taking price from user
        price = int(input("Enter your price: "))
        banner_menu(f"Showing products above {price} \n")
        products = show_above_price(price)
        print(show_filter_results(products))

    elif choice == 12:
        set_color(color="green")
          #taking price from user
        price = int(input("Enter your price: "))
        banner_menu(f"Showing products below {price} \n")
        products = show_below_price(price)
        print(show_filter_results(products))

    elif choice == 0:
        print("Goodbye 👋")
        break

    else:
        set_color("red")
        print("Invalid choice!")
        set_color("white")

if __name__ == "__main__":
    run_app()