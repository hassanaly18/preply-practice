import csv


total =0

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total = total + int(row["price"])

print("Total sales:", total)




















# with open("data2.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print("Name:", row["name"], "  |  Age:",  row["age"])














# #update data in a csv file
# with open("data2.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Jacob", 33, "Manchester"])









#write data in a csv file
# with open("data2.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "age", "city"])
#     writer.writerow(["Alex", 14, "LA"])
#     writer.writerow(["David", 16, "Washington"])
#     writer.writerow(["Paul", 19, "Liverpool"])
#     writer.writerow(["Alex", 14, "LA"])



#reading data from a csv file
# with open("data2.csv", "r") as file:
#     content = csv.reader(file)
#     for row in content:
#         print(row)