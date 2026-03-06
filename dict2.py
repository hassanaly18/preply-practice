cart =[
    {"name": "apple", "price": 89},
    {"name": "eggs", "price": 78}]

def removeItem():
    global cart
    name = input("Enter item to remove: ")
    for item in cart:
        if name == item["name"]:
            cart.remove(item)
            print("Item deleted successfully")
            break
    
def calculate_total(cart):
    total =0
    for item in cart:
        total += item["price"]
    print("The total bill: $", total)

def addItem():
    global cart
    name = input("\nEnter item's name: ")
    price = int(input("Enter item's price: "))
    item = {
        "name": name,
        "price": price
    }
    cart.append(item)
    print(name, "added to cart successfully")

def showItems():
    global cart
    print("\nItems in tha cart\n")
    for item in cart:
        print(item["name"], "|", item["price"])

while True:
    print("\n1. Add item \n2. Show all items \n3. Calculate total \n4. Remove an Item \n5.Exit")
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            addItem()
        case 2:
            showItems()
        case 3:
            calculate_total(cart)
        case 4:
            removeItem()
        case 5:
            break
        case _:
            print("Invalid input..")













#question 11

# cart = []

# def addItem():
#     global cart
#     name = input("\nEnter name of item: ")
#     price = input("Enter price of item: ")
#     cart.append({"name": name, "price": price})
#     print(name, "added to cart successully..!")

# def showItems(cart):
#     print("\n")
#     for item in cart:
#         print(item["name"], ":", item["price"])
        
# def removeitem():
#     global cart
#     name = input("Enter name of item to remove: ")
#     for item in cart:
#         if name == item["name"]:
#             cart.remove(item)
#             print(item["name"], "removed from cart")

# def calc_bill(cart):
#     total =0
#     for item in cart:
#         total = total + item["price"]
#     print("The total bill:", total)

# print("**** Mini Store System ****")

# while True:
#     print("\n1. Add item \n2. Show Items \n3. Remove an item \n4. Calculate total bill \n5. Exit")
#     choice = int(input("What do you wanna do: "))
    
#     match choice:
#         case 1:
#             addItem()
#         case 2:
#             showItems(cart)
#         case 3:
#             removeitem()
#         case 4:
#             calc_bill(cart)
#         case 5: 
#             break
#         case _:
#             print("Invalid input")
            
            


#question 10

# items = [
# {"name": "Apple", "price": 10},
# {"name": "Milk", "price": 20},
# {"name": "Cake", "price": 50}
# ]

# highestP =""
# highest = 0

# for item in items:
#     if item["price"] > highest:
#         highest = item["price"]
#         highestP = item

# print("The highest priced item is", highestP["name"], "with the price:", highestP["price"])



#question 6

# students = {
# "s1": {"name": "Ali", "marks": 80},
# "s2": {"name": "Sara", "marks": 90}
# }

# highestM = 0
# highestS = ""

# for student in students:
#     print("Name:" , students[student]["name"], "|","Marks:", students[student]["marks"])
    
# name = input("\nEnter name of new student: ")
# marks = int(input("Enter marks of new student: "))
# students["s3"] = {"name": name, "marks": marks}

# print("\nStudent info after adding a student")
# for student in students:
#     print("Name:" , students[student]["name"], "|","Marks:", students[student]["marks"])
#     if students[student]["marks"] > highestM:
#         highestM = students[student]["marks"]
#         highestS = student

# print("\nStudent with highest marks:", students[highestS]["name"], "and his marks are:", highestM)






#question 7

# items = {}

# while True:
#     print("\n1. Add item \n2. View Items \n3. Exit")
#     choice = int(input("Enter your choice(1,2,3): "))
    
#     match choice:
#         case 1:
#             name = input("Enter name of item: ")
#             price = int(input("Enter price of item: "))
#             items[name] = price
#             print(name, "added to cart successfully")
        
#         case 2:
#             print("\n")
#             for item in items:
#                 print("Name :", item, "| Price:", items[item])
        
#         case 3:
#             print("Program exiting..!")
#             break
        
#         case _:
#             print("Wrong input")



#question 5

# users = {
# "admin": "1234",
# "hassan": "abcd"
# }

# username = input("Enter username: ")
# password = input("Enter password: ")

# for user in users:
#     if user == username and users[user] == password:
#         print("Success -> Welcome")
#         break
#     else:
#         print("Fail → Invalid credentials")












# question 4

# cart = [
# {"name": "Apple", "price": 10},
# {"name": "Milk", "price": 20}]

# total = 0

# num = int(input("How many items you want to add in the cart? "))

# for i in range(num):
#     name = input("Enter item's name: ")
#     price = int(input("Enter item's price: "))
#     cart.append({"name": name, "price": price})
    
# remove = input("Item's name to remove: ")

# for item in cart:
#     if remove == item["name"]:
#         cart.remove(item)
    
# print("\nItems in cart \nName  | Price")
# for item in cart:
#     print(item["name"], ":", item["price"])
#     total = total+item["price"]

# print("\nTotal bill:", total)

#question 3

# sentence = input("Enter a sentence: ")
# freq = {}

# words = sentence.split()
# print(words)

# for word in words:
#     if word in freq:
#         freq[word] = freq[word] +1
#     else:
#         freq[word] = 1

# print(freq)

#question 2
# inventory = {
# "apple": 10,
# "banana": 5,
# "milk": 8
# }

# item = input("Enter name of item: ")
# qty = int(input("Enter quantity of item: "))

# inventory[item] = qty    #adding new itemin dictionary
# inventory["apple"] = 12  #updating quantity of existing item
# del inventory['milk']    #delete milk

# print("\nName | Quantity")
# for key in inventory:
#     print(key, ":", inventory[key])

#question 1
# student = {
#     "name": "John Doe",
#     "marks": [85, 89, 92]
# }

# total =0

# print("Name:",student["name"])
# for mark in student['marks']:
#     print("Marks:", mark)
#     total = total+mark

# print("\nTotal Marks:", total)

# avg = total/3

# if avg>80:
#     print("Grade A")
# elif avg >50:
#     print("Grade B")
# else:
#     print("Fail")