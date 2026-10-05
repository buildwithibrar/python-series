# A tuple is a collection used to store multiple values in a single variable.
# Lists are mutable. Tuples are immutable.

#---------------------------------------------------------------------------

animals = ("cat", "dog", "lion", "tiger")
# You can also create one without parentheses
print(animals)
# Output: ('cat', 'dog', 'lion', 'tiger')


# Tuple With Different Data Types
#---------------------------------------------------------------------------

person = ("Bilal", 23, 5.8, True)
print(person)
# Output: ('Bilal', 23, 5.8, True)


# To create a tuple with one item, you need a comma:
#---------------------------------------------------------------------------

number = (10,)
print(type(number))
# Output: <class 'tuple'>


# Task 1
# Create a tuple containing:
# "apple", "banana", "orange", "mango"
fruits = "apple", "banana", "orange", "mango"

# Task 2
# Print the tuple.
print(fruits)


# Task 3
# Create a tuple containing:
# your name, your age, and your favorite food.
my_Details = "Buildwithibrar", "24", "apple"


# Task 4
# Print the type of your tuple.
print(type(my_Details))


# Task 5
# Create a single-item tuple containing the number 100.
number = (100),
print(number)


# Task 6
# Create a tuple containing different data types:
# string, integer, float, boolean
datatypes = ("Ibrar", 24, 25.5, True)


# Task 7
# Create a tuple without using parentheses.
# Example:
# "Python", "JavaScript", "C++"
datatypes = "ibrar", 24, 25.5, True
print(type(datatypes))


# Task 8
# Create an empty tuple.
# Print the type of the Tuple.
empty_Tuple = ()
print(type(empty_Tuple))


# Task 9
# Create a tuple containing 5 programming languages.
languages = ("Python", "Java", "Javascript", "Rust", "Ruby")


# Task 10
# Create a single-item tuple containing 50.
# Verify its type.

number = (50,)
print(type(number))


# Tuple Indexing & Slicing
#---------------------------------------------------------------------------

colors = ("red", "green", "blue", "yellow", "black", "white")

# Task 11
# Access the third item.
print(colors[2])

# Task 12
# Access the second-last item.
print(colors[-2])

# Task 13
# Extract:
# ("green", "blue", "yellow")
new_Colors = colors[1:4]
print(new_Colors)

# Task 14
# Extract the last three items using slicing.
last3_Items = colors[-3:]
print(last3_Items)

# Task 15
# Reverse the entire tuple using slicing.
print(colors[::-1])


numbers = (10, 20, 30, 40, 10, 50, 30)
# Task 16
# Count how many times 10 appears.
print(numbers.count(10))

# Task 17
# Find the index of 30.
print(numbers.index(30))

# Task 18
# Find the index of the first occurrence of 10.
first_Index = numbers.index(10)
print(first_Index)

# Task 19
# Find the index of the second occurrence of 10.
second_Index = numbers.index(10, first_Index + 1)
print(second_Index)


# Task 20
# Determine whether a value exists in the tuple
# before using index().
if 30 in numbers:
    print(True)
    print(numbers.index(30))


# Tuple Operators
#---------------------------------------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Task 21
# Combine tuple1 and tuple2.

total_Tuple = tuple1 + tuple2
print(total_Tuple)


# Task 22
# Repeat tuple1 three times.
tuple3x = tuple1 * 3
print(tuple3x)

# Task 23
# Check whether 5 exists in tuple2.
if 5 in tuple2:
    print(True)

# Task 24
# Check whether 10 does NOT exist in tuple2.
if 10 not in tuple2:
    print("Correct, it's not in Tuple 2")


# Tuple Unpacking
#---------------------------------------------------------------------------

person = ("Bilal", 24, "Pakistan")
# Task 25
# Unpack the tuple into:
# name, age, country

Name, Age, Country = person
print("Name:",Name)
print("Age:",Age)
print("Country:",Country)


# Extended unpacking
#---------------------------------------------------------------------------

new_Numbers = (10, 20, 30, 40, 50)

# Task 26
# Unpack the first number into first,
# the last number into last,
# and all middle numbers into middle.

first, *middle, last = new_Numbers
middle = tuple(middle)

print(first)
print(middle)
print(last)



# Tuple ↔ List
#---------------------------------------------------------------------------

numbers = (10, 20, 30, 40)

# Task 27
# Convert the tuple into a list.
convert_List = list(numbers)
print(type(convert_List))
print(convert_List)

# Task 28
# Add 50 to the converted list.
convert_List.append(50)
print(convert_List)

# Task 29
# Convert the list back into a tuple.
again_Tuple = tuple(convert_List)
print(again_Tuple)
print(type(again_Tuple))


# Built-in Functions With Tuples
#---------------------------------------------------------------------------

numbers = (50, 10, 30, 20, 40)

# Task 30
# Find the length.

print("Length:", len(numbers))

# Task 31
# Find the Minimum value.
print("Smallest Value:", min(numbers))

# Task 32
# Find the Maximum value.
print("Largest Value:", max(numbers))

# Task 33
# Calculate the total.
print("Total:", sum(numbers))

# Task 34
# Sort the tuple using sorted().
print("Sorted:", sorted(numbers))


# Nested Tuples
#---------------------------------------------------------------------------

students = (
    ("Bilal", 85),
    ("Ali", 90),
    ("Ahmed", 78)
)

# Task 35
# Access the complete first student's tuple.

first_Student = students[0]
print(first_Student)

# Task 36
# Access Bilal's marks.
first_Student = students[0][1]
print(first_Student)

# Task 37
# Access Ahmed's name.
print(students[2][0])

# Task 38
# Access Ali's marks.
print(students[1][1])

# Task 39
# Use nested tuple unpacking to extract:
# name and marks for the first student.

first_Name, first_Marks = students[0]
print(first_Name)
print(first_Marks)


# Tuple Packing & Unpacking
#---------------------------------------------------------------------------

# Task 40
# Create three variables:
name = "Bilal"
age = 24
country = "Pakistan"

# Pack them into one tuple.
main_Tuple = ()
main_Tuple = name, age, country
print(main_Tuple)

# Task 41
# Unpack that tuple back into three variables.
new_Name, new_Age, new_Country = main_Tuple
print(new_Name)
print(new_Age)
print(new_Country)


# Task 42
# Swap these two variables using tuple unpacking.

a = 10
b = 20

new_Tuple = ()
new_Tuple = a, b
a = new_Tuple[1]
b = new_Tuple[0]
print("a:",a)
print("b:",b)