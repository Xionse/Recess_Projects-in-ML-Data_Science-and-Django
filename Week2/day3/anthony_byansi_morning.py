# Inheritance in python: Day3 week2-Byansi Anthony

# Key Features of Inheritance in Python:

# 1. Enables classes to inherit attributes and behaviors from other classes.
# 2. Creates a hierarchy of classes, with base classes and derived classes.
# 3. Derived classes can access and use attributes and methods of the base class.
# 4. Allows overriding and extension of base class methods in the derived class.
# 5. Supports single, multiple, and multi-level inheritance.
# 6. Promotes code reusability and reduces code duplication.
# 7. Facilitates code organization, modularity, and extensibility.
# 8. Forms a hierarchical structure of related classes.
# 9. Provides flexibility in modeling real-world relationships and building complex systems.
# 10. Enables the creation of specialized classes based on existing ones.


# Base Class: Phone
class Phone:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def make_call(self):
        print("Making a call...")
    
    def send_message(self):
        print("Sending a message...")
    

# Derived Class: Smartphone
class Smartphone(Phone):

    def __init__(self, brand, model, operating_system):
        super().__init__(brand, model)
        self.operating_system = operating_system
    
    def browse_internet(self):
        print("Browsing the internet...")
    
    # Overriding the make_call method from the base class
    def make_call(self):
        print("Making a call using a smartphone...")
    

# Derived Class: FeaturePhone
class FeaturePhone(Phone):

    def __init__(self, brand, model, physical_keyboard):
        super().__init__(brand, model)
        self.physical_keyboard = physical_keyboard
    
    def play_music(self):
        print("Playing music on a feature phone...")


# Creating objects of the derived classes
smartphone = Smartphone("Samsung", "Galaxy S21", "Android")
feature_phone = FeaturePhone("Nokia", "3310", True)

# Accessing attributes and methods from the base class and derived classes
print(smartphone.brand) 
print(feature_phone.model)  
smartphone.make_call()  
feature_phone.send_message()  
smartphone.browse_internet()  
feature_phone.play_music()  

# Exercise:  Demonstrate using inheritance to calculate the area and perimeter of a circle and rectangle respectively. 
# Base Class: Shape
class Shape:

    def __init__(self):
        pass
    
    def get_area(self):
        pass
    
    def get_perimeter(self):
        pass


# Derived Class: Circle
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        area = 3.14159 * self.radius ** 2
        return area
    
    def get_perimeter(self):
        perimeter = 2 * 3.14159 * self.radius
        return perimeter


# Derived Class: Rectangle
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_area(self):
        area = self.length * self.width
        return area
    
    def get_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter


# Creating objects of the derived classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculating and displaying the area and perimeter of the circle
circle_area = circle.get_area()
circle_perimeter = circle.get_perimeter()
print("Circle Area:", circle_area)  
print("Circle Perimeter:", circle_perimeter)  
# Calculating and displaying the area and perimeter of the rectangle
rectangle_area = rectangle.get_area()
rectangle_perimeter = rectangle.get_perimeter()
print("Rectangle Area:", rectangle_area)  
print("Rectangle Perimeter:", rectangle_perimeter)  






# Polymorphism 
# Base Class: Phone
class Phone:
    def __init__(self, brand):
        self.brand = brand
    
    def make_call(self, number):
        pass


# Derived Class: Smartphone
class Smartphone(Phone):
    def __init__(self, brand):
        super().__init__(brand)
    
    def make_call(self, number):
        print(f"Calling {number} using {self.brand} smartphone.")


# Derived Class: FeaturePhone
class FeaturePhone(Phone):
    def __init__(self, brand):
        super().__init__(brand)
    
    def make_call(self, number):
        print(f"Calling {number} using {self.brand} feature phone.")


# Derived Class: LandlinePhone
class LandlinePhone(Phone):
    def __init__(self, brand):
        super().__init__(brand)
    
    def make_call(self, number):
        print(f"Calling {number} using {self.brand} landline phone.")


# Creating objects of different phone types
smartphone = Smartphone("Samsung")
feature_phone = FeaturePhone("Nokia")
landline_phone = LandlinePhone("Panasonic")

# Polymorphic behavior
phone_list = [smartphone, feature_phone, landline_phone]
for phone in phone_list:
    phone.make_call("1234567890")
    
    

# Demonstrate abstraction using calculation of area of a circle and Rectangle. 
from abc import ABC, abstractmethod

# Abstract Base Class: Shape
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


# Concrete Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


# Concrete Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# Function to calculate and display the area of a shape
def display_area(shape):
    area = shape.calculate_area()
    print(f"The area of the shape is: {area}")


# Using Abstraction to calculate the area of a Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(6, 8)

display_area(circle)
display_area(rectangle)




#Assignment: Create a receipt printing program with GUI interface

import tkinter as tk
from tkinter import messagebox

class ReceiptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Printing Program")
        
        self.create_widgets()

    def create_widgets(self):
        # Creating labels, entry fields, and buttons
        self.label_item = tk.Label(self.root, text="Item:")
        self.entry_item = tk.Entry(self.root)
        self.label_price = tk.Label(self.root, text="Price:")
        self.entry_price = tk.Entry(self.root)
        self.button_add_item = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.button_print_receipt = tk.Button(self.root, text="Print Receipt", command=self.print_receipt)

        # Creating a text widget to display the receipt
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

# Creating the main application window
root = tk.Tk()

# Creatig an instance of the ReceiptApp class
app = ReceiptApp(root)

# Start the main event loop
root.mainloop()
