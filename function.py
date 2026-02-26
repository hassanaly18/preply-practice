#task 9

def delivery_charge(distance):
    if distance<=5:
        return 100
    elif distance<=10:
        return 200
    else:
        return 300

dist = int(input("Enter the distance: "))
bill = int(input("Enter bill amount: "))

total = delivery_charge(dist) + bill

print("Total ampount to pay: ", total)












#task 2

# def deposit_money(balance, amount):
#     balance = balance + amount
#     print("Deposit successful")
#     return balance

# balance = int(input("Enter balance: "))
# amount = int(input("Enter amount to deposit: "))

# updatedBalance = deposit_money(balance, amount)

# print("Your new balance is:", updatedBalance)






#task 1

# def discountSystem(amount):
#     if amount>1000:
#         amount = amount * 0.9
    
#     print("Total bill:", amount)

# bill = int(input("Enter bill amount: "))

# discountSystem(bill)

















# def salary_after_tax(salary):
#     if salary >100000:
#         return salary * 0.9
#     else:
#         return salary * 0.95
 
# print("Total salary after tax deduction:", salary_after_tax(120000)) 
# print("Total salary after tax deduction:", salary_after_tax(95000)) 


















# #task 5
# def calculate_total(price, quantity, tax):
#     total = price * quantity
#     final_bill = total + (total * (tax/100))
#     return final_bill



# print("Total bill including tax:",calculate_total(40, 3, 16))








#task 4
# def fuel_cost(distance, fuel_price, average):
#     total = (distance / average) * fuel_price
#     return total

# distance = float(input("Enter distance(km): "))
# fuel_price = float(input("Enter cost of fuel per liter: "))
# average = float(input("Give car's per liter average: "))

# print("The total fuel cost:", fuel_cost(distance, fuel_price, average))


# def calculate_grade(marks):
#     if marks>=90:
#         print("A")
#     elif marks >=75:
#         print("B")
#     elif marks>=60:
#         print("C")
#     else:
#         print("fail")
                       


















# #defining/making a function
# def hello():
#     print("Hello world 67")
#     print("Hello world 12")
#     print("Hello world 98")
    
# def greet(name):
#     print("Welcome", name) 
    
# def square(a):
#     print("The square is:", a*a)
  
# def evenOdd(num):
#     if num%2==0:
#         print("the num is even")
#     else:
#         print("the num is odd")
     
# def add(a,b):
#     return a+b

# def check(age):
#     if age>=18:
#         return  "legal"
#     else:
#         return "illegal"
    
# print("status:",check(12))    

# c = add(7865, 45542) 
  
# print("the sum is:", c)
# print("the sum of calculation is:", c) 
     
# evenOdd(12)              
  
  
    
# num1 = int(input("Enter a number: "))

# square(num1)        
# greet("David")       
# greet("Mike")       

# hello()

# add = 90
# print(add)

# hello()




















# def greet_user(name):    #parameter, argument
#     print("Welcome to the program,", name)

# def abc(name, age):
#     print("Your name is", name, "and your age is", age)
    
# def add(a, b, c):
#     print("The sum is:", a+b+c)  
    
# def add2():
#     a = int(input("Enter 1st number: "))      
#     b = int(input("Enter 2nd number: "))
#     print("The sum is", a+b)  
    
# def square(n):
#     return n*n
    
# def calculator(a, b, operator):   
#     match operator:
#         case "+":
#             print(a+b)    
#         case "-":
#             print(a-b)    
#         case "*":
#             print(a*b)    
#         case "/":
#             print(a/b) 
#         case "sq":
#             print(square(a))     #function within another function
#         case _:
#             print("Wrong input")
            
# # calculator(9, 65, "sq")            

# # calculator(43, 88, "+")        

# def add3(a,b):
#     return a+b

# def give_name():
#     return "David"

# def check_age(age):
#     if age >= 18:
#         return "Allowed"
#     else:
#         return "Not Allowed"
    
# def check(age=22 ):
#     return "Allowed" if age >= 18 else "Not Allowed"

# def rock(a,b):
#     x = a+b
#     y=a-b
#     z = a*b
#     return x,y,z

# s, d, m = rock(10, 5)

# print("the sum is:",s)
# print("the difference is:",d)
# print("the product is:",m)

# print(check())    
# print(check(11))    
    
# print(check_age(12))    

# print("The name is",give_name())

# result = add3(56, 18)
# print(result)











           
    
# add2()
    
# add(67, 12, 54)     #return type, void

    
# abc("Khan", 20)        

# greet_user("David")    
# greet_user("Larry")  

# name = input("Enter your name: ")
# greet_user(name) 

# def hello():
#     print("Hello world 1")
#     print("Hello world 2")
#     print("Hello world 3")
#     print("Hello world 4")
    
# def age_show():
#     age = int(input("Enter your age: "))
#     print("Your age is", age)    

# hello()

# age_show()

# print(7+8)

# hello()


























# def greet():
#     print("Hello world")
#     print("Hello 123")

# #argument / parameter

# def greetUser(name):
#     print("Welcome to the program", name)
    

# greetUser("David")    
# greetUser("Julia")    
# greetUser("Logan")    