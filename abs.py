from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, holder, balance):
        super().__init__()
        self.holder = holder
        self.balance = balance
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Updated balance after Deposit:", self.balance)
        
    def showBalance(self):
        print("Current Balance:", self.balance)
                
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance-amount
            print("Updated balance after Withdrawal:", self.balance)    
        else:
            print("Insufficient balance")

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance+5000:              
            self.balance = self.balance-amount
            print("Updated balance after Withdrawal:", self.balance)   
        else:
            print("Overdraft limit exceeded")       
            
a = SavingsAccount("Mike", 6777)
b = CurrentAccount("david", 8000)

a.withdraw(4800)
b.withdraw(9000)            

















# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

# class Cash(Payment):
#     def pay(self, amount):
#         print("Paid", amount, "Using cash") 
        
# class CreditCard(Payment):
#     def pay(self, amount):
#         print("Paid", amount, "Using Credit Card")

# a = Cash()
# b= CreditCard()

# a.pay(6788)
# b.pay(1200)











# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
# class Rectangle(Shape):
#     def __init__(self,length, width):
#         super().__init__()
#         self.length = length
#         self.width = width
    
#     def area(self):
#         print("Area:", self.length * self.width)   
        
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()
#         self.radius = radius
    
#     def area(self):
#         print("Area:", 3.14* self.radius*self.radius)
                 
    
# rect = Rectangle(78, 8)
# circ = Circle(23)

# rect.area()    
# circ.area()        