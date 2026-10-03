user = input("Enter a sentence: ")  #Ask User to Enter a Sentence.
print(user)

total = len(user)                   #Total number of characters
print(total)

first_Character = user[0]           #First character
print(first_Character)

last_Character = user[-1]           #Last character
print(last_Character)

first_Five = user[0:5]              #First 5 characters
print(first_Five)

last_Five = user[-5:]               #Last 5 characters
print(last_Five)

reversed_text = user[::-1]          #The sentence reversed
print(reversed_text)