# OOP = Object Oriented Programming
#inheritance


























# class Account:
#     def __init__(self, holder, balance):
#         self.holder = holder
#         self.balance = balance
    
#     def showBalance(self):
#         print("\nBalance for", self.holder, ":", self.balance)
        
# class SavingsAccount(Account):
#     def __init__(self, holder, balance):
#         super().__init__(holder, balance)
#         self.interest = 5
        
#     def addInterest(self):
#         self.balance = self.balance + (self.balance * self.interest/100)     
#         print("Interest applied on balance")               

# a1 = SavingsAccount("Kim", 1200)
# a2 = Account("Saul", 1200)
# a2.showBalance()
# a1.addInterest()
# a1.showBalance()


















# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# class Student(Person):
#     def __init__(self, name, age, rollNo):
#         super().__init__(name, age)        
#         self.rollNo = rollNo
    
#     def show_info(self):
#         super().show_info()
#         print("Roll No:", self.rollNo)
        
# s1 = Student("Mike", 18, 131)        
# s2 = Student("David", 17, 127)

# s1.show_info()
# s2.show_info()        
            




















#task2

# class Student:
#     def __init__(self, name):
#         self.__name = name
#         self.__marks = -1

#     def set_marks(self, marks):
#         if marks >= 0 and marks <=100:
#             self.__marks = marks
#             print("Marks for", self.__name, "have been updated")
#         else:
#             print("Marks should be between 0 and 100")
    
#     def display(self):
#         print("\nStudent Info")
#         print("Student's name:", self.__name)
#         if self.__marks == -1:
#             print("Marks have not been set for this student")
#         else:
#             print("Marks:", self.__marks)  
            
# s1 = Student("Mike")
# s2 = Student("John")

# s1.set_marks(95)
# s1.display()      
        
                        



















#task 1
# class BankAccount:
#     def __init__(self):
#         self.__balance = 0
    
#     def deposit(self, amount):
#         if amount>0:
#             self.__balance = self.__balance + amount
#             print("Amount added into account")
#         else:
#             print("Amount must be more than 0")
    
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance = self.__balance - amount
#             print("Amount withdrew from Account")
#         else:
#             print("Insufficient balance")
            
#     def get_balance(self):
#         print("\nYour account's balance:", self.__balance, "\n")                    
                    
# xyz = BankAccount()
# xyz.get_balance()
# xyz.deposit(700)
# xyz.get_balance()
# xyz.withdraw(250)
# xyz.get_balance()











# class Student:
#     def __init__(self, balance):
#         self.__balance = balance
        
# s1 = Student(600)

# print(s1.__balance)        











# class Book:
#     def __init__(self, name, author):
#         self.name = name
#         self.author = author
#         self.available = True
    
#     def borrow(self):
#         if self.available == True:
#             print("You just borrowed ", self.name)
#             self.available = False    
#         else:
#             print("Book is already borrowed by someone..!")  
    
#     def returnBook(self):
#         if self.available == True:
#             print("You havent borrowed this book, so cannot return it")
#         else:
#             print("Thanks for returning", self.name)
#             self.available = True

# b1 = Book("Harry Potter", "abc")
# b2 = Book("Game of Thrones", "xyz")

# b1.borrow()
# b2.borrow()

# b1.returnBook()
# b1.borrow()
# b2.returnBook()
# b2.borrow()





  
  
  
  
  
  
  
  
         
# class Student:
#     def __init__(self, name, marks): #constructor
#         self.name = name
#         self.marks = marks
    
#     def show(self):
#         print("Student Info...!")
#         print("Name:", self.name)    
#         print("Marks:", self.marks)    

# student1 = Student("Mike", 88)
# student2 = Student("David", 95)

# student1.show() 

# student2.show()      


























# import librarySystem
# import cart
# import phone
# import atm

# a1 = atm.ATM()

# a1.setPin(1122)

# a1.getPin()

# p1 = phone.Phone("iphone", 89)

# p1.__battery= 77
# # print(p1.__battery)
# p1.show()
# p1.change()
# p1.newBattery(77)
# p1.show()

#oop = object oriented programming
#encapsultion
#inheritance
#abstraction
#polymorphism

#getters and setters

# p1 = cart.Product("Chips", 5, 20)
# p2 = cart.Product("Coke", 3, 15)
# p3 = cart.Product("Detergent", 6, 9)

# p1.show_product()
# p1.total_price()
# p3.total_price()



# b1 = librarySystem.Book("Harry Potter", "abc")
# b2 = librarySystem.Book("ALice in Wonderland", "xyz")
# b3 = librarySystem.Book("Basics of Python", "George Boole")
# b4 = librarySystem.Book("Stranger Things", "123")

# b1.borrow()
# b2.return_book()
# b1.return_book()
# b3.borrow()

# b3.show_status()















# class Phone:
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery
    
#     def usage(self):
#         self.battery = self.battery - 10
#         print("Battery %age:", self.battery)    


# p1 = Phone("Samsung", 90) #object

# p1.usage()       
# p1.usage()       
# p1.usage()       
        





# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance = self.balance + amount    
#         print("Your new balance for ", self.name,": ", self.balance)
    
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#             print("Withdrawal Successful, new balance:", self.balance)
#         else:
#             print("Insufficient balance")      
    
#     def show_balance(self):
#         print("Your bank balance", self.name, ":", self.balance)          
        
# acc1 = BankAccount("George", 12000)

# acc1.deposit(2500)        
# acc1.withdraw(7500)
# acc1.show_balance()
















# class Student:
#     def __init__(self, name, age): #constructor
#         self.name = name
#         self.age = age
    
#     def detail(self):
#         print("The name is: ", self.name)    
#         print("The age is: ", self.age)    
        
        
# s1 = Student("Mike", 19)        
# s2 = Student("Dave", 19)

# s1.detail()     
# s2.detail()










# class Student:
#     name  = "Ali"  #attributes
#     grades = 89


# s1 = Student()
# s2 = Student()  #making an object
# s2.name = "David"

# print(s1.name)
# print(s1.grades)

# print(s2.name)