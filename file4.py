import csv

people= int(input("How many people would you like to add?: "))

for i in range(people):
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    city=input("Enter your ciy: ")

    with open("data4.csv", "a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([name,age,city])

























# with open("data4.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Hassan", 22, "Wellington"])


















#writing data in a csv file
# with open("data4.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["name", "age", "city"])
#     writer.writerow(["John", 25, "Lahore"])
#     writer.writerow(["David", 23, "LA"])
#     writer.writerow(["Jacob", 24, "DC"])
















#reading data from a csv file
# with open("data4.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)