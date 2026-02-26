questions = ["What is the capital of France", "Which planet is called the Red Planet"]
options = [["Rome", "Paris", "Madrid", "Barcelona"], ["Venus", "Jupiter", "Mars", "Neptune"]]
answers = [2, 3]

def show_question(question, option):
    print("\n" + question)
    for i in range(len(option)):
        print(i+1,".", option[i])

def check(choice, answer):
    if choice == answer:
        print("Correct..!")
        return 10
    else:
        print("Wrong..!") 
        return -5   

def play(questions, options, answers):
    score = 0
    
    print("Welcome to the quiz..!")
    
    for i in range(len(questions)):
        show_question(questions[i], options[i])
        choice = int(input("Enter your choice(1/2/3/4): "))
        
        score = score + check(choice, answers[i])
        print("Current Score:", score)
    
    return score    

while True:
    final = play(questions, options, answers)
    print("\nQuiz is Over..\nFinal Score:", final)
    
    play_again = input("\nDo you want to attempt the quiz again?(yes/no): ").lower()      

    if play_again != "yes":
        print("Thanks for taing the quiz..!")
        break












# # problem 1

# # item1 = input("enter an item: ")
# # item2 = input("enter an item: ")
# # item3 = input("enter an item: ")
# # item4 = input("enter an item: ")
# # item5 = input("enter an item: ")

# # cart = {
# #     item1,
# #     item2,
# #     item3,
# #     item4,
# #     item5
# # }

# prices = []
# # total = 0

# for i in range(5):
#     price = int(input("Enter item's price: "))
#     prices.append(price)

# print("Total bill: ", sum(prices))    

# #problem 2

# name = input("enter your name: ")
# rollnum = input("enter you roll number: ")
# marks = int(input("enter your grade: "))

# studentinfo = {
#     "name" : name,
#     "rollnum": rollnum,
#     "marks": marks
# }
# print("Name: ", studentinfo["name"] , "\nRoll Num: ", studentinfo["rollnum"] , "\nMarks: " , studentinfo["marks"])

# #problem 3

# marks = int(input("enter your marks: "))

# if marks >= 90:
#     print("grade A")
# elif marks >= 75:
#     print("grade B")
# elif marks >= 50:
#     print("grade C")
# else:
#     print("Fail")

# #problem 4

# num = int(input("enter a number from 1-7: "))
# match num:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")
#     case _:
#         print("invalid day")    



# #problem 5

# temps = (
#     40,
#     50,
#     60,
#     100, 
#     70,
#     80,
#     90
# )

# print("Highest: ", max(temps), "\nLowest: ", min(temps))

# #problem 6

# sentence = input("enter a sentence: ")

# print(len(sentence))
# print(len(sentence.split()))
# print(sentence.upper())

# #problem 7

# username = "hello123"
# password = "12348765"

# user = input("enter your username: ")
# pw = input("enter your password: ")

# if username == user and pw == password:
#     print("you're logged in")
# else:
#     print("Access denied")

# #problem 8

# with open("message.txt", "r") as file:
#     data = file.read()
# print(data) 

# #problem 9

# name = input("enter student name: ")
# marks = input("enter student marks: ")

# studentinfo2 = {
#     "name" : name,
#     "marks" : marks
# }

# with open("message.txt", "w") as file:
#     file.write("Name: " + studentinfo2["name"] + "\nMarks: " + studentinfo2["marks"] )

# #problem 10

# items = []
# quantity = int(input("Enter no. of items bought: "))

# for i in range(quantity):
#     price = int(input("Enter item's price: "))
#     items.append(price)

# total = sum(items)   

# if total > 10000:
#     total = total * 0.8
# elif total > 5000:
#     total = total * 0.9        

# print("Total payable amount: ", total)

# #problem 11

# sentence2 = input("enter a sentence")
# word = input("enter a word")

# if word in sentence2:
#     print("word found: ")
# else:
#     print("word not found: ")

# #problem 12

# # names = ("mike","alice", "AJ")
# # numbers = (243-435-6432, 123-325-4953, 125-903-3920)

# # contacts = {
# #     names,
# #     numbers
    
# # }
# # name = input("enter a name")
# # if name in contacts:
# #     print 

# #problem 13

# with open("message.txt", "r") as file:
#     data = file.read()
    
# words = data.split()   
# print("no of words: ", len(words)) 

# problem 14

# print("1. Check balance \n2. Deposit \n3. Withdraw")
# choice = input("Enter a choice: ")

# match choice:
#     case "1":
#         print("Balance")
#     case "2":
#         print("Deposit")
#     case "3":
#         print("Withdraw")
#     case _:
#         print("Invalid")   

# problem 15

# password = input("Enter a password: ")

# if len(password) < 6:
#     print("weak")
# elif len(password) <10:
#     print("medium")
# else:
#     print("strong")                 