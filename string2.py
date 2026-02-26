#key-value pairs

user = {
    "username": "mike12",
    "password": "abc123"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username == user["username"] and password == user["password"]:
    print("You are logged in")
else: 
    print("Wrong info")




item = {
    "name": "Bread",
    "price": 30,
    "quantity": 4
}

# total = item["price"] * item["quantity"]
# print("Total:", total)

# The total bill of 4 Bread is 120












student1 = {
    "name": "Mike",
    "marks": 99,
    "age": 12
}
# student1.clear()
# print(student1.keys())
# print(student1.values())
# print(student1.items())
# for key, value in student1.items():
#     print(key, ":", value)

# for key in student1:
#     print(key)

# for value in student1.values():
#     print(value)

student2 = {
    "name": "Ali",
    "marks": 94,
    "age": 13
}



# student1.popitem()
# student1.popitem()
# print(student1)
# del student2["age"]
# student2.pop("age")
# student1["grade"] = "A"
# student2["marks"] = 97  #update value in dictionary
# print(student2)
# print(student1)














# sentence = input("Enter sentence: ")

# sentence= sentence.split()
# print("Number of words:", len(sentence))











# email = "abc@gmail.com"

# if "@" in email and email.endswith(".com"):
#     print("Valid email address")
# else:
#     print("Invalid")





# name = "Hassan"
# age = 22


# print(f"My name is {name} and my age is {age}") #fstring

# print("My name is {} and my age is {}".format("Hassan", 22))

# for letter in name:
#     print(letter)









# text = "Paris, Rome, Milan, Madrid, Miami"
# text1 = text.split(",")
# print(text)
# print(text1)

# text2 = ["Python", "is", "a", "computer", "language"]
# text3 = " ".join(text2)
# print(text2)
# print(text3)












# a = "Hello"
# b= "1234"
# c= "abc123"

# print(a.isalpha())
# print(b.isdigit())
# print(a.isalnum())


# email = "abc@gmail.com"
# domain = "http:\\www.google.com"

# print(email.endswith("gmail.com"))
# print(domain.startswith("https"))

# if domain.startswith("https"):
#     print("The site is secure")
# else:
#     print("No SSL certificate found")








# text = "I like working in Java, right now Java is very famous"
# # updated = text.replace("Java", "Python")
# print(text.count("a"))

# text2 = "Hello John"
# print(text2.find("World"))



# word = "Python"
# print(word[4])

# text = "Python programming"
# print(text[7:])

# country1 = "NEW ZEAland"
# print(country1.lower())
# print(country1.upper())
# print(country1.title())

# sentence = "  Python  "
# print("left" + sentence.rstrip() + "right")