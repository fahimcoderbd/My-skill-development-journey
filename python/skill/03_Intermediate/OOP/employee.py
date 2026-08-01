class Employee:
      def __init__(self ,name,salary):
            self.name = name
            self.salary = salary

       #method 1
      def show_info(self):
          return f"Name: {self.name}, Salary: {self.salary}"
      
      #method 2
      def work(self):
          return f"{self.name} is working"
      
class Developer(Employee):
      def __init__(self, name, salary,programming_language):
           super().__init__(name, salary)
           self.language = programming_language

      def work(self):
           return f"Developer {self.name} is coding in {self.language}"
      
class Manager(Employee):
      def __init__(self,name,salary,team_size):
           super().__init__(name,salary)
           self.team = team_size

      def work(self):
           return f"Manager {self.name} is managing a team of {self.team} people"
      

employees = [Developer(
"Fahim",
10000,
"python"  
), Manager(
 "Abrar",
 100000 ,
  5  
)]

for employee in employees:
     employee.salary += employee.salary * 0.1
     print(employee.show_info())
     print(employee.work())