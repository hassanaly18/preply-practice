#conditional statements
# if, else, elif, match/case
# nested if else

corr_user = "hassan18"
corr_pass = "abc123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == corr_user:
    if password == corr_pass:
        print("Logged in..!")
    else:
        print("wrong password..!")
else:
    print("Wrong username..!")












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