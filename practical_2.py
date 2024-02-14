# A) Create a list and apply methods (append, extend, remove, reverse), arrange created list in ascending and descending order.
my_list = [3, 1, 4, 2, 5] 
print("Original List:", my_list)

my_list.append(6)  # Append element to the list
print("After appending 6:", my_list)

my_list.extend([7, 8])  # Extend list with another list
print("After extending with [7, 8]:", my_list)

my_list.remove(4)  # Remove element from the list
print("After removing 4:", my_list)

my_list.reverse()  # Reverse the list
print("After reversing:", my_list)

# Arrange list in ascending and descending order
my_list.sort()  # Ascending order
print("Ascending order:", my_list)

my_list.sort(reverse=True)  # Descending order
print("Descending order:", my_list)


# B) From a nested list, get word "orange" and "Python" & repeat the list five times without using loops
List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]
word_orange = List1[-1][-1]
word_python = List1[4][0].capitalize()

print("Word 'orange':", word_orange)
print("Word 'Python':", word_python)

# Repeat the list five times without using loops
Repeated_List1 = [List1] * 5
print("Repeated List:", Repeated_List1)


# C) Create a list and copy it using slice function
original_list = [10, 20, 30, 40, 50]
copied_list = original_list[:]
print("Original List:", original_list)
print("Copied List:", copied_list)


# D) Create a tuple and apply different type of mathematical operation on it (Sum, Maximum, minimum etc.).
my_tuple = (3, 1, 4, 2, 5)
print("Tuple:", my_tuple)
print("Sum of elements:", sum(my_tuple))
print("Maximum element:", max(my_tuple))
print("Minimum element:", min(my_tuple))
