#question 8
sentence = input("ENter sentence: ")

print("The first occurence of python:", sentence.find("python"))

sentence = sentence.replace("python", "Java")
sentence = sentence.title()
print(sentence)











#question 6

# sentence = input("ENter sentence: ")
# words = sentence.split()

# print(words)
# print("The number of words: ",len(words))

# sentence = ("-").join(words)
# print(sentence)








#question 5

# email = input("Enter an email: ")
# email = email.strip()
# email = email.lower()

# print(email)

# if email.find("@") != -1 and email.endswith(".com"):
#     print("Valid email")
# else:
#     print("Invalid email")




#question 4
# sentence = input("Entar a sentence: ")

# sentence = sentence.replace(" ", "_")
# sentence = sentence.upper()
# print(sentence)

# print(sentence.endswith("!"))











#question 3
# word = input("Enter a word: ")

# if word.startswith(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')):
#     print("Starts with vowel")
# else:
#     print("doesnt start with vowel")
    
# word = word.upper()
# print(word)
# print("Letters in word: ",len(word))









# #question 2
# name = input("Enter name: ")

# name = name.strip()
# name = name.title()

# print(name)
# print(name.isalpha())









#question 1
# sentence = input("Enter a sentence: ")
# sentence = sentence.lower() 
# sentence = sentence.strip()  #removing spaces
# num = sentence.count('a')  #count any word/letter

# print(sentence)
# print("The number of 'a's in the sentence:", num)