#r = read mode
#w = write mode
#a = append/update mode


# with open("data1.txt", "w") as file:
#     file.write("We just learned about reading \ntext from a file using python")
#     file.write("\nAnything")


username = input("Enter username: ")
password = input("Enter password: ")

with open("data1.txt", "a") as file:
    file.write("Username: " + username+" Password: " + password + "\n")


print("Login info saved successfully..")










# line_no=1
# with open("data1.txt", "r") as file:
#     for line in file:
#         print(line_no,".",line.strip())
#         line_no+=1



# file = open("data1.txt", "r")  #opening file in variable
# content = file.read()          #reading and storing content of file
# print(content)                 #printing content
# print(file)
# file.close()                   #closing file