# Python Data Types

# Python has several built-in data types:

# 1. int       → Integer numbers
# 2. str       → String/text
# 3. float     → Decimal numbers
# 4. bool      → True or False
# 5. list      → Ordered and mutable collection
# 6. set       → Unordered collection of unique elements
# 7. tuple     → Ordered and immutable collection
# 8. dict      → Collection of key-value pairs

# --------------------------------------------------

# 1. Boolean (bool)

# --------------------------------------------------

is_Student1 = True
is_Student2 = False

print(is_Student1)
print(is_Student2)

print(type(is_Student1))
print(type(is_Student2))

print(5 > 4)
print(5 < 4)

# Output:

# True

# False

# <class 'bool'>

# <class 'bool'>

# True

# False

# --------------------------------------------------

# 2. List

# --------------------------------------------------

# A list is an ordered and mutable collection.

# Mutable means we can change its elements after creating the list.

# Lists allow duplicate values.

numbers = [10, 20, 30]

# Index:    0   1   2

numbers[1] = 200

print(numbers)
print(numbers[1])
print(type(numbers))

# Output:

# [10, 200, 30]

# 200

# <class 'list'>

# --------------------------------------------------

# 3. Set

# --------------------------------------------------

# A set is an unordered collection of unique elements.

# Sets do not allow duplicate values.

# Sets are mutable, which means we can add or remove elements.

# Sets do NOT support indexing because they are unordered.

#

# Note:

# The set itself is mutable, but its elements must be immutable

# (for example: int, float, string, tuple).

names = {"aditya", "bob", "john"}

print(names)
print(type(names))

# Example of adding an element:

names.add("rahul")

print(names)

# --------------------------------------------------

# 4. Tuple

# --------------------------------------------------

# A tuple is an ordered and immutable collection.

# Immutable means we cannot change its elements after creation.

# Tuples support indexing.

user_profile = ("john", "bangalore", 26, 54.6)

print(user_profile)
print(user_profile[0])
print(user_profile[1])
print(type(user_profile))

# Output:

# ('john', 'bangalore', 26, 54.6)

# john

# bangalore

# <class 'tuple'>

# --------------------------------------------------

# 5. Dictionary

# --------------------------------------------------

# A dictionary stores data in key-value pairs.

# It is mutable.

# Keys must be unique.

# Values can be of different data types.

student = {
"name": "John",
"city": "Bangalore",
"age": 26,
"marks": 54.6
}

print(student)
print(student["name"])
print(student["age"])
print(type(student))

# We can change a value:

student["age"] = 27

print(student)

# --------------------------------------------------

# Quick Revision

# --------------------------------------------------

# int       → Whole numbers

# str       → Text

# float     → Decimal numbers

# bool      → True / False

# list      → Ordered, mutable, allows duplicates

# set       → Unordered, mutable, unique elements

# tuple     → Ordered, immutable, allows duplicates

# dict      → Key-value pairs, mutable, unique keys
