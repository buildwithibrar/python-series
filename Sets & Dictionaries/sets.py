# ------------------------------------------------------------

# Create a set called fruits containing:
fruits = {"apple", "banana", "orange", "mango"}

# Duplicate Values
# ------------------------------------------------------------
numbers = {10, 20, 10, 30, 20, 40}
print(numbers)

# Check the Type
print(type(fruits))

# Empty Set
empty_Set = set()
print(type(empty_Set))

# Convert List → Set
number_List = [10, 20, 20, 30, 30, 40, 40, 50]
print(type(number_List))

into_Set = set(number_List)
print(type(into_Set))

# Add an Item
# ------------------------------------------------------------
new_Fruits = {"apple", "orange"}
print("Original:", new_Fruits)

new_Fruits.add("pineapple")
print("Add 1 Item: ", new_Fruits)

new_Fruits.update(["grape", "peach"])
print("Add More Items: ", new_Fruits)

# Remove an Item
# ------------------------------------------------------------
new_Fruits.remove("pineapple")
print("Remove Item:",new_Fruits)

# new_Fruits.remove("Horse")
# Gives Error
# new_Fruits.discard("Horse")
# Not Gives Error 
# We use discard method so program cannot gives error and crashed.


# Set Membership
# ------------------------------------------------------------

languages = {"Python", "JavaScript", "Java", "C++", "PHP"}

# Check whether "PHP" exists in the set.
if "PHP" not in languages:
    print("PHP is not available in the Set.")



# Set Operations
# ------------------------------------------------------------

set_A = {"apple", "banana", "orange"}
set_B = {"orange", "mango", "grape"}

# Union combines all unique items from both sets.
result = set_A | set_B
print(result)

# Intersection finds items that exist in BOTH sets.
result = set_A & set_B
print(result)

# Difference finds items that exist in the first set but NOT in the second set.
result = set_A - set_B
print(result)

# Symmetric difference finds items that are NOT shared between the two sets.
set_A = {"apple", "banana", "orange"}
set_B = {"orange", "mango", "banana"}

result = set_A ^ set_B
print(result)


# Set Comparisons
# ------------------------------------------------------------

# Checks whether all items of Set A exist inside Set B.
set_A = {"apple", "banana"}
set_B = {"apple", "banana", "orange", "mango"}
print(set_A.issubset(set_B))


# Checks whether Set A contains all items of Set B.
set_A = {"apple", "banana", "orange", "mango"}
set_B = {"apple", "banana"}
print(set_A.issuperset(set_B))


# Checks whether two sets have NO common items.
set_A = {"apple", "banana"}
set_B = {"orange", "mango"}
print(set_A.isdisjoint(set_B))


# Practice Tasks
# ------------------------------------------------------------

# Task 1 — issubset()
python_students = {"Ali", "Ahmed", "Bilal"}
all_students = {"Ali", "Ahmed", "Bilal", "Usman", "Hamza"}

print("Yes, it's a Sub-Set:", python_students.issubset(all_students))
print("Yes:", python_students <= all_students)


# Task 2 — issuperset()
print("Yes, is's a Super-Set:", all_students.issuperset(python_students))
print("Yes:", all_students >= python_students)


# Task 3 — isdisjoint()
morning_class = {"Ali", "Ahmed", "Bilal"}
evening_class = {"Usman", "Hamza", "Zain"}
print("Not Common:", morning_class.isdisjoint(evening_class))

