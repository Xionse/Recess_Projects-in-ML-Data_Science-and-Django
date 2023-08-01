import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        messagebox.showinfo("Result", f"The sum is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def subtract_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        messagebox.showinfo("Result", f"The difference is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        messagebox.showinfo("Result", f"The product is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def divide_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 != 0:
            result = num1 / num2
            messagebox.showinfo("Result", f"The quotient is: {result}")
        else:
            messagebox.showerror("Error", "Cannot divide by zero!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create the main window
window = tk.Tk()
window.title("ChatGPT Calculator")

# Create the input fields
entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()

# Create the buttons
add_button = tk.Button(window, text="Addition", command=add_numbers)
add_button.pack()

subtract_button = tk.Button(window, text="Subtraction", command=subtract_numbers)
subtract_button.pack()

multiply_button = tk.Button(window, text="Multiplication", command=multiply_numbers)
multiply_button.pack()

divide_button = tk.Button(window, text="Division", command=divide_numbers)
divide_button.pack()

# Start the GUI event loop
window.mainloop()
