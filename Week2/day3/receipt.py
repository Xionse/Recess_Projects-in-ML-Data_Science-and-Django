import tkinter as tk
from tkinter import messagebox

class ReceiptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Printing Program")
        
        self.create_widgets()

    def create_widgets(self):
        # Create labels, entry fields, and buttons
        self.label_item = tk.Label(self.root, text="Item:")
        self.entry_item = tk.Entry(self.root)
        self.label_price = tk.Label(self.root, text="Price:")
        self.entry_price = tk.Entry(self.root)
        self.button_add_item = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.button_print_receipt = tk.Button(self.root, text="Print Receipt", command=self.print_receipt)

        # Create a text widget to display the receipt
        self.text_receipt = tk.Text(self.root, width=40, height=10)

        # Grid layout
        self.label_item.grid(row=0, column=0, sticky="w")
        self.entry_item.grid(row=0, column=1, pady=5)
        self.label_price.grid(row=1, column=0, sticky="w")
        self.entry_price.grid(row=1, column=1, pady=5)
        self.button_add_item.grid(row=2, column=0, pady=10)
        self.button_print_receipt.grid(row=2, column=1, pady=10)
        self.text_receipt.grid(row=3, columnspan=2, pady=10, padx=10)

    def add_item(self):
        item = self.entry_item.get()
        price = self.entry_price.get()

        if item and price:
            self.text_receipt.insert(tk.END, f"{item}: ${price}\n")
            self.entry_item.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both item and price.")

    def print_receipt(self):
        receipt = self.text_receipt.get("1.0", tk.END)
        if receipt:
            messagebox.showinfo("Receipt", "Printing receipt:\n\n" + receipt)
            self.text_receipt.delete("1.0", tk.END)
        else:
            messagebox.showerror("Error", "No items to print.")

# Create the main application window
root = tk.Tk()

# Create an instance of the ReceiptApp class
app = ReceiptApp(root)

# Start the main event loop
root.mainloop()
