#question 7

items = {}

while True:
    print("\n1. Add item \n2. View Items \n3. Exit")
    choice = int(input("Enter your choice(1,2,3): "))
    
    match choice:
        case 1:
            name = input("Enter name of item: ")
            price = int(input("Enter price of item: "))
            items[name] = price
            print(name, "added to cart successfully")
        
        case 2:
            print("\n")
            for item in items:
                print("Name :", item, "| Price:", items[item])
        
        case 3:
            print("Program exiting..!")
            break
        
        case _:
            print("Wrong input")



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