## 💻 Exercises: Day 8

#1. Create  an empty dictionary called dog
dog= {}
print("\nEmpty dict is : ",dog)

#2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Baghira','color':'black','breed':'lebra','legs':4,'age':2}
print("\nDictonaries After Filling Details : ",dog)

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Ashwin','last_name':'Gadhvi','gender':'male','age':19,'marital status':'unmarried','skills':'web devloper','country':'india','address':'adipur'}
print("\nAfter Making Student Dictonarie : ",student)

#4. Get the length of the student dictionary
print("\nlength of Student Dictonarie is : ",len(student))

#5. Get the value of skills and check the data type, it should be a list
print("\nGetting Skill : ",student['skills'])
print("\nData Type Of Skills : ",type(student['skills']))

#6. Modify the skills values by adding one or two skills
student['skills']="Athlate","ePlayer"
print("\nAfter Modifiying the skills of student : ",student)

#7. Get the dictionary keys as a list
all_key = list(student.keys())
print("\nAll Keys After Transfer As List : ",all_key)

#8. Get the dictionary values as a list
all_value=list(student.values())
print("\nAll Values After Transfer As List : ",all_value)

#9. Change the dictionary to a list of tuples using _items()_ method
lst=student.items()
print("\nAfter Changing The List of Tuples",lst)

#10. Delete one of the items in the dictionary
del student['last_name']
print("\nAfter Deleting Last Name From Dict : ",student)

#11. Delete one of the dictionaries
empty = {}
del empty
