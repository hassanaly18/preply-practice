#tuples
colors = ("red", "blue", "green")
nums = (1,2,3,4,5,2,5,1,6,9,2,2,2)


print(nums.count(2))   #counting the number of times a number is present in a tuple
print(nums.index(6))   #finding the index number of a number
print(nums.index(2))
print(len(nums))       #giving the length of a tuple














#dictionary/object
#key : value

# student1 = {
#     "name": "David",
#     "age": 17,
#     "marks": 85
# }
# student2 = {
#     "name": "Mary",
#     "age": 16,
#     "marks": 89
# }

# car1 = {
#     "brand": "Nissan",
#     "model": "GTR R35",
#     "year": 2024,
#     "color": "Black"
# }

# car2 = car1.copy()             #making copy of an object
# car2.update({"color": "Orange"})

# print(car1)
# print(car2)

# print(car.keys())
# print(car.values())
# print(car.items())

# car.update({"color":"White"})   #update value
# print(car["color"])


# for key in car:
#     print(key, ":", car[key])

# for key in car:
#     print(key)

# print("\n")

# for value in car.values():
#     print(value)

# car.popitem()    #delete the last key of an object
# print(car)



# print(student2)
# student2.clear()   #deletes everything from the object
# print(student2)

# del student1["age"] #deleting specific key from object
# print(student1)


# print(student2)
# student2["color"] = "Blue"  #adding a new key
# print(student2)




# print(student2["marks"])

# student2["marks"] = 95  #updating marks

# print(student2["marks"])


# print(student1)
# print("The student's name is", student1["name"], "and his age is", student1["age"],"and his marks are", student1["marks"])

# print(student2.get("color"))
