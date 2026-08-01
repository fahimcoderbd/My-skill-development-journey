'''
3. Product Discount Calculator 🛒
Scenario

Shop এ discount calculate করা হবে।

Rules

Input:

Product Price
Discount %

যদি

price <=0

অথবা

discount <0
discount >100

হয়

raise ValueError

নাহলে

Final Price বের করো।

Example

Price : 500
Discount : 20

Final Price = 400
'''

#sollution
def calculate_product_discount(price:float, discount:int):
    try:
        if price <= 0 or discount < 0 or discount > 100:
            raise ValueError
        
        discount_price = (price* (discount/100))
        final_price = price - discount_price

        return (
            f"Price: {price} \n"
            f"Discount (%): {discount} \n"
            f"Final price = {final_price}"
        )
        
    except ValueError:
        return "Enter a valid price or discount"

#testing
print(calculate_product_discount(500, 20))