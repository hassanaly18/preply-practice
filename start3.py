#dictionary/object
#key-value pairs
student1 = {
    "name": "Mike",
    "age": 15,
    "marks": 95
}
student2 = student1.copy()
student2["name"] = "John"

print(student1)
print(student2)


# for key in student1:
#     print(key)

# for value in student1.values():
#     print(value)

# for key in student1:
#     print(key, ":", student1[key])

# for item in student1.items():
#     print(item)


#del student2["age"]
#student2.pop("name")

# print(student1)
# print(student2)