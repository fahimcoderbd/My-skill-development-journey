#Cart Total & Discount Calculator

'''
Tomar kache ekti array ache jekhane user-er cart-er sob gulo item-er price dewa ache. Tomake niche dewa 3 ti kaj korte hobe:

Total Price Ber Koro: Cart-er sob gulo product er total daam koto seta calculate koro.

Premium Product Khujo: Array theke sobcheye dami (highest price) product ti ber koro.

Discount Apply Koro: Jodi Total Price 500 Taka-r beshi hoy, tahole total bill er upor 10% discount daw tracking purpose-e.

📥 Input Data (Array)
Tumi nicher eii array ti diye start korte paro:

Python
cart_prices = [120, 45, 250, 80, 150]
📤 Expected Output
Tomar code run korle terminal-e output thik eivabe dekhano dorkar:

Plaintext
Total Original Price: 645 Taka
Highest Product Price: 250 Taka
Discount Applied (10%): Yes
Final Payable Amount: 580.5 Taka
'''

def cart_feature(arr):
    if not arr:
        return None
    
    total = sum(arr)
    premium_product_price = max(arr)
    is_discount_applied = "No"
    final_pay = total

    if total > 500:
       discount_value = discount_apply(total)
       is_discount_applied = "Yes"
       final_pay = (total - discount_value)

    return (
        f"Total Original Price : {total} Taka \n"
        f"Highest Product Price : {premium_product_price} Taka \n"
        f"Discount Applied: {is_discount_applied} \n "
        f"Final Payable Amount: {final_pay} Taka"
        )


def discount_apply(total_value):
    discount = (total_value * 10 / 100)
    return discount

cart_prices = [120, 45, 250, 80, 150]
print(cart_feature(cart_prices))
