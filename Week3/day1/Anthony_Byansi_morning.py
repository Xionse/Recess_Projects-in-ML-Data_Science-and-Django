

"""


- Definition: Regular expressions are sequences of characters that define a search pattern.
- Module: Python provides the re module for working with regular expressions.
- Pattern: A regular expression pattern is a sequence of characters that defines the search criteria.
- Match: A match is the result of applying a regular expression pattern to a string.
- Functions: The re module provides functions like search(), match(), findall(), and sub() to work with regular expressions.
- Metacharacters: Metacharacters are special characters with a symbolic meaning in regular expressions, such as . (any character), ^ (start of a line), $ (end of a line), * (zero or more occurrences), + (one or more occurrences), ? (zero or one occurrence), etc.
- Character Classes: Character classes allow specifying a set of characters to match, such as [0-9] (digits), [a-zA-Z] (letters), [aeiou] (vowels), etc.
- Quantifiers: Quantifiers specify how many times a character or group should occur, such as {n} (exactly n times), {n,} (at least n times), {n,m} (between n and m times), etc.
- Anchors: Anchors are used to specify the position of a match in a string, such as ^ (start of a line), $ (end of a line), \b (word boundary), etc.
- Grouping and Capturing: Parentheses () are used for grouping and capturing parts of a pattern.
- Modifiers: Modifiers are used to modify the behavior of regular expressions, such as i (case-insensitive), s (dot matches all), m (multiline mode), etc.
- Special Sequences: Special sequences represent predefined sets of characters, such as \d (digits), \w (word characters), \s (whitespace), etc.
- Escape Characters: Backslashes \ are used to escape metacharacters and create special sequences.
- Flags: Flags can be used as optional arguments in regular expression functions to modify the behavior of the pattern matching.


"""

# Regular Expressions available in Python
"""
In Python, regular expressions are supported through the `re` module. Here's a list of commonly used regular expressions:

- `re.search(pattern, string)`: Searches for a pattern match anywhere in the string.
- `re.match(pattern, string)`: Checks if the pattern matches at the beginning of the string.
- `re.findall(pattern, string)`: Returns all non-overlapping matches of the pattern in the string.
- `re.finditer(pattern, string)`: Returns an iterator yielding match objects for all matches.
- `re.sub(pattern, repl, string)`: Replaces occurrences of the pattern in the string with the replacement string.
- `re.split(pattern, string)`: Splits the string by the occurrences of the pattern.

Here are some commonly used elements in regular expression patterns:

- `.`: Matches any character except a newline.
- `^`: Matches the start of the string.
- `$`: Matches the end of the string.
- `*`: Matches zero or more occurrences of the previous character or group.
- `+`: Matches one or more occurrences of the previous character or group.
- `?`: Matches zero or one occurrence of the previous character or group.
- `[]`: Specifies a character class, matches any character within the brackets.
- `|`: Matches either the pattern before or after the pipe.
- `()`: Groups characters or patterns together.
- `\`: Escapes special characters or introduces special sequences.
- `\d`: Matches any digit character.
- `\w`: Matches any alphanumeric character.
- `\s`: Matches any whitespace character.
- `\b`: Matches a word boundary.

"""




"""
Matching:

Matching is the process of checking if a pattern exists at the beginning of a string.
It is done using the re.match() function.
Successful matching returns a match object or None if no match is found.
Searching:

Searching involves finding all occurrences of a pattern in a string.
It is done using the re.search() function.
Searching looks for the pattern anywhere in the string.
Successful searching returns a match object or None if no match is found.
"""

import re

phones_data = "I have Samsung, iPhone, and Xiaomi phones."


pattern = r"\b(iPhone|Samsung|Xiaomi)\b"

match = re.search(pattern, phones_data)

if match:

    print("Found phone:", match.group(0))
else:
    print("Phone not found.")
    

print("------------------------------------------------------------------------------")




# Email Validation

import re

# Example email addresses
emails = [
    "anthony.byansi@example.com",
    "anthony_smith123@gmail.com",
    "info@company.com",
    "invalid.email",
    "user@domain"
]

pattern = r'^[\w.-]+@[a-zA-Z_-]+\.[a-zA-Z]{2,}$'

# Check if each email is valid
for email in emails:
    if re.match(pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is an invalid email address.")


# Generators and Iterators in Python

# Iterators and Generators in the Context of Regular Expressions

"""
Iterators and generators are concepts in Python that relate to handling and processing data in a sequential manner.
In the context of regular expressions, iterators and generators can be used to efficiently process and iterate over matches found in a given text using regular expression patterns.
"""

# Iterators:
"""
- An iterator is an object that represents a stream of data, allowing you to iterate over the elements of that data.
- In the context of regular expressions, iterators can be used to iterate over matches found in a text.
- The `re.finditer()` function returns an iterator yielding match objects for all non-overlapping matches of a pattern in a string.
- By iterating over the match objects, you can access the matched substrings and perform further processing on them.
"""

# Example of using an iterator with regular expressions:
import re

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
pattern = r"\b\w{5}\b" #

matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())  

# Generators:
"""
- A generator is a special type of iterator that can be defined with a generator function or expressed using a generator expression.
- In the context of regular expressions, generators can be used to yield matches found in a text one at a time, rather than returning all matches at once.
- This can be particularly useful when dealing with large texts or when memory efficiency is a concern.
"""

# Example of using a generator with regular expressions:
import re

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
pattern = r"\b\w{5}\b"  
matches = (match.group() for match in re.finditer(pattern, text))
for match in matches:
    print(match)  


# Decorators in python 

def uppercase_decorator(func):
    def wrapper():
        result = func()
        modified_result = result.upper()
        return modified_result
    return wrapper

# Defining a function to be decorated
def greet():
    return "hello, world!"

decorated_greet = uppercase_decorator(greet)

# Call the decorated function
print(decorated_greet()) 



def __main__():
    if __name__ == "__main__":
        print("poor decorator")
        
    else if __name__ == "__main__ 