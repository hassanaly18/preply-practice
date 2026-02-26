name = "John Abraham Doe"
country1 = "new zealand"
country2 = "CANADA"
data = "    hello   "
text = "I am working in java right now, java is easier than C"

print(len(country2))

#counting vowels in string
# vowels = text.lower().count("a") + text.lower().count("e") + text.lower().count("i") + text.lower().count("o") + text.lower().count("u")

# print("No. of vowels: ", vowels)

# email = input("Enter email: ")

# if "@" in email and ".com" in email:
#     print("Valid email")
# else:
#     print("Invalid email")    







fruits = "apples, strawberries, mango, guava"
fruits = fruits.split(",")  #breaking a string into a list

students = ["david", "logan", "john", "peter"]
students = " | ".join(students)
# print(students)

email = "logan@gmail.com"
# print(email.endswith(".com"))

url = "https://www.preply.com"
# print(url.startswith("https"))

a = "1223"
b = "nabsjdj"
c = "378ydyu3"

# print(a.isdigit())
# print(b.isalpha())
# print(c.isalnum())











# print(fruits[0])















# print(text.index("java"))    
# print(text.find("Python"))   #no error, -1 if not found












# print(text.count("a"))





# print(text.replace("java", "Python"))

# print("abc" + data.strip() +"123")
# print("abc" + data.lstrip() +"123")
# print("abc" + data.rstrip() +"123")

# print(country1[0:3])
# print(country1[4:])
# print(country1[:7], "\n", country1[0:3])

# print(country1[0::2])

# print(country1.upper() + "\n" + country2.lower() + "\n" + country1.title())















#string indexing
# print(name[0])
# print(name[3])
# print(name[6])

# #negative string indexing
# print(name[-1])
# print(name[-3])



























#task 1
# name = "    john doe   "
# name = name.strip().title()
# print(name)

#task 2
# email = "abc@GMAIL.Com"
# print(email.lower())

#task 3
# data = "Jacob,24,DC"
# data = data.replace(",", ";")
# print(data)

#task 4
# email = "logan@yahoo.com"
# # domain = email[email.index("@")+1 : ]
# # print(domain)

# #task 5
# username = email[0 : email.index("@")]
# print(username)

#task 6
# yyyy-mm-dd
# date = "2024-03-16"
# year = date[:4]
# month = date[5:7]
# print(year, month)

#task 7
# file = "myphoto.webp.png"
# extension = file.split(".")[-1]
# print(extension)

#task 8
# password = input("Enter password: ")

# if len(password) >=8 and password.isalpha():
#     print("Strong password")
# else:
#     print("Weak password")    



#task 9
# sentence = input("Enter sentence: ")
# words = sentence.split()
# print("No of words: ", len(words))

#task 10
# card = input("Enter card number: ")
# mask = "*" * (len(card)-4) + card[-4:]
# print(mask)














#task 1
# name = "   john doe   "
# print(name.strip().title())

#task 2
# email = "abc@GMAIL.Com"
# print(email.lower())

#task 3
# data = "John,22,Los Angeles"
# print(data.replace(",", ";"))

#task 4
# email = "david123@yahoo.com"
# print(email[email.index("@")+1 : ])

# #task 5
# print(email[0 : email.index("@")])

#task 6
# yyyy-mm-dd
# date = "2025-03-01"
# year = date[0:date.index("-")]
# print(year)

#task 7
# file = "myphoto1.org.jpeg"
# # print(file[file.index(".")+1 : ])
# extension = file.split(".")[-1]
# print(extension)

#task 8
# password = input("Enter a new password: ")

# if len(password) >= 8 and password.isalnum():
#     print("Strong password")
# else:
#     print("weak password")

#task 9
# sentence = input("Enter sentence: ")
# words = sentence.split()
# print("The number of words:",len(words))
























#task 1
# name = "    david miller   "

# name = name.strip().title()
# print(name)

#task 2
# email = "abc@GMAIL.Com"
# email = email.lower()
# print(email)

#task 3
# line = "John, 22, Multan"
# line = line.replace(",", ";")
# print(line)

#task 4
# email = "abc123@gmail.com"
# domain = email[email.index("@")+1 : ]
# print(domain)

#task 5
# email = "babar56@gmail.com"
# # username = email[: email.index("@")]
# # print(username)

# username = email.split("@")[0]
# print(username)

#task 6
# yyyy-mm-dd
# date = "2023-09-15"
# year = date[:4]
# print(year)

#task 7
# filename = "myphoto.png"
# # extension = filename[filename.index(".")+1:]
# extension = filename.split(".")[-1]
# print(extension)

#task 8
# card = input("Enter card number: ")
# mask = "*" * (len(card) - 4) + card[-4:]
# print(mask)










# name = "John Doe"
# country1 = "New Zealand"
# country2 = "CANADA"
# welcome = "welcome to python"
# hello = "    hello   "
# text = "I like java, java is easier than C"
# email = "abc@gmail.com"
# url = "https:\\www.google.com"

# print(email.endswith(".com"))
# print(url.startswith("https"))











# print(welcome.index("python"))
# print(text.index("easier"))
# print(text.find("Python"))














# print(country2.lower().count("a"))
# print(text.count("java"))











#replacing text in string
# print(text.replace("java", "Python"))










#remove spaces from string
# print("abc" + hello.strip() + "123")
# print("abc" + hello.lstrip() + "123")
# print("abc" + hello.rstrip() + "123")







# print(country1.upper())  #making string uppercase
# print(country2.lower())  #making string lowercase
# print(welcome.title())   #making the string a title

#string indexing
# print(name[0])
# print(name[5])
# print(name[-1])
# print(name[-3])

#slicing 

# print(country1[0:3])
# print(country1[4:])
# print(country1[:5])

# print(country1[0::2])











# name = "John Doe"
# country1 = "new zealand"
# country2 = "CANADA"
# welcome = "welcome to python"
# word = '    hello   '
# text = "I like java, java is easier than C"
# email = "abc@gmail.com"
# url = "https://www.google.com"

# print("1234".isdigit())
# print("abcdef".isalpha())

# print("abc123".isalnum())


# print(email.endswith(".com"))
# print(url.startswith("https"))
















# print(text.replace("java", "Python"))

# print(country1.count("e"))
# print(text.count("java"))

# print(text.index("easier"))
# print(text.find("python"))














# print("abc"+word.strip()+"123")
# print("abc"+word.lstrip()+"123")
# print("abc"+word.rstrip()+"123")




















# print(country1.upper())
# print(country2.lower())
# print(welcome.title())


















#slicing
# print(country1[0:3])
# print(country1[4:11])
# print(country1[5:8])
# print(country1[7:])
# print(country1[:8])
# print(country1[0:11:2])









#printing single alphabets of a string
# print(name[0])
# print(name[3])
# print(name[-1])
# print(name[-3])






























# country1 = "new zealand"
# country2 = "CANADA"
# sentence = "welcome to python"
# data = "    hello   "
# text = "I like to work in Java, Java is an old language"
# fruits = ["apple", "mango", "strawberries"]
# email = "abc@gmail.com"
# web = "https:\\www.google.com"

# print("123".isdigit())
# print("hello".isalpha())
# print("abc123".isalnum())




# print(web.startswith("https"))
# print(email.endswith(".com"))















# fruits1 = " | ".join(fruits)
# print(fruits1)





# list1 = fruits.split(",") 
# print(list1[0])









# print(text.index("work"))










# print(country2.lower().count("a"))










# print(text.replace("Java", "Python"))













#strip method in python
# print(data.strip())
# print(data.rstrip())
# print(data.lstrip())









# print(country1.upper())
# print(country2.lower())
# print(sentence.title())















# print(country[0:3])
# print(country[4:11])
# print(country[:5])
# print(country[4:])

# print(country[0:11:2])


# name = "David"

# print(name[0])
# # print(name[1])
# # print(name[2])
# # print(name[3])
# # print(name[4])
# print(name[-2])
