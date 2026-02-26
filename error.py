age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age can not be negative")        

print("Your age",age)












# try:
#     file = open("data9.txt", "r")
#     file.read()
# except:
#     print("File not found")















# try:
#     amount = int(input("Enter amount: "))
# except:
#     print("Write valid amount")
# else:
#     print("You withdrew: ", amount)
# finally:
#     print("Thanks for using the ATM")        

  
    






# age = int(input("enter age: "))
# print(10/age)


# try:
#     age = int(input("enter age: "))
#     print(10/age)
# except ValueError:
#     print("enter only an integer")
# except ZeroDivisionError:
#     print("You cant divide a number by 0, write anything other than 0")    

# print("Hello")

















#runtime Error

# try:
#     file = open("data9.txt")
#     print(file.read())
# except:
#     print("File is not present")    




















# try:
#     a = int(input("Enter numerator: "))
#     b = int(input("Enter denominator: "))
#     c = a/b
    
# except Exception as e:
#     print("Something went wrong: ", e)

# else:
#     print("The result:", c)

# finally:
#     print("Program ended.")    







# try:
#     num = int(input("Enter a number: "))
#     print("Result: ", num+5)
# except ValueError:
#     print("Write correct input kindly..")
     
# print("hello after error")