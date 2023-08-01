
# Python Dictionaries(Afternoon-Evening Session)

"""
Dictionaries are defined using curly braces {} and contain comma-separated key-value pairs.
# Each key-value pair is separated by a colon : where the key is followed by its corresponding value.

# Dictionary Syntax:
# dictionary_name = {key1: value1, key2: value2, key3: value3}

 Key:
# A key is an immutable object (such as a string, number, or tuple) that is used to access its associated value.
# Keys must be unique within a dictionary, and they provide a way to identify and retrieve the corresponding values.

# Value:
# A value can be of any data type (e.g., string, number, list, or even another dictionary).
# Values are associated with their respective keys and can be accessed using the key.

"""

phone_prices = {"iPhone": 1000, "Samsung": 900, "Google Pixel": 800}


iphone_price = phone_prices["iPhone"]
print("Price of iPhone:", iphone_price)

# Finding the datatype of the dictionary
dictionary_type = type(phone_prices)
print("Data type of phone_prices:", dictionary_type)

# Determining the length of the dictionary
dictionary_length = len(phone_prices)
print("Length of phone_prices:", dictionary_length)

# Modifying values using keys
phone_prices["Samsung"] = 950
print("Updated price of Samsung:", phone_prices["Samsung"])

# Adding new key-value pairs
phone_prices["OnePlus"] = 700
print("Price of OnePlus:", phone_prices["OnePlus"])

# Removing a key-value pair
del phone_prices["Google Pixel"]
print("Updated phone prices:", phone_prices)



#EXERCISE 1: use the values() method to a list of items in the dictionary 
phone_prices = {"iPhone": 1000, "Samsung": 900, "Google Pixel": 800}

price_list = list(phone_prices.values())
print("List of prices:", price_list)



#EXERCISE 2: to check if a key exists in the dictionary
phone_prices = {"iPhone": 1000, "Samsung": 900, "Google Pixel": 800}

key = input("Enter a phone brand: ")
if key in phone_prices:
    print(f"{key} exists in the dictionary!")
else:
    print(f"{key} does not exist in the dictionary.")




#EXERCISE 3: Give an sample on how to change dictionary items, how to updapte
## CHANGING
phone_prices = {"iPhone": 1000, "Samsung": 900, "Google Pixel": 800}
phone_prices["Samsung"] = 950
print("Updated phone prices:", phone_prices)

## UPDATING 
phone_prices = {"iPhone": 1000, "Samsung": 900}
additional_prices = {"Google Pixel": 800, "OnePlus": 700}
phone_prices.update(additional_prices)
print("Updated phone prices:", phone_prices)




#EXERCISE 4: Give an example on how to add dictionary items, How to remove dictionary items 
phone_prices = {"iPhone": 1000, "Samsung": 900}

##adding 
phone_prices["Google Pixel"] = 800
print("Updated phone prices:", phone_prices)

##removing
phone_prices = {"iPhone": 1000, "Samsung": 900, "Google Pixel": 800}
del phone_prices["Samsung"]
print("Updated phone prices:", phone_prices)





#EXERCISE 5: Give an sample on how to loop through a dictionary and how to nest dictionaries 
##Looping through a dictionary
phone_prices = {"iPhone": 1000, "Samsung": 900, "Google Pixel": 800}

for brand, price in phone_prices.items():
    print(f"The price of {brand} is {price}")


##Nesting dictionaries
phone_prices = {
    "iPhone": {"Price": 1000, "Color": "Silver"},
    "Samsung": {"Price": 900, "Color": "Black"},
    "Google Pixel": {"Price": 800, "Color": "White"}
}


for brand, details in phone_prices.items():
    print(f"{brand}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
    print()
    
    
    
    
    
    """
#Numbers in Python(Afternoon-Evening Session)
1. Integer (int): Integers are whole numbers without a decimal point. They can be positive or negative, such as -1, 0, 1, 100, etc. Python's integers have unlimited precision.

2. Floating-Point (float)

3. Complex (complex)

"""

# Integer
age = 25

# Floating-Point
pi = 3.14159


# Complex
z = 2 + 3j

#simple operation 
result = age * pi - z
print("Result:", result)


#Type Conversion
# Convert an integer to a float
num_int = 5
num_float = float(num_int)
print("Float:", num_float)

# Convert a float to a complex number
num_float = 3.14
num_complex = complex(num_float)
print("Complex:", num_complex)


# Convert a complex number to a float
num_complex = 2 + 3j
num_float = float(num_complex.real)
print("Float:", num_float)




#Casting in python
"""
int(): Converts a value to an integer data type
float(): Converts a value to a floating-point data type
complex(): Converts a value to a complex data type
str(): Converts a value to a string data type
bool(): Converts a value to a boolean data type

""" 


#STRING IN PYTHON
#formated strings
name = 'byansi anthony'
age = 12
greeting = f"Hello, {name}. You are {age} years old."

##Raw string    
path = r'C:\Users\Documents\file.txt'
regex = r'\d+'

#Concatenation methods 
words = ["Recess", "2023"]
result = " ".join(words)
print(result)

str1 = "byansi, "
str1 += "anthony!"
print(str1)


name = "Anthony"
age = 12
print(f"My name is {name} and I am {age} years old.")







#EXERCISE 1: Use the len() function to return the length of a string 
text = "RECESS"
length = len(text)
print("Length of the string:", length)



#EXERCISE 2: Give an example of using a for loop in a string 
text = "RECESSERS 2023"

# Iterate over each character in the string
for char in text:
    print(char)
    
    
    
#EXERCISE 3: Give an example of slicing in a string
phone = "iPhone 14 Pro Max"
brand = phone[:6]
model = phone[7:16]
variant = phone[17:]

print("Brand:", brand)
print("Model:", model)
print("Variant:", variant)

#EXERCISE: use a condition to show how to use booleans

x = 5
y = 10

# a condition with booleans
if x < y:
    print("x is less than y")
else:
    print("x is greater than or equal to y")
    
    
    
    
age = 25

is_adult = age >= 18
is_teenager = age >= 13 and age <= 19

print(is_adult)     
print(is_teenager)  





