# Task 1 — Name Validator
# Check whether the name contains only alphabetic characters.
#------------------------------------------------------------

user1 = input("Enter your name: ")
remove_Spaces = user1.replace(" ", "")

print(remove_Spaces.isalpha())


# Task 2 — Age Validator
#Check whether the input contains only digits
#------------------------------------------------------------

user2 = input("Enter your age: ")
print(user2.isdigit())


# Task 3 — Username Validator
#Check whether the username contains only letters and numbers
#------------------------------------------------------------

user3 = input("Enter your username: ")
print(user3.isalnum())


# Task 4 — Type Cases
#Check the Text All Cases
#------------------------------------------------------------


user4 = input("Enter your sentence: ")
print("IsLowerCase:", user4.islower())
print("IsUpperCase:", user4.isupper())
print("IsTitleCase:", user4.istitle())


# Task 5 — Numeric Validation

# isdecimal() -> Only decimal digits
# isdigit()   -> Decimal digits + some digit characters
# isnumeric() -> Digits + digit characters + other numeric characters