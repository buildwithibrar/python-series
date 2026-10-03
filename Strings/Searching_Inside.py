user = input("Enter a sentence: ")
search_Word = input("Enter a word to search for: ")

check_Word = search_Word in user
print("Word Exists:", check_Word)

check_Not = search_Word not in user
print("Not Exists:", check_Not)