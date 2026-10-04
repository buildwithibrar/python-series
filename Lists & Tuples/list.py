# 1. Lists -- To make collection of different types of Data
# ------------------------------------------------------------

# Numbers List
number = [10, 20, 30]

# String List
fruits = ["apple", "orange", "pineapple", "banana"]

# Number and String List
mixed_List = ["apple", 3, "pineapple", 10, 7]


# 2. List Methods
# ------------------------------------------------------------


# Append Method
# Add language inside Programming Language list

# programming_Languages = ["python", "Html", "Java"]
# programming_Languages.append("Javascript")
# print(programming_Languages)


# Extend Method
#Add more than 1 values in the list

# fruit = ["banana"]
# fruit.extend(["apple", "peach"])
# print(fruit)


# We can also add another list

# vegetables = ["lettuce", "garlic"]
# vegetables2 = ["cucumber", "carrot", "potato"]

# vegetables.extend(vegetables2)
# print(vegetables)


# Insert Method
# Add an item at a specific Index

# car_Brands = ["Toyota", "BMW", "Ferrari", "Lamborghini"]
# car_Brands.insert(len(car_Brands), "Hundai")
# print(car_Brands)


# Remove Method
# Removes the first matching item

# furtniture = ["table", "chair", "showcase", "chair", "window", "dining table"]
# furtniture.remove("chair")
# print(furtniture)


# Pop Method
# Removes and returs an item

# electronics = ["tv", "laptop", "keyboard", "mouse", "speaker", "lcd"]
# print(electronics.pop(3))
# print(electronics)

# Clear Method
#Removes all items

# flowers = ["rose", "tulip", "sunflower", "daisy"]
# print(flowers)
# flowers.clear()
# print(flowers)


# Index Method
# Returns the index of an item

# planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
# print(planets.index("saturn"))
# print(planets)


# Count Method
# Counts how many times an item appears

# continents = ["asia", "africa", "north-america", "south-america", "antarctica", "europe", "australia", "south-america"]
# print(continents.count("south-america"))
# print(continents)


# Sort Method
# Sorts the list

# continents.sort()
# print(continents)


# Reverse Method
# Reverses the list

# continents.reverse()
# print(continents)


# Task 1
# Print "lion" using positive indexing.

animals = ["cat", "dog", "lion", "tiger"]
print(animals[2])


#Task 2
# Using the same list, print "tiger" using negative indexing

print(animals[-1])


# Task 3
# Change "dog" to "horse" using its index.

animals[1] = "horse"
print(animals)


# Task 4
# Change "cat" to "rabbit" using negative indexing.

animals[-4] = "rabbit"
print(animals)



# List Slicing
# List slicing allows us to get multiple items from a list.

fruits = ["apple", "banana", "orange", "mango", "grapes"]
print(fruits[1:4])

# You can leave start empty

fruits = ["apple", "banana", "orange", "mango", "grapes"]
print(fruits[:3])

# You can leave end empty
print(fruits[2:])

# Copying the whole list with slicing

print(fruits[:])

# Key Points
# list[start:end]
# list[:end]
# list[start:]
# list[:]


# List Slicing with Step

# list[start:end:step]
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[0:6:2])
# output: [10, 30, 50]



# List Operators

# + — Concatenation
first_List = [1, 2, 3]
second_List = [4, 5, 6]
combined_List = first_List + second_List

print(combined_List)
# [1, 2, 3, 4, 5, 6]


# * — Repetition
numbers = [1, 2, 3]

result = numbers * 3

print(result)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]


# in — Membership
fruits = ["apple", "banana", "mango"]
print("banana" in fruits)
# True

# not in
fruits = ["apple", "banana", "mango"]
print("orange" not in fruits)
# True



# Built-in Functions with Lists

# len()
fruits = ["apple", "banana", "mango", "orange"]
print(len(fruits))
# 4

# min()
numbers = [40, 10, 30, 20]
print(min(numbers))
# 10

# max()
numbers = [40, 10, 30, 20]
print(max(numbers))
# 40

# sum()
numbers = [10, 20, 30, 40]
print(sum(numbers))
# 100

# sorted()
numbers = [40, 10, 30, 20]

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
# [10, 20, 30, 40]
# [40, 10, 30, 20]


# List Unpacking

numbers = [10, 20, 30]

a, b, c = numbers
print(a)
print(b)
print(c)

# 10
# 20
# 30


# Nested Lists

numbers = [[1, 2], [3, 4], [5, 6]]
print(numbers)
# [[1, 2], [3, 4], [5, 6]]


# Accessing a Nested List
numbers = [[1, 2], [3, 4], [5, 6]]
print(numbers[0])
# [1, 2]


# Updating Nested List Items
numbers = [[1, 2], [3, 4], [5, 6]]
numbers[1][0] = 30
print(numbers)

# [[1, 2], [30, 4], [5, 6]]