def analyze():
    positive =0
    negative =0
    even =0
    odd =0
    
    for i in range(5):
        num = int(input("Enter a number: "))
        
        if num>=0:
            positive = positive+1
        else:
            negative = negative+1
        
        if num%2 ==0:
            even = even+1
        else:
            odd = odd +1
    
    print("Positive:",  positive)    
    print("Negative:",  negative)    
    print("Even:", even)    
    print("Odd:", odd)    

def grade_student(marks):
    if marks>=80:
        return "A"
    elif marks >=70:
        return "B"
    elif marks >=60:
        return "C"
    elif marks >=50:
        return "D"
    else:
        return "Fail"

def login_system():
    correct = "123abc"
    
    for i in range(3):
        password = input("Enter password: ")
        if password == correct:
            print("Access granted")
            return
        else:
            print("Wrong password")
    
    print("Account locked")

# login_system()

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Cannot divide by zero"
    
    return a/b

# while True:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
    
#     print("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Exit")
#     choice = int(input("Enter your choice: "))
    
#     match choice:
#         case 1:
#             print("The sum is:", add(num1,num2))
#         case 2:
#             print("The difference is:", subtract(num1, num2))
#         case 3:
#             print("The product is:", multiply(num2, num1))
#         case 4:
#             print("The quotient is:", divide(num1,num2))
#         case 5:
#               print("Thanks for using our program")
#               break      


def atm():
    balance = 4000
    
    while True:
        print("*******ATM********\n1. Check Balance \n2. Deposit \n3. Withdraw \n4. Exit")
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                print("Balance:", balance)
            case 2:
                amount = int(input("Enter amount to deposit: "))
                balance = balance+amount
            case 3:
                amount = int(input("Enter amount to withdraw: "))
                
                if amount<=balance:
                    balance = balance-amount
                else:
                    print("Insufficient balance..")
            case 4:
                print("Thanks for using our program")
                break 
        



def largest(a,b,c):
    max = a
    
    if b> max:
        max =b
    if c>max:
        max=c
    
    print("The largest number:", max)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest(num1, num2, num3)