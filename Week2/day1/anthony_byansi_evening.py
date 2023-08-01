# Week 2- Day1-Evening Session 

'''
Functions in Python:

Functions are blocks of reusable code that perform a specific task. They allow us to break down a complex program into smaller, manageable pieces. Functions are defined using the 'def' keyword, followed by the function name and a set of parentheses. They can take input parameters (arguments) and return output values.

The structure of a function in Python is as follows:

def function_name(parameters):
# Function body
# Code to be executed

'''


def describe_phone(brand, model, color):
    description = f"This phone is a {color} {brand} {model}."
    print(description)


def calculate_discounted_price(price, discount):
    
    discounted_price = price - (price * discount)
    return discounted_price


def compare_phones(phone1, phone2):

    return phone1


def get_phone_specifications(brand, model):
    
    specifications = {
        "brand": brand,
        "model": model,
        "screen_size": 6.7,
        "storage": "128GB",
        "camera": "Quad-camera setup",
    }

    return specifications


#Python modules 

"""
PhoneModule.py - A module for phone-related functions
"""

# Function to check if a phone is expensive
def is_expensive(phone_price):
    if phone_price > 1000:
        return True
    else:
        return False

# Function to format the phone name
def format_phone_name(phone_name):
    return phone_name.upper()

print("----------------------------------------------------------------")


import PhoneModule

price = 1200
is_expensive = PhoneModule.is_expensive(price)
formatted_name = PhoneModule.format_phone_name("iPhone")
discounted_price = PhoneModule.calculate_discounted_price(price, 10)

print(is_expensive)
print(formatted_name)









#Input and Output in python 


