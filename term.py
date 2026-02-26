from colorama import Fore, Back, Style, init
init()

print(Fore.CYAN + "==== MENU ====")
print(Fore.GREEN + "1. Start Game")
print(Fore.YELLOW + "2. Settings")
print(Fore.RED + "3. Exit" + Style.RESET_ALL)

choice = int(input("Enter your choice: "))

if choice ==1:
    print(Fore.GREEN + "Game started..!"  + Style.RESET_ALL)
elif choice ==2: 
    print(Fore.YELLOW + "Opening the settings..!"  + Style.RESET_ALL)
elif choice ==3:
    print(Fore.RED + "Exiting...!"  + Style.RESET_ALL)
else:
    print(Fore.RED + "Invalid option..!"  + Style.RESET_ALL)













#print(Fore.WHITE + Back.BLUE + Style.BRIGHT + "Welcome to my app!" + Style.RESET_ALL)

#foreground
# print(Fore.RED + "This is red text")
# print(Fore.GREEN + "This is green text")
# print(Fore.BLUE + "This is blue text")

# #background
# print(Back.YELLOW + "Yellow background")
# print(Back.RED + "Red background" + Style.RESET_ALL)

# print("Hello world")

# print(Style.BRIGHT + "Bright text")
# print(Style.DIM + "Dim text")
# print(Style.NORMAL + "Normal text")