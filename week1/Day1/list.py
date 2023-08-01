# A list in Python is an ordered collection of elements enclosed in square brackets.
# Lists can contain elements of different types, such as numbers, strings, or even other lists.
# Lists are mutable, allowing modification of their elements.
# Elements in a list are accessed using zero-based indexing.
# Lists support various operations like adding or removing elements, slicing, sorting, and more.



# List are for Duplicate values
empty_list = []
numbers = [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "orange"]

mixed = [1, "apple", True, 3.14]

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

constructor_list = list(range(1, 6))

# Creating list using list comprehension
comprehension_list = [x for x in range(1, 6)]

repeated_list = [0] * 10

## Accessing items in a list
print(fruits[0])
print(fruits[1:3])
print(fruits[::2])  
print(fruits[::-1])

# Apppend and inserting items in a list
fruits.append("mango")
fruits.insert(1, "grapes")

print(fruits)

# iterating through the list 
index = 0

# Iterating through the list using a while loop
while index < len(fruits):
    print(fruits[index])
    index += 1
