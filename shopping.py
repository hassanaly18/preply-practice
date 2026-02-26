




# #Items available in the shop
# items = [
#     {"name": "Apple", "price": 10},
#     {"name": "Bread", "price": 15},
#     {"name": "Milk", "price": 20},
#     {"name": "Eggs", "price": 8},
#     {"name": "Chocolate", "price": 5},
# ]

# cart = [] 

# def show_items():
#     print("\nAvailable items:")
#     for i in range(len(items)):
#         print(i+1, ".", items[i]["name"], "-", items[i]["price"])
        
# def add_to_cart():
#     show_items()
#     choice = int(input("Enter item number to add: ")) - 1
    
#     if choice>=0 and choice < len(items):
#         cart.append(items[choice])
#         print(items[choice]["name"], "added to cart successfully")
#     else:
#         print("Invalid choice")
        
# def remove_items():
#     if len(cart) ==0:
#         print("Cart is already empty")
#         return
#     print("\nYour Cart:")
#     for i in range(len(cart)):
#         print(i+1, ".", items[i]["name"], "-", items[i]["price"])
    
#     choice = int(input("Which item do you want to remove? "))
#     if choice>=0 and choice<len(items):
#         removed = cart.pop(choice-1)
#         print(removed["name"], "removed from the cart")
#     else:
#         print("invalid Choice..!")    
        
# def view_cart():
#     if len(cart)==0:
#         print("Your cart is empty")
#         return
    
#     total = 0
#     print("\nYour Cart:")
#     for i in range(len(cart)):
#         print(i+1, ".", cart[i]["name"], "-", cart[i]["price"])
#         total = total + cart[i]["price"]
    
#     print("Total bill:", total)    

# while True:
#     print("SHopping Cart Menu\n")
#     print("1. View Items")
#     print("2. Add items to cart")
#     print("3. Remove from Cart")
#     print("4. View the Cart")
#     print("5. Exit")
    
#     choice = int(input("Choose an option(1-5): "))
    
#     match choice:
#         case 1:
#             show_items()
#         case 2:
#             add_to_cart()
#         case 3:
#             remove_items()
#         case 4:
#             view_cart()
#         case 5:
#             print("Thanks for using the shopping cart")
#             break
#         case _:
#             print("Invalid option. Try again..!")                
