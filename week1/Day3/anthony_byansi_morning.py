# Day 3: Basic Operators and Expressions(Input and output operators)

# 1. Arithmetic Operators:
"""
- Addition (+): Adds two operands together.
- Subtraction (-): Subtracts the second operand from the first.
- Multiplication (*): Multiplies two operands.
- Division (/): Divides the first operand by the second.
- Modulo (%): Returns the remainder of the division.
- Exponentiation (**): Raises the first operand to the power of the second.
- Floor Division (//): Returns the quotient of the division, discarding the remainder.
    
"""

#2. Assignment Operators:
"""
- Assign (=): Assigns a value to a variable.
- Add and Assign (+=): Adds the right operand to the left operand and assigns the result to the left operand.
- Subtract and Assign (-=): Subtracts the right operand from the left operand and assigns the result to the left operand.
- Multiply and Assign (*=): Multiplies the right operand with the left operand and assigns the result to the left operand.
- Divide and Assign (/=): Divides the left operand by the right operand and assigns the result to the left operand.
- Modulo and Assign (%=): Computes the modulus of the left operand with the right operand and assigns the result to the left operand.
- Exponentiate and Assign (**=): Raises the left operand to the power of the right operand and assigns the result to the left operand.
- Floor Divide and Assign (//=): Performs floor division on the left operand by the right operand and assigns the result to the left operand.
"""

#3. Comparison Operators:
"""
- Equal to (==): Checks if two operands are equal.
- Not Equal to (!=): Checks if two operands are not equal.
- Greater than (>): Checks if the left operand is greater than the right operand.
- Less than (<): Checks if the left operand is less than the right operand.
- Greater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand.
- Less than or equal to (<=): Checks if the left operand is less than or equal to the right operand.
"""

#4. Logical Operators:
"""
- Logical AND (and): Returns True if both operands are true.
- Logical OR (or): Returns True if at least one of the operands is true.
- Logical NOT (not): Returns the opposite of the operand's truth value.
"""

#5. Assignment Operators:
"""
- Assign (=): Assigns a value to a variable.
- Add and Assign (+=): Adds the right operand to the left operand and assigns the result to the left operand.
- Subtract and Assign (-=): Subtracts the right operand from the left operand and assigns the result to the left operand.
- Multiply and Assign (*=): Multiplies the right operand with the left operand and assigns the result to the left operand.
- Divide and Assign (/=): Divides the left operand by the right operand and assigns the result to the left operand.
- Modulo and Assign (%=): Computes the modulus of the left operand with the right operand and assigns the result to the left operand.
- Exponentiate and Assign (**=): Raises the left operand to the power of the right operand and assigns the result to the left operand.
- Floor Divide and Assign (//=): Performs floor division on the left operand by the right operand and assigns the result to the left operand.
"""

#6. Membership Operators:
"""
- In: Returns True if a value is found in a sequence.
- Not in: Returns True if a value is not found in a sequence.
"""

#7. Identity Operators:
"""
- is: Returns True if both operands refer to the same object.
- is not: Returns True if both operands do not refer to the same object.
"""


#8. Bitwise Operators:
"""
- Bitwise AND (&): Performs a bitwise AND operation between two operands.
- Bitwise OR (|): Performs a bitwise OR operation between two operands.
- Bitwise XOR (^): Performs a bitwise XOR (exclusive OR) operation between two operands.
- Bitwise NOT (~): Inverts the bits of the operand.
- Left Shift (<<): Shifts the bits of the left operand to the left by the number of positions specified by the right operand.
- Right Shift (>>): Shifts the bits of the left operand to the right by the number of positions specified by the right operand.

"""

#Examples 
## 1. Arithmetic Operators:
x = 5
y = 2

addition = x + y      # Output: 7
subtraction = x - y   # Output: 3
multiplication = x * y   # Output: 10
division = x / y    # Output: 2.5
modulo = x % y    # Output: 1
exponentiation = x ** y   # Output: 25
floor_division = x // y   # Output: 2

## 2. Assignment Operators:
x = 5

x += 2   # Equivalent to: x = x + 2
x -= 3   # Equivalent to: x = x - 3
x *= 4   # Equivalent to: x = x * 4
x /= 2   # Equivalent to: x = x / 2
x %= 3   # Equivalent to: x = x % 3
x **= 2  # Equivalent to: x = x ** 2
x //= 5  # Equivalent to: x = x // 5

## 3. Comparison Operators:
x = 5
y = 2

equal = x == y         # Output: False
not_equal = x != y     # Output: True
greater_than = x > y   # Output: True
less_than = x < y      # Output: False
greater_than_or_equal = x >= y   # Output: True
less_than_or_equal = x <= y      # Output: False



## 4. Logical Operators:
x = 5
y = 2

logical_and = (x > 0) and (y < 10)     # Output: True
logical_or = (x > 0) or (y > 10)       # Output: True
logical_not = not (x > 0)              # Output: False



## 5. Membership Operators:
numbers = [1, 2, 3, 4, 5]

in_sequence = 3 in numbers     # Output: True
not_in_sequence = 6 not in numbers   # Output: True



## 6. Identity Operators:
x = 5
y = 5
z = [1, 2, 3]

is_same_x_y = x is y          # Output: True
is_not_same_x_y = x is not y  # Output: False
is_same_x_z = x is z          # Output: False
is_not_same_x_z = x is not z  # Output: True



## 7. Bitwise Operators:
x = 5
y = 3

bitwise_and = x & y     # Output: 1
bitwise_or = x | y      # Output: 7
bitwise_xor = x ^ y     # Output: 6
bitwise_not = ~x        # Output: -6
left_shift = x << 2     # Output: 20
right_shift = x >> 1    # Output: 2


# EXCERCISE 1: create a simple calculator program with a GUI interface. Make the title of the calculator program window with your name
import tkinter as tk

# Function to perform calculation
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Byansi Anthony - Calculator")

# Create an entry widget to display the expression and results
entry = tk.Entry(window, width=25)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Function to handle button clicks
def button_click(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + value)

# Add buttons to the window
row = 1
col = 0
for button in buttons:
    tk.Button(window, text=button, width=5, command=lambda value=button: button_click(value)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the equal button to perform the calculation
tk.Button(window, text='=', width=20, command=calculate).grid(row=row, column=0, columnspan=4)

# Start the main loop
window.mainloop()
