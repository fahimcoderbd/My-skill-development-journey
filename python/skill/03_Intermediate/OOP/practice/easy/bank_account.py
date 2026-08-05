class BankAccount:
     def __init__(self, name:str,balance:float):
          self.owner_name = name
          self.balance = balance

     def check_balance(self):
          return f"Balance: {self.balance}"
    

     def deposit(self,amount:float):
         if amount <= 0: return "Invalid amount! Please try again"
         self.balance += amount
         return (
              f"{self.owner_name} Deposited: {amount} \n"
              f"{self.check_balance()}"
         )
         

     def withdraw(self,amount:float):
          if amount <= 0: return "Invalid amount! Please try again"
          if amount > self.balance: return f"Insufficient balance!"
          self.balance -= amount
          return (
              f"{self.owner_name} withdrawn : {amount} \n"
              f"{self.check_balance()}"
          )


user1 = BankAccount(name="Fahim", balance=1000)
print(user1.deposit(100))
print(user1.withdraw(100))
print(user1.deposit(0))
print(user1.deposit(-1))
print(user1.withdraw(1200))
