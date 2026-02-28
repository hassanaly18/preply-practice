store = {}
total =0

num = int(input("How many items do you wanna add: "))

for i in range(num):
    name = input("Enter name of item: ")
    price = int(input("Enter price of item: "))
    
    store["item"+str(i)] = {"name": name, "price": price}

print("\nItems in your Cart...")
for item in store:
    print("Name:", store[item]["name"], ",Price:", store[item]["price"])
    total = total + store[item]["price"]

remove = input("Enter name of item to remove: ")
for item in store:
    if remove == store[item]["name"]:
        del store[item]
        print("Item deleted")
        break

print("\nYour total bill:", total)
