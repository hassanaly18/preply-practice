print("...Calculator...\n")

while True:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    choice = input("What do you wanna do(+,-,*,/)? ")
    
    match choice:
        case "+":
            print("The sum is:", num1+num2)
        case "-":
            print("The difference is:", num1-num2)
        case "*":
            print("The product is:", num1*num2)
        case "/":
            print("The quotient is:", num1/num2) 
        case _:
            print("Wrong choice")  
    
    again = input("Do you want to use the calculator again(y/n)?")
    
    if again =="n":
        print('\nThanks for using the calculator..!\n')
        break         
    

















# for i in range(1,6):
#     spaces = " " *(5-i) #4
#     stars = "*" * (2*i-1)
#     print(spaces+stars)




# for i in range(5,0,-1):
#     print("*" * i)
    
# print("a" * 6)    
    
# secret = 67 

# for i in range(3):
#     guess = int(input("Guess the number: "))
    
#     if guess == secret:
#         print("You guessed right..!")
#         break
#     else:
#         print("try again..")
    
# print("game over")











# for i in range(10):
#     if i==6:
#         continue
#     print(i)

# print("Outside the loop")


# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     if num*i >=40:
#         break
#     print(num, "*", i, "=", num*i)

# print("Outside the loop")








# total = 0

# # total = 15, i = 6
# for i in range(1,6):
#     total = total + i

# print("Total:", total)





# name = "Python"

# for letter in name:
#     print("letter",letter)

# for i in range(10, 0, -1):
#     print(i)














# correct = "123abc"

# password = input("Enter password:")

# while password != correct:
#     password = input("Enter password:")
    
# print("Logged in..!")    
















# total = 0
# count =0

# num = int(input("How many items did you buy? "))

# while count < num:
#     price = int(input("enter price of item "+ str(count+1)+ ": "))
#     total = total + price
#     count = count+1

# print("Total bill:", total)










# count = 1

# while count <20:
#     print(count)
#     count = count+2

# while count<20:
#     if count%2 == 1:
#         print(count)
#     count = count+1    




# num = int(input("Enter a number: "))

# while num != 7:
#     num = int(input("Enter a number: "))
    
# print('end of loop')    