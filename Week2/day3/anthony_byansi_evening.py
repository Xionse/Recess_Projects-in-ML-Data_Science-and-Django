phones = ["iPhone", "Samsung", "Nokia"]

# SyntaxError
print("Number of phones:", len(phones)

# TypeError
total_phones = len(phones) + " phones"

# NameError
print(nonexistent_variable)

# IndexError
print(phones[3])

# KeyError
phone_dict = {"brand": "Samsung", "model": "Galaxy"}
print(phone_dict["color"])

# ValueError
invalid_num = int("abc")

# AttributeError
class Phone:
    def __init__(self, brand):
        self.brand = brand

my_phone = Phone("iPhone")
print(my_phone.color)

# IOError
file = open("nonexistent_file.txt", "r")

# ZeroDivisionError
result = 10 / 0

# ImportError
import non_existent_module






#try-except block
phones = ["iPhone", "Samsung", "Nokia"]

try:
    print(phones[3])
except IndexError:
   
    print("Invalid index. Phone not found.")




# try-except-else block
phones = ["iPhone", "Samsung", "Nokia"]

try:
    print(phones[1])
except IndexError:
    print("Invalid index. Phone not found.")
else:
    print("Phone found.")





# Exception handling for files 

try:
    file = open("./phones.csv", "r")
    # Performing file operations
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except IOError as e:
    print("An error occurred:", str(e))
finally:
    file.close()

# Alternatively
with open("./phones.csv", "r") as file:
  
# Reading the entire contents of a file
content = file.read()

# Reading a single line from a file
line = file.readline()

# Reading all lines of a file into a list
lines = file.readlines()
