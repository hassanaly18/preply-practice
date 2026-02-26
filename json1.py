import json
#json = javascript object notation

# with open("student.json", "r") as f

with open("school.json", "r") as file:
    data = json.load(file)
    
# print(data)

for student in data["students"]:
    print("Name:", student["name"])    


# with open("student.json", "r") as file:
#     data = json.load(file)
    
# print(data)    
# print(data["name"])    



# with open("student.json", "w") as file:
#     json.dump(student, file, indent=4)