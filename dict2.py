#question 3

sentence = input("Enter a sentence: ")
freq = {}

words = sentence.split()
print(words)

for word in words:
    if word in freq:
        freq[word] = freq[word] +1
    else:
        freq[word] = 1

print(freq)

#question 2
# inventory = {
# "apple": 10,
# "banana": 5,
# "milk": 8
# }

# item = input("Enter name of item: ")
# qty = int(input("Enter quantity of item: "))

# inventory[item] = qty    #adding new itemin dictionary
# inventory["apple"] = 12  #updating quantity of existing item
# del inventory['milk']    #delete milk

# print("\nName | Quantity")
# for key in inventory:
#     print(key, ":", inventory[key])

#question 1
# student = {
#     "name": "John Doe",
#     "marks": [85, 89, 92]
# }

# total =0

# print("Name:",student["name"])
# for mark in student['marks']:
#     print("Marks:", mark)
#     total = total+mark

# print("\nTotal Marks:", total)

# avg = total/3

# if avg>80:
#     print("Grade A")
# elif avg >50:
#     print("Grade B")
# else:
#     print("Fail")