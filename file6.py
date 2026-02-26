import csv

with open("data6.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Available books: ")

    for row in reader:
        if row["issued"] == "no":
            print(row["book"])
      














# total = 0

# with open("data6.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         row_total = float(row["price"]) * int(row["qty"])
#         total = total + row_total
#         print("The total for", row["item"] + ":", row_total)

# print("Your total bill:", total)















# total = 0
# count = 0

# with open("data6.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         total = total + int(row["age"])
#         count = count+1

# average = total/count
# print("Average age: ", average, "years")        

















# search = input("Enter name to search: ")
# found = False

# with open("data6.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         if row["name"] == search:
#             print("Record found: ", row["name"], row["age"], row["grade"])
#             found = True
#             break

# if found == False:
#     print("Student not found")
















# name = input("Enter student's name:")
# age = input("Enter student's age:")
# grade = input("Enter student's grade:")

# with open('data6.csv', "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, age, grade])










# total = 0

# with open("data6.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print("Item name:", row["item"], ", Item Price:", row["price"])
#         total = total + int(row["price"])

# print("The total bill is:", total)














# with open("data6.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Ali", 27, "DC"])















# with open("data6.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print("Name:", row["name"], "Age:", row["age"])



#reading data from a csv file
# with open("data6.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)