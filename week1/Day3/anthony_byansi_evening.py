#Day3 - Evening session - Byansi Anthony


# Exercise1 (Lists)
#1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
names = ["John", "Emily", "Michael", "Sophia", "Daniel"]
print(names[1])


#2. Write a python program to change the value of the first item to a new value
names = ["John", "Emily", "Michael", "Sophia", "Daniel"]
names[0] = "Andrew"
print(names)

#3.  Write a python program to add a sixth item to the list
names = ["John", "Emily", "Michael", "Sophia", "Daniel"]
names.append("Olivia")

print(names)


#4. Write a python program to add “Bathel” as the 3rd item in your list
names = ["John", "Emily", "Michael", "Sophia", "Daniel"]
names.insert(2, "Bathel")
print(names)

#5. Write a python program to remove the 4th item from the list
names = ["John", "Emily", "Michael", "Sophia", "Daniel"]
del names[3]
print(names)


#6.Use negative indexing to print the last item in your list
names = ["John", "Emily", "Michael", "Sophia", "Daniel"]
last_item = names[-1]
print(last_item)

#7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
for i in range(2, 5):
    print(items[i])
    


#8. Write a list of countries and make a copy of it
countries = ["USA", "Canada", "Australia", "Germany", "Japan"]
countries_copy = countries.copy()

print("Original List:", countries)
print("Copy of the List:", countries_copy)


#9. Write a python program to loop through the list of countries
countries = ["USA", "Canada", "Australia", "Germany", "Japan"]
for country in countries:
    print(country)
    

#10. Write a list of animal names and sort them in both descending and ascending order.
animal_names = ["Tiger", "Lion", "Elephant", "Giraffe", "Kangaroo", "Zebra", "Monkey"]

# Sort the animal names in ascending order
ascending_order = sorted(animal_names)
print("Ascending Order:", ascending_order)

# Sort the animal names in descending order
descending_order = sorted(animal_names, reverse=True)
print("Descending Order:", descending_order)


#11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them
filtered_names = [name for name in animal_names if 'a' in name.lower()]
print("Animal Names with 'a':", filtered_names)



#12. Write two lists, one containing your first names and the other your second names. Join the two lists.
# Lists of first and last names
first_names = ["Anthony"]
last_names = ["Byansi"]

# Join the two lists
full_names = [first + " " + last for first, last in zip(first_names, last_names)]
print("Full Names:", full_names)



## Exercise2 (Tuples)

#1. Consider the tuple below; x = (“samsung”, “iphone”, “tecno”, “redmi”). Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
favorite_phone_brand = x[1]
print("Favorite Phone Brand:", favorite_phone_brand)

#2. Use negative indexing to print the 2nd last item in your tuple. 
second_last_item = x[-2]
print("2nd Last Item:", second_last_item)

#3. Using the phones list above, write a python program to update “iphone” to “itel”
x = list(x)
x[x.index("iphone")] = "itel"
x = tuple(x)
print("Updated Tuple:", x)

#4. Write a python program to add “Huawei” to your tuple.
x = x + ("Huawei",)
print("Updated Tuple with Huawei:", x)

#5. Write a python program to loop through the tuple above.
print("Looping through the Tuple:")
for item in x:
    print(item)


#6. Write a python program to remove/delete the first item in your tuple.
x = x[1:]
print("Tuple after removing first item:", x)

#7. Using the tuple() constructor, create a tuple of the cities in Uganda.
cities_in_uganda = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print("Cities in Uganda Tuple:", cities_in_uganda)

#8. Write a python program to unpack your tuple.
first_city, second_city, third_city, fourth_city, fifth_city = cities_in_uganda
print("Unpacked Cities:", first_city, second_city, third_city, fourth_city, fifth_city)


#9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
cities_range = cities_in_uganda[1:4]
print("Cities using Range of Indexes:", cities_range)

#10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("John", "Emily", "Michael", "Sophia")
last_names = ("Smith", "Johnson", "Williams", "Brown")
full_names = first_names + last_names
print("Joined Names Tuple:", full_names)


#11. Create a tuple of colors and multiply it by 3.
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print("Multiplied Colors Tuple:", multiplied_colors)


#12. Return the number of times 8 appears in this tuple thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_eight = thistuple.count(8)
print("Count of 8:", count_eight)


## Exercise3 (Sets)
# 1. Use the set() constructor to create a set of 3 of your favorite beverages.
# Solution:
favorite_beverages = set(["coffee", "tea", "juice"])

# 2. Use the correct method to add 2 more items to the beverages set.
# Solution:
favorite_beverages.add("soda")
favorite_beverages.update(["water", "milk"])

# 3. Given the set below, check if microwave is present in the set.
# Solution:
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

# 4. Write a python program to remove "kettle" from the set above.
# Solution:
mySet.remove("kettle")
print("Set after removing 'kettle':", mySet)

# 5. Write a python program to loop through the set above.
# Solution:
print("Looping through the set:")
for item in mySet:
    print(item)

# 6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
# Solution:
set_items = {"apple", "banana", "orange", "pear"}
list_items = ["grape", "pineapple"]
set_items.update(list_items)
print("Updated set:", set_items)

# 7. Write two sets, one containing your ages and the other your first names. Join the two sets.
# Solution:
ages = {25, 30, 35}
first_names = {"John", "Emily", "Michael"}
joined_set = ages.union(first_names)
print("Joined set:", joined_set)



## Exercise4 (Strings)

# 1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
# Solution:
integer_variable = 10
string_variable = "Hello"
concatenated_string = str(integer_variable) + string_variable
print("Concatenated String:", concatenated_string)

# 2. Consider the example below, output the string without spaces at the beginning, in the middle, and at the end.
# Solution:
txt = " Hello, Uganda! "
trimmed_string = txt.strip()
print("Trimmed String:", trimmed_string)

# 3. Write a python program to convert the value of 'txt' to uppercase.
# Solution:
uppercase_txt = txt.upper()
print("Uppercase Text:", uppercase_txt)

# 4. Write a python program to replace character 'U' with 'V' in the string above.
# Solution:
replaced_txt = txt.replace('U', 'V')
print("Replaced Text:", replaced_txt)

# 5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd, and 4th position.
y = "I am proudly Ugandan"
character_range = y[1:4]
print("Character Range:", character_range)


# 6. The piece of code below will give an error when output;
# x = "All "Data Scientists" are cool!"
# Write a python program to correct it.
# Solution:
x = 'All "Data Scientists" are cool!'
print("Corrected String:", x)





##Exercise5 (Dictionaries)
# 1. With reference to the dictionary below, write a python program to print the value of the shoe size.
# Add this dictionary to your .py file
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print("Shoe Size:", Shoes["size"])

# 2. Write a python program to change the value "Nick" to "Adidas"
# Solution:
Shoes["brand"] = "Adidas"
print("Updated Brand:", Shoes["brand"])

# 3. Write a python program to add a key/value pair "type": "sneakers" to the dictionary
# Solution:
Shoes["type"] = "sneakers"
print("Updated Dictionary:", Shoes)

# 4. Write a python program to return a list of all the keys in the dictionary above.
# Solution:
keys_list = list(Shoes.keys())
print("Keys List:", keys_list)

# 5. Write a python program to return a list of all the values in the dictionary above.
# Solution:
values_list = list(Shoes.values())
print("Values List:", values_list)

# 6. Check if the key "size" exists in the dictionary above.
# Solution:
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")

# 7. Write a python program to loop through the dictionary above.
# Solution:
print("Looping through the dictionary:")
for key, value in Shoes.items():
    print(key, ":", value)

# 8. Write a python program to remove "color" from the dictionary.
# Solution:
Shoes.pop("color")
print("Updated Dictionary:", Shoes)

# 9. Write a python program to empty the dictionary above.
# Solution:
Shoes.clear()
print("Emptied Dictionary:", Shoes)

# 10. Write a dictionary of your choice and make a copy of it.
# Solution:
my_dict = {"name": "John", "age": 25}
copy_dict = my_dict.copy()
print("Original Dictionary:", my_dict)
print("Copied Dictionary:", copy_dict)

# 11. Write a python program to show nested dictionaries.
# Solution:
nested_dict = {
    "person1": {
        "name": "John",
        "age": 25
    },
    "person2": {
        "name": "Emily",
        "age": 30
    }
}
print("Nested Dictionary:", nested_dict)

