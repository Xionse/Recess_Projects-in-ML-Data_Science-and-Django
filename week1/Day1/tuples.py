'''
a tuple is an ordered, immutable collection of elements. 
Tuples are similar to lists, but they cannot be modified once created. 
They are defined using parentheses () or can be created without parentheses by separating the elements with comma

'''

phones = ("iPhone 14", "Samsung Galaxy S22", "Google Pixel 5", "OnePlus 9")

# Accessing elements
print(phones[0])  
print(phones[2])  

# Length of the tuple
print(len(phones))  

# Count occurrences
print(phones.count("iPhone 14"))  

# Index of an element
print(phones.index("Samsung Galaxy S22"))  

# Sorting the tuple (creates a new list)
sorted_phones = sorted(phones)
print(sorted_phones)  

# Converting a list to a tuple
my_list = [10, 20, 30]
converted_tuple = tuple(my_list)
print(converted_tuple)  

# Concatenating tuples
more_phones = ("Sony Xperia", "LG G8")
combined_tuple = phones + more_phones
print(combined_tuple)  

# Repeating a tuple
repeated_tuple = phones * 2
print(repeated_tuple)  

# Different data types with in a tuple.
my_tuple = ("apple", 42, 3.14, True)
print(my_tuple)

# Accessing tuples within a tuple
my_tuple = ("apple", "banana", "orange")

print(my_tuple[0]) 
print(my_tuple[2]) 

# Adding to a tuple 
phones = ("iPhone 14", "Samsung Galaxy S22", "Google Pixel 6", "OnePlus 9")
new_phone = "Sony Xperia"

updated_phones = phones + (new_phone,)

print(updated_phones)


# Concatenating two tuples
laptops1 = ("Dell XPS", "HP Spectre", "Lenovo ThinkPad")
laptops2 = ("MacBook Pro", "Asus ZenBook")


combined_laptops = laptops1 + laptops2

print(combined_laptops)


for laptop in laptops1:
    print(laptop)


