from tabulate import tabulate
from colorama import Fore, Back, Style, init
init(autoreset=True)

students = [
    [Fore.MAGENTA +"Mike", 95, 15],
    ["Theodore", 87, 14],
    ["Harry", 85, 16],
    ["Hassan", 99, 15],
    ["Emma", 92, 17],
    ["John", 65, 15],
]

while True:
    print("\n1. Add student \n2. View Students \n3. Exit")
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            name = input("Enter name of student: ")
            marks = input("Enter marks of student: ")
            age = input("Enter age of student: ")
            students.append([name, marks, age])
            print("New student added")
        case 2:
            print(tabulate( students, headers=[Fore.CYAN + Back.WHITE + Style.BRIGHT + "Name",Fore.RED + "Marks", Fore.GREEN +"Age" + Style.RESET_ALL], tablefmt="rounded_grid"))

        case 3:
            print("Exiting..")
            break
        case _:
            print("Invalid input")