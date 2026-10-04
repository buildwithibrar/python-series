#  *********** PYTHON STRINGS — REPLACE AND SPLIT  ***********


# Task 1: Replace a Word
# ------------------------------------------------------------

sentence_1 = input("Enter a sentence:")

replace_Result = sentence_1.replace("friends", "fellows")
print(replace_Result)
print()


# Task 2: Replace every space with a hyphen
# ------------------------------------------------------------

sentence_2 = input("Enter a sentence:")
sentence_Hyphen = sentence_2.replace(" ", "-")

print(sentence_Hyphen)


# Task 3: Limited Replacement
#Replace only the first two occurences of "Python"
# ------------------------------------------------------------

sentence_3 = "Python Python Python Python"
result = sentence_3.replace("Python", "Javascript", 2)
print("Original:",sentence_3)
print("Updated:", result)


# Task 4: Split a Sentence
# ------------------------------------------------------------

sentence_4 = input("Enter a sentence: ")
words = sentence_4.split()

print("Original:", sentence_4)
print("Words:", words)


# Task 5: Split Comma-Separated Values
# ------------------------------------------------------------

languages = input("Enter Favourite Languages separated by comma: ")
comma_Separated = languages.split(",")

print("Languages:", comma_Separated)


# TASK 6: Split Using a Custom Separator
# ------------------------------------------------------------

hyphen_Text = "A-B-C-D-E"
hyphen_Separated = hyphen_Text.split("-")

print("Original:", hyphen_Text)
print("Updated:", hyphen_Separated)



# TASK 7: Sentence Information
# Find the total number of words, first word, and last word.
# ------------------------------------------------------------

sentence7 = input("Enter a sentence: ")

words = sentence7.split()

print("Original:", sentence7)
print("Total Words:", len(words))
print("First Word:", words[0])
print("Last Word:", words[-1])