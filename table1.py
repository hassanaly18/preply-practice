from tabulate import tabulate
from colorama import Back, Fore, Style, init
init(autoreset=True)

cart = []

def show_cart():
    total =0
    table=[]
    
    if not cart:
        print(Fore.RED+"Cart is empty")
        return
    
    for item in cart:
        table.append([item["name"], item["price"]])
        total = total + item["price"]
    
    print(tabulate(table, headers=["Item", "Price"], tablefmt="grid"))
    print(Fore.GREEN+f"Total: {total}")

def add_item():
    name = input("Enter item's name: ")
    
    try:
        price = int(input("Enter price of item: "))
    except ValueError:
        print(Fore.RED+"Invalid price..!")
        return
    
    cart.append({
        "name": name,
        "price": price
    })
    print(Fore.GREEN+"Item added successfully..!")
    

while True:
    print(Fore.CYAN+"\n1. Add Item \n2. View Cart \n3.Exit")
    choice = int(input("Enter choice: "))
    
    match choice:
        case 1:
            add_item()
        case 2:
            show_cart()
        case 3:
            print(Fore.YELLOW+"Goodbye..!")
            break
        case _:
            print(Fore.RED+"Invalid input")














# systems = [
#     ["Server", "Online"],
#     ["Database", "Offline"],
#     ["API", "Online"],
# ]
# table = []

# for name, status in systems:
#     if status == "Online":
#         status_colored = Fore.GREEN + status
#     else:
#         status_colored = Fore.RED + status
    
#     table.append([name, status_colored])

# print(tabulate(table, headers=[Style.BRIGHT +"System", "Status"], tablefmt="pipe"))
















# students = [
#     ["Mike", 85],
#     ["John", 45],
#     ["Emma", 70],
#     ["Tyson", 99]
# ]
# table=[]

# for name, marks in students:
#     if marks>=80:
#         grade = Fore.GREEN+"A"
#     elif marks>= 50:
#         grade = Fore.YELLOW + "B"
#     else:
#         grade = Fore.RED + "F"
    
#     table.append([name, marks, grade])

# print(tabulate(table, headers=["Name", "Marks", "Grade"], tablefmt="fancy_grid"))



# data = [
#     [Fore.GREEN+"Apple", 10],
#     [Fore.RED +"Cherry", 5],
#     [Fore.YELLOW+"Orange", 7]
# ]
# headers = [Style.BRIGHT +"Item", "Price"]

# print(tabulate(data, headers=headers, tablefmt="grid"))