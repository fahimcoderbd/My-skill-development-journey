#payment system

from abc import ABC, abstractmethod

#parent class
class payment(ABC):
      
      @abstractmethod
      def pay(self, taka):
          pass
    
#child class
class bkash(payment):
      def pay(self, taka):
          print(f"Taka disi {taka} using bkash")

class nagad(payment):
      def pay(self, taka):
          print(f"Taka disi {taka} using nagad")

p1 = bkash()
p1.pay(100)

p2 = nagad()
p2.pay(200)
      
