from tabulate import tabulate
from colorama import Back, Fore, Style, init
init()

students =[
    ["Mike", 99],
    ["Theodore", 55],
    ["Emma", 77],
    ["John", 85],
]

table =[]

for name, marks in students:
    if marks>=80:
        color = Fore.GREEN
    elif marks>=50:
        color = Fore.YELLOW
    else:
        color = Fore.RED
        
    table.append([name, color + str(marks)])

print(tabulate(table, headers=['Name', "Marks"], tablefmt="grid"))

# #list of lists
# data = [
#     ["Apples", 120],
#     ["Peach", 70], 
#     ["Snickers", 65],
#     ["Eggs", 50]
# ]

# data2 = [
#     {"name": "Apples", "price": 120},
#     {"name": "Snickers", "price": 20},
#     {"name": "Monster", "price": 70},
#     {"name": "Guava", "price": 65},
# ]

# table = []
# total =0

# for item in data2:
#     table.append([ Fore.CYAN +item["name"], Fore.YELLOW + str(item["price"])])
#     total = total + item["price"]

# print(tabulate(table, headers=["Name", "Price"], tablefmt="grid"))
# print(Fore.GREEN + "Total Price: ", total)
# print(tabulate(data, headers=["Item", "Price"], tablefmt="grid"))
# print(tabulate(data, headers=["Item", "Price"], tablefmt="pretty"))