# user = input("Enter a sentence: ")                         #Get Sentence from User
# search_Word = input("Enter a word to search for: ")        #Get word from User

# check_Word = search_Word in user                           #Checking If word inside the sentence.
# print("Word Exists:", check_Word)

# check_Not = search_Word not in user                        #Checking If word is not inside the sentence.
# print("Not Exists:", check_Not)

# PYTHON STRINGS — find() METHOD

# 1. BASIC find() -- Return the index of the value
# ------------------------------------------------------------

text1 = "I love Python"
position = text1.find("Python")
print("Position:", position)


# 2. To rFind() -- Return the Index of last Occurence.

text2 = "I love Python. Python is a great Programming Language."
postition2 = text2.rfind("Python")
print("Last Occurence:", postition2)
print(postition2.index("Python"))
