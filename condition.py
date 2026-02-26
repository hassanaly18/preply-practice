#conditional statemants
#if, else, elif, match/case

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

option = input("What do you wanna do(+, -, *, /): ")

match option:
    case "+":
        print("The sum is:", num1+num2)
    case "-":
        order = int(input("1. num1-num2 \n2. num2-num1\n"))
        if order == 1:
            print("The difference is: ", num1-num2)
        elif order == 2:
            print("The difference is: ", num2-num1)
        else:
            print("Wrong input")    
    case "*":
        print("The product is: ", num1*num2)
    case "/":
        order = int(input("1. num1/num2 \n2. num2/num1\n"))
        if order == 1:
            print("The quotient is: ", num1/num2)
        elif order == 2:
            print("The quotient is: ", num2/num1)
        else:
            print("Wrong input")  
    case _:
        print("Error..!")


















# signal = input("Enter color of light: ")

# match signal:
#     case "red":
#         print("STOP..")
#     case "yellow":
#         print("Warning..!")
#     case "green": 
#         print("Go..!")  
#     case _:
#         print("Wrong color..!")



# if signal=="Red":   #2
#     print(" STOP")
# elif signal=="Yellow":   #2
#     print("GET READY !!!")
# elif signal=="Green":    #2
#     print(" GO !")       #2
# else:
#     print(" Wrong colour , please try again ! ")














# temp = int(input("Enter temperature: "))

# if temp > 40:
#     print("Very hot")

# elif temp > 30:
#     print("Warm")

# elif temp > 20:
#     print("Pleasant")

# else:
#     print("Cold")














# marks = int(input("Enter marks: "))

# if marks >= 80:
#     print("Grade A")

# elif marks >=70:
#     print("Grade B")

# elif marks >=60:
#     print("Grade C")

# elif marks >= 50:
#     print("Grade D")

# else:
#     print("Grade F, FAIL")
















#nested if else

#ask the user for total bill,
#if bill is more than 2000, then
#if you have membership, then 25% discount, otherwise 10% discount

#if bill is les than 2000
#then we'll check if it is more than 1000, we'll give 5% discount
#less than 100, no discount

# bill = int(input("Enter total shopping bill: "))

# if bill >= 2000:
#     member = input("Do you have a membership(yes/no): ")
#     if member == "yes":
#         bill = bill * 0.75
#         print("Your discounted bill:", bill)
#     else:
#         bill = bill * 0.90  
#         print("Your discounted bill:", bill)
# else:  
#     if bill >= 1000:
#         bill = bill*0.95
#         print("Your discounted bill:", bill)
#     else:
#         print("Total bill without discount:", bill)
























# balance = 2500

# print("Choose an option")
# print("1. balance\n2. deposit \n3. withdraw")
# option = int(input("Your option(1-3): "))

# match option:
#     case 1:
#         print("Your total balance: ", balance)
#     case 2:
#         dep_amount = int(input("Enter deposit amount: "))
#         balance = balance+dep_amount 
#         print("New balance: ", balance)
#     case 3:
#         w_amount = int(input("Enter amount to withdraw: "))
        
#         if w_amount > balance:
#             print("Insufficient balance...")
#         else:
#             balance = balance - w_amount
#             print("Transaction succesful\nNew balance: ", balance)




# print("\n********************************")
# print("Welcome to our calculator..!")
# print("********************************\n")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# operator = input("What do you wanna do(+, -, *, /): ")

# match operator:
#     case "+":
#         print("The sum is:", num1+num2)

#     case "-":
#         print("1. num1-num2 \n2. num2-num1")
#         option = int(input("Write 1 or 2: "))
#         if option ==1:
#             print("The result is:", num1-num2)
#         elif option == 2:
#             print("The result is:", num2-num1)
#         else:
#             print("Wrong input")

#     case "*":
#         print("The product is:", num1*num2)
#     case "/":
#         print("The quotient is:", num1/num2)
#     case _:
#         print("Sorry, Wrong input, run the calculator again")

# print("\n**********************************")
# print("Thank you for using our Calculator..!")
# print("**********************************\n")









# # day = input("Write day number(1-7): ")

# # match day:
# #     case "1":
# #         print("Monday")
# #     case "2":
# #         print("Tuesday")
# #     case "3":
# #         print("Wednesday")        
# #     case "4":
# #         print("Thursday")        
# #     case "5":
# #         print("Friday")        
# #     case "6":
# #         print("Saturday")        
# #     case "7":
# #         print("Sunday")    
# #     case _:
# #         print("Wrong number")   



# # color = input("Enter color of light: ")

# # match color:
# #     case "red":
# #         print("STOP....")
# #     case "yellow":
# #         print("WARNING...")
# #     case "green":
# #         print("Go....")
# #     case _:
# #         print("Wrong color")      




# # if color == "red":
# #     print("STOP....")
# # elif color == "yellow":
# #     print("WARNING...")
# # elif color == "green":
# #     print("GO...")
# # else:
# #     print("Wrong color")        













# # Task: Password Strength Check

# # password = input("Enter password: ")

# # length = len(password)

# # if length<4:
# #     print("Very weak")
# # elif length<8:
# #     print("Weak")
# # elif length<12:
# #     print("Strong")
# # else: 
# #     print("Very strong")














# #Task: Sports Category Checker
# # age = int(input("Enter your age: "))

# # if age<=10:
# #     print('Under-11 Category')
# # elif age<=15:
# #     print("Under-16 Category")
# # elif age<=18:
# #     print("Under-19 Category")
# # else:
# #     print("Adult Category")








# # check = input("Do you have a license(y/n): ")

# # if check == "y":
# #     print("You can drive")

# # if check == "n":
# #     print("You can NOT drive")

# # if check != "y" and check != "n":
# #     print("wrong input")








# # correct = "abc123"
# # password = input("Enter password: ")

# # if password == correct:
# #     print("Logged in...")

# # if password != correct:
# #     print("Wrong password...")








# # age = 18

# # if age >= 18:
# #     print("You are an adult")

# # if age < 18:
# #     print("You are NOT an adult")

# # print("welcome")    