balance = 8000

print("ATM Machine \n1. Check balance \n2. Withdraw \n3. Deposit")
choice = int(input("Enter your choice(1,2,3): "))

match choice:
    case 1:
        print("Your current balance is:", balance)
    case 2:
        amount = int(input("How much do you want to withdraw: "))
        if amount<=balance:
            balance = balance - amount
            print(balance, "successfully withdrew..\nThe new balance is", balance)   
        else:
            print("Insuffucient balance")
    case 3:             














# match choice:
#     case 1:
#         marks = int(input("Enter your marks: "))
#         if marks>=50:
#             if marks >=85:
#                 print("Grade A")
#             elif marks>=75:
#                 print("Grade B")
#             elif marks>=65:
#                 print("Grade C")
#             else:
#                 print("Grade D")            
#         else:
#             print("You are fail")  
        





# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# choice = input("Enter choice (+, -, *, /): ")

# match choice:
#     case "+":
#         print("the sum is", num1+num2)
#     case "-":
#         print("Enter your option \n1. num1-num2 \n2. num2-num1")
#         option = int(input("Your option(1,2): "))
        
#         if option ==1:
#             print("using - ", num1-num2)
#         elif option ==2:
#             print("using - ", num2-num1)
#         else:
#             print("wrong option")
                
#     case "*":
#         print ("using * multiplication", num1*num2)
#     case "/":
#         print ("using division",num1/num2)
#     case _:
#         print("not defined in this calculator")



















# letter = input("Enter a letter: ")

# match letter:
#     case "a":
#         print("a is a vowel")
#     case "e":
#         print("e is a vowel")
            
# if letter=="a" or letter=="e" or letter== "i" or letter=="o" or letter=="u"




# day=int(input("Enter the day number: "))

# match day:
#     case 1:
#         print ("that's Monday") 
#     case 2: 
#         print("tues")
#     case 3:
#         print("wed")
#     case 4:
#         print("thurs")
#     case 5:
#         print("frid") #2
#     case 6:
#         print("sat")
#     case 7:
#         print("sun") 
#     case _:
#         print("wrong input")                       
    
# if day == 1:   #1
#     print ("that's Monday") 
# elif day ==2: #1
#     print ("that's Tuesday")
# elif day ==3: #1
#     print ("that's WEdnesday")
# elif day==4: #1
#     print ("thats Thursday")
# elif day ==5: #1
#     print ("Friday") #1
# elif day==6: #1
#     print ("Saturday")
# elif day==7: #1
#     print("Sunday")
# else: #1
#     print("day can't be more than 7") #1













# marks = int(input("Enter marks: "))

# if marks>=50:
#     if marks >=85:
#         print("Grade A")
#     elif marks>=75:
#         print("Grade B")
#     elif marks>=65:
#         print("Grade C")
#     else:
#         print("Grade D")            
# else:
#     print("You are fail")    










# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin":
#     if password == "1234":
#         print("Logged in")
#     else:
#         print("wrong password") 
# else:
#     print("wrong username")         














# num = int(input("Enter a number: "))

# if num>=0:
#     if num ==0:
#         print("The number is zero")
#     else:
#         print("The number is positive")
# else:
#     print("The number is negative")            



















# age = 18

# if age >= 18:
#     print("I can drive")
# else:    
#     print("I can not drive")

# num = 8

# if num > 0:
#     print("Positive")
# elif num<0:
#     print("Negative")
# else:
#     print("The number is Zero")    

# marks = 86

# age = 45

# if age >= 20 and age <=30:
#     print("You are a young person")
    
# if age>= 20 or age<=30:
#     print("you are a young person")






# if num%2 == 1:
#     print("The number is odd")
# else:
#     print("The num is even")    