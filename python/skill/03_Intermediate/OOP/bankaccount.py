class BankAccount:
      def __init__(self,owner,balance):
            self.owner = owner
            self.balance = balance
            self.__transactions = []

      #deposit method
      def deposit(self, ammount):
          if ammount <= 0:
               print("Must need an positive number")
          else:
               self.balance += ammount
               self.__transactions.append(
                    {'Deposited': ammount}
               )
               print("Your deposit was successful,\n" \
               f"{self.balance} is new balance")
      
      #cash widthraw method
      def widthraw(self,ammount):
            if ammount <= 0:
               print("Must need an positive number")
            elif ammount > self.balance:
               print("Insufficient Balance")
            else:
                self.balance -= ammount
                self.__transactions.append(
                    {'Widhrew': ammount}
               )
                print("Your widthraw was successful")
                print(f"New balance: {self.balance}")
      
      #show current balance
      def check_balance(self):
           if not self.balance:
               print("Balance is empty!")
           else:
               print(f"Your current balance: {self.balance}")

      def show_transactions(self):
           print("Showing transactions history =>: ")
           for dict in self.__transactions:
                for key,data in dict.items():
                     print(f"{key} : {data}")
                

acc1 = BankAccount("Fahim",1000)
acc1.deposit(1000) #2000
acc1.widthraw(500) #1500
acc1.check_balance()
acc1.show_transactions()

acc2 = BankAccount("Rahib",1500)
acc2.deposit(1000) 
acc2.widthraw(500) 
acc2.check_balance()
acc2.show_transactions()
