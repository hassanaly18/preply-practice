#while, for

total = 0
num = 0

while num != -1:
    total += num
    num = int(input("Enter number to add(-1 to stop: )"))

print("The total is:", total)























# correct_pin = 1122
# attempts = 0

# while attempts<3:
#     pin = int(input("Enter pin: "))
    
#     if pin == correct_pin:
#         print("Correct pin")
#         break
#     else:
#         print("Incorrect pin")
#         attempts+=1
    
# if attempts >=3:
#     print("Account locked..!")        














# password = ""

# while password != "abc1234":
#     password = input("Enter password: ")
    
# print("You're logged in")










# battery = 15

# while battery <=100:
#     print("Charging...", battery, "%")
#     battery += 1











# i = 1

# while i<=20:
#     print(i)
#     i = i+2
























# run = True

# while run == True:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     option = input("What do you wanna do(+, -, *, /, exit): ")

#     match option:
#         case "+":
#             print("The sum is:", num1+num2)
#         case "-":
#             order = int(input("1. num1-num2 \n2. num2-num1\n"))
#             if order == 1:
#                 print("The difference is: ", num1-num2)
#             elif order == 2:
#                 print("The difference is: ", num2-num1)
#             else:
#                 print("Wrong input")    
#         case "*":
#             print("The product is: ", num1*num2)
#         case "/":
#             order = int(input("1. num1/num2 \n2. num2/num1\n"))
#             if order == 1:
#                 print("The quotient is: ", num1/num2)
#             elif order == 2:
#                 print("The quotient is: ", num2/num1)
#             else:
#                 print("Wrong input")  
#         case "exit":
#             print("Thank you for using")
#             run = 0      
#         case _:
#             print("Error..!")




























# total = 0
# num = 0

# while num != -1:
#     num = int(input("enter number to add(-1 to stop): "))
#     total = total+num

# total = total+1
# print("The total:", total)


















# correct_pin = 1122
# attempts = 0
# balance = 4500

# while attempts<3:
#     pin = int(input("Enter pin: "))

#     if pin == correct_pin:
#         print("Correct pin")
#         withdraw = int(input("How much do you want to withdraw: "))
        
#         if withdraw <= balance:
#             balance = balance -withdraw
#             print("Withdrawal successful, new balance: ", balance)
#         else:
#             print("Insufficient balance")    
#         break
#     else:
#         print("Wrong pin")
#         attempts = attempts+1 













# password=""

# while password != "abc123":
#     password = input("Enter password: ")

# print("You're logged in")  


















# battery = 10

# while battery<=100:
#     print("Charging...", battery,"%")
#     battery=battery+1







# i = 0

# while i<=5:
#     print("Hello", i)
#     i=i+1 