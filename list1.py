#list/array

students =[]
marks = []

while True:
    choice = int(input("\nWhat do you want to do? \n1. Add new student \n2. Delete student \n3. Show all Students \n4. Exit \nEnter your choice: "))

    match choice:
        case 1:
            name = input("\nEnter name of student: ")
            m = int(input("Enter marks: "))
            students.append(name)
            marks.append(m)
            print("Student Added..")
        case 2:
            delete = input("\nWhich student you wanna delete? ")
            index = students.index(delete)
            students.remove(delete)
            marks.pop(index)
            print("Student deleted..")
        case 3:
            print("\n")
            for i in range(len(students)):
                print("\nName of student:", students[i])
                print("Marks of student:", marks[i])
        case 4:
            print("\n\nThanks for using our program..!\n\n")
            break         
        case _:
            print("Wrong choice")

# for i in range(num):
#     name = input("Enter name of student: ")
#     students.append(name)

# print("\n")    
    
# for name in students:
#     print("The name of student:", name)

















# marks = [12,45,21,83,53,99,33]

# # marks.sort()
# # marks.reverse()
# print(marks)





# marks.remove(99)  #deleting an element by value
# marks.pop()       #delete the last element
# marks.pop(2)      #dleete from specific index number
# marks.clear()     #empty the list
# print(marks)


# marks.insert(2, 75)
# print(marks)