# Python Loops
# Loops are one of the most important Python topics because they allow you to repeat code automatically.

# ------------------------------------------------------------------------------------------------------

# for variable in sequence:
#     # code

animals = ["cat", "dog", "lion"]

for animal in animals:
    print(animal)

print()

# The Loop Variable
fruits = ["orange", "mango", "banana", "peach", "strawberry"]

for fruit in fruits:
    print(fruit)

# Looping Through a String
name = "Bilal"

for letter in name:
    print(letter)


# Looping Through a Tuple
friends = ("ibrar", "ahmed", "bilal", "ali", "hamid")

for friend in friends:
    print(friend)

# Looping Through a Set
number = {12, 20, 30, 22, 40, 50}

for i in number:
    print(i)


# Looping Through a Dictionary
person = {
    "name": "Bilal",
    "age": 24
}

for key in person:
    print(key)


# range() in Python
# Using range()

numbers = [10, 15, 20, 25, 30]

for i in range(4):
    print(numbers[i])


# Using range(len())
for i in range(len(numbers)):
    if i < 3:
        print(numbers[i])

# Using enumerate()
for i, value in enumerate(numbers):
    if i == 3:
        break
    print(value)

# Using slicing + loop
flowers = ["Rose", "Sunflower", "NightQueen", "Tulip"]
for i in flowers[1:3]:
    print(i)

# Using a counter
count = 0

for value in numbers:
    if count == 3:
        break

    print(value)
    count += 1

# Using enumerate() with slicing
for i, value in enumerate(numbers[:3]):
    print(value)

print()

# for loop + conditions
my_Numbers = [13, 44, 26, 5, 34, 53, 22]

for my_number in my_Numbers:
    if my_number > 20:
        print(my_number)



# Task 1 — Number Classifier
#---------------------------------------------------------------------------


# Loop through the list and classify every number:
# - 0 → "Zero"
# - Negative → "Negative"
# - Positive and less than 10 → "Small Positive"
# - Positive from 10 to 50 → "Medium Positive"
# - Positive greater than 50 → "Large Positive"

new_Numbers = [0, -5, 12, 17, -20, 33, 100, -1, 50]

for number in new_Numbers:
    if number == 0:
        print("Zero")
    elif number < 0:
        print("Negative")
    elif number <= 10:
        print("Small Positive")
    elif number <= 50:
        print("Medium Positive")
    else:
        print("Large Positive Numbers")


# Task 2 — Student Grade Analyzer
#---------------------------------------------------------------------------
marks = [95, 82, 76, 64, 58, 49, 35, 20, 100]

marks = [95, 82, 76, 64, 58, 49, 35, 20, 100]

for mark in marks:
    if mark >= 90 and mark <= 100:
        print("A+")
    elif mark >= 80:
        print("A")
    elif mark >= 70:
        print("B")
    elif mark >= 60:
        print("C")
    elif mark >= 50:
        print("D")
    else:
        print("Fail")


# break

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        break

    print(number)


# continue
for number in numbers:
    if number == 30:
        continue

    print(number)


# pass
for number in numbers:
    if number == 30:
        pass

    print(number)


# Nested for loops
for i in range(3):
    for j in range(3):
        print(i, j)


# Loop + counters
count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print(count)


# Loop + accumulator
total = 0

for number in numbers:
    total += number

print(total)


# for loop with else
for number in numbers:
    print(number)
else:
    print("Loop finished")


# while loop
#---------------------------------------------------------------------------

# while condition:
#     code

count = 1

while count <= 5:
    print(count)
    count += 1


# Task 1 — Reverse Countdown
number = 20

while number >= 1:
    print(number)
    number -= 1
print("Blast Off!")


# Task 2 — Sum Until 100

number = 1
sum = 0

while number <= 100:
    print(f"Adding: {number}")
    sum += number
    number += 1
print(f"Total Sum: {sum}")
