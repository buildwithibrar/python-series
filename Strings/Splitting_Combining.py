sentence = "Python is easy to learn"

# Split the string at the first occurrence of "is"
result = sentence.partition("is")

print(result)


sentence2 = "Python-is easy to learn-programming"

# Split the string at the last occurence of "-"
result2 = sentence2.rpartition("-")

print(result2)


# join() combines multiple strings into ONE string.
#--------------------------------------------------

words = ["Python", "is", "easy"]

result3 = "-".join(words)

print(result3)

