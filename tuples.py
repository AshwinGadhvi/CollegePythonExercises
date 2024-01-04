### Exercises: Level 1

#1. Create an empty tuple
empty_tuple = ()
print("\nEmpty Tuple : ",empty_tuple)

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
empty_tuple = ("Kishan","Hasu","Disha","Shashwat","Prashant","Shiva")
print("\nAfter Making Tuple : ",empty_tuple)

#3. Join brothers and sisters tuples and assign it to siblings
brothers=("Kishan", "Shashwat","Prashant","Shiva")
sisters=("Hasu","Disha")
siblings=", ".join(brothers+sisters)
print("\nJoining Sibling And Print Tuple : ",siblings)

#4. How many siblings do you have?
count=list(siblings.split(","))
print("\nWe Are : ",len(count)," Siblings")

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parent=("Jethalal","Ramila Ben")
family_members=(siblings,parent)
print("\nAfter Adding All Together : ",family_members)

### Exercises: Level 2

#1. Unpack siblings and parents from family_members
(siblings),(parent)=family_members
print("\nParents : ",parent)
print("\nSiblings : ",siblings)

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=("Apple","Mango","Banana")
vegetables=("Carrot","Cucumber","Tomato")
animal=("Lion","Tiger","Horse")
foof_stuff_tp=fruits+vegetables+animal
print("\nAfter Merging Three Tuple Assign : ",foof_stuff_tp)

#3. Change the about food_stuff_tp  tuple to a food_stuff_lt list
foof_stuff_lt=list(foof_stuff_tp)
print("\nAfter Changing Name : ",foof_stuff_lt)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle=list(foof_stuff_tp)
count=len(middle)//2
print("\nMiddle Element From Tuple : ",middle[count])
print("\nMiddle Element From List : ",foof_stuff_tp[count])

#5. Slice out the first three items and the last three items from food_staff_lt list
print("First Three Item : ",foof_stuff_lt[:3])
print("Last Three Item : ",foof_stuff_lt[-3:])

#6. Delete the food_staff_tp tuple completely
del foof_stuff_tp

#7. Check if an item exists in  tuple:
print('\ncake' in foof_stuff_lt)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

#- Check if 'Estonia' is a nordic country
print("Is That Estonia Is A nodric_Countries : ",'Estonia' in nordic_countries)

#- Check if 'Iceland' is a nordic country
print("Is That Estonia Is A nodric_Countries : ",'Iceland' in nordic_countries)

