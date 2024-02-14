# A) String Operations
# Reverse a string
string1 = "hello"
reversed_string = string1[::-1]
print("Reversed string:", reversed_string)

# Replace string with other string
string2 = "hello world"
new_string = string2.replace("world", "universe")
print("String after replacement:", new_string)

# Merge two strings
string3 = "hello"
string4 = "world"
merged_string = string3 + " " + string4
print("Merged string:", merged_string)

# Find character in string without using loops
char_to_find = "o"
print(f"Is '{char_to_find}' in '{string1}'? {'Yes' if char_to_find in string1 else 'No'}")

# Split string into multiple words and characters
string5 = "hello world"
words = string5.split()
characters = list(string5)
print("Words:", words)
print("Characters:", characters)

# B) Dictionaries Operations
# Apply Update, Delete, clear, popitem, pop, get, keys, and values operation in dictionary
my_dict = {"a": 1, "b": 2, "c": 3}

# Update
my_dict.update({"d": 4})

# Delete
del my_dict["a"]

# Clear
my_dict.clear()

# Create a new dictionary to demonstrate other operations
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

# Popitem
key, value = my_dict.popitem()
print("Popped item:", key, value)

# Pop
value = my_dict.pop("c")
print("Popped value of 'c':", value)

# Get
print("Value of 'a':", my_dict.get("a"))

# Keys
print("Keys:", my_dict.keys())

# Values
print("Values:", my_dict.values())

# Create 3 dictionaries and merge them into 1 dictionary
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}
merged_dict = {**dict1, **dict2, **dict3}
print("Merged dictionary:", merged_dict)
