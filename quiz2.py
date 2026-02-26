questions = ["Witch book did you refer to when you asked me wht the tallest tree in the world was?","what happend in the big bang?","What are Elliptical galaxies shaped like?"]
options = [["My childrens encyclopedia","Warriors","Kay's anatomy","Ratburger"],["an expansion","pp","an explosion","Zeus was born"],["Pluma","Balls","Eggs","Your head"]]
answers =[1,1,3]


def show_questions(questions, options):
    print("\n" + questions)
    for i in range(len(options)):
        print(i+1 ,".",options[i])
        
def check(choice,answer):
    if choice == answer:
        print("Correct..!")
        return 10
    else:
        print("Wrong..!")
        return -5
        
        
def play(questions,options,answers):
    score = 0
    
    print("Welcome to the quiz..!")
    for i in range(len(questions)):
        show_questions(questions[i],options[i])
        choice= int(input("Enter your choice(1/2/3/4):"))
        
        score = score + check(choice, answers[i])
        print("Current Score:",score)
    return score   

while True:
    final = play(questions,options,answers)
    print("\nQuiz is Over..\nFinal Score:", final)
    
    play_again = input("\nDo you want to attempt the quis]z again?(yes/no): ").lower()
    
    if play_again != "yes":
        print("Thanks for taking the quiz..!")
        break