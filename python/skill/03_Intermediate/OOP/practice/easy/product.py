class Product:
    def __init__(self, name:str, price:float, stock:int):
        self.name = name
        self.price = price
        self.stock = stock

    #show product info
    def display(self):
        return (
            f"Product name: {self.name} \n"
            f"Product price: {self.price} usd \n"
            f"Product stock: {self.stock} \n"
        )

    #buying a product with quantity
    def buy(self, quantity:int):
         if self.stock <= 0 : return "Invalid input"
         if quantity > self.stock : return "Out of stock"

         self.stock -= quantity
         return (
             f"{quantity} {self.name} purchased successfully! \n"
             f"Remaining stock: {self.stock}"
        )


#testing
iphone = Product(name="Iphone 15 pro max", price=1500, stock=100)
print(iphone.display())
print(iphone.buy(100))
print(iphone.buy(10)) #should show error message

    
        