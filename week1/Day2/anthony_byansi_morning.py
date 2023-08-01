# Day 2 - Python Programming

"""
# if statement:
# The if statement is used to execute a block of code only if a certain condition is true.
# It can be followed by an optional elif (short for "else if") and else clauses.
# Indentation is crucial to define the scope of the code block.
# Example:
if condition1:
    # code block executed if condition1 is true
elif condition2:
    # code block executed if condition2 is true and condition1 is false
else:
    # code block executed if both condition1 and condition2 are false

# for loop:
# The for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.
# It executes a block of code for each element in the sequence.
# Example:
for item in sequence:
    # code block executed for each item in the sequence

# while loop:
# The while loop is used to repeatedly execute a block of code as long as a certain condition is true.
# It keeps executing the code block until the condition becomes false.
# Example:
while condition:
    # code block executed as long as the condition is true

# break statement:
# The break statement is used to exit the current loop prematurely, even if the loop condition is still true.
# It is commonly used to terminate a loop based on a certain condition.
# Example:
while condition:
    if some_condition:
        break
    # code block executed until some_condition is true, then the loop is terminated

# continue statement:
# The continue statement is used to skip the current iteration of a loop and move to the next iteration.
# It is useful when you want to bypass specific iterations but continue looping.
# Example:
for item in sequence:
    if some_condition:
        continue
    # code block executed unless some_condition is true, then it moves to the next iteration

# pass statement:
# The pass statement is a placeholder that does nothing.
# It is used when a statement is required syntactically but you don't want to perform any action.
# Example:
def some_function():
    pass
    # code block will be empty, but the function is syntactically correct

# try-except statement:
# The try-except statement is used to handle exceptions (errors) that may occur during the execution of code.
# It allows you to catch and handle specific exceptions gracefully, preventing the program from crashing.
# Example:
try:
    # code that may raise an exception
except SomeException:
    # code executed if SomeException is raised
except AnotherException:
    # code executed if AnotherException is raised
else:
    # code executed if no exceptions are raised
finally:
    # code executed regardless of whether an exception occurred or not

# The examples above provide a brief overview of control flow statements in Python.
# These statements allow you to control the flow and behavior of your code based on different conditions and requirements.

"""

number =2023   
if number % 2 == 0:
    print("Even number") 
elif number % 2 != 0:
    print("Odd number")
else:
    print("Invalid number")
    

age = 25

if age < 18:
    print("You are underage")
elif age >= 18 and age <= 65:
    print("You are an adult")
else:
    print("You are a senior citizen")
    
    
    
    
# For loop
phones = ("iPhone 14", "Samsung Galaxy S22", "Google Pixel 6", "OnePlus 9")

for phone in phones:
    print(phone)
    
    
# While looop 
phones = ["iPhone 14", "Samsung Galaxy S22", "Google Pixel 6", "OnePlus 9"]

index = 0
while index < len(phones):
    print(phones[index])
    index += 1

    

# Break statemen
phones = ["iPhone", "Samsung", "Google Pixel", "OnePlus"]
index = 0


search_phone = "Google Pixel"

while index < len(phones):
    if phones[index] == search_phone:
        print("Phone found:", phones[index])
        break
    index += 1

if index == len(phones):
    print("Phone not found:", search_phone)


#continue statement
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
    


# Pass statement
def some_function():
    pass




# Try-except statement
num1 = 10
num2 = 0

try:
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
    
    

# List of phones
phones = ["iPhone", "Samsung", "Google Pixel", "OnePlus"]

try:
    
    index = int(input("Enter the index of the phone you want to access: "))


    selected_phone = phones[index]
    print("Selected phone:", selected_phone)

except IndexError:
    print("Invalid index! The list does not have an element at the specified index.")

except ValueError:
    print("Invalid input! Please enter a valid integer index.")

except Exception as error:
    print("An error occurred:", str(error))

finally:
    print("Exception handling completed.")


## Exercise 1
## Prompting  a student to enter their mental health rating
print("Welcome to the Student Mental Health Survey")

responses = []

num_students = int(input("Enter the number of students: "))

for i in range(1, num_students + 1):
    response = input(f"Student {i}, please rate your mental health on a scale of 1-10: ")
    responses.append(response)

print("\n--- Survey Results ---")
for i, response in enumerate(responses):
    print(f"Student {i + 1}: {response}")



