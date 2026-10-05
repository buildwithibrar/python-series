# Creating Dictionaries
# ------------------------------------------------------------

person = {
    "name": "Bilal",
    "age": 24,
    "country": "Pakistan"
}

# Check Type
print(type(person))

# Empty Dictionary
empty_Dict = {}

# Access Values
print(person["name"])
print(person["age"])
print(person["country"])

# get()
print(person.get("email"))

# Add a New Item
person["email"] = "ibrar@gmail.com"
print("Person Detail:", person.items())

# Update an Item
person["age"]= 27
print(person)

person.update({
    "name" : "ibrar",
    "age" : 30,
    "country": "Malaysia"
})

print(person)


# Membership
if "age" in person and "country" in person:
    print("Available")

else:
    print("Not Available")


# pop() and popitem()
# ------------------------------------------------------------

# pop() removes a specific item using its key.
product = {
    "name": "Burger",
    "price": 8.99,
    "category": "Food",
    "available": True
}

product.pop("price")
print(product)

product.popitem()
print(product)


# Store the Removed Value
student = {
    "name": "Ali",
    "age": 22,
    "country": "Pakistan",
    "course": "Python"
}

removed_Item = student.pop("age")
print(removed_Item)
print(student)


# clear() removes all items from a dictionary.
person = {
    "name": "Bilal",
    "age": 24,
    "country": "Pakistan"
}

person.clear()
print(person)


# copy() creates a separate copy of a dictionary.

person = {
    "name": "Bilal",
    "age": 24
}

new_person = person.copy()

print(new_person)