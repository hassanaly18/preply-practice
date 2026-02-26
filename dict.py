# contacts = {}

# for i in range(3):
#     name = input("Enter name: ")
#     phone = input("Enter phone number: ")
#     contacts[name] = phone

# print(contacts)


student1 = {
    "name": "Mike",
    "age": 12,
    "course": "CS",
    "marks": [67,98,78,82]
}

for key in student1:
    print(key)
    
for value in student1.values():
    print(value)
    

# # print(student1.get("name"))

# # del student1["height"]

# student1.pop("height", "Key not found") #safer approach for deleting a key-value pair

# print(student1)
