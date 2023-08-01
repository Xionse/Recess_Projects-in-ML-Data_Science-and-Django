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
