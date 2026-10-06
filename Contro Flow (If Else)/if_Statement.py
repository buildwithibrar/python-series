""""

# if Statement
# ------------------------------------------------------------

# if condition:
    # code to execute

# Normal if

age = 20

if age >= 18:
    print("Adult")

# if Else
if age >= 18:
    print("Adult Again")
else:
    print("Minor")


# Ternary if
# ------------------------------------------------------------

new_Age = 16

status = "Adult" if new_Age >= 18 else "Minor"
print(status)


# match / case
# ------------------------------------------------------------

status = "ibrar"

match status:

    case "Adult":
        print("You are Adult")

    case "Minor":
        print("You are Minor") 

    case _:
        print("Not Available ")


# Boolean Values
# ------------------------------------------------------------

is_student = True
is_employed = False

print(is_student)
print(is_employed)

# Print the type of both variables.

print(type(is_student))
print(type(is_employed))


# Task 1 — Adult Check
user_Age = 24

if user_Age >= 18:
    print("Adult")
else:
    print("Minor")

# Task 2 — Positive Number
if user_Age > 0:
    print(user_Age, ": Positive Number")
elif user_Age < 0:
    print(user_Age, ": Negative Number")
else:
    print(user_Age, ": Zero")

# Task 3 — Even Number
if user_Age % 2 == 0:
    print(user_Age,": Even Number")
else:
    print(user_Age,": Not Even Number")

# Task 3 — Password
password = "python123"

if password == "python123":
    print("Access Granted")
else:
    print("Access not Granted")

# Task 4 — Divisible by 5
number = int(input("Enter your Number: "))

if number % 5 == 0:
    print("Divisible")
else:
    print("Not Divisible")

# Task 5 — Number Range
number = 75
user_Number = int(input("Enter your Number:"))

if user_Number >= 50 and user_Number <= 100:
    print("In Range")
else:
    print("Not in Range")

# Task 6 — Login Check
username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login Successful!")
else:
    print("Worng Input!")



# Control Flow — Next: elif
# Check Temperature
# ------------------------------------------------------------


temperature = int(input("Enter your Temperature: "))

if temperature >= 40:
    print(f"{temperature}: Very Hot")
elif temperature >= 30:
    print(f"{temperature}: Hot")
elif temperature >= 25:
    print(f"{temperature}: Normal")
elif temperature >= 15:
    print(f"{temperature}: Cold")
elif temperature >= 1:
    print(f"{temperature}: Very Cold")
elif temperature <= 0:
    print(f"{temperature}: Freezing Temperature")
else:
    print("Enter a Correct Temperature Number.")

# Login System
# ------------------------------------------------------------

username = "admin123"
password = "12345%"

enter_Username = input("Enter Your Username: ")
enter_Password = input("Enter Your Password: ")

if username == enter_Username and password == enter_Password:
    print("Login Successful")

elif username == enter_Username and password != enter_Password:
    print("Incorrect Password")

elif password == enter_Password and username != enter_Username:
    print("Incorrect Username")

else :
    print("Both are Incorrect!")



# Simple Calculator
# ------------------------------------------------------------

operand1 = int(input("Enter a Number: "))
operand2 = int(input("Enter another Number: "))

operator = input("Enter Operator: ")

if operator == "+":
    print(f"{operand1} {operator} {operand2} = {operand1 + operand2} ")

elif operator == "-":
    print((f"{operand1} {operator} {operand2} = {(operand1 - operand2)}"))
    
elif operator == "*":
    print(f"{operand1} {operator} {operand2} = {operand1 * operand2}")
    
elif operator == "/":
    print(f"{operand1} {operator} {operand2} = {operand1 / operand2}")

elif operator not in ["+", "-", "*", "/"]:
    print("Enter Correct Operator")
"""

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------



# Critical Combining-Conditions Tasks
# ------------------------------------------------------------

# Print "Allowed" only when:
# - age is 18 or older
# - AND the person has a ticket

age = 25
has_ticket = True
if age > 18 and has_ticket:
    print("Allowed")


# Print "Weekend" when the day is:
# - "Saturday"
# - OR "Sunday"
# Otherwise print "Weekday".

day = input("Enter Day: ")

if day == "sunday" or day == "saturday":
    print("Weekend")
else:
    print("Weekday")


# Print "Access granted" when:
# - age is 18 or older
# - AND has an ID
# - AND is not banned
# Otherwise print "Access denied".

age = int(input("Enter Age: "))
id = True
is_banned = False

if age >= 18 and id and not is_banned:
    print("Access Granted")
else:
    print("Access Denied")
