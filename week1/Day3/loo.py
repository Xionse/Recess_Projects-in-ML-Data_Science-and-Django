import tkinter as tk
from tkinter import messagebox

# Function to perform addition
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        messagebox.showinfo("Result", "The result is: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numbers.")

# Function to perform subtraction
def subtract_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        messagebox.showinfo("Result", "The result is: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numbers.")

# Function to perform multiplication
def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        messagebox.showinfo("Result", "The result is: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numbers.")

# Function to perform division
def divide_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
        else:
            result = num1 / num2
            messagebox.showinfo("Result", "The result is: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numbers.")

# Create the main window
window = tk.Tk()
window.title("ChatGPT Calculator")

# Create the input fields
label1 = tk.Label(window, text="First Number:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Second Number:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

# Create the buttons
add_button = tk.Button(window, text="Add", command=add_numbers)
add_button.pack()

subtract_button = tk.Button(window, text="Subtract", command=subtract_numbers)
subtract_button.pack()

multiply_button = tk.Button(window, text="Multiply", command=multiply_numbers)
multiply_button.pack()

divide_button = tk.Button(window, text="Divide", command=divide_numbers)
divide_button.pack()

# Start the main loop
window.mainloop()
