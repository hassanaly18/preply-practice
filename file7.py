# r = read mode
# w = write mode
# a = append mode

# def studentMarks():
#     my = open("random.txt", "a")
    
#     name = input("Enter name: ")
#     marks = input("Enter marks: ")
    
#     my.write(name + " " + marks + "\n")
#     my.close()
    
# studentMarks()    

# def empty_file(filename):
    
#     file = open(filename, "w")
#     file.close()

# empty_file("info.txt")    









# def register():
#     user = input("Enter new username: ")
#     password = input("Enter a password: ")
    
#     file = open("users.txt", "a")
#     file.write(user + "," + password + "\n")
#     file.close()
#     print("New user registered!\n")
 
# def login():
#     print("Login")
#     user = input("Enter username: ")
#     password = input("Enter a password: ")
    
#     file = open("users.txt", "r")
#     for line in file:
#         u,pwd = line.strip().split(",")
        
#         if u==user and pwd==password:
#             print("Login Successful")
#             return
#     print("Login Failed")

# login()





















# def add_expense():
#     item = input("Enter name of item: ")
#     price = input("Enter price: ")
    
#     file = open("expenses.txt", "a")
#     file.write(item + "," + price + "\n")
#     file.close()
    
# def total_expenses():
#     total = 0
    
#     file = open("expenses.txt", "r")
    
#     for line in file:
#         parts = line.strip().split(",")
        
#         total = total + int(parts[1])    
    
#     print("The total expense: ", total)    
    
    
# total_expenses()

















# #task 1
# def addToFile():
#     file = open("student.txt", "a")

#     name = input("Enter name: ")
#     file.write(name + "\n")
#     file.close()
    
# def show_students():
#     file = open("student.txt", "r")
#     print("\nStudents List\n")
#     print(file.read())    

# show_students()









# file = open("randomdata.txt", "a")
# file.write("\nThis is the updated data")
# file.close()

















# file = open("randomdata.txt", "w")
# file.write("This is the new data")
# file.close()


# with open("randomdata.txt", "w") as file:
#     file.write("New data from the second method")










# file = open("randomdata.txt", "r")
# data = file.read()
# file.close()

# print(data)

# with open("randomdata.txt", "r") as file:
#     data = file.read()
#     print(data)
    
    