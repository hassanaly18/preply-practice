def sumOfList(a):
    total = 0
    for i in a:
        total = total + i
    return total        


def countVowels(word):
    count =0
    
    for letter in word:
        if letter.lower()=="a" or letter.lower()=="e" or letter.lower()=="i" or letter.lower()=="o" or letter.lower()=="u":
            count = count+1
    
    return count

sentence = input("Enter your sentence: ")

print("Num of vowels in the word:",countVowels(sentence))







def findMax(a,b):
    if a>b:
        return a
    return b

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print("The larger number is:",findMax(num1, num2))























# def calories_burned(minutes, calories_per_minute):
#     return minutes*calories_per_minute

# time = int(input("Enter duration of exercise: "))
# cal = int(input("Enter calories burned per minute: "))

# c_burned = calories_burned(time, cal)

# print("You burned",c_burned ,"calories today!")





















def add1(a,b): #void/none
    print(a+b)

def add2(a,b):
    return a+b















def greet(name, age):
    print("welcome to the program,", name, ", and your age is:", age)
    
def largest(a,b,c):
    if a>b and a>c:
        print(a,"is teh largest")
    elif b>a and b>c:
        print(b,"is the largest")
    else:
        print(c, "is the largest")    
        
def add(a,b):
    print(a+b)

