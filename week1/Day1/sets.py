"""a set is an unordered collection of unique elements. 
    Sets are used to store a collection of distinct items where the order of elements is not important. 
    Sets are defined using curly braces {} or the set() function
"""
    
my_set = {1, 2, 3, 4}

for item in my_set:
    print(item)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set) 

intersection_set = set1.intersection(set2)

#Accessing Elements in a Set

laptops = {"Dell XPS", "HP Spectre", "Lenovo ThinkPad"}

for laptop in laptops:
    print(laptop)
    
#Getting the length of a set
laptops = {"Dell XPS", "HP Spectre", "Lenovo ThinkPad"}

length = len(laptops)
print(length)  




#  Adding items to a set
laptops = {"Dell XPS", "HP Spectre"}

laptops.add("Lenovo ThinkPad")
laptops.update(["MacBook Pro", "Asus ZenBook"])

print(laptops)


# Adding two sets together
laptops1 = {"Dell XPS", "HP Spectre"}
laptops2 = {"Lenovo ThinkPad", "MacBook Pro"}

combined_laptops = laptops1.union(laptops2)

print(combined_laptops)


## Data types of sets
laptops = {"Dell XPS", "HP Spectre", "Lenovo ThinkPad"}

print(type(laptops))  







