student1 = {
    "name": "Abraham", 
    "age": 19
}
#deep and shallow copy
student2 =student1.copy()
student2["name"] = "John"

print(student1)
print(student2)

with open("object.txt", "w") as file:
    file.write("Name: "+ student1["name"] +"\nAge: "+ str(student1["age"]))












# #dictionary
# #key value

# students = [{"name": "Mike","marks": 99,"age": 17},
#             {"name": "John","marks": 85,"age": 16},
#             {"name": "Emma","marks": 77,"age": 20}]
# student = {
#     "name": "Donald",
#     "marks": 95.5,
#     "age": 15,
#     "enrolled": True,
#     "subjects": ["english", "maths", "chem"],
#     "record": {
#         "averageGrade": "B",
#         "Failed": False
#     }
# }
# students.append(student)
# print(students[3]["record"]["Failed"])
