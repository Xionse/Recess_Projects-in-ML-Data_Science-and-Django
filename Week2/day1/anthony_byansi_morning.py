#Day1 of week 3 

# An object in Python is an instance of a class. It is a real-world entity that is created based on the defined class.
# An object has its own unique identity, state (attributes), and behavior (methods). It represents a specific
# occurrence or occurrence of a class, and it can access and modify the attributes and invoke the methods defined
# in the class.

class Phone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage} GB")
        print(f"Price: ${self.price}")
        
# Creating phone objects
phone1 = Phone("Samsung", "Galaxy S22", 128, 999)
phone2 = Phone("Apple", "iPhone 14", 256, 1099)
phone3 = Phone("Google", "Pixel 6", 128, 699)


phone1.display_info()
print()
phone2.display_info()
print()
phone3.display_info()

# Exercise 1: calculate the area and Circumference of a circle 
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return area

    def calculate_circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference

# Taking input from the user for the radius
radius = float(input("Enter the radius of the circle: "))

# Creating a circle object
circle = Circle(radius)

# Calculating the area and circumference
area = circle.calculate_area()
circumference = circle.calculate_circumference()

print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")





#Exercise 2: calculate the area and perimeter of a Rectangle 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

# Taking input from the user for the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Creating a rectangle object
rectangle = Rectangle(length, width)

# Calculating the area and perimeter
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

# Displaying the results
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")


#Excercise 3: calculate and display employee bonuses(15%) of Salary (emplyee1: 150000, emplyee: 230000)
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_bonus(self):
        bonus = 0.15 * self.salary
        return bonus

# employee objects
employee1 = Employee(150000)
employee2 = Employee(230000)

# Calculating bonuses
bonus1 = employee1.calculate_bonus()
bonus2 = employee2.calculate_bonus()

# Displaying bonuses
print(f"The bonus for employee 1 is: {bonus1}")
print(f"The bonus for employee 2 is: {bonus2}")


# Convert temperature from 37 Celcius to fahrenheit and use Encapsulation
class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, celsius):
        self._celsius = celsius

    def convert_to_fahrenheit(self):
        fahrenheit = (self._celsius * 9/5) + 32
        return fahrenheit


# Creating a TemperatureConverter object
temperature = TemperatureConverter(37)

# Getting the Celsius temperature
celsius = temperature.get_celsius()
print(f"The temperature in Celsius is: {celsius}")

# Converting Celsius to Fahrenheit
fahrenheit = temperature.convert_to_fahrenheit()
print(f"The temperature in Fahrenheit is: {fahrenheit}")



# Show encapsulation with employee information to give a pay increment (Salary with employee information to new_salary)e.g from 850000 to 1000000
class Employee:
    def __init__(self, emp_id, name, salary):
        self._emp_id = emp_id
        self._name = name
        self._salary = salary

    def get_emp_id(self):
        return self._emp_id

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def apply_pay_increment(self, increment_amount):
        self._salary += increment_amount


# Creating an Employee object
employee = Employee(1, "Byansi Anthony", 850000)

# Getting employee information
emp_id = employee.get_emp_id()
name = employee.get_name()
salary = employee.get_salary()

print(f"Employee ID: {emp_id}")
print(f"Name: {name}")
print(f"Salary: {salary}")

# Applying pay increment
increment_amount = 150000
employee.apply_pay_increment(increment_amount)

# Getting updated salary
new_salary = employee.get_salary()
print(f"New Salary: {new_salary}")

