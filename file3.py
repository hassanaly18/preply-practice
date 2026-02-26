#r = read mode
#w = write mode
#a = append/update mode

name = input("Enter your name: ")
age = input("Enter age: ")

with open("data3.txt", "a") as file:
    file.write("Name: "+ name +"\n")
    file.write("Age:" + age + "\n")








# name = input("Enter your name: ")
# age = input("Enter age: ")

# with open("data3.txt", "w") as file:
#     file.write("Name: "+ name +"\n")
#     file.write("Age:" + age)










# with open("data3.txt", "w") as file:
#     file.write("Today we are learning file handling!")


# #read a file line by line
# with open("data3.txt", "r") as file:
#     for line in file:
#         print("Student:", line.strip())


#reading a file in python
# with open("data3.txt", "r") as file:
#     content = file.read()
#     print(content)