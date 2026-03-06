#conditional statements
# if, else, elif, match/case
# nested if else

total = int(input("Enter total shopping amount: "))

if total > 2000:
    card = input("Do you have a membership card?(yes/no): ")
    
    if card == "yes":
        total = total * 0.75
        print("The total after 25 percent discount:", total)
    else:
        total = total * 0.9
        print("The total after 10 percent discount:", total)

else: 
    if total >1000:
        total = total * 0.95
        print("The total after 5 percent discount:", total)
    else:
        print("The total after no discount:", total)
        
print("Total after updating it:", total)













# balance = 9000
# age = int(input("Enter your age: "))

# if age >= 18:
#     movie = input("Do you wanna watch a 3D movie(yes/no): ")
#     if movie == "yes":
#         print("Price: $800")
#     else:
#         print("Price: $600")

# else:
#     parent = input("Are you with a parent(yes/no): ")
#     if parent == "yes":
#         print("Price: $500")
#     else:
#         print("You can not watch this movie")    













# corr_user = "hassan18"
# corr_pass = "abc123"

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == corr_user:
#     if password == corr_pass:
#         print("you are logged in")
#     else:
#         print("wrong password")
# else:
#     print("Wrong username")











# age = int(input("Enter your age: "))

# if age >= 18:
#     license = input("Do you have a license?(yes/no): ")
#     if license == "yes":
#         print("You can drive")
#     else:
#         print("You can not drive, no license")
# else:
#     print("You can not drive, underage")











# username = input("Enter username: ")
# password = input("Enter password: ")

# if username not in password:
#     print(True)
# else:
#     print(False)





# age = int(input("Enter your age: "))
# price =0

# if age >= 18:
#     movie3d = input("Do you want to watch a 3D movie?(yes/no): ")
    
#     if movie3d == "yes":
#         price = 800
#     else:
#         price =600

# else:
#     parent = input("Are you with a parent? (yes/no): ")
#     if parent == "yes":
#         price=500
#     else:
#         print("You cannot watch this movie")

# print("Price for ticket:", price)
    














# corr_user = "hassan123"
# corr_pass = "abc123"

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == corr_user:
#     if password == corr_pass:
#         print("You're logged in")
#     else:
#         print("Incorrect password")
        
# elif username != corr_user and password!=corr_pass:
#     print("Incorrect username and password")
# else:
#     print("incorrect username")














# age = int(input("Enter your age: "))

# if age <18:
#     print("You can not drive, underage")
# else:
#     license = input("Do you have a license(yes/no): ")
#     if license == "yes":
#         print("You can drive")
#     elif license == "no":
#         print("You can not drive, no license")
#     else:
#         print("Invalid input")


















# corr_user = "hassan18"
# corr_pass = "abc123"

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == corr_user:
#     if password == corr_pass:
#         print("Logged in..!")
#     else:
#         print("wrong password..!")
# else:
#     print("Wrong username..!")












# if age <18, you can not drive
# if age >=18, do you have license, if yes license, drive, else no drive

# age = int(input("Enter your age: "))

# if age>=18: 
#     license = input("Do you have a license(yes/no): ")
#     if license == "yes":
#         print("You can drive")
#     else:
#         print("you cannot drive, no license")
# else:
#     print("you can not drive, age less than 18")











# num = int(input("Enter a number: "))

# if num%2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")





# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     print("num1 is larger number:", num1)
# elif num1<num2:
#     print("num2 is the larger number:", num2)
# else:
#     print("Both numbers are equal")











# points = int(input("Enter your points: "))

# if points >= 50 and points < 101:  
#     print("Pass")                  
# elif points>=0 and points<50:        
#     print("Failed")                
# else:                              
#     print("Enter points between 0 and 100") 


# pin = int(input("Enter pin: "))

# if pin == 1122:
#     print("Correct pin..!")
# else:
#     print("Try again, wrong pin..!")

# age = 18

# if age >= 18:
#     print("You can drive")
# else:
#     print("You can NOT drive")