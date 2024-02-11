# String
# 1. Reverse the given string (You can take any string)
name=input("Enter Your Name : ")
print("Name in reverse is: ",name[::-1])


# 2. Replace some character of the string with another character without using a loop.
string="Hello World"
print(string.replace('o','*'))

# 3. Find whether the character in the given string or not.
char = input("Enter a Character to check :")
if char in "Hello World":
    print("Character Found!")
else:
    print("Character Not Found!")

# 4. Create tuple, list and set and convert them into the different strings.
    tup = ("apple", "banana", "cherry")
    lst = ["apple", "banana", "cherry"]
    st = {"apple", "banana", "cherry"}
    str_tup = str(tuple(lst))
    str_lst = str(lst)
    str_st = str(st)
    print("Tuple to String : ",str_tup)
    print("List to String : ",str_lst)
    print("Set to String : ",str_st)
    

# 5. Convert all the string characters to the upper and the lower case and split it with the different methods.
names=input("Enter Your Name : ")
print("Printing In UpperCase : ",names.upper())
print("Printing In LowerCase : ",names.lower())
print("Printing Split By Space : ",names.split(" "))
print("Printing Split By Word : ",names.split("Gadhvi"))

# 6. Perform the following operations to the tuple and the list
# 	Find max, min, len, sum
marks=(90,99,89,100,75,33)
print("Finding Max : ",max(marks))
print("Finding Min : ",min(marks))
print("Finding Len : ",len(marks))
print("Finding Sum : ",sum(marks))

# 7. Copy one list to the another list without using the copy command.
lst=["Ashwin","Vishwaraj","Jayraj","Sidhu","Samarth"]
new_list=[]
new_list=lst
print("Printing List Without Copying : ",new_list)
# 8. Perform below task as instructed
# 	-> Create a dictionary named student with keys: 'name', 'age', and 'grade'. Assign 	values accordingly.
# 	Access Dictionary Values:
student={'name':'Ashwin','age':19,'grade':'A1'};
print("Dictionary Access by Name : ",student['name'])
print("Dictionary Access by Age : ",student["age"])
print("Dictionary Access by Grade : ",student["grade"])

# 	-> Print the 'age' of the student from the dictionary created in Exercise 1.
# 	Modify Dictionary Values:

print("Dictionary Access by Age : ",student["age"])
student["age"]="20"

# 	-> Update the 'grade' of the student to a new value.
student["grade"]='B1'

# 	-> Check if the key 'gender' is present in the student dictionary. Print a message 	based on the result.
if 'gender' in student:
    print("The Gender Key Is Present")
else:
    print("The Gender Key Is Not Present")

# 9. Perform below task as instructed
# 	-> Create two sets: set1 with elements (1, 2, 3) and set2 with elements (3, 4, 5).
    set1={1,2,3}
    set2={3,4,5}

# 	Union of Sets:
    new_set=set1.union(set2)

# 	-> Find the union of set1 and set2 and print the result.
    print("Printing The Union Of Set : ",new_set)
# 	Intersection of Sets:
    intersection=set1.intersection(set2)
    
# 	-> Find the intersection of set1 and set2 and print the result.
    print("Printing The Intersection Of set : ",intersection)
# 	Difference of Sets:
    difference=set1.difference(set2)

# 	-> Find the elements that are in set1 but not in set2 and print the result.
    print("Printing The Difference Of set : ",difference)

# 	Check Subset:
    check = set1.issubset(set2)
# 	-> Check if set1 is a subset of set2. Print a message based on the result.
    if check==True:
        print("Set1 Is A Subset Of Set2 ")
    else:
        print("Set1 Is Not A Subset Of Set2")

# 10. Perform below task as instructed
# 	Create a dictionary where keys are subjects ('math', 'science') and values are sets of students who take those subjects.
    sub={'math':{'Ashwin','Sam','Lalu','Babu','Sidhu'},'science':{'Ashwin','Vis','Jay','Sid','Dip'}}

# 	Update Set Values:
    for i in list(sub['math']):
        sub['math'].remove(i)
        sub['science'].add(i)
        print("Updated Dictionary Value : ",sub)

# 	Add a new student to the 'math' subject in the dictionary from Exercise 11.
        sub['math'].add('John')
        print("Dictionary After Adding John To Math Subject : ",sub)
# 	Remove Set Values:
        del sub['science']
        print("Dictionary After Removing Science From Key : ",sub)

# 	Remove a student from the 'science' subject in the dictionary from Exercise 11.
        science_students=list(sub['science'])
        science_students.remove('Jay')
        sub['science']=set(science_students)
        print("Dictionary After Removing Jay From Science Subject : ",sub)
# 	Check Common Students:
        common_students=set(sub['math']).intersection(sub['science'])
        print("Common Students In Both Math And Science : ",common_students)

# 	Find and print the students who take both 'math' and 'science'.
        sub = {'math': {'Ashwin', 'Sam', 'Lalu', 'Babu', 'Sidhu'}, 'science': {'Ashwin', 'Vis', 'Jay', 'Sid', 'Dip'}}

    math_students = sub.get('math', set())
    science_students = sub.get('science', set())
    both = math_students.intersection(science_students)
print("Students who take both 'math' and 'science':", both)

# 	Nested Dictionary:
nested_dict = {'name':'Ashwin','age':19,'skills':{'programming':'good','designing':'excellent'}}

# 	Create a nested dictionary where each key represents a country, and the value is another dictionary containing cities and their populations.
world = {
    'USA': {'New York': 8398748, 'Los Angeles': 3990456, 'Chicago': 2705994},
    'India': {'Mumbai': 12442373, 'Delhi': 11034555, 'Bangalore': 8443675},
    'China': {'Shanghai': 24256800, 'Beijing': 21516000, 'Guangzhou': 14043500}
}

# 11. Create two lists, one containing elements at even indices and the other containing elements at odd indices from the original list.
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_indices = original_list[::2]
odd_indices = original_list[1::2]

print("Elements at even indices:", even_indices)
print("Elements at odd indices:", odd_indices)

# 12. Use tuple packing and unpacking to swap the values of two variables without using a temporary variable.
a = 5
b = 10
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# 13. Check if a given list is a palindrome using slicing.
def is_palindrome(lst):
    return lst == lst[::-1]
my_list = [1, 2, 3, 2, 1]
print("Is my_list a Palindrome?",is_palindrome(my_list))

# 14. oncatenate two tuples without using the + operator.
tup1=(1,2,3)
tup2=('a','b')
lst1=list(tup1)
lst2=list(tup2)
lst1.append(lst2)
print("After Printing tup3 : ",tuple(lst1))