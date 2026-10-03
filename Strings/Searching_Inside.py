user = input("Enter a sentence: ")                         #Get Sentence from User
search_Word = input("Enter a word to search for: ")        #Get word from User

check_Word = search_Word in user                           #Checking If word inside the sentence.
print("Word Exists:", check_Word)

check_Not = search_Word not in user                        #Checking If word is not inside the sentence.
print("Not Exists:", check_Not)