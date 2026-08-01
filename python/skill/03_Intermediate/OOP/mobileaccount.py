class MobileAccount:
     def __init__(self,balance):
          self.__balance = balance

     def recharge(self, amount):
             if amount <= 0:
                return "Must provide more than zero"
             self.__balance += amount
             return f"Amount: {amount} recharged successfully!"
        
     def call(self, cost):
         if self.__balance < cost:
             return "Not enough balance"
         else:
             self.__balance -= cost
             return f"Amount: {cost} cut successfully!"

     def get_balance(self):
         if not self.__balance:
             return "You haven't any balance now!"
         else:
             return f"Your balance is {self.__balance}"


