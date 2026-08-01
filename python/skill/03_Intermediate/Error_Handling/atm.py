#1 solve

#atm system
class Atm:
    def __init__(self):
        self.balance = 5000

    def withdraw(self, amount):
        try:
           amount = int(amount)
           if amount <= 0:
            raise ValueError("Invalid amount")
           elif amount > self.balance:
            raise ValueError("Insufficient balance")
           else:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"
        except ValueError:
            return "Withdraw failed: Invalid amount or insufficient balance"

atm = Atm()
while True:
      widthdraw_amount = input("Enter amount to withdraw: ")
      final = atm.withdraw(widthdraw_amount)
      print(final)