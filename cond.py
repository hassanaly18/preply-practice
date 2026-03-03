#conditional statements
# if, else, elif, match/case

points = int(input("Enter your points: "))

if points >= 50 and points < 101:  
    print("Pass")                  
elif points>=0 and points<50:        
    print("Failed")                
else:                              
    print("Enter points between 0 and 100") 


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